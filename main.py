#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261117.

Writes the bundled front-page image of Tuesday 17 November 2026's world
news to the output directory. Standard library only, no network, fully
deterministic: every run writes the exact same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"bundled image missing: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("copy incomplete: size mismatch")


if __name__ == "__main__":
    main()
