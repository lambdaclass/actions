"""parse_lane_findings: a reviewer that answered without a tool call keeps its answer (the diff is in
its prompt), with a note; an answer that does not parse still fails the lane.

Offline: imports run_pilot (no main()), no network, no keys.
Run: python3 -I -B -m unittest discover -s ai-review/tests -v
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run_pilot as rp  # noqa: E402

FINDING = {"title": "Closing an empty order leaves the sale selected", "severity": "medium",
           "category": "logic", "file": "lib/orders.ex", "line": 42, "quote": "close(order)",
           "mechanism": "close/1 does not clear the selection", "trigger": "close an order with no items",
           "impact": "the next action applies to a closed sale", "confidence": "medium"}


class ZeroToolCalls(unittest.TestCase):
    def lane(self, text: str, tool_calls: int) -> dict:
        res = {"lane": "claude", "status": "ok", "tool_calls": tool_calls, "final_text": text, "warnings": []}
        with tempfile.TemporaryDirectory() as d:
            rp.parse_lane_findings(res, Path(d))
        return res

    def test_findings_kept_without_tool_calls(self):
        res = self.lane(json.dumps({"summary": "s", "findings": [FINDING]}), 0)
        self.assertEqual(res["status"], "ok")
        self.assertEqual([f["title"] for f in res["findings"]], [FINDING["title"]])
        self.assertTrue(any("0 tool calls" in w for w in res["warnings"]))

    def test_no_findings_without_tool_calls_is_ok(self):
        res = self.lane(json.dumps({"summary": "nothing", "findings": []}), 0)
        self.assertEqual((res["status"], res["findings"]), ("ok", []))

    def test_no_note_with_tool_calls(self):
        res = self.lane(json.dumps({"summary": "nothing", "findings": []}), 3)
        self.assertEqual(res["warnings"], [])

    def test_unparseable_answer_still_fails(self):
        res = self.lane("I could not finish.", 0)
        self.assertEqual(res["status"], "failed")
        self.assertIn("not parseable", res["error"])


if __name__ == "__main__":
    unittest.main()
