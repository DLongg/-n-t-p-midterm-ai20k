# scripts/author_day12.py
# -*- coding: utf-8 -*-
"""
Day 12 Aggregator: Questions 1 to 73 (d12-q002 to d12-q159)
Combines DAY12_PART1 (36 questions) and DAY12_PART2 (37 questions)
"""

from scripts.day12_part1 import DAY12_PART1
from scripts.day12_part2 import DAY12_PART2

DAY12_DATA = {}
DAY12_DATA.update(DAY12_PART1)
DAY12_DATA.update(DAY12_PART2)

print(f"Loaded Day 12 Complete: {len(DAY12_DATA)} questions.")
