"""plan_units: one unit with every code and test file of the PR; a PR over MAX_EFFECTIVE is too big.

Offline: no git, no network.
Run: python3 -I -B -m unittest discover -s ai-review/tests -v
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import seed  # noqa: E402


def rec(path: str, add: int, kind: str = "code") -> seed.FileRec:
    return seed.FileRec(path=path, status="M", old_path=None, add=add, dele=0, add_raw=add, del_raw=0, kind=kind)


class PlanUnits(unittest.TestCase):
    def test_one_unit_holds_every_code_and_test_file(self):
        recs = [rec("src/a.rs", 3000), rec(f"src/deep/{'x/' * 6}b.rs", 9000), rec("tests/t.rs", 400, "test"),
                rec("docs/d.md", 50, "docs"), rec("Cargo.lock", 900, "filtered"), rec("(root)/c.rs", 2)]
        (u,) = seed.plan_units(recs, {})
        self.assertEqual(sorted(u.files), ["(root)/c.rs", "src/a.rs", f"src/deep/{'x/' * 6}b.rs", "tests/t.rs"])
        self.assertEqual((u.code_files, u.test_files, u.docs_files), (3, 1, ["docs/d.md"]))
        self.assertEqual(u.effective, 3000 + 9000 + 2 + 0.5 * 400)
        self.assertTrue(all(r.unit == "u01" for r in recs if r.kind in ("code", "test")))
        self.assertEqual(seed.not_reviewed(recs)["files"], [])

    def test_a_file_in_no_unit_is_listed(self):
        r = rec("src/a.rs", 10)
        self.assertEqual(seed.not_reviewed([r])["files"], [{"file": "src/a.rs", "why": "not placed in a part"}])

    def test_low_risk_only_if_all_its_code_is(self):
        cfg = {"low_risk": ["examples/**"]}
        self.assertTrue(seed.plan_units([rec("examples/a.rs", 50), rec("tests/a.rs", 10, "test")], cfg)[0].low_risk)
        self.assertFalse(seed.plan_units([rec("examples/a.rs", 50), rec("src/a.rs", 1)], cfg)[0].low_risk)
        self.assertFalse(seed.plan_units([rec("examples/a.rs", 50)], {})[0].low_risk)   # no config: nothing is
        self.assertFalse(seed.plan_units([rec("tests/a.rs", 10, "test")], cfg)[0].low_risk)   # no code at all

    def test_size_class(self):
        self.assertEqual(seed.size_class(seed.MAX_EFFECTIVE), "normal")
        self.assertEqual(seed.size_class(seed.MAX_EFFECTIVE + 0.5), "too big")
        recs = [rec("src/a.rs", seed.MAX_EFFECTIVE), rec("tests/t.rs", 2, "test")]
        self.assertEqual(seed.sizes(recs)["class"], "too big")


if __name__ == "__main__":
    unittest.main(verbosity=2)
