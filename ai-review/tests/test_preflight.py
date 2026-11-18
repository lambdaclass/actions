"""Pre-flight: OpenRouter credit is checked only against what OpenRouter will bill (not Anthropic-billed
Opus, not reused lanes); a --reuse-from run is reused only for the same head and merge-base.

Offline: imports run_pilot (no main()), no network, no keys.
Run: python3 -I -B -m unittest discover -s ai-review/tests -v
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace as NS
from unittest import mock

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run_pilot as rp  # noqa: E402


def args(auth: str, reuse_from: str = "") -> NS:
    return NS(mode_list=["agentic"], claude_auth=auth, judge="gpt", reuse_from=reuse_from, reuse_lanes="all")


UNIT = NS(uid="u01", lanes=["claude", "gpt", "kimi"], files=["src/a.rs"])
EST = {"claude": 3.0, "gpt": 2.0, "kimi": 1.0}


class Preflight(unittest.TestCase):
    def setUp(self):
        self.enterContext(mock.patch.object(rp, "est_agentic", lambda p, x, m, c: EST[x]))
        self.enterContext(mock.patch.object(rp, "log", lambda *a, **k: None))
        self.tmp = Path(self.enterContext(tempfile.TemporaryDirectory()))

    def earlier_run(self, head="h", base="mb") -> Path:
        d = self.tmp / "old"
        (d / "units/u01/agentic/gpt").mkdir(parents=True)
        (d / "summary.json").write_text(json.dumps({"head": head, "base": base}))
        (d / "plan.json").write_text(json.dumps({"units": [{"uid": "u01", "files": ["src/a.rs"]}]}))
        (d / "units/u01/agentic/gpt/result.json").write_text(json.dumps({"status": "ok", "findings": []}))
        return d

    def est(self, a, reuse=(None, set(), set())) -> float:
        return rp.openrouter_estimate(a, [UNIT], {}, {}, {}, est_total=6.5, est_ver=0.5, reuse=reuse)

    def test_anthropic_billed_opus_is_not_held_against_openrouter_credit(self):
        self.assertEqual(self.est(args("anthropic")), 3.5)
        self.assertEqual(self.est(args("openrouter")), 6.5)

    def test_reused_lanes_are_not_estimated_again(self):
        a = args("openrouter", str(self.earlier_run()))
        reuse = rp.reuse_plan(a, [UNIT], "h", "mb")
        self.assertEqual(self.est(a, reuse), 4.5)   # gpt reused

    def test_reuse_needs_the_same_head_and_merge_base(self):
        a = args("openrouter", str(self.earlier_run(base="old-mb")))
        _, reuse, _ = rp.reuse_plan(a, [UNIT], "h", "mb")
        self.assertEqual(reuse, set())
        _, reuse, _ = rp.reuse_plan(a, [UNIT], "other-head", "old-mb")
        self.assertEqual(reuse, set())
        self.assertTrue(rp.reuse_plan(a, [UNIT], "h", "old-mb")[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
