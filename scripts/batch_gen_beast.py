#!/usr/bin/env python3
"""
批量生成兽灵族52只宠物的图片（4张/只）+ 全身图抠图
调用 gemini-image-gen skill 生成图片，rembg 去背景。
已存在的文件自动跳过。
"""
import os, sys, re, time, subprocess
from pathlib import Path

# ── 配置 ──
PROJECT_DIR = Path(__file__).resolve().parent.parent
PROMPTS_MD = PROJECT_DIR / "宠物美术资源提示词.md"
OUTPUT_DIR = PROJECT_DIR / "assets" / "pets_gen"
SKILL_SCRIPT = Path.home() / ".codebuddy" / "skills" / "gemini-image-gen" / "scripts" / "generate_images.py"
RACE_FILTER = "兽灵族"
DELAY_BETWEEN_CALLS = 6  # 秒，避免 rate limit

# 分辨率后缀
RES_FULL = " Resolution: 512x512px target, the character should fill about 70-80% of the canvas height."
RES_AVATAR = " Resolution: 128x128px target, circular crop friendly composition."

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def parse_prefixes(text):
    prefixes = {}
    for m in re.finditer(r'### 前缀([ABCD])：.*?\n```\n(.*?)\n```', text, re.DOTALL):
        prefixes[m.group(1)] = m.group(2).strip()
    return prefixes


def parse_race_pets(text, race):
    pets = []
    race_pattern = rf'### {re.escape(race)}（\d+只）'
    race_match = re.search(race_pattern, text)
    if not race_match:
        return pets
    start = race_match.start()
    next_race = re.search(r'\n### (?!' + re.escape(race) + r')', text[start+1:])
    end = start + 1 + next_race.start() if next_race else len(text)
    race_text = text[start:end]

    pet_pattern = r'#### (.+?)（(.+?)）— (.+?) (.+?) ' + re.escape(race)
    pet_matches = list(re.finditer(pet_pattern, race_text))
    for i, pm in enumerate(pet_matches):
        ps = pm.start()
        pe = pet_matches[i+1].start() if i+1 < len(pet_matches) else len(race_text)
        blocks = re.findall(r'```\n(.*?)\n```', race_text[ps:pe], re.DOTALL)
        if len(blocks) == 4:
            pets.append({
                'cn_name': pm.group(1), 'pet_id': pm.group(2),
                'rarity': pm.group(3), 'element': pm.group(4),
                'descs': {
                    'normal_full': blocks[0].strip(),
                    'normal_avatar': blocks[1].strip(),
                    'awakened_full': blocks[2].strip(),
                    'awakened_avatar': blocks[3].strip(),
                }
            })
    return pets


def generate_image(prompt_text, output_path):
    """调用 skill 脚本生成图片"""
    # 先写 prompt 到临时文件（避免 shell 参数长度限制）
    prompt_file = output_path.with_suffix('.prompt.tmp')
    prompt_file.write_text(prompt_text, encoding='utf-8')
    
    cmd = [
        sys.executable, str(SKILL_SCRIPT),
        '--prompt-file', str(prompt_file),
        '--output', str(output_path),
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        prompt_file.unlink(missing_ok=True)  # 清理临时文件
        if result.returncode == 0 and output_path.exists():
            return True
        else:
            stderr = result.stderr.strip()[-200:] if result.stderr else ''
            stdout = result.stdout.strip()[-200:] if result.stdout else ''
            print(f"    FAIL: rc={result.returncode} {stderr or stdout}", flush=True)
            return False
    except subprocess.TimeoutExpired:
        prompt_file.unlink(missing_ok=True)
        print(f"    TIMEOUT", flush=True)
        return False
    except Exception as e:
        prompt_file.unlink(missing_ok=True)
        print(f"    ERROR: {e}", flush=True)
        return False


def main():
    if not SKILL_SCRIPT.exists():
        print(f"ERROR: skill 脚本不存在: {SKILL_SCRIPT}")
        sys.exit(1)

    print("读取提示词文档...", flush=True)
    md_text = PROMPTS_MD.read_text(encoding='utf-8')
    prefixes = parse_prefixes(md_text)
    print(f"前缀: {len(prefixes)} 个", flush=True)

    pets = parse_race_pets(md_text, RACE_FILTER)
    print(f"{RACE_FILTER}: {len(pets)} 只宠物\n", flush=True)

    img_types = [
        ('normal_full', 'A', RES_FULL),
        ('normal_avatar', 'B', RES_AVATAR),
        ('awakened_full', 'C', RES_FULL),
        ('awakened_avatar', 'D', RES_AVATAR),
    ]

    stats = {'gen': 0, 'skip': 0, 'fail': 0, 'nobg': 0, 'nobg_skip': 0}

    for pi, pet in enumerate(pets):
        pid = pet['pet_id']
        cn = pet['cn_name']
        print(f"[{pi+1}/{len(pets)}] {cn} ({pid}) — {pet['rarity']} {pet['element']}", flush=True)

        full_img_paths = []

        for img_type, prefix_key, res_suffix in img_types:
            fname = f"{pid}_{img_type}.png"
            out_path = OUTPUT_DIR / fname

            if out_path.exists() and out_path.stat().st_size > 1000:
                print(f"  {img_type}: 已存在({out_path.stat().st_size//1024}KB)，跳过", flush=True)
                stats['skip'] += 1
                if 'full' in img_type:
                    full_img_paths.append((img_type, out_path))
                continue

            # 拼接完整 prompt
            full_prompt = f"{prefixes[prefix_key]} {pet['descs'][img_type]}{res_suffix}"

            # 同时保存 prompt 文本备用
            (OUTPUT_DIR / f"prompt_{pid}_{img_type}.txt").write_text(full_prompt, encoding='utf-8')

            print(f"  {img_type}: 生成中...", end=" ", flush=True)
            t0 = time.time()
            ok = generate_image(full_prompt, out_path)
            elapsed = time.time() - t0

            if ok:
                kb = out_path.stat().st_size / 1024
                print(f"OK ({elapsed:.1f}s, {kb:.0f}KB)", flush=True)
                stats['gen'] += 1
                if 'full' in img_type:
                    full_img_paths.append((img_type, out_path))
            else:
                print(f"FAILED ({elapsed:.1f}s)", flush=True)
                stats['fail'] += 1

            time.sleep(DELAY_BETWEEN_CALLS)

        # 全身图抠图
        for img_type, fpath in full_img_paths:
            nobg_path = OUTPUT_DIR / f"{pid}_{img_type}_nobg.png"
            if nobg_path.exists() and nobg_path.stat().st_size > 500:
                print(f"  {img_type}_nobg: 已存在，跳过", flush=True)
                stats['nobg_skip'] += 1
                continue
            if not fpath.exists():
                continue
            print(f"  {img_type}_nobg: 抠图中...", end=" ", flush=True)
            t0 = time.time()
            try:
                remove_bg(fpath, nobg_path)
                kb = nobg_path.stat().st_size / 1024
                print(f"OK ({time.time()-t0:.1f}s, {kb:.0f}KB)", flush=True)
                stats['nobg'] += 1
            except Exception as e:
                print(f"FAILED: {e}", flush=True)

    print(f"\n{'='*50}", flush=True)
    print(f"完成！{RACE_FILTER} {len(pets)} 只宠物", flush=True)
    print(f"  图片生成: {stats['gen']} 张", flush=True)
    print(f"  图片跳过: {stats['skip']} 张（已存在）", flush=True)
    print(f"  图片失败: {stats['fail']} 张", flush=True)
    print(f"  抠图完成: {stats['nobg']} 张", flush=True)
    print(f"  抠图跳过: {stats['nobg_skip']} 张（已存在）", flush=True)


# ── rembg 抠图 ──
_rembg_session = None

def remove_bg(input_path, output_path):
    os.environ["OMP_NUM_THREADS"] = "8"
    from rembg import remove, new_session
    from PIL import Image
    global _rembg_session
    if _rembg_session is None:
        providers = ['CPUExecutionProvider']
        print("\n  加载 rembg birefnet-general...", end=" ", flush=True)
        t0 = time.time()
        _rembg_session = new_session("birefnet-general", providers=providers)
        print(f"OK ({time.time()-t0:.1f}s)\n  ", end="", flush=True)
    inp = Image.open(str(input_path))
    out = remove(inp, session=_rembg_session)
    out.save(str(output_path))


if __name__ == '__main__':
    main()
