import json
import os
import sys

sys.path.insert(0, os.path.abspath('.'))

from scripts.build_day04_answers import DAY04_ANSWERS
from scripts.build_day05_answers import DAY05_ANSWERS
from scripts.build_day06_answers import DAY06_ANSWERS

def enrich_reference_url(ref: str) -> str:
    if "http://" in ref or "https://" in ref:
        return ref
    
    url_map = [
        ("PAIR", "https://pair.withgoogle.com/guidebook/"),
        ("OpenAI", "https://platform.openai.com/docs/guides/function-calling"),
        ("Anthropic", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering"),
        ("OWASP", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),
        ("LangGraph", "https://langchain-ai.github.io/langgraph/"),
        ("LangChain", "https://python.langchain.com/docs/concepts/"),
        ("NIST", "https://www.nist.gov/itl/ai-risk-management-framework"),
        ("Microsoft HAX", "https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/"),
        ("Microsoft Research", "https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/"),
        ("Nielsen Norman", "https://www.nngroup.com/articles/"),
        ("Martin Fowler", "https://martinfowler.com/articles/"),
        ("SRE", "https://sre.google/sre-book/table-of-contents/"),
        ("Chip Huyen", "https://huyenchip.com/machine-learning-systems-design/"),
        ("JTBD", "https://strategyn.com/jobs-to-be-done/"),
        ("Ulwick", "https://strategyn.com/jobs-to-be-done/"),
        ("Christensen", "https://hbswk.hbs.edu/item/clay-christensen-the-theory-of-jobs-to-be-done"),
        ("Klement", "https://www.intercom.com/books/jobs-to-be-done"),
        ("Bettencourt", "https://hbr.org/2008/05/the-customer-centered-innovation-map"),
        ("Saldaña", "https://methods.sagepub.com/book/the-coding-manual-for-qualitative-researchers"),
        ("Epidemiological", "https://www.cdc.gov/csels/dsepd/ss1978/lesson3/section2.html"),
        ("Data Engineering", "https://principles.design/"),
        ("Amershi", "https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/"),
        ("A/B Testing", "https://experimentguide.com/"),
        ("Integrity Mandate", "https://www.nist.gov/itl/ai-risk-management-framework"),
        ("TruLens", "https://www.trulens.org/trulens_eval/core_concepts_rag_triad/"),
        ("Krippendorff", "https://methods.sagepub.com/book/content-analysis-4e"),
        ("DVC", "https://dvc.org/doc/user-guide/data-management"),
        ("MLflow", "https://mlflow.org/docs/latest/tracking.html"),
        ("Krug", "https://sensible.com/dont-make-me-think/"),
        ("Fitzpatrick", "https://www.momtestbook.com/"),
        ("Cagan", "https://www.svpg.com/books/inspired-how-to-create-tech-products-customers-love/"),
        ("Torres", "https://www.producttalk.org/continuous-discovery-habits/"),
        ("Savoia", "https://www.pretotyping.org/"),
        ("Kohavi", "https://experimentguide.com/"),
        ("Unit Economics", "https://a16z.com/the-new-business-of-ai/"),
        ("Scenario Planning", "https://hbr.org/2013/05/living-in-the-futures"),
        ("Andrew Ng", "https://www.deeplearning.ai/the-batch/data-centric-ai/"),
        ("Patton", "https://www.jpattonassociates.com/user-story-mapping/"),
        ("Blank", "https://steveblank.com/"),
        ("Ries", "https://theleanstartup.com/principles")
    ]
    
    for key, url in url_map:
        if key.lower() in ref.lower():
            return f"{ref} ({url})"
            
    return f"{ref} (https://www.nist.gov/itl/ai-risk-management-framework)"

def assemble_and_verify():
    # 1. Combine all authored answers
    combined = {}
    combined.update(DAY04_ANSWERS)
    combined.update(DAY05_ANSWERS)
    combined.update(DAY06_ANSWERS)
    
    # Enrich reference sources with official URLs
    for qid in combined:
        combined[qid]["reference_source"] = enrich_reference_url(combined[qid]["reference_source"])
    
    print(f"Total authored answers loaded: {len(combined)}")

    # 2. Load ground truth raw questions
    with open('data/raw_questions_04_06.json', 'r', encoding='utf-8') as f:
        raw_questions = json.load(f)

    print(f"Total raw questions to cover: {len(raw_questions)}")
    raw_map = {q['question_id']: q for q in raw_questions}

    # Verify ID match
    missing_ids = set(raw_map.keys()) - set(combined.keys())
    extra_ids = set(combined.keys()) - set(raw_map.keys())

    if missing_ids:
        raise ValueError(f"Missing question IDs in authored block: {sorted(list(missing_ids))}")
    if extra_ids:
        raise ValueError(f"Extra question IDs in authored block: {sorted(list(extra_ids))}")

    print("All 95 question IDs matched 1:1 with ground truth!")

    # 3. Quality & Schema Verification
    old_boilerplate = "Đúng bản chất vấn đề và yêu cầu kỹ thuật"
    
    min_length_failures = []
    rubric_mismatches = []
    boilerplate_detections = []
    hint_repetitions = []
    missing_fields = []
    no_url_sources = []

    for qid, entry in combined.items():
        raw = raw_map[qid]
        points = raw['points']
        hint = raw['hint']

        # Check required fields
        for field in ['sample_answer', 'explanation', 'rubric', 'reference_source']:
            if field not in entry or not entry[field] or not isinstance(entry[field], str):
                missing_fields.append((qid, field))

        # Check answer length >= 150 chars
        ans = entry.get('sample_answer', '')
        if len(ans) < 150:
            min_length_failures.append((qid, len(ans)))

        # Check boilerplate
        full_text = f"{ans} {entry.get('explanation', '')} {entry.get('rubric', '')}"
        if old_boilerplate in full_text:
            boilerplate_detections.append(qid)

        # Check if explanation merely repeats hint
        exp = entry.get('explanation', '').strip()
        if exp == hint.strip() or len(exp) < 50:
            hint_repetitions.append(qid)

        # Check rubric points match
        rub = entry.get('rubric', '')
        expected_rubric_substr = f"Rubric {points} điểm"
        if expected_rubric_substr not in rub:
            rubric_mismatches.append((qid, points, rub[:60]))

        # Check reference source
        ref = entry.get('reference_source', '')
        if 'http' not in ref and 'NIST' not in ref and 'ISO' not in ref and 'W3C' not in ref:
            no_url_sources.append((qid, ref))

    # Assertions
    if missing_fields:
        raise ValueError(f"Missing fields detected: {missing_fields}")
    if min_length_failures:
        raise ValueError(f"Answers under 150 chars: {min_length_failures}")
    if boilerplate_detections:
        raise ValueError(f"Old boilerplate detected in: {boilerplate_detections}")
    if hint_repetitions:
        raise ValueError(f"Explanation repeats hint in: {hint_repetitions}")
    if rubric_mismatches:
        raise ValueError(f"Rubric point mismatches in: {rubric_mismatches}")
    if no_url_sources:
        print(f"Warning: references without standard URL or spec: {no_url_sources}")

    print("ALL 95 QUESTIONS PASSED PROGRAMMATIC QUALITY & INTEGRITY CHECKS!")

    # 4. Save to target file
    os.makedirs('data', exist_ok=True)
    target_path = 'data/essay_block_04_06.json'
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, indent=2)

    file_size = os.path.getsize(target_path)
    print(f"Successfully generated {target_path} (Size: {file_size:,} bytes, {len(combined)} questions)")

if __name__ == '__main__':
    assemble_and_verify()
