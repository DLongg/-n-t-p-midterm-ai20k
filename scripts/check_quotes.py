with open('scripts/author_day02_part2.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    s = l.strip()
    if s.startswith('""') or s.endswith('""') or s.endswith('"",') or '""' in s:
        print(f"Line {i+1}: {repr(s)}")
