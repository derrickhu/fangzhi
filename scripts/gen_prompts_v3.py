#!/usr/bin/env python3
"""
Generate all 236 pet prompts for v3 design.
Reads pet data from 宠物设计和合成方案v3.md, generates prompts using templates.
Output: 宠物美术资源提示词v3.md + individual prompt txt files
"""
import os, re, sys
from pet_desc_en import DESC_EN

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT = os.path.join(BASE, "宠物设计和合成方案v3.md")
OUTPUT = os.path.join(BASE, "宠物美术资源提示词v3.md")
PROMPT_DIR = os.path.join(BASE, "assets", "pets_gen")

# ─── Style blocks ───
S_AV = "chibi 2D Chinese ink wash painting game character icon, super deformed cute style, big head small body ratio 2:1, Chinese calligraphy brush-style black ink outlines with varying thickness and expressive brush stroke feel, ink wash coloring with subtle tonal gradation and soft layered shading to create gentle volume and three-dimensional depth, light and shadow rendered through ink density variation — lighter wash on highlighted areas and denser ink in recessed folds and under the chin and belly, rich varied color palette mixing traditional Chinese mineral pigments with natural animal tones, Chinese Xianxia mythology aesthetic, NOT Western fantasy, NOT realistic, NOT 3D rendered, square 1:1 aspect ratio, close-up showing oversized head and upper shoulders, solid plain single-color background light gray #E0E0E0, expressive ink-painted eyes with reflective highlights, game icon style, clean sharp ink-line edges for easy cutout."

S_FL = "chibi 2D Chinese ink wash painting game character, super deformed cute style, big head small body ratio 2:1, Chinese calligraphy brush-style black ink outlines with varying thickness and expressive brush stroke feel, ink wash coloring with subtle tonal gradation and soft layered shading to create gentle volume and three-dimensional depth, light and shadow rendered through ink density variation — lighter wash on highlighted areas and denser ink in recessed folds and under limbs, rich varied color palette mixing traditional Chinese mineral pigments with natural animal tones, Chinese Xianxia mythology aesthetic, NOT Western fantasy, NOT realistic, NOT 3D rendered, full body view front-facing centered on canvas, solid plain single-color background light gray #E0E0E0, expressive ink-painted eyes with reflective highlights, game asset style, clean sharp ink-line edges for easy cutout."

S_AA = "chibi 2D Chinese ink wash painting game character icon, super deformed cute style, big head small body ratio 2:1, Chinese calligraphy brush-style black ink outlines with varying thickness and expressive brush stroke feel, ink wash coloring with subtle tonal gradation and soft layered shading to create gentle volume and three-dimensional depth, light and shadow rendered through ink density variation — lighter wash on highlighted areas and denser ink in recessed folds creating natural cel-shaded dimensionality, rich varied color palette mixing traditional Chinese mineral pigments with natural and warm tones, Chinese Xianxia mythology aesthetic with ornate accessories and flowing ribbons, NOT Western fantasy, NOT realistic, NOT 3D rendered, square 1:1 aspect ratio, close-up showing oversized head and upper shoulders, solid plain single-color background light gray #E0E0E0, expressive ink-painted eyes with reflective highlights, game icon style, clean sharp ink-line edges for easy cutout, more refined details and ornate accessories than base version, golden star-rank accents on key accessories."

S_AF = "chibi 2D Chinese ink wash painting game character, super deformed cute style, big head small body ratio 2:1, Chinese calligraphy brush-style black ink outlines with varying thickness and expressive brush stroke feel, ink wash coloring with subtle tonal gradation and soft layered shading to create gentle volume and three-dimensional depth, light and shadow rendered through ink density variation — lighter wash on highlighted areas and denser ink in recessed folds creating natural cel-shaded dimensionality, rich varied color palette mixing traditional Chinese mineral pigments with natural and warm tones, Chinese Xianxia mythology aesthetic with ornate accessories and flowing ribbons, NOT Western fantasy, NOT realistic, NOT 3D rendered, full body view front-facing centered on canvas, solid plain single-color background light gray #E0E0E0, expressive ink-painted eyes with reflective highlights, game asset style, clean sharp ink-line edges for easy cutout, more refined details and ornate accessories than base version, golden star-rank accents on key accessories."

F_N = "STRICTLY FORBIDDEN: any text, letters, characters, words, writing, labels, captions, watermark, signature, runes, sigils, symbols, glyphs, seals, calligraphy marks, Daoist script, mystical writing, floating characters, icon overlays, any mark that resembles text or written language. STRICTLY FORBIDDEN: white outline outside black ink outlines, white border around character, white edge glow, white halo, any white fringe between character outline and background. The black ink outline must be the absolute outermost edge directly touching the background with zero gap. Also forbidden: glow effects, blur, soft edges, lighting effects. STRICTLY FORBIDDEN: humanoid form, human face, human body, human hair, human ears, human hands, human feet, bipedal humanoid stance, anthropomorphic human features. This creature MUST be an ANIMAL or BEAST, NOT a human or humanoid being. This is the NORMAL base form (not evolved)."

F_A = "STRICTLY FORBIDDEN: any text, letters, characters, words, writing, labels, captions, watermark, signature, runes, sigils, symbols, glyphs, seals, calligraphy marks, Daoist script, mystical writing, floating characters, icon overlays, any mark that resembles text or written language, any floating decorative elements that look like script or language. STRICTLY FORBIDDEN: white outline outside black ink outlines, white border around character, white edge glow, white halo, any white fringe between character outline and background. The black ink outline must be the absolute outermost edge directly touching the background with zero gap. Also forbidden: glow effects, blur, soft edges, lighting effects. STRICTLY FORBIDDEN: humanoid form, human face, human body, human hair, human ears, human hands, human feet, bipedal humanoid stance, anthropomorphic human features. This creature MUST be an ANIMAL or BEAST, NOT a human or humanoid being. This is the AWAKENED max-star evolved form."

R_AV = "Resolution: 128x128px target, circular crop friendly composition."
R_FL = "Resolution: 512x512px target, the character should fill about 70-80% of the canvas height."

# ─── Element -> visual mapping ───
ELEM_MAP = {
    "火": {"colors":"warm cream and soft peach with amber-orange accents","accent":"ember-orange, vermilion-red, coral","gem":"ruby","ring":"golden-flame","energy":"fire","body_adj":"warm","shadow_adj":"warm"},
    "水": {"colors":"soft brown and cream-beige with teal-blue accents","accent":"cerulean-blue, teal, aquamarine","gem":"sapphire","ring":"sapphire-blue","energy":"water","body_adj":"cool","shadow_adj":"cool"},
    "草": {"colors":"warm brown and olive-cream with emerald-green accents","accent":"emerald-green, jade, spring-green","gem":"jade","ring":"emerald-green","energy":"nature","body_adj":"warm","shadow_adj":"warm"},
    "土": {"colors":"deep brown and sandy-cream with amber-gold accents","accent":"amber-gold, sienna, bronze","gem":"amber","ring":"topaz-gold","energy":"earth","body_adj":"warm","shadow_adj":"warm"},
    "风": {"colors":"silver-white and pearl with pale cyan accents","accent":"pale cyan, silver, lavender","gem":"moonstone","ring":"diamond-white","energy":"wind","body_adj":"cool","shadow_adj":"cool"},
    "雷": {"colors":"dark brown and cream-yellow with electric-yellow accents","accent":"electric-yellow, golden, bright amber","gem":"citrine","ring":"electric-white","energy":"thunder","body_adj":"warm","shadow_adj":"warm electrified"},
    "光": {"colors":"pale gold and cream-white with warm gold accents","accent":"warm gold, white-gold, pale rose","gem":"sunstone","ring":"white-gold","energy":"holy light","body_adj":"warm","shadow_adj":"warm golden"},
    "影": {"colors":"midnight-black and plum-purple with deep violet accents","accent":"deep purple, dark violet, magenta","gem":"dark amethyst","ring":"dark-violet","energy":"shadow","body_adj":"deep","shadow_adj":"deep purple"},
    "心": {"colors":"iridescent lavender and pale rose with soft gold accents","accent":"rose-pink, lavender, soft gold","gem":"rose quartz","ring":"golden-pink","energy":"heart","body_adj":"warm","shadow_adj":"warm prismatic"},
}

# Handle multi-element by using first element
def get_elem(elem_str):
    """Get the primary element from an element string that may contain +."""
    first = elem_str.split("+")[0].strip()
    if first in ELEM_MAP:
        return ELEM_MAP[first]
    if first == "全元素" or first == "全水系" or first == "混沌":
        return ELEM_MAP["光"]  # Use 光 as default for multi/chaos
    return ELEM_MAP["心"]  # Fallback

# ─── Parse pets from v3 document ───
def parse_pets():
    with open(INPUT, "r", encoding="utf-8") as f:
        content = f.read()
    
    pets = []
    # Match table rows: | # | name | pet_id | rarity | element | description |
    # Two table formats:
    # Base: | # | 名称 | pet_id | 稀有度 | 元素 | 外观简述 |
    # Synth: | # | 名称 | pet_id | 种族 | 元素 | 稀有度 | 合成来源说明 |
    
    current_race = ""
    current_section = ""
    
    for line in content.split("\n"):
        # Track race headers
        if line.startswith("#### ") and "（" in line:
            m = re.search(r"(\d+)\.\s*(\S+族?)（", line)
            if m:
                current_race = m.group(2)
                if not current_race.endswith("族"):
                    current_race += "族"
        
        if "跨种族终极" in line:
            current_race = "跨种族"
        if "神级终极" in line:
            current_race = "神级"
        
        # Parse base pet rows: | # | 名称 | pet_id | 稀有度 | 元素 | 外观简述 |
        m = re.match(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(\w+)\s*\|\s*(R|SR|SSR)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|", line)
        if m:
            num, name, pid, rarity, elem, desc = m.groups()
            pets.append({
                "num": int(num),
                "name": name.strip(),
                "pid": pid.strip(),
                "rarity": rarity.strip(),
                "element": elem.strip(),
                "race": current_race,
                "desc": desc.strip(),
                "is_synth": False
            })
            continue
        
        # Parse synth pet rows: | # | 名称 | pet_id | 种族 | 元素 | 稀有度 | 合成来源说明 |
        m = re.match(r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(\w+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(R|SR|SSR)\s*\|\s*(.+?)\s*\|", line)
        if m:
            num, name, pid, race, elem, rarity, synth_desc = m.groups()
            pets.append({
                "num": int(num),
                "name": name.strip(),
                "pid": pid.strip(),
                "rarity": rarity.strip(),
                "element": elem.strip(),
                "race": race.strip() if race.strip().endswith("族") else race.strip(),
                "desc": synth_desc.strip(),
                "is_synth": True
            })
    
    return pets

# ─── Creature type mapping from pet_id ───
CREATURE_MAP = {
    "fox":"fox spirit","otter":"otter spirit","deer":"deer spirit","badger":"badger spirit",
    "weasel":"weasel spirit","marten":"marten spirit","hedgehog":"hedgehog spirit",
    "wolf":"wolf spirit","armadillo":"armadillo spirit","leopard":"snow leopard spirit",
    "lion":"lion spirit","raccoon":"raccoon-dog spirit","lizard":"lizard spirit",
    "ox":"ox spirit","tiger":"tiger spirit","qilin":"qilin spirit",
    "chick":"vermilion bird chick","falcon":"falcon spirit","petrel":"storm petrel spirit",
    "butterfly":"butterfly spirit","eagle":"eagle spirit","bat":"bat spirit",
    "moth":"moth spirit","sparrow":"sparrow spirit","owl":"owl spirit",
    "gull":"seagull spirit","crane":"crane spirit","raven":"raven spirit",
    "phoenix":"phoenix spirit","roc":"roc spirit","wing":"divine bird spirit",
    "fish":"fish spirit","turtle":"turtle spirit","shrimp":"shrimp spirit",
    "octopus":"octopus spirit","jelly":"jellyfish spirit","frog":"frog spirit",
    "crab":"crab spirit","lantern":"anglerfish spirit","clam":"clam spirit",
    "seahorse":"seahorse spirit","whale":"whale spirit","eel":"eel spirit",
    "mushroom":"mushroom spirit","dandelion":"dandelion spirit","lotus":"lotus spirit",
    "vine":"vine spirit","cactus":"cactus spirit","bamboo":"bamboo spirit",
    "bloom":"crystal flower spirit","maple":"maple leaf spirit","moss":"moss orb spirit",
    "orchid":"orchid spirit","banyan":"banyan tree spirit","wisp":"elemental wisp",
    "elemental":"elemental spirit","spirit":"spirit entity","wraith":"wraith spirit",
    "tapir":"tapir spirit","devourer":"shadow devourer","sprite":"emotion sprite",
    "mirror":"mirror spirit","galaxy":"galaxy spirit","nether":"nether spirit",
    "psyche":"psyche spirit","illusion":"illusion spirit","myriad":"myriad spirit",
    "realm":"realm master spirit","dragon":"dragon spirit","serpent":"serpent dragon spirit",
    "drake":"drake spirit","wyvern":"wyvern spirit","ceratops":"ceratops dragon spirit",
    "lindworm":"lindworm spirit","pteranodon":"pteranodon spirit",
    "beast":"beast spirit","steam":"steam creature","char":"charred creature",
    "lava":"lava creature","mud":"mud creature","flash":"lightning creature",
    "mist":"mist creature","thorn":"thorn creature","soul":"soul creature",
    "frost":"frost creature","thunder":"thunder creature","jade":"jade creature",
    "phantom":"phantom creature","iron":"iron creature","inferno":"inferno creature",
    "fire":"fire creature","water":"water creature","heart":"heart creature",
    "divine":"divine beast","ancient":"ancient dragon","cosmos":"cosmic dragon",
    "chaos":"chaos dragon","genesis":"genesis dragon-qilin beast","primordial":"primordial titan dragon-beast",
    "sovereign":"sovereign dragon","void":"void beast","aurora":"aurora beast",
    "stellar":"stellar creature","dream":"dream creature","twin":"twin phantasm",
    "radiant":"radiant creature","light":"light creature","shadow":"shadow creature",
    "ocean":"ocean dragon","abyss":"abyss creature","star":"star creature",
    "world":"world tree spirit","origin":"origin beast","crystal":"crystal creature",
    "deep":"deep-sea creature","tide":"tide creature","storm":"storm creature",
    "bolt":"bolt creature","gale":"gale creature","ember":"ember creature",
    "blaze":"blaze creature","aqua":"aqua creature","flora":"flora creature",
    "herb":"herb spirit","pollen":"pollen creature","sand":"sand creature",
    "dark":"dark creature","moon":"moon creature","psyche":"psyche creature",
    "cyclone":"cyclone creature","tempest":"tempest dragon","quake":"quake creature",
    "coastal":"coastal dragon","magma":"magma dragon","purgatory":"purgatory dragon",
    "realm":"realm beast","heart":"heart creature","soul":"soul creature",
}

def guess_creature(pid, desc):
    """Guess a creature type from the pet_id and description."""
    # Try direct word matches
    for key in sorted(CREATURE_MAP.keys(), key=len, reverse=True):
        if key in pid:
            return CREATURE_MAP[key]
    # Fallback: use desc
    return "mystical spirit creature"

# ─── Generate prompts for a pet ───
def gen_prompts(pet):
    e = get_elem(pet["element"])
    creature = guess_creature(pet["pid"], pet["desc"])
    pid = pet["pid"]
    name = pet["name"]
    rarity = pet["rarity"]
    is_synth = pet["is_synth"]
    
    # Determine body description based on element and creature
    body_colors = e["colors"]
    accent = e["accent"]
    gem = e["gem"]
    ring = e["ring"]
    energy = e["energy"]
    shadow = e["shadow_adj"]
    
    # Use English descriptions from DESC_EN if available
    if pid in DESC_EN:
        normal_feat, battle_pose, awaken_feat, awaken_battle = DESC_EN[pid]
        
        # Normal avatar
        nav = (
            f"A young {creature}, {body_colors} body with ink wash brush texture showing volume through tonal shading, "
            f"{normal_feat}, "
            f"a tiny {gem} bead on a thin cord around the neck, "
            f"subtle {shadow} shadow under the chin giving depth and roundness."
        )
        
        # Normal full
        nfl = (
            f"A young {creature} in battle-ready stance, {body_colors} body with ink wash brush strokes showing volume through tonal variation, "
            f"{normal_feat}, "
            f"large expressive eyes with alert determined battle gaze, "
            f"{battle_pose}, "
            f"subtle {shadow} shadows under the belly and between limbs giving depth."
        )
        
        # Awakened avatar
        aav = (
            f"A majestic evolved {creature}, magnificent form with rich {accent} accents on {body_colors} base with flowing ink wash texture, "
            f"{awaken_feat}, "
            f"an ornate {gem} pendant in golden filigree on a silk cord, "
            f"{'absolute divine majesty' if rarity == 'SSR' else 'proud powerful warrior'} expression, "
            f"subtle {shadow} depth shadows."
        )
        
        # Awakened full
        afl = (
            f"in dynamic battle pose. A majestic evolved {creature} mid-attack, magnificent form with rich {accent} accents on {body_colors} base with flowing ink wash brush strokes, "
            f"{awaken_feat}, "
            f"{awaken_battle}, "
            f"body surging with {'divine' if rarity == 'SSR' else 'fierce'} momentum, "
            f"subtle {shadow} depth shadows enhancing three-dimensionality."
        )
    else:
        # Fallback: use Chinese desc directly (should not happen with complete DESC_EN)
        desc = pet["desc"]
        nav = (
            f"A young {creature}, {body_colors} body with ink wash brush texture showing volume through tonal shading, "
            f"{desc}, "
            f"large expressive eyes with reflective highlights, "
            f"a tiny {gem} bead on a thin cord around the neck, "
            f"subtle {shadow} shadow under the chin giving depth and roundness."
        )
        nfl = (
            f"A young {creature} in battle-ready stance, {body_colors} body with ink wash brush strokes showing volume through tonal variation, "
            f"{desc}, "
            f"large expressive eyes with alert determined battle gaze, "
            f"a tiny {gem} bead on a cord at the neck, "
            f"dynamic combat-ready pose with body slightly crouched and leaning forward, "
            f"fierce yet cute expression, "
            f"subtle {shadow} shadows under the belly and between limbs giving depth."
        )
        aav = (
            f"A majestic evolved {creature}, magnificent form with rich {accent} accents on {body_colors} base with flowing ink wash texture, "
            f"evolved version of: {desc} — now more elaborate and ornate, "
            f"large blazing eyes with a {ring} ring in the pupil radiating {energy} mastery, "
            f"adorned with tiny golden ornamental earrings, "
            f"an ornate {gem} pendant in golden filigree on a silk cord, "
            f"{'absolute divine majesty' if rarity == 'SSR' else 'proud powerful warrior'} expression, "
            f"subtle {shadow} depth shadows."
        )
        afl = (
            f"in dynamic battle pose. A majestic evolved {creature} mid-attack, magnificent form with rich {accent} accents on {body_colors} base with flowing ink wash brush strokes, "
            f"evolved version of: {desc} — now more elaborate and ornate with {energy} energy visible, "
            f"large blazing eyes with a {ring} ring radiating fierce {energy} power, "
            f"golden ornamental earrings angled back aggressively, "
            f"an ornate {gem} pendant swinging with movement, "
            f"dynamic {'devastating ultimate' if rarity == 'SSR' else 'powerful leaping'} attack pose, "
            f"body surging with {'divine' if rarity == 'SSR' else 'fierce'} momentum, "
            f"{'absolute supreme power' if rarity == 'SSR' else 'intense warrior fury'} expression, "
            f"subtle {shadow} depth shadows enhancing three-dimensionality."
        )
    
    return nav, nfl, aav, afl

# ─── Hand-crafted prompt files (manually curated, do not overwrite) ───
HANDCRAFTED_PIDS = {"flame_fox"}

def load_handcrafted(pid, variant):
    """Load hand-crafted prompt if it exists and is in the whitelist."""
    if pid not in HANDCRAFTED_PIDS:
        return None
    path = os.path.join(PROMPT_DIR, f"prompt_{pid}_{variant}.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None

# ─── Main ───
def main():
    pets = parse_pets()
    print(f"Parsed {len(pets)} pets from v3 design document")
    
    # Re-number synth pets to continue from 104
    base_count = sum(1 for p in pets if not p["is_synth"])
    synth_idx = base_count + 1
    global_num = 1
    for p in pets:
        if not p["is_synth"]:
            p["global_num"] = global_num
        else:
            p["global_num"] = synth_idx
            synth_idx += 1
        global_num += 1
    
    # Generate document
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("# 《灵宠放置传》宠物美术资源提示词 v3\n\n")
        f.write("> 基于宠物设计和合成方案 v3，共 236 只宠物 × 4 变体 = 944 个提示词\n")
        f.write("> 每只宠物包含：normal_avatar (128×128)、normal_full (512×512)、awakened_avatar (128×128)、awakened_full (512×512)\n>\n")
        f.write("> **v3 提示词改进**：\n")
        f.write("> 1. 严禁任何文字/符文/符号出现\n")
        f.write("> 2. 水墨风格增加立体感（墨色浓淡变化营造体积感）\n")
        f.write("> 3. 配色活泼多样，不再单一使用元素主色\n\n---\n\n")
        
        current_race = ""
        prompt_count = 0
        txt_count = 0
        
        for pet in pets:
            race = pet["race"]
            if race != current_race:
                current_race = race
                section = "基础捕捉宠" if not pet["is_synth"] else "合成专属宠"
                f.write(f"\n## {race}{'' if pet['is_synth'] else '（基础）'}{'（合成）' if pet['is_synth'] else ''}\n\n---\n\n")
            
            pid = pet["pid"]
            f.write(f"### #{pet['global_num']} {pet['name']} ({pid}) — {pet['rarity']} · {pet['element']} · {race}\n\n")
            
            # Check for hand-crafted prompts first, otherwise generate
            variants = ["normal_avatar", "normal_full", "awakened_avatar", "awakened_full"]
            gen = gen_prompts(pet)
            styles = [S_AV, S_FL, S_AA, S_AF]
            forbids = [F_N, F_N, F_A, F_A]
            resolutions = [R_AV, R_FL, R_AV, R_FL]
            
            for i, var in enumerate(variants):
                handcrafted = load_handcrafted(pid, var)
                if handcrafted:
                    prompt = handcrafted
                else:
                    prompt = f"{styles[i]} {forbids[i]} {gen[i]} {resolutions[i]}"
                
                f.write(f"**{var}** (`prompt_{pid}_{var}.txt`):\n")
                f.write(f"```\n{prompt}\n```\n\n")
                
                # Write individual txt file
                # Always overwrite auto-generated files; skip only hand-crafted ones
                txt_path = os.path.join(PROMPT_DIR, f"prompt_{pid}_{var}.txt")
                if handcrafted:
                    pass  # Don't overwrite hand-crafted files
                else:
                    with open(txt_path, "w", encoding="utf-8") as tf:
                        tf.write(prompt)
                    txt_count += 1
                
                prompt_count += 1
            
            f.write("---\n\n")
        
        f.write(f"\n> 共 {len(pets)} 只宠物，{prompt_count} 个提示词\n")
    
    print(f"Written {len(pets)} pets, {prompt_count} prompts to {OUTPUT}")
    print(f"Written {txt_count} new prompt txt files to {PROMPT_DIR}")

if __name__ == "__main__":
    main()
