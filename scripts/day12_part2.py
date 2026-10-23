# scripts/day12_part2.py
# -*- coding: utf-8 -*-
"""
Day 12 Part 2 Aggregator: Questions 37 to 73 (d12-q079 to d12-q159)
"""

from scripts.day12_part2_a import DAY12_PART2_A
from scripts.day12_part2_b import DAY12_PART2_B
from scripts.day12_part2_c import DAY12_PART2_C

DAY12_PART2 = {}
DAY12_PART2.update(DAY12_PART2_A)
DAY12_PART2.update(DAY12_PART2_B)
DAY12_PART2.update(DAY12_PART2_C)

print(f"Loaded Day 12 Part 2 complete: {len(DAY12_PART2)} questions.")
