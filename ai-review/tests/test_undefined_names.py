"""Every global name a function of the runner reads exists: catches a variable moved into another function
and still used in the old one (a NameError only at run time, after the paid calls). Offline.
Run: python3 -I -B -m unittest discover -s ai-review/tests -v
"""

from __future__ import annotations

import builtins
import importlib
import symtable
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def undefined(module_name: str) -> list[str]:
    mod = importlib.import_module(module_name)
    path = ROOT / f"{module_name}.py"
    known = set(vars(mod)) | set(dir(builtins))
    out = []

    def walk(t: symtable.SymbolTable) -> None:
        # module-level code already ran on import; only function bodies can hide a missing name
        for s in (t.get_symbols() if t.get_type() != "module" else []):
            if s.is_referenced() and s.is_global() and s.get_name() not in known:
                out.append(f"{path.name}: {t.get_name()} line {t.get_lineno()}: {s.get_name()}")
        for c in t.get_children():
            walk(c)
    walk(symtable.symtable(path.read_text(), str(path), "exec"))
    return out


class UndefinedNames(unittest.TestCase):
    def test_runner_and_seed(self):
        self.assertEqual(undefined("run_pilot") + undefined("seed"), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
