"""
Unified Day 03 essay authoring module.
Merges Day 03 Part 1 (26 questions) and Part 2 (26 questions) to provide all 52 questions.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.author_day03_part1 import get_day03_part1_data
from scripts.author_day03_part2 import get_day03_part2_data

def get_day03_data():
    data = {}
    data.update(get_day03_part1_data())
    data.update(get_day03_part2_data())
    return data

if __name__ == "__main__":
    d03 = get_day03_data()
    print(f"Total Day 03 questions loaded: {len(d03)}")
