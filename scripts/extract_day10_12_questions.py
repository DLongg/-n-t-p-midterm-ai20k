import json

def extract_questions():
    with open('vlearn-app/src/multiphase_course_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for phase in data.get('phases', []):
        for day in phase.get('days', []):
            day_num = day.get('day_num')
            if day_num in (10, 11, 12):
                for q in day.get('essay_questions', []):
                    questions.append({
                        'day_num': day_num,
                        'question_id': q.get('question_id'),
                        'q_num': q.get('q_num'),
                        'points': q.get('points', 4),
                        'kc_title': q.get('kc_title', ''),
                        'prompt': q.get('interaction', {}).get('prompt', ''),
                        'hints': [h.get('text', '') for h in q.get('hints', [])],
                        'current_rubric': q.get('rubric', ''),
                        'current_explanation': q.get('explanation', '')
                    })
    
    with open('scripts/extracted_day10_12_questions.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(questions)} questions.")

if __name__ == '__main__':
    extract_questions()
