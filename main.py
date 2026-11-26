import os

LINE = "fix: fixed the fix that fixed the fix — 3am me says sorry, 3:05am me says ship it"

assert 1 <= len(LINE) <= 139
assert LINE.strip()

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
