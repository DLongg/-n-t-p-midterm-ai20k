# scripts/author_day10.py
# -*- coding: utf-8 -*-
"""
Day 10: Data Pipeline & Observability
Aggregates Part 1 and Part 2 (48 questions: d10-q001 to d10-q108)
"""
import sys
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.day10_part1 import DAY10_PART1
from scripts.day10_part2 import DAY10_PART2

DAY10_DATA = {}
DAY10_DATA.update(DAY10_PART1)
DAY10_DATA.update(DAY10_PART2)

if __name__ == '__main__':
    print(f"Total Day 10 questions loaded: {len(DAY10_DATA)}")
