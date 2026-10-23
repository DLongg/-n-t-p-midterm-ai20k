"""
Unified Day 02 essay authoring module.
Merges Day 02 Part 1 (42 questions) and Part 2 (44 questions) to provide all 86 questions.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.author_day02_part1 import get_day02_part1_data
from scripts.author_day02_part2 import get_day02_part2_data

def get_day02_data():
    data = {}
    data.update(get_day02_part1_data())
    data.update(get_day02_part2_data())
    return data

if __name__ == "__main__":
    d02 = get_day02_data()
    print(f"Total Day 02 questions loaded: {len(d02)}")
