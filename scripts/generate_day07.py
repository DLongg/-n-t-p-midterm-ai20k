# -*- coding: utf-8 -*-
"""
Day 07 Full Generator: Merges Part 1 (23 questions) and Part 2 (22 questions) = 45 questions.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.day07_part1 import DAY_07_PART1
from scripts.day07_part2 import DAY_07_PART2

DAY_07_ALL = {}
DAY_07_ALL.update(DAY_07_PART1)
DAY_07_ALL.update(DAY_07_PART2)

if __name__ == '__main__':
    print(f"Total Day 07 questions assembled: {len(DAY_07_ALL)}")
    for qid, data in sorted(DAY_07_ALL.items()):
        assert len(data['sample_answer']) >= 150, f"{qid} answer too short: {len(data['sample_answer'])}"
        assert 'rubric' in data and len(data['rubric']) > 20
        assert 'explanation' in data and len(data['explanation']) > 20
        assert 'reference_source' in data and len(data['reference_source']) > 10
    print("All 45 Day 07 questions validated successfully!")
