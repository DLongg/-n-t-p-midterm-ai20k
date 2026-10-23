# -*- coding: utf-8 -*-
"""
Build and validate data/essay_block_07_09.json
Contains exactly 148 essay questions for Days 07, 08, 09.
"""

import sys
import os
import json
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.generate_day07 import DAY_07_ALL
from scripts.generate_day08 import DAY_08_ALL
from scripts.generate_day09 import DAY_09_ALL

OUTPUT_FILE = 'data/essay_block_07_09.json'
COURSE_DATA_FILE = 'vlearn-app/src/multiphase_course_data.json'

def build_block():
    merged_block = {}
    merged_block.update(DAY_07_ALL)
    merged_block.update(DAY_08_ALL)
    merged_block.update(DAY_09_ALL)

    print(f"Total entries in merged block: {len(merged_block)}")
    assert len(merged_block) == 148, f"Expected 148 questions, got {len(merged_block)}"

    # Load master course data to verify IDs and point values
    with open(COURSE_DATA_FILE, 'r', encoding='utf-8') as f:
        course_data = json.load(f)

    p1 = course_data['phases'][0]
    expected_days = [d for d in p1['days'] if d.get('day_num') in [7, 8, 9]]
    
    expected_ids = {}
    for d in expected_days:
        day_num = d.get('day_num')
        for q in d.get('essay_questions', []):
            qid = q.get('question_id')
            expected_ids[qid] = {
                'day': day_num,
                'points': q.get('points'),
                'prompt': q.get('interaction', {}).get('prompt'),
                'hints': [h.get('text', '') for h in q.get('hints', [])]
            }

    print(f"Total expected essay questions in Days 07-09: {len(expected_ids)}")
    assert len(expected_ids) == 148

    # Check that all expected IDs are present
    missing_ids = set(expected_ids.keys()) - set(merged_block.keys())
    extra_ids = set(merged_block.keys()) - set(expected_ids.keys())

    assert len(missing_ids) == 0, f"Missing IDs in block: {missing_ids}"
    assert len(extra_ids) == 0, f"Extra unexpected IDs in block: {extra_ids}"

    # Validate each item thoroughly
    boilerplate_pattern = re.compile(r"Đúng bản chất vấn đề và yêu cầu kỹ thuật|Đầy đủ các tiêu chí chấp nhận")
    
    short_answers = []
    boilerplate_items = []
    missing_fields = []
    
    for qid, item in merged_block.items():
        exp_meta = expected_ids[qid]
        pts = exp_meta['points']

        for field in ['sample_answer', 'explanation', 'rubric', 'reference_source']:
            if field not in item or not item[field] or len(item[field].strip()) == 0:
                missing_fields.append((qid, field))

        # Length check
        ans_len = len(item.get('sample_answer', '').strip())
        if ans_len < 150:
            short_answers.append((qid, ans_len))

        # Boilerplate check
        rubric_text = item.get('rubric', '')
        expl_text = item.get('explanation', '')
        if boilerplate_pattern.search(rubric_text):
            boilerplate_items.append((qid, 'rubric'))

        # Check if explanation merely repeats hint
        for hint in exp_meta['hints']:
            if hint and hint.strip() in expl_text and len(expl_text.strip()) < len(hint.strip()) + 30:
                boilerplate_items.append((qid, 'explanation_equals_hint'))

        # Rubric point mentions
        rubric_point_str = f"Rubric {pts} điểm"
        if rubric_point_str not in rubric_text and f"Rubric {pts}.0 điểm" not in rubric_text:
            print(f"Warning: {qid} rubric might not mention expected {pts} points header: {rubric_text[:60]}")

    assert len(missing_fields) == 0, f"Missing fields: {missing_fields}"
    assert len(short_answers) == 0, f"Short answers: {short_answers}"
    assert len(boilerplate_items) == 0, f"Boilerplate detected: {boilerplate_items}"

    # Write output JSON file
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(merged_block, f, ensure_ascii=False, indent=2)

    print(f"\n=======================================================")
    print(f"SUCCESS: Written {len(merged_block)} questions to {OUTPUT_FILE}")
    print(f"File size: {os.path.getsize(OUTPUT_FILE):,} bytes")
    print(f"=======================================================")

if __name__ == '__main__':
    build_block()
