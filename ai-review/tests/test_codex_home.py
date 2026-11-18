"""codex_home_for gives each Codex lane a model catalog entry for the exact model string it sends, with the
model's real window, and save_codex_trace records per-request usage and compactions in requests.jsonl.

Offline: imports run_pilot (no main()), no network, no keys, no codex binary.
Run: python3 -I -B -m unittest discover -s ai-review/tests -v
"""

from __future__ import annotations

import json
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run_pilot as rp  # noqa: E402

GLM, GLM_SENT = "z-ai/glm-5.3", "z-ai/glm-5.3@preset/air-z-ai-glm-5-3"
PRICES = {GLM: {"context_length": 1_048_576}, "openai/gpt-6.1-sol": {"context_length": 1_050_000,
                                                                     "max_prompt_tokens": 922_000},
          "tight/model": {"context_length": 1_000_000, "max_prompt_tokens": 800_000}}


class CodexHome(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def home(self, model: str, sent: str | None = None) -> tuple[dict, dict | None]:
        home = rp.codex_home_for(self.dir / model.replace("/", "_"), model, PRICES, sent_model=sent)
        cfg = tomllib.loads((home / "config.toml").read_text())
        cat = home / "model_catalog.json"
        return cfg, (json.loads(cat.read_text()) if cat.exists() else None)

    def test_catalog_entry_for_the_sent_model_string(self):
        cfg, cat = self.home(GLM, GLM_SENT)
        (entry,) = cat["models"]
        limit = int(1_048_576 * 0.85)
        self.assertEqual((entry["slug"], entry["display_name"]), (GLM_SENT, GLM_SENT))
        self.assertEqual((entry["context_window"], entry["max_context_window"], entry["auto_compact_token_limit"]),
                         (1_048_576, 1_048_576, limit))
        self.assertEqual(cfg["model_catalog_json"], str(self.dir / "z-ai_glm-5.3" / "model_catalog.json"))
        self.assertEqual((cfg["model_context_window"], cfg["model_auto_compact_token_limit"]), (1_048_576, limit))

    def test_everything_else_is_the_frozen_template(self):
        _, cat = self.home(GLM, GLM_SENT)
        template = json.loads(rp.CODEX_CATALOG_ENTRY.read_text())
        filled = {"slug", "display_name", "context_window", "max_context_window", "auto_compact_token_limit"}
        self.assertEqual({k: v for k, v in cat["models"][0].items() if k not in filled},
                         {k: v for k, v in template.items() if k not in filled})
        self.assertGreater(len(template["base_instructions"]), 10_000)

    def test_slug_defaults_to_the_model(self):
        _, cat = self.home(GLM)
        self.assertEqual(cat["models"][0]["slug"], GLM)

    def test_limit_stays_below_the_hosts_max_prompt(self):
        cfg, cat = self.home("openai/gpt-6.1-sol")
        self.assertEqual(cfg["model_auto_compact_token_limit"], 892_500)   # 0.85 x 1.05M < 0.97 x 922k
        cfg, cat = self.home("tight/model")
        self.assertEqual(cfg["model_auto_compact_token_limit"], 776_000)   # 0.97 x 800k < 0.85 x 1M
        self.assertEqual(cat["models"][0]["auto_compact_token_limit"], 776_000)

    def test_no_catalog_without_a_known_window(self):
        cfg, cat = self.home("unknown/model")
        self.assertIsNone(cat)
        self.assertNotIn("model_catalog_json", cfg)
        self.assertNotIn("model_auto_compact_token_limit", cfg)


class RequestsLog(unittest.TestCase):
    def test_requests_and_compactions(self):
        def tok(last_in: int, total_in: int) -> dict:
            return {"type": "event_msg", "payload": {"type": "token_count", "info": {
                "last_token_usage": {"input_tokens": last_in, "output_tokens": 10},
                "total_token_usage": {"input_tokens": total_in}, "model_context_window": 996_147}}}
        events = [tok(300_000, 300_000), tok(300_000, 300_000),   # Codex repeats a token count
                  {"type": "event_msg", "payload": {"type": "context_compacted"}}, tok(2_000, 302_000),
                  {"type": "response_item", "payload": {"type": "message", "role": "assistant",
                                                        "content": [{"type": "output_text", "text": "done"}]}}]
        with tempfile.TemporaryDirectory() as t:
            home, out = Path(t) / "codex_home", Path(t) / "lane"
            (home / "sessions" / "2026").mkdir(parents=True)
            out.mkdir()
            (home / "sessions" / "2026" / "s.jsonl").write_text("".join(json.dumps(e) + "\n" for e in events))
            self.assertEqual(rp.save_codex_trace(home, out / "trace.jsonl"),
                             {"compactions": 1, "max_context": 300_000, "window": 996_147})
            rows = [json.loads(x) for x in (out / "requests.jsonl").read_text().splitlines()]
            self.assertFalse((home / "sessions").exists())
        self.assertEqual([r["kind"] for r in rows], ["request", "compacted", "request"])
        self.assertEqual((rows[0]["input_tokens"], rows[0]["window"], rows[2]["total_input"]), (300_000, 996_147, 302_000))


class ContextReport(unittest.TestCase):
    def test_section_and_summary(self):
        ctx = {"lane_rows": [{"unit": "u01", "lane": "gpt", "compactions": 0, "max_context": 284_000,
                              "context_window": 996_147},
                             {"unit": "u01", "lane": "glm", "compactions": 2, "max_context": 345_000,
                              "context_window": 0}],
               "aux_rows": [{"unit": "-", "lane": "merge"}]}
        out = "\n".join(rp.context_lines(ctx))
        self.assertIn("Compactions: 2 in 1 of 2 agentic lane(s)", out)
        self.assertIn("| u01 | gpt | 284,000 | 996,147 | 29% | 0 |", out)
        self.assertIn("| u01 | glm | 345,000 | 0 | - | 2 |", out)
        self.assertNotIn("merge", out)
        self.assertEqual(rp.context_summary(ctx), "2 compaction(s); largest request 345,000 tokens (u01/glm)")
        self.assertEqual(rp.context_lines({"lane_rows": [], "aux_rows": []}), [])


if __name__ == "__main__":
    unittest.main()
