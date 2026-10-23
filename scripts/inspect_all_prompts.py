import json

with open('vlearn-app/src/multiphase_course_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

p1 = data['phases'][0]
days = [d for d in p1['days'] if d.get('day_num') in [7, 8, 9]]

all_items = []
for d in days:
    for q in d.get('essay_questions', []):
        all_items.append({
            'day': d.get('day_num'),
            'id': q.get('question_id'),
            'pts': q.get('points'),
            'kc': q.get('kc_title'),
            'prompt': q.get('interaction', {}).get('prompt', ''),
            'hint': q.get('hints', [{}])[0].get('text', '') if q.get('hints') else ''
        })

print(f"Total extracted: {len(all_items)}")
for day in [7, 8, 9]:
    day_items = [x for x in all_items if x['day'] == day]
    print(f"Day {day}: {len(day_items)} questions, IDs: {day_items[0]['id']} to {day_items[-1]['id']}")
