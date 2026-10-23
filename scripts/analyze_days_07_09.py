import json

def analyze():
    with open('vlearn-app/src/multiphase_course_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    p1 = data['phases'][0]
    days_7_9 = [d for d in p1['days'] if d.get('day_num') in [7, 8, 9]]

    for d in days_7_9:
        day_num = d.get('day_num')
        eqs = d.get('essay_questions', [])
        print(f"\n==========================================")
        print(f"=== DAY {day_num:02d}: {d.get('day_title')} ({len(eqs)} essay questions) ===")
        print(f"==========================================")
        for i, q in enumerate(eqs, 1):
            qid = q.get('question_id')
            pts = q.get('points')
            kc = q.get('kc_title')
            prompt = q.get('interaction', {}).get('prompt', '').replace('\r\n', '\n').strip()
            hints = [h.get('text', '') for h in q.get('hints', [])]
            print(f"[{i:02d}] {qid} | Points: {pts} | KC: {kc}")
            print(f"    Prompt: {prompt}")
            print(f"    Hints: {hints}")

if __name__ == '__main__':
    import sys
    target_day = int(sys.argv[1]) if len(sys.argv) > 1 else None
    with open('vlearn-app/src/multiphase_course_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    p1 = data['phases'][0]
    days = [d for d in p1['days'] if d.get('day_num') in ([target_day] if target_day else [7, 8, 9])]

    for d in days:
        day_num = d.get('day_num')
        eqs = d.get('essay_questions', [])
        print(f"\n==========================================")
        print(f"=== DAY {day_num:02d}: {d.get('day_title')} ({len(eqs)} essay questions) ===")
        print(f"==========================================")
        for i, q in enumerate(eqs, 1):
            qid = q.get('question_id')
            pts = q.get('points')
            kc = q.get('kc_title')
            prompt = q.get('interaction', {}).get('prompt', '').replace('\r\n', '\n').strip()
            hints = [h.get('text', '') for h in q.get('hints', [])]
            print(f"[{i:02d}] {qid} | Points: {pts} | KC: {kc}")
            print(f"    Prompt: {prompt}")
            print(f"    Hints: {hints}")
