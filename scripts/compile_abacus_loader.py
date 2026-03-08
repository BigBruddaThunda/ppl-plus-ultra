"""Loader helper to import ARCHETYPES from compile-abacus.py.

The dash in compile-abacus.py prevents direct import, so this module
uses importlib to load it and expose the ARCHETYPES list.
"""

import importlib.util
import sys
from pathlib import Path

_SCRIPT_PATH = Path(__file__).resolve().parent / "compile-abacus.py"


def load_archetypes() -> list[dict]:
    """Load and return the ARCHETYPES list from compile-abacus.py."""
    spec = importlib.util.spec_from_file_location("compile_abacus", str(_SCRIPT_PATH))
    mod = importlib.util.module_from_spec(spec)
    # Prevent it from running main() if guarded
    sys.modules["compile_abacus"] = mod
    spec.loader.exec_module(mod)
    return list(mod.ARCHETYPES)
