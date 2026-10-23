import json
import sys

def inspect_days(start_day, end_day):
    with open("data/judge_evaluation_raw.json", "r", encoding="utf-8") as f:
        items = json.load(f)

    for day in range(start_day, end_day + 1):
        print(f"\n==================== DAY {day:02d} ====================")
        day_items = [it for it in items if it["day"] == f"Day {day:02d}"]
        for it in day_items:
            print(f"\n--- [{it['qid']}] (Points: {it['points']}) ---")
            print(f"PROMPT:\n{it['full_prompt']}")
            print(f"\nSAMPLE ANSWER:\n{it['sample_answer']}")
            print(f"\nRUBRIC:\n{it['rubric']}")
            print(f"\nREFERENCE SOURCE:\n{it['reference_source']}")
            print("-" * 70)

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end = int(sys.argv[2]) if len(sys.argv) > 2 else start
    inspect_days(start, end)
