#!/usr/bin/env python3
"""把 src/ 下的片段按文件名顺序拼成单文件 index.html。"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"

parts = sorted(SRC.glob("*.html"))
html = "\n".join(p.read_text(encoding="utf-8") for p in parts)
out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")

words = len("".join(html.split()))
print(f"built {out}  ({len(html)/1024:.1f} KB, ~{words/1000:.1f}k chars, {len(parts)} parts)")
for p in parts:
    print(f"  {p.name:24s} {len(p.read_text(encoding='utf-8'))/1024:7.1f} KB")
