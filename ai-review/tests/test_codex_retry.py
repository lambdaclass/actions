"""A Codex lane that ends without an answer is asked once more, in the same session, for the answer only;
its final file is masked.

Offline: a fake `codex` script on AI_REVIEW_PATH, no network, no keys.
Run: python3 -I -B -m unittest discover -s ai-review/tests -v
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run_pilot as rp  # noqa: E402

FAKE = r'''#!/bin/sh
# first run: one command, then an empty answer; `exec resume`: the answer
out=""; prev=""
for a in "$@"; do [ "$prev" = "-o" ] && out="$a"; prev="$a"; done
cat > /dev/null
echo "$@" >> "$(dirname "$0")/calls.txt"
if [ "$2" = "resume" ]; then
  [ -f "$(dirname "$0")/still_empty" ] && ans='' || ans='{"summary":"s","findings":[]} sk-or-v1-0123456789abcdef0123456789abcdef'
  echo '{"type":"turn.completed","usage":{"input_tokens":10,"cached_input_tokens":0,"output_tokens":5,"reasoning_output_tokens":0}}'
  printf '%s' "$ans" > "$out"
  echo 'INFO feedback_tags: last_model_response_id="gen-3"' >&2
else
  echo 'INFO feedback_tags: last_model_response_id="gen-1"' >&2
  echo 'INFO feedback_tags: last_model_response_id="gen-2"' >&2
  echo '{"type":"thread.started","thread_id":"t-123"}'
  echo '{"type":"item.completed","item":{"type":"command_execution","command":"ls"}}'
  echo '{"type":"turn.completed","usage":{"input_tokens":100,"cached_input_tokens":0,"output_tokens":8000,"reasoning_output_tokens":8000}}'
  : > "$out"
fi
'''


class EmptyAnswerRetry(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.bin, self.wt, self.out = d / "bin", d / "wt", d / "lane"
        self.bin.mkdir(), self.wt.mkdir()
        (self.bin / "codex").write_text(FAKE)
        (self.bin / "codex").chmod(0o755)
        self.old = os.environ.get("AI_REVIEW_PATH"), rp.GATE_ROOT
        os.environ["AI_REVIEW_PATH"], rp.GATE_ROOT = str(self.bin), d / "gates"

    def tearDown(self):
        if self.old[0] is None:
            os.environ.pop("AI_REVIEW_PATH", None)
        else:
            os.environ["AI_REVIEW_PATH"] = self.old[0]
        rp.GATE_ROOT = self.old[1]
        self.tmp.cleanup()

    def run_lane(self) -> dict:
        m = "deepseek/deepseek-v4-pro-0813"

        def gen(url, key=None, body=None, timeout=0):
            p = {"gen-1": "Baidu", "gen-2": "Baidu"}.get(url.rsplit("=", 1)[1])
            if not p:
                raise RuntimeError("HTTP 404")
            return {"data": {"provider_name": p}}
        self.enterContext(mock.patch.object(rp, "http_json", gen))
        self.enterContext(mock.patch.object(rp.time, "sleep", lambda s: None))
        return rp.run_codex("deepseek", m, m, "prompt", self.out / "schema.json", self.wt, self.out, "k",
                            {m: {"context_length": 1_000_000, "prompt": 1e-6, "cache_read": 1e-7, "cache_write": 0,
                                 "completion": 2e-6}}, 60)

    def test_asks_once_more_and_masks_the_answer(self):
        res = self.run_lane()
        calls = (self.bin / "calls.txt").read_text().splitlines()
        self.assertEqual(len(calls), 2)
        self.assertIn("resume", calls[1].split()[:2])
        self.assertIn("t-123", calls[1].split())
        self.assertEqual(res["status"], "ok")
        self.assertTrue(res["final_text"].startswith('{"summary"'))
        self.assertNotIn("sk-or-v1-0123", (self.out / "last_message.txt").read_text())
        self.assertEqual(res["usage"]["input"], 110)   # usage of both runs
        self.assertIn("empty answer; asked once more for the answer", res["warnings"])
        # which provider served each response, from OpenRouter's generation lookup ("?" = not found)
        self.assertEqual(res["served_by"], {"Baidu": 2, "?": 1})
        self.assertIn("served by Baidu 2, ? 1", res["warnings"])
        rows = [json.loads(x) for x in (self.out / "requests.jsonl").read_text().splitlines()]
        self.assertEqual([(r["id"], r["provider"]) for r in rows if r.get("kind") == "generation"],
                         [("gen-1", "Baidu"), ("gen-2", "Baidu"), ("gen-3", "?")])

    def test_still_empty_is_reported(self):
        (self.bin / "still_empty").write_text("")
        res = self.run_lane()
        self.assertEqual(res["final_text"], "")
        self.assertIn("empty answer; asked once more for the answer, still empty", res["warnings"])


class CredentialDenies(unittest.TestCase):
    def test_registry_and_git_credentials_are_denied_to_both_harnesses(self):
        with tempfile.TemporaryDirectory() as t, mock.patch.object(rp, "existing", lambda ps: list(ps)):
            claude = json.dumps(rp.claude_settings(Path(t)))   # (only paths that exist are listed)
        for p in ("~/.npmrc", "~/.git-credentials", "~/.pypirc", "~/.gem/credentials"):
            self.assertIn(p, rp.LANE_READ_DENY)
            self.assertIn(p, claude)


if __name__ == "__main__":
    unittest.main(verbosity=2)
