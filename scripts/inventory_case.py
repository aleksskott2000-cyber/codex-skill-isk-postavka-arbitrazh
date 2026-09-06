#!/usr/bin/env python3
"""Create a complete, hash-backed inventory of a case folder without modifying it."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("case_folder", type=Path)
    parser.add_argument("--exclude", action="append", default=["0. Исковое заявление.docx"])
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    root = args.case_folder.resolve()
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    excluded = {name.casefold() for name in args.exclude}
    files = []
    for path in sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: str(p).casefold()):
        if path.name.casefold() in excluded:
            continue
        files.append(
            {
                "relative_path": str(path.relative_to(root)),
                "extension": path.suffix.lower(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )

    result = {"case_folder": str(root), "file_count": len(files), "files": files}
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    print(payload)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(payload + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

