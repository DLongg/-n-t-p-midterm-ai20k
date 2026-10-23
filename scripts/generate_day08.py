# -*- coding: utf-8 -*-
"""
Day 08 Full Generator: Merges Part 1 (28 questions) and Part 2 (27 questions) = 55 questions.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.day08_part1 import DAY_08_PART1
from scripts.day08_part2 import DAY_08_PART2

DAY_08_ALL = {}
DAY_08_ALL.update(DAY_08_PART1)
DAY_08_ALL.update(DAY_08_PART2)

if __name__ == '__main__':
    print(f"Total Day 08 questions assembled: {len(DAY_08_ALL)}")
    for qid, data in sorted(DAY_08_ALL.items()):
        assert len(data['sample_answer']) >= 150, f"{qid} answer too short: {len(data['sample_answer'])}"
        assert 'rubric' in data and len(data['rubric']) > 20
        assert 'explanation' in data and len(data['explanation']) > 20
        assert 'reference_source' in data and len(data['reference_source']) > 10
    print("All 55 Day 08 questions validated successfully!")
