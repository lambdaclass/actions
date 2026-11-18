"""verification_queue: which merged findings the judge checks. Offline.
Run: python3 -I -B -m unittest discover -s ai-review/tests -v
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run_pilot  # noqa: E402


def finding(mid: str, severity: str, category: str = "logic") -> dict:
    return {"mid": mid, "severity": severity, "category": category}


class VerificationQueue(unittest.TestCase):
    def test_docs_findings_are_judged(self):
        fs = [finding("M1", "low", "docs"), finding("M2", "high")]
        queue = run_pilot.verification_queue(fs, "low")
        self.assertEqual([f["mid"] for f in queue], ["M2", "M1"])   # most severe first
        self.assertTrue(all("verify_skipped" not in f for f in fs))

    def test_below_the_threshold_is_skipped_with_a_reason(self):
        fs = [finding("M1", "low", "docs"), finding("M2", "medium")]
        queue = run_pilot.verification_queue(fs, "medium")
        self.assertEqual([f["mid"] for f in queue], ["M2"])
        self.assertEqual(fs[0]["verify_skipped"], "severity low below verification threshold")


if __name__ == "__main__":
    unittest.main(verbosity=2)
