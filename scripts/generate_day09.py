# -*- coding: utf-8 -*-
"""
Day 09 Full Generator: Merges Part 1 (24 questions) and Part 2 (24 questions) = 48 questions.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.day09_part1 import DAY_09_PART1
from scripts.day09_part2 import DAY_09_PART2

DAY_09_ALL = {}
DAY_09_ALL.update(DAY_09_PART1)
DAY_09_ALL.update(DAY_09_PART2)

if __name__ == '__main__':
    print(f"Total Day 09 questions assembled: {len(DAY_09_ALL)}")
    for qid, data in sorted(DAY_09_ALL.items()):
        assert len(data['sample_answer']) >= 150, f"{qid} answer too short: {len(data['sample_answer'])}"
        assert 'rubric' in data and len(data['rubric']) > 20
        assert 'explanation' in data and len(data['explanation']) > 20
        assert 'reference_source' in data and len(data['reference_source']) > 10
    print("All 48 Day 09 questions validated successfully!")
