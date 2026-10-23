import json
from pathlib import Path

files = [
    Path("data/essay_block_01_03.json"),
    Path("vlearn-app/src/multiphase_course_data.json"),
]

def clean_obj(obj):
    mod = False
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str):
                if "\x0c" in v:
                    obj[k] = v.replace("\x0crac", r"\frac").replace("\x0c", "")
                    mod = True
            elif isinstance(v, (dict, list)):
                if clean_obj(v):
                    mod = True
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)):
                if clean_obj(item):
                    mod = True
    return mod

for p in files:
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)

    if clean_obj(data):
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Cleaned illegal control characters in {p}")
    else:
        print(f"No illegal control characters in {p}")
