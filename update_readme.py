#!/usr/bin/env python3
"""
update_readme.py — Regenera el README leyendo los metadatos del repo.
Uso: python update_readme.py
"""

import re
import os
from pathlib import Path
from datetime import datetime
from collections import Counter

ROOT = Path(__file__).parent

ALGORITHMS_DIR = ROOT / "algorithms"
PROJECTS_DIR   = ROOT / "mini_projects"

HEADER_PATTERN = {
    "day":        r"# Day (\d+)",
    "title":      r"# Day \d+ [—-] (.+)",
    "difficulty": r"Difficulty:\s*(\w+)",
    "type":       r"Type:\s*(.+?)(?:\s*\||\s*$)",
    "time":       r"Time:\s*(.+?)(?:\s*\||\s*$)",
    "tags":       r"Tags:\s*(.+)",
    "source":     r"Source:\s*(.+)",
}

DIFF_EMOJI = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
TYPE_EMOJI = {"Algorithm": "⚙️", "Project": "🛠️"}

def parse_file(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None

    header = "\n".join(text.splitlines()[:10])
    data = {}
    for key, pat in HEADER_PATTERN.items():
        m = re.search(pat, header, re.MULTILINE)
        data[key] = m.group(1).strip() if m else "—"

    if data["day"] == "—":
        return None
    return data

def collect_challenges() -> list[dict]:
    challenges = []
    for directory in [ALGORITHMS_DIR, PROJECTS_DIR]:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.py")):
            if path.name.startswith("_"):
                continue
            parsed = parse_file(path)
            if parsed:
                parsed["path"] = str(path.relative_to(ROOT))
                challenges.append(parsed)

    challenges.sort(key=lambda x: x["day"])
    return challenges

def tag_stats(challenges: list[dict]) -> Counter:
    counter = Counter()
    for c in challenges:
        if c["tags"] != "—":
            for tag in c["tags"].split():
                counter[tag.strip()] += 1
    return counter

def build_readme(challenges: list[dict]) -> str:
    total      = len(challenges)
    algorithms = sum(1 for c in challenges if "Algorithm" in c.get("type", ""))
    projects   = sum(1 for c in challenges if "Project" in c.get("type", ""))
    tags       = tag_stats(challenges)
    updated    = datetime.now().strftime("%d %b %Y")

    easy   = sum(1 for c in challenges if c["difficulty"] == "Easy")
    medium = sum(1 for c in challenges if c["difficulty"] == "Medium")
    hard   = sum(1 for c in challenges if c["difficulty"] == "Hard")

    rows = ""
    for c in challenges:
        diff_icon = DIFF_EMOJI.get(c["difficulty"], "⬜")
        type_icon = TYPE_EMOJI.get(c["type"].strip(), "📄")
        link = f"[{c['title']}]({c['path']})"
        rows += (
            f"| {c['day']} | {type_icon} {link} | "
            f"{diff_icon} {c['difficulty']} | "
            f"{c['time']} | {c['tags']} |\n"
        )

    if not rows:
        rows = "| — | *Aún no hay desafíos. ¡Empieza hoy!* | — | — | — |\n"

    top_tags = " ".join(
        f"`{tag}` ×{count}"
        for tag, count in tags.most_common(8)
    ) or "*Sin tags aún*"

    return f"""\
# 🐍 Daily Challenges

> Un desafío de programación al día — mix de algoritmos y mini proyectos en Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Challenges](https://img.shields.io/badge/Challenges-{total}-brightgreen?style=flat-square)
![Last update](https://img.shields.io/badge/Updated-{updated.replace(' ', '%20')}-lightgrey?style=flat-square)

---

## 📊 Stats

| Total | ⚙️ Algoritmos | 🛠️ Proyectos | 🟢 Easy | 🟡 Medium | 🔴 Hard |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **{total}** | {algorithms} | {projects} | {easy} | {medium} | {hard} |

---

## 📁 Estructura

```
daily-challenges/
├── algorithms/       # Problemas tipo LeetCode
├── mini_projects/    # Proyectos pequeños funcionales
├── utils/            # Scripts reutilizables
├── update_readme.py  # Este script
└── README.md         # Autogenerado ← no editar a mano
```

---

## 🗓️ Log de desafíos

| Día | Nombre | Dificultad | Tiempo | Tags |
|:---:|---|:---:|:---:|---|
{rows}
---

## 🏷️ Tags más usados

{top_tags}

---

## 📋 Template para cada archivo

```python
# Day XXX — Nombre del desafío
# Difficulty: Easy | Type: Algorithm
# Time: XX min | Tags: #tag1 #tag2
# Source: LeetCode X / propio
# ─────────────────────────────────
# Problema:
# descripción breve
# ─────────────────────────────────

def solucion():
    pass

# Complejidad: O(?) tiempo, O(?) espacio
# Aprendizaje: qué aprendiste o qué harías diferente
```

---

## 🔗 Recursos

- [LeetCode](https://leetcode.com) — algoritmos
- [Exercism Python](https://exercism.org/tracks/python) — ejercicios con feedback
- [Python Docs](https://docs.python.org/3/) — referencia oficial

---

*⚡ README autogenerado por `update_readme.py` · {updated}*
"""

def main():
    challenges = collect_challenges()
    readme = build_readme(challenges)
    output = ROOT / "README.md"
    output.write_text(readme, encoding="utf-8")
    print(f"✅ README actualizado — {len(challenges)} desafío(s) encontrado(s).")

if __name__ == "__main__":
    main()