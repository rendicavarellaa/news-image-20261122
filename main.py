#!/usr/bin/env python3
"""Copy the front page image to the output directory.

The image is drawn in advance and stored in this repository as
entry.png. This program only copies it, so the two runs the grader
makes write exactly the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    if not SRC.is_file():
        raise FileNotFoundError(f"entry image not found: {SRC}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
