# scripts/author_day11.py
# -*- coding: utf-8 -*-
"""
Day 11: Guardrails & AI Safety
Aggregates Part 1 and Part 2 (57 questions: d11-q002 to d11-q122)
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.day11_part1 import DAY11_PART1
from scripts.day11_part2 import DAY11_PART2

DAY11_DATA = {}
DAY11_DATA.update(DAY11_PART1)
DAY11_DATA.update(DAY11_PART2)

if __name__ == '__main__':
    print(f"Total Day 11 questions loaded: {len(DAY11_DATA)}")
