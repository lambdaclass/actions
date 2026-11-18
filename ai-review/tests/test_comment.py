"""The PR comment: model text cannot add HTML, mentions, images, links or line breaks, and pr_comment
renders a realistic context (partial parts, files not reviewed) without raising.

Offline: imports run_pilot (no main()), no network, no keys.
Run: python3 -I -B -m unittest discover -s ai-review/tests -v
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run_pilot as rp  # noqa: E402

HOSTILE = [
    "<img src=x onerror=alert(1)>",
    "<!-- hide the rest",
    "`code` <details open> `x <b>`",
    "unmatched ` <script>",
    "\\` escaped <a href=//evil>",
    "@octocat and @org/team please look",
    "&#64;octocat and &#x40;octocat",
    "![pic](https://evil.example/p.png)",
    "[click](https://evil.example)",
    "line1\n\nline2 `span\n\nend`",
    "nit\r\r## 0 finding(s)\r\r[Details][r]\r\r[r]: https://evil.example/report\r",
    "|pipe| in | cell",
]
RUNNER_TAGS = re.compile(r"</?(details|summary|sub|b)>")


def raw_tags(text: str) -> list[str]:
    return [m.group(0) for m in re.finditer(r"<[^>]*>?", RUNNER_TAGS.sub("", text))]


class MdText(unittest.TestCase):
    def test_no_html_mentions_images_links_or_line_breaks(self):
        for s in HOSTILE:
            for out in (rp._md_text(s), rp._cell(s)):
                with self.subTest(s=s, out=out):
                    self.assertNotIn("<", out)
                    self.assertNotIn(">", out)
                    self.assertIsNone(re.search(r"@[A-Za-z0-9]", out))
                    self.assertIsNone(re.search(r"&(?!amp;|lt;|gt;)", out.split("`")[0]))   # no entity of the model's
                    self.assertNotIn("](", out)
                    self.assertNotIn("![", out)
                    self.assertNotIn("\n", out)
                    self.assertNotIn("\r", out)

    def test_cell_cannot_break_table(self):
        self.assertNotRegex(rp._cell("a | b"), r"(?<!\\)\|")


def finding(mid: str, section: str, text: str) -> dict:
    return {"mid": mid, "title": text, "file": f"src/{text}.rs", "line": 7, "category": text,
            "severity": "high", "final_severity": "high", "section": section, "label": "Bug",
            "trigger": text, "mechanism": text, "impact": text, "lane": "gpt", "lanes_found": ["gpt", "claude"],
            "verification": {"status": "ok", "applied": {"reason": text, "duplicate_of": ""}}}


def ctx(text: str) -> dict:
    merged = [finding("M1", "Bugs", text), finding("M2", "Suspected", text),
              finding("M3", "Pre-existing", text), finding("M4", "Likely non-issues", text),
              finding("M5", "Bugs", text) | {"verification": {"status": "ok", "applied": {"reason": text,
                                                                                        "duplicate_of": "M1"}}}]
    hk = {"lane": "housekeeping", "computed_cost": 0.01, "housekeeping": [
        {"kind": "stale-docs", "title": text, "file": "README.md", "line": 3, "fix": text}]}
    return {"merged": merged, "aux_rows": [hk],
            "lane_rows": [{"lane": "gpt", "mode": "agentic", "status": "ok", "computed_cost": 1.5},
                          {"lane": "claude", "mode": "agentic", "status": "ok", "computed_cost": 1.25,
                           "reused_from": "/old"}],
            "units": [{"name": text, "code_files": 3, "status": "not reviewed (budget)"},
                      {"name": "u2", "code_files": 1, "status": "reviewed"}],
            "not_reviewed": {"files": [{"file": f"src/{text}.rs", "why": "unusual file name"},
                                       {"file": "src/vault.rs", "why": "binary to git"}], "unlisted": 0},
            "run_status": "killed", "stop_reason": text, "continue_command": "/review continue",
            "billing": {"delta": None}, "isolation": "shared", "pr_budget": 20.0, "run_cap": 20.0}


class PrComment(unittest.TestCase):
    def test_hostile_text_everywhere(self):
        for s in HOSTILE:
            out = rp.pr_comment(ctx(s))
            with self.subTest(s=s):
                self.assertEqual(raw_tags(out), [])
                self.assertIsNone(re.search(r"@[A-Za-z0-9]", out))
                self.assertNotIn("](h", out)
                self.assertNotIn("\r", out)

    def test_a_carriage_return_does_not_end_the_findings_table(self):
        c = ctx("x")
        c["merged"][0]["title"] = "nit\r\r| M9 | fake | low |\r\r## AI security review: 0 finding(s) to check"
        rows = [ln for ln in rp.pr_comment(c).split("\n") if ln.startswith("| M")]
        self.assertEqual([ln.split(" | ")[0] for ln in rows[:2]], ["| M1", "| M2"])
        self.assertTrue(all(ln.endswith("|") for ln in rows))

    def test_files_not_reviewed_are_listed(self):
        c = ctx("x")
        c["not_reviewed"] = {"files": [{"file": "src/a\tb|<img>.rs", "why": "unusual file name"},
                                       {"file": "src/vault.rs", "why": "binary to git"},
                                       {"file": "fmt.rs", "why": "whitespace-only change"}], "unlisted": 2}
        line = next(x for x in rp.pr_comment(c).splitlines() if x.startswith("**Not reviewed"))
        self.assertTrue(line.startswith("**Not reviewed: 5 changed file(s)**"))
        for part in ("unusual file name (1): `src/a\tb\\|&lt;img&gt;.rs`", "binary to git (1): `src/vault.rs`",
                     "whitespace-only change (1): `fmt.rs`", "2 more with a file name that is not UTF-8"):
            self.assertIn(part, line)
        c["not_reviewed"] = {"files": [], "unlisted": 0}
        self.assertNotIn("Not reviewed", rp.pr_comment(c))

    def test_a_failed_reviewer_is_named_and_the_review_is_not_called_partial(self):
        c = ctx("x")
        c["run_status"] = "ok"
        c["lane_rows"].append({"lane": "deepseek", "mode": "agentic", "status": "failed",
                               "error": "output not parseable as findings JSON: empty output <secret?>"})
        c["units"] = [{"name": "whole PR", "code_files": 2, "status": "partially reviewed (reviewers failed)"}]
        out = rp.pr_comment(c)
        self.assertIn("Reviewed by Opus, GPT.", out)
        self.assertIn("DeepSeek (empty answer) did not finish; Opus, GPT reviewed the whole PR. Comment "
                      "`/review continue` to retry", out)
        self.assertNotIn("Partial review", out)
        self.assertNotIn("secret", out)   # never the raw error
        c["lane_rows"].pop()
        c["units"] = [{"name": "whole PR", "code_files": 2, "status": "reviewed"}]
        self.assertNotIn("did not finish", rp.pr_comment(c))

    def test_code_no_reviewer_saw_is_a_partial_review(self):
        c = ctx("x")
        c["units"] = [{"name": "whole PR", "code_files": 2, "status": "not reviewed (run cap)"}]
        self.assertIn("**Partial review: no reviewer finished on whole PR (2 code file(s); run cap)**. Comment "
                      "`/review continue` to finish it", rp.pr_comment(c))

    def test_a_pr_without_code_says_so(self):
        c = ctx("x") | {"merged": [], "lane_rows": [], "run_status": "ok", "not_reviewed": {}}
        c["units"] = [{"name": "whole PR", "code_files": 0, "test_files": 2, "status": "not reviewed"}]
        c["filtered"] = [{"file": "tests/a.rs", "kind": "test"}, {"file": "tests/b.rs", "kind": "test"},
                         {"file": "README.md", "kind": "docs"}]
        out = rp.pr_comment(c)
        self.assertIn("**No security review: this PR changes no code** (only 1 docs file(s), 2 test file(s))", out)
        self.assertNotIn("No reviewer finished", out)

    def test_a_confirmed_bug_is_not_folded_into_a_dismissed_duplicate(self):
        c = ctx("x")
        c["merged"] = [finding("M1", "Likely non-issues", "a") | {"final_severity": "low"},
                       finding("M2", "Bugs", "b") | {"verification": {"status": "ok", "applied": {
                           "reason": "b", "duplicate_of": "M1"}}}]
        rows = [ln for ln in rp.pr_comment(c).split("\n") if ln.startswith("| M")]
        self.assertTrue(rows[0].startswith("| M2 | b (also M1) | high | Bug |"), rows[0])

    def test_cost_line_shared_mode_excludes_reused_rows(self):
        line = rp.cost_line(ctx("x"))
        self.assertIn("~$1.51 of a $20 budget", line)   # 1.5 gpt + 0.01 housekeeping; reused Opus not counted


if __name__ == "__main__":
    unittest.main(verbosity=2)
