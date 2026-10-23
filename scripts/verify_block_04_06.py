import json
from pathlib import Path

def test_chunk_04_06():
    chunk_path = Path("data/essay_block_04_06.json")
    assert chunk_path.exists(), "essay_block_04_06.json missing"
    
    with open(chunk_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. Exact count: 95
    assert len(data) == 95, f"Expected 95 questions, got {len(data)}"
    
    # 2. Check each day's count
    d4 = [k for k in data if k.startswith("d04-")]
    d5 = [k for k in data if k.startswith("d05-")]
    d6 = [k for k in data if k.startswith("d06-")]
    assert len(d4) == 30, f"Expected 30 in Day 4, got {len(d4)}"
    assert len(d5) == 38, f"Expected 38 in Day 5, got {len(d5)}"
    assert len(d6) == 27, f"Expected 27 in Day 6, got {len(d6)}"

    # 3. Check each item fields, lengths, boilerplate
    old_boilerplate = "Đúng bản chất vấn đề và yêu cầu kỹ thuật"
    
    for qid, item in data.items():
        assert "sample_answer" in item, f"Missing sample_answer in {qid}"
        assert "explanation" in item, f"Missing explanation in {qid}"
        assert "rubric" in item, f"Missing rubric in {qid}"
        assert "reference_source" in item, f"Missing reference_source in {qid}"
        
        ans = item["sample_answer"]
        exp = item["explanation"]
        rub = item["rubric"]
        ref = item["reference_source"]
        
        assert len(ans.strip()) >= 150, f"Answer too short in {qid}: {len(ans)} chars"
        assert len(exp.strip()) >= 50, f"Explanation too short in {qid}: {len(exp)} chars"
        assert len(rub.strip()) >= 50, f"Rubric too short in {qid}: {len(rub)} chars"
        assert len(ref.strip()) >= 10, f"Reference too short in {qid}: {len(ref)} chars"
        
        assert old_boilerplate not in ans, f"Old boilerplate in sample_answer of {qid}"
        assert old_boilerplate not in exp, f"Old boilerplate in explanation of {qid}"
        assert old_boilerplate not in rub, f"Old boilerplate in rubric of {qid}"
        
        assert "http" in ref or "NIST" in ref or "ISO" in ref or "W3C" in ref, f"Invalid reference in {qid}: {ref}"

    print(f"VERIFICATION SUCCESS: All 95 essay questions in {chunk_path} meet 100% of quality criteria!")

if __name__ == '__main__':
    test_chunk_04_06()
