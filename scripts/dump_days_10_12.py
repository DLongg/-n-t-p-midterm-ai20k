import json

def main():
    with open('vlearn-app/src/multiphase_course_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for phase in data.get('phases', []):
        for day in phase.get('days', []):
            day_num = day.get('day_num')
            if day_num in (10, 11, 12):
                eqs = day.get('essay_questions', [])
                print(f"=== Day {day_num}: {day.get('title')} ({len(eqs)} questions) ===")
                for i in [0, len(eqs)//2, len(eqs)-1]:
                    q = eqs[i]
                    print(f"Index {i} | ID: {q.get('question_id')} | Pts: {q.get('points')} | KC: {q.get('kc_title')}")
                    print(f"Prompt: {q.get('interaction', {}).get('prompt')}")
                    print(f"Rubric: {repr(q.get('rubric'))}")
                    print(f"Explanation: {repr(q.get('explanation'))}")
                    print(f"Hints: {q.get('hints')}")
                    print("-" * 50)

if __name__ == '__main__':
    main()
