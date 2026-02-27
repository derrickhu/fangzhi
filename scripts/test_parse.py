import re
from pathlib import Path

md = Path('宠物美术资源提示词.md').read_text(encoding='utf-8')

# 解析前缀
prefixes = {}
for m in re.finditer(r'### 前缀([ABCD])：.*?\n```\n(.*?)\n```', md, re.DOTALL):
    prefixes[m.group(1)] = m.group(2).strip()[:80] + '...'
print(f'前缀数: {len(prefixes)}')
for k,v in prefixes.items():
    print(f'  {k}: {v}')

# 解析兽灵族
race_match = re.search(r'### 兽灵族（\d+只）', md)
start = race_match.start()
next_race = re.search(r'\n### (?!兽灵族)', md[start+1:])
end = start + 1 + next_race.start() if next_race else len(md)
race_text = md[start:end]

pet_pattern = r'#### (.+?)（(.+?)）— (.+?) (.+?) 兽灵族'
pets = list(re.finditer(pet_pattern, race_text))
print(f'\n兽灵族宠物数: {len(pets)}')

# 验证每只宠物都有4条描述
for i, pm in enumerate(pets):
    cn = pm.group(1)
    pid = pm.group(2)
    ps = pm.start()
    pe = pets[i+1].start() if i+1 < len(pets) else len(race_text)
    blocks = re.findall(r'```\n(.*?)\n```', race_text[ps:pe], re.DOTALL)
    status = "OK" if len(blocks) == 4 else f"WARN({len(blocks)})"
    if i < 5 or status != "OK":
        print(f'  [{i+1}] {cn}({pid}): {status}')

print(f'\n前5只和最后3只:')
for i in list(range(5)) + list(range(len(pets)-3, len(pets))):
    pm = pets[i]
    print(f'  [{i+1}] {pm.group(1)}({pm.group(2)}) — {pm.group(3)} {pm.group(4)}')
