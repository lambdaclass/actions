"""seed.housekeeping_scan: the scripted leads for the housekeeping lane (paths and make targets the PR
references that the head does not have; names the PR adds that nothing else references).

Offline: temporary git repositories built with plumbing, no network, no keys, no model.
Run: python3 -I -B -m unittest discover -s ai-review/tests -v
"""

from __future__ import annotations

import os
import sys
import types
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull})   # seed.git() inherits it

import run_pilot as rp  # noqa: E402
import seed  # noqa: E402
from gitrepo import Repo  # noqa: E402

MAKEFILE = ".PHONY: build test \\\n\tlint\n# make expands $(X) here\nbuild:\n\tcargo build\ntest: build\n\tcargo test\n" \
           "lint:\n\tcargo clippy\nbench-%:\n\tcargo bench $*\n"
BASE = {"Makefile": MAKEFILE, "README.md": "# x\n", "src/lib.py": "OLD = 1\n", "docs/guide.md": "old\n",
        ".gitignore": "/.local/\nout/\n", "deploy/real.yml": "a: 1\n", "tests/test_lib.py": "x = 1\n"}


class Scan(unittest.TestCase):
    def setUp(self):
        self.repo = Repo()
        self.addCleanup(self.repo.close)

    def scan(self, head_changes: dict, cfg: dict | None = None) -> dict:
        mb = self.repo.commit(BASE)
        head = self.repo.commit(dict(BASE) | head_changes, parent=mb)
        recs = seed.classify_files(self.repo.path, mb, head, cfg or {}, None)
        return seed.housekeeping_scan(self.repo.path, mb, head, recs)

    def refs(self, scan: dict) -> set[tuple[str, str]]:
        return {(x["kind"], x["ref"]) for x in scan["missing"]}

    def test_missing_paths_and_make_targets_in_docs(self):
        doc = ("# Guide\n\nAlerts live in `deploy/prometheus/` and `deploy/real.yml`; see DEPLOYMENT.md and\n"
               "[the manual](docs/manual.md). Run `make observability-up`, `make build` or `make bench-x`.\n"
               "Make sure to read https://example.com/a/b.md and `owner/repo` and `out/report.md`,\n"
               "`.local/state.json`, `../outside.md` and `src/*.md`.\n\n"
               "```sh\nmake test lint\nmake -C sub VAR=1 e2e-custom\n```\nmake sure the docs are right.\n")
        refs = self.refs(self.scan({"docs/guide.md": doc}))
        self.assertEqual(refs, {("path", "deploy/prometheus/"), ("path", "DEPLOYMENT.md"), ("path", "docs/manual.md"),
                                ("make", "observability-up"), ("make", "e2e-custom")})

    def test_relative_paths_resolve_against_the_file_and_known_subpaths(self):
        doc = "See `real.yml`, `../README.md`, `checkout/deploy/real.yml` and `deploy/missing.md`.\n"
        refs = self.refs(self.scan({"deploy/README.md": doc}))
        self.assertEqual(refs, {("path", "deploy/missing.md")})

    def test_code_comments_and_strings(self):
        code = ("import os  # an import line is not checked: `docs/import-only.md`\n"
                "x = 1  # see `docs/gone.md`\n"
                "from x import y\n"
                "OUT = 'result.json'        # a bare name in code: an output, not a reference\n"
                "CFG = 'deploy/conf.toml'   # a path in a string: checked\n"
                "# make sure this stays fast; DEPLOYMENT.md has the steps\n"
                "def f():\n    return OLD\n")
        refs = self.refs(self.scan({"src/lib.py": "OLD = 1\n" + code}))
        self.assertEqual(refs, {("path", "docs/gone.md"), ("path", "deploy/conf.toml"), ("path", "DEPLOYMENT.md")})

    def test_makefile_comments_are_prose_but_recipes_are_checked(self):
        mk = MAKEFILE + "# make expands nothing here\nall:\n\t$(MAKE) build\n\tmake e2e-custom\n"
        refs = self.refs(self.scan({"Makefile": mk}))
        self.assertEqual(refs, {("make", "e2e-custom")})

    def test_no_makefile_no_make_checks(self):
        base = {k: v for k, v in BASE.items() if k != "Makefile"}
        mb = self.repo.commit(base)
        head = self.repo.commit(base | {"README.md": "Run `make anything`.\n"}, parent=mb)
        recs = seed.classify_files(self.repo.path, mb, head, {}, None)
        self.assertEqual(seed.housekeeping_scan(self.repo.path, mb, head, recs)["missing"], [])

    def test_tests_and_ignored_files_are_not_scanned(self):
        scan = self.scan({"tests/test_lib.py": "P = 'docs/fixture-only.md'\n", "vendor/x.md": "`docs/nope.md`\n"},
                         cfg={"ignore": ["vendor/**"]})
        self.assertEqual(scan["missing"], [])

    def test_unreferenced_new_names(self):
        code = ("OLD = 1\n"
                "PROTECTED = {'a'}\n"          # new, never read: reported
                "USED = 2\n"                   # new, read below
                "def helper():\n    return USED\n"
                "def _private():\n    return 1\n"   # new, never called: reported
                "def main():\n    helper()\n"      # entry point: never reported
                "class Thing:\n    def method(self):\n        return 1\n")   # method: not module level
        scan = self.scan({"src/lib.py": code, "src/other.py": "from lib import Thing\n"})
        self.assertEqual([x["name"] for x in scan["unreferenced"]], ["PROTECTED", "_private"])
        self.assertEqual(scan["unreferenced"][0]["at"], ["src/lib.py:2"])

    def test_a_name_that_existed_before_is_not_new(self):
        # OLD is moved to a new file; the base already had it, so it is not reported even if unused now
        scan = self.scan({"src/lib.py": "\n", "src/consts.py": "OLD = 1\n"})
        self.assertEqual(scan["unreferenced"], [])

    def test_rust_private_items_only(self):
        rs = ("pub fn api() {}\nfn unused_helper() {}\npub(crate) const LIMIT: u32 = 3;\nfn main() {}\n"
              "impl X {\n    fn indented() {}\n}\n")
        scan = self.scan({"src/main.rs": rs})
        self.assertEqual([x["name"] for x in scan["unreferenced"]], ["unused_helper", "LIMIT"])

    def test_leads_in_the_comment(self):
        self.assertEqual(rp.scan_lead_lines({}), [])
        out = "\n".join(rp.scan_lead_lines({
            "missing": [{"ref": "e2e-custom", "kind": "make", "at": ["a.md:1"], "count": 1},
                        {"ref": "deploy/x.md", "kind": "path", "at": ["b.md:2", "c.md:3"], "count": 2}],
            "unreferenced": [{"name": "FOO", "at": ["x.py:3"]}]}))
        self.assertIn("Leads from a script (not checked): 3", out)
        self.assertIn("- `make e2e-custom`: no Makefile defines this target (referenced at a.md:1)", out)
        self.assertIn("- `deploy/x.md` does not exist in the repository (referenced at b.md:2, c.md:3)", out)
        self.assertIn("- `FOO` is added by this PR and referenced nowhere else (x.py:3)", out)


class Plan(unittest.TestCase):
    def test_build_plan_carries_the_scan_and_the_prompt_has_no_hints(self):
        repo = Repo()
        self.addCleanup(repo.close)
        mb = repo.commit(BASE)
        head = repo.commit(dict(BASE) | {"src/lib.py": "OLD = 1\nNEVER_READ = 2\n# see `docs/gone.md`\n"}, parent=mb)
        args = types.SimpleNamespace(paths=None, lane_list=["claude", "gpt"], mode_list=["agentic"])
        plan = rp.build_plan(args, {"title": "t", "body": ""}, repo.path, mb, head, {}, repo.dir / "scratch",
                             repo.dir / "run")
        self.assertEqual([x["ref"] for x in plan["housekeeping_scan"]["missing"]], ["docs/gone.md"])
        self.assertEqual([x["name"] for x in plan["housekeeping_scan"]["unreferenced"]], ["NEVER_READ"])
        self.assertNotIn("{{HINTS}}", (Path(rp.ROOT) / "prompts" / "housekeeping.md").read_text())


if __name__ == "__main__":
    unittest.main()
