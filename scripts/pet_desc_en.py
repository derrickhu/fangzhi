#!/usr/bin/env python3
"""
English descriptions for all 236 pets.
Each entry: pet_id -> (normal_features, battle_pose, awaken_features, awaken_battle)
- normal_features: appearance details for normal avatar/full
- battle_pose: extra details for normal_full battle stance
- awaken_features: appearance details for awakened avatar/full
- awaken_battle: extra details for awakened_full battle pose
"""

DESC_EN = {
    # ═══════════════════════════════════════════════════
    # 兽灵族 BASE (1-16)
    # ═══════════════════════════════════════════════════
    "flame_fox": (
        "warm cream and soft peach body fur, bright amber-orange ear tips fading from the cream base, a small fluffy tail with the very tip glowing ember-orange suggesting warmth, large sparkling teal-green eyes with a curious lively expression, tiny coral-red silk ribbon tied in a bow at the neck, rosy pink inner ears",
        "front paws spread in a low combat stance ready to pounce, body slightly crouched and leaning forward, mouth slightly open showing tiny fangs in a fierce cute growl, tail raised high with the tip glowing ember-orange like a small flame",
        "luxurious cream-white and warm amber fur, vivid golden-orange flame patterns along the cheeks like elegant war paint, large blazing teal-green eyes with a golden star-shaped ring in the pupil radiating fierce battle spirit, pointed ears tipped with fiery vermilion-red and adorned with tiny golden bell earrings, bushy dual tails — cream base with brilliant sunset-orange and vermilion tips",
        "dynamic leaping attack pose with one front paw swiping forward showing tiny claws, body twisting mid-strike with powerful momentum, magnificent dual tails fanned out behind like twin flames, mouth open in a battle cry showing fangs"
    ),
    "brook_otter": (
        "teal-blue and cream-white sleek body fur with rippling water-like patterns on the back, small webbed paws, a smooth tapered tail with cerulean-blue tip, large round bright blue eyes with a playful cheerful expression, tiny water droplets clinging to the fur like dew, small rounded ears with pale blue inner coloring",
        "body coiled low in a swimmer's lunge stance, front paws raised ready to splash, tail curled behind for balance, alert playful battle expression",
        "shimmering aquamarine and pearl-white fur with flowing stream patterns that seem to ripple, large blazing sapphire-blue eyes with a teal ring in the pupil, ornate tiny sapphire earrings, flowing water-mist scarf around the neck, twin tail tips that trail misty water vapor",
        "powerful diving attack pose surging forward, water-patterned fur rippling with momentum, paws extended with splashing energy, fierce aquatic warrior expression"
    ),
    "leaf_deer": (
        "emerald-green and warm fawn-brown body with leaf-vein patterns along the flanks, tiny budding antlers with fresh green sprouts and miniature leaves growing from the tips, large gentle dark-green eyes with a serene peaceful expression, a small jade bead on a vine cord at the neck, white speckled spots on the back like sunlit forest floor, tiny cloven hooves",
        "body poised mid-leap with front legs tucked, antler buds pointing forward, a graceful yet alert stance, determined eyes with natural courage",
        "magnificent jade-green and golden-fawn body with intricate vine-pattern markings, grand branching antlers with full blooming cherry blossoms and emerald leaves, large blazing emerald-green eyes with a golden-green ring, ornate golden vine circlet on the head, flowing petal-scattered mane",
        "majestic leaping attack with blooming antlers lowered to charge, body stretched mid-gallop, cherry blossom petals trailing behind, fierce forest guardian expression"
    ),
    "rock_badger": (
        "dark brown and sandy-cream fur with rocky plate-like patterns on the back and shoulders, a broad flat head with strong jaw, small sturdy legs with thick claws, large round amber-gold eyes with a stubborn grumpy expression, stone-textured stripe running from nose to tail, short bristly tail",
        "low crouching defensive stance with claws dug into the ground, head lowered showing the rocky back plates, fierce determined expression",
        "deep bronze and obsidian-black fur with glowing amber-gold crack patterns across stone-armored back, large blazing topaz-gold eyes with an amber ring, golden metal claw-caps, ornate amber crystal on a chain at the neck, thicker stone plates with golden veining",
        "powerful charging attack with head lowered like a battering ram, stone plates glowing with golden cracks, earth energy visible, unstoppable force expression"
    ),
    "gale_weasel": (
        "silver-white and pearl-gray sleek fur with wind-swept styling, extremely long slender body built for speed, large round bright cyan eyes with an energetic mischievous expression, tiny swept-back ears, a long thin tail with a wispy silver tip that seems to trail wind, small agile paws",
        "body stretched in a mid-sprint pose, fur blown back by speed, tail trailing like a wind streak, excited lightning-fast expression",
        "shimmering pearl-white and silver fur with swirling wind-pattern markings in pale cyan, large blazing diamond-white eyes with a cyan ring, tiny silver wind-chime earrings, a moonstone pendant on a silver chain, flowing windswept fur that defies gravity",
        "blinding speed attack blur with body nearly horizontal in a dash, wind trails spiraling around, paws barely touching ground, exhilarating fierce expression"
    ),
    "thunder_marten": (
        "dark chocolate-brown and cream-yellow fur with black jagged lightning-bolt stripes, a sleek elongated body with bushy tail, large round electric-yellow eyes with a sharp alert expression, tiny sparking whiskers, pointed ears with yellow inner coloring, small bright sparks occasionally visible on the fur tips",
        "arched back with fur standing on end crackling with static, front paws spread wide ready to pounce, tail bristled with electricity, fierce electrified expression",
        "jet-black and brilliant gold fur with pulsing electric-yellow circuit-like patterns, large blazing electric-white eyes with a golden ring, tiny golden lightning-bolt earrings, a citrine crystal pendant crackling with energy, fur constantly rippling with visible static discharge",
        "explosive attack leap with body surrounded by electric arcs, fur blazing with golden lightning, claws extended crackling with thunder energy, devastating electrified fury expression"
    ),
    "thorn_hedgehog": (
        "dark green and warm brown body with back spines made of living thorny vines with tiny leaves and buds, a round chubby body shape, large round dark-green eyes with a shy timid expression, tiny pink nose, small curled paws, belly fur is soft cream-colored, a few tiny flowers blooming among the thorns",
        "curled into a defensive ball with thorn-vines extended outward bristling, peeking out with fierce determined eyes, ready to roll-charge",
        "deep emerald-green and golden-brown body with magnificent thorn-vine spines now blooming with vibrant flowers, large blazing emerald eyes with a jade ring, golden thorn-crown circlet, tiny jade bead earrings, vine patterns crawling along the cheeks",
        "uncurling from a spin-attack with thorn-vines whipping outward, flowers launching like projectiles, fierce blooming warrior expression"
    ),
    "crimson_wolf": (
        "dark crimson-red and charcoal-gray fur with ember-like glowing markings on the legs, lean muscular body with thick neck ruff, large fierce amber-red eyes with fire reflections in the pupils, pointed ears with dark red tips, a long bushy tail with smoldering ember-orange underside, sharp visible fangs",
        "standing in a commanding alpha pose with head slightly lowered showing teeth, front paw forward, tail raised dominantly, fierce predator expression",
        "deep blood-crimson and obsidian-black fur with vivid flame patterns flowing along the body, large blazing golden-flame eyes with a vermilion ring, ornate golden fang-shaped earrings, a ruby pendant on a dark chain, magnificent ruff of fur that smolders with inner fire",
        "lunging attack with jaws open wide showing blazing fangs, body stretched in a powerful strike, flame-marked fur trailing fire energy, terrifying alpha predator expression"
    ),
    "iron_armadillo": (
        "iron-gray and steel-blue segmented shell plates with metallic sheen, a round compact body, large round gentle silver eyes with a calm sleepy expression, tiny clawed feet poking out from under the armor, a segmented tail with a metallic ball tip, small pointed ears barely visible between plates",
        "curled into an armored ball mid-roll, metallic plates gleaming, rolling forward as a living cannonball, stoic determined expression",
        "polished silver and dark steel shell plates with golden rivets and glowing amber crack-patterns, large blazing topaz eyes with a steel ring, ornate golden-trimmed plate edges, an amber crystal embedded in the forehead plate, magnificent fortress-like armored form",
        "uncurling from a devastating roll-slam attack, plates expanding outward with golden energy, earth tremor effect, unstoppable iron fortress expression"
    ),
    "cloud_leopard": (
        "pure white and pale silver fur with soft cloud-like swirl markings, a sleek graceful feline body, large round bright pale-cyan eyes with a cool aloof expression, long curving tail with wispy cloud-pattern tip, small rounded ears with silver inner coloring, elegant long whiskers",
        "crouching low in a stalking pose ready to spring, tail swishing, eyes locked on target with predatory focus, graceful hunter expression",
        "shimmering pearl-white and silver-lavender fur with flowing cloud and wind-trail patterns, large blazing diamond-white eyes with a pale cyan ring, tiny platinum earrings shaped like clouds, a moonstone pendant on a silk cord, fur that seems to float and billow like clouds",
        "swift pouncing attack from above descending like a cloud, body twisting gracefully mid-air, trail of mist behind, elegant yet lethal predator expression"
    ),
    "blaze_lion": (
        "rich golden-amber and deep crimson mane-fur with flame-shaped mane strands, a proud compact lion cub body, large fierce golden eyes with inner fire glow, small rounded ears with fiery orange inner coloring, broad paws with warmth-glow, a fluffy tail with a flame-like tip, regal proud expression",
        "standing tall with chest puffed out and mane blazing, one paw raised in a commanding roar pose, mouth open showing teeth, king-of-beasts pride",
        "magnificent golden-white and blazing vermilion mane with living flame tendrils, large blazing white-gold eyes with a flame ring, ornate golden crown-circlet with a tiny ruby, golden mane ornaments, dual fiery tail tips, regal imperial warrior form",
        "devastating roar-attack with mane erupting in flames, body surging forward with royal fury, golden fire energy radiating, supreme lion king expression"
    ),
    "frost_raccoon": (
        "ice-blue and silver-white fur with frost crystal patterns on the cheeks and tail rings, a round chubby raccoon-dog body, large round bright icy-blue eyes with a mischievous sly expression, characteristic dark mask marking in deep blue, a bushy ringed tail with ice-crystal tips, small round ears with frosty white inner coloring",
        "standing on hind legs with front paws raised to exhale a frost breath, tail curled up defensively, crafty defensive battle pose",
        "shimmering crystal-ice blue and pearl-white fur with intricate frost-flower patterns, large blazing sapphire eyes with an ice-crystal ring, ornate tiny silver snowflake earrings, a sapphire pendant in silver filigree, magnificent ice-crystal patterns blooming across the fur, three ringed tail tips sparkling with frost",
        "spinning frost-breath attack with ice crystals spiraling outward, fur crystallizing with cold energy, paws directing the blizzard, fierce ice trickster expression"
    ),
    "jade_lizard": (
        "deep jade-green and emerald body with iridescent scale patterns, moss and tiny flower growing along the spine ridge, a sleek lizard body with four splayed legs, large round amber-green eyes with a calm wise expression, a forked tongue occasionally flicking, long tail with moss-covered tip, tiny clawed toes",
        "low stalking pose with body pressed close to ground, tail raised for balance, tongue flicking to sense the battlefield, patient predator expression",
        "magnificent deep emerald and golden-jade scales with blooming moss-garden on the back, large blazing jade-green eyes with a golden ring, ornate golden spine-crest with tiny jade gems, vine patterns along the body, flowering moss creating a miniature garden landscape",
        "lunging attack with jaw open wide, tail whipping as a weapon, moss-garden blooming with attack energy, fierce ancient jungle guardian expression"
    ),
    "boulder_ox": (
        "deep chocolate-brown and granite-gray hide with rock-textured patches, a massive stocky body with powerful legs, large horns made of actual boulder-stone with rough rocky texture, large round deep amber eyes with a calm steady expression, broad flat nose with a stone ring, thick hooves that look like carved rock",
        "head lowered with boulder-horns aimed forward in a charge stance, hooves pawing the ground, immovable mountain expression",
        "dark obsidian-brown and golden-veined rocky hide with glowing amber crack-patterns, massive golden-tipped boulder horns with embedded amber crystals, large blazing topaz eyes with a golden ring, ornate golden nose-ring, stone plates forming natural armor along the shoulders",
        "devastating charging headbutt with boulder-horns glowing, earth cracking underfoot, body surging with mountain-crushing force, unstoppable earthen titan expression"
    ),
    "storm_tiger": (
        "white and jet-black striped fur with electric-blue lightning patterns running along the stripes, a powerful compact tiger cub body, large fierce electric-yellow eyes with crackling energy, dark striped ears with blue-white inner glow, thick paws with visible spark claws, a thick tail with a lightning-bolt tip shape",
        "powerful pounce stance with one paw raised crackling with electricity, body tensed like a coiled spring, jaws parted showing electric fangs, fierce thunder warrior expression",
        "brilliant white and obsidian-black striped fur with pulsing electric-blue and golden lightning patterns, large blazing electric-white eyes with a golden-lightning ring, ornate golden thunder-crown between the ears, tiny lightning-bolt earrings, crackling storm energy visible around the body, magnificent electrified tiger form",
        "devastating lightning-strike attack leaping through the air, body wreathed in electric arcs, claws extended with thunder force, jaws wide open releasing a bolt, supreme thunder beast expression"
    ),
    "spirit_qilin": (
        "iridescent rainbow-shimmer scales over a deer-like body with soft golden-cream underbelly, a single small spiraling horn with prismatic glow, large luminous golden-pink eyes with a gentle benevolent expression, tiny dragon-like whiskers, cloven hooves with golden glow, a flowing mane and tail in soft pastel rainbow colors, an aura of gentle warmth",
        "standing in a dignified pose with horn glowing softly, one hoof raised gracefully, tail flowing behind, serene yet alert guardian expression",
        "magnificent prismatic scales shifting through all colors over a regal deer-dragon body, grand spiraling golden horn with a rose-quartz crystal embedded at the base, large blazing golden-pink eyes with a rainbow ring, ornate golden filigree crown, flowing ribbon-like mane in seven colors, tiny golden bell on a silk cord",
        "divine charging pose with horn blazing prismatic light, body surrounded by golden heart-energy, all colors intensifying, hooves trailing rainbow sparks, absolute divine benevolence expression"
    ),

    # ═══════════════════════════════════════════════════
    # 羽翼族 BASE (17-31)
    # ═══════════════════════════════════════════════════
    "vermilion_chick": (
        "bright scarlet-red and warm gold downy feathers with tiny fire-sparks at the tail tips, a round chubby chick body with small stubby wings, large round bright orange-gold eyes with an eager excited expression, a tiny yellow beak, small red crest feathers on the head, pink feet",
        "wings spread wide with tail sparks intensifying, hopping forward in an attack stance, beak open in a tiny fierce chirp",
        "magnificent scarlet and gold plumage with flowing flame-pattern tail feathers, large blazing golden-flame eyes with a vermilion ring, ornate tiny golden head-crest, flame patterns along wing edges, elegant longer tail streamers with fire-tips",
        "diving attack with wings blazing, tail feathers trailing fire, beak aimed forward like a fiery arrow, fierce young phoenix warrior expression"
    ),
    "wind_falcon": (
        "pale gray-white and silver feathers with wind-swept styling, a sleek streamlined falcon body built for speed, large sharp pale cyan eyes with a focused intense expression, hooked dark beak, pointed wing tips, a banded tail with silver-white bars, small sharp talons",
        "wings tucked in a diving stoop position, body streamlined for maximum speed, intense focused predator expression",
        "shimmering silver-white and pearl feathers with swirling wind-trail patterns on the wings, large blazing diamond-white eyes with a cyan ring, ornate tiny silver wind-chime on a leg band, magnificent swept-back crest feathers, wing tips that trail wind energy",
        "devastating dive-bomb attack at extreme speed, wings creating sonic wind-blade trails, talons extended, unstoppable wind-blade expression"
    ),
    "storm_petrel": (
        "deep navy-blue and white breast feathers with water-mist droplets on the wing tips, a small graceful seabird body with long narrow wings, large round bright blue eyes with a brave adventurous expression, a small dark beak, forked tail with blue tips, webbed feet",
        "banking in flight with one wing dipped, water droplets spraying from wing tips, brave stormy seas expression",
        "shimmering deep sapphire and pearl-white feathers with flowing ocean-wave patterns, large blazing sapphire eyes with a teal ring, ornate tiny aquamarine pendant on a neck cord, magnificent elongated wing feathers trailing sea mist, forked tail with glowing blue tips",
        "diving through a wave-wall attack with water spiraling around the body, wings cutting through spray, fierce ocean storm-rider expression"
    ),
    "blossom_butterfly": (
        "pink-green and soft lavender wings with flower-petal patterns and veining like real petals, a tiny cute insect body with fluffy thorax, large round bright green eyes with a gentle dreamy expression, curled proboscis, delicate antennae with tiny flower buds at the tips, iridescent wing edges",
        "wings flapping in a pollen-burst hover, body angled forward, scattering sparkly pollen with each wingbeat, gentle yet determined expression",
        "magnificent rose-pink and emerald wings with intricate living flower-petal patterns that seem to bloom, large blazing emerald eyes with a jade ring, ornate golden antennae with blooming flower tips, delicate golden body markings, wings that scatter real flower petals",
        "spinning petal-storm attack with wings creating a vortex of flower petals, body glowing with nature energy, fierce blooming fairy expression"
    ),
    "bolt_eagle": (
        "golden-yellow and dark brown feathers with electric-spark patterns on the wing edges, a young eagle body with broad wings, large sharp electric-yellow eyes with a fierce proud expression, hooked dark beak with a gold tip, powerful talons with tiny sparks between claws, a broad fanned tail with yellow-gold bars",
        "wings spread wide in a threatening display, talons extended crackling with electricity, head thrown back in a screech, fierce eagle warrior expression",
        "brilliant gold and obsidian-brown feathers with pulsing lightning-bolt patterns across the wings, large blazing electric-white eyes with a gold ring, ornate golden head-crest crown, tiny citrine gems embedded in the talons, magnificent crackling storm wings",
        "devastating lightning-dive attack with talons leading, body wreathed in electric arcs, wings trailing thunder-bolts, supreme sky predator expression"
    ),
    "dusk_bat": (
        "deep purple-black and dark plum membrane wings with shadow-swirl patterns, a small cute bat body with large ears, large round glowing violet eyes with a mysterious curious expression, tiny fangs peeking from the mouth, wing-claws visible at the wing joints, a small fluffy body with dark purple-gray fur",
        "wings spread in a swooping dive pose, shadow patterns intensifying, eyes glowing in the dark, mysterious night hunter expression",
        "magnificent deep violet and obsidian-black wings with flowing shadow-vortex patterns, large blazing dark-violet eyes with a purple ring, ornate tiny amethyst earrings on the large ears, shadow mist trailing from wing edges, elegant dark silk collar",
        "shadow-dive attack phasing through darkness, wings creating shadow-blade trails, body partially translucent, terrifying shadow predator expression"
    ),
    "glow_moth": (
        "pale gold and soft cream wings with gentle luminous glow and delicate feathery antenna, a fluffy round moth body, large round warm golden eyes with a serene peaceful expression, feathery white antennae that glow softly, fuzzy body fur in cream and pale gold, wing patterns like soft lantern light",
        "hovering with wings creating a gentle light pulse, antennae extended sensing the battlefield, calm yet alert guardian of light expression",
        "magnificent golden-white and warm amber wings with radiant sun-pattern markings that truly glow, large blazing white-gold eyes with a golden ring, ornate golden antennae with tiny sunstone tips, body radiating gentle holy warmth, wings leaving golden light trails",
        "blinding light-burst attack with wings fully spread releasing waves of golden light, antennae blazing, body at the center of a light nova, serene yet overwhelming divine moth expression"
    ),
    "bamboo_sparrow": (
        "fresh green and warm brown feathers with bamboo-leaf patterns on the wings, a small round sparrow body, large round bright dark-green eyes with a cheerful chirpy expression, a small beak holding a tiny bamboo leaf, green-tipped tail feathers, tiny orange feet",
        "hopping forward with wings half-spread, bamboo leaf held like a tiny sword, fierce little warrior chirp expression",
        "emerald-green and jade feathers with intricate bamboo-grove patterns, large blazing emerald eyes with a jade ring, ornate tiny jade bead on a neck thread, magnificent green-gold tail feathers like bamboo leaves, wing tips trailing green energy",
        "rapid wing-slash attack scattering bamboo-leaf blades, body spinning in a green whirlwind, fierce bamboo warrior expression"
    ),
    "sand_owl": (
        "sandy-yellow and warm buff-brown feathers with desert sand-ripple patterns, a round fluffy owl body with a flat face, large round piercing amber-gold eyes with a wise solemn expression, small ear tufts, feathered legs and feet, mottled sandy camouflage patterns",
        "head rotated slightly with eyes locked on target, talons gripping tight, silent deadly focus expression",
        "deep golden-sand and rich amber feathers with swirling desert-wind patterns, large blazing topaz-gold eyes with an amber ring, ornate golden ear-tuft ornaments, tiny amber crystal embedded in the forehead, magnificent feathered cloak-like wings with golden edges",
        "silent dive-attack swooping down with wings spread wide, sand energy trailing, talons extended with earth power, wise but lethal desert guardian expression"
    ),
    "ice_gull": (
        "white and pale ice-blue feathers with frost-crystal tips on the wings, a sleek seagull body, large round bright icy-blue eyes with a free spirited expression, orange-pink beak, long pointed wings with ice-crystal edges, webbed feet, a forked tail with ice tips",
        "banking in flight with ice crystals forming on wing tips, calling out a battle cry, spirited ocean warrior expression",
        "shimmering pearl-white and crystal-blue feathers with intricate ice-flower patterns on the wings, large blazing sapphire eyes with an ice ring, ornate tiny ice-crystal pendant, magnificent frost-edged wings that leave crystal trails, elegant icicle tail streamers",
        "ice-storm diving attack scattering frost crystals from wings, body surrounded by freezing wind, fierce arctic warrior expression"
    ),
    "ember_crane": (
        "deep vermilion-red and warm white plumage with flame-pattern markings on the wings, a tall elegant crane body with long legs, large piercing amber-gold eyes with a dignified noble expression, a red crown patch on the head, long dark beak, graceful neck, broad wings with fiery red edges",
        "one leg raised in a crane stance, wings half-spread showing flame patterns, regal martial arts master expression",
        "magnificent scarlet and white-gold plumage with living flame patterns flowing along the wings, large blazing golden-flame eyes with a vermilion ring, ornate golden crown-crest, tiny ruby earrings, magnificent trailing tail feathers like streams of fire, golden leg bands",
        "sweeping wing attack creating a wall of flame, body spinning in a crane-dance strike, tail feathers trailing fire arcs, divine fire dancer expression"
    ),
    "shadow_raven": (
        "jet-black and deep purple-sheen feathers with shadow-mist clinging to the plumage, a sleek raven body, large round glowing pale violet eyes with an intelligent mysterious expression, strong dark beak, glossy black wings with purple iridescence, tail feathers that seem to dissolve into shadow",
        "perched with wings slightly raised showing shadow aura, head tilted with an ominous knowing look, dark intelligence expression",
        "obsidian-black and deep violet feathers with flowing shadow-smoke patterns, large blazing dark-violet eyes with a purple ring, ornate tiny dark amethyst pendant, shadow tendrils flowing from wing tips and tail, elegant dark silk thread on one leg, mysterious dark ruler presence",
        "shadow-dive attack phasing through darkness, wings creating blades of shadow, body partially dissolved into dark mist, terrifying shadow master expression"
    ),
    "breeze_phoenix": (
        "teal-green and pale gold feathers with wind-swirl patterns, a young elegant phoenix-bird body with long flowing tail, large bright emerald-green eyes with a graceful proud expression, a small colorful crest, long flowing tail feathers with wind-pattern tips, delicate build",
        "hovering with tail feathers streaming in the wind, wings creating gentle breezes, graceful airborne battle pose",
        "magnificent jade-green and golden feathers with flowing wind-and-cloud patterns, large blazing emerald eyes with a golden-green ring, ornate golden crest with tiny jade ornaments, magnificent flowing tail streamers with wind-trail effects, golden wing-edge accents",
        "devastating wind-storm attack with spiral gusts around the body, tail feathers creating wind-blade trails, wings generating cyclone force, majestic storm phoenix expression"
    ),
    "thunder_roc": (
        "dark golden-black and electric-blue feathers with crackling energy along the wing edges, a massive young roc body with enormous wingspan, large fierce golden eyes with electric flashes, powerful dark beak, thick scaled legs with lightning-spark talons, broad thundercloud-dark wings",
        "wings spread to maximum span creating electric arcs between wing tips, body radiating storm energy, overwhelming sky-lord expression",
        "magnificent obsidian-gold and brilliant electric-blue feathers with pulsing lightning patterns across enormous wings, large blazing electric-gold eyes with a lightning ring, ornate golden crown of tiny thunderbolts, crackling electric field around the body, massive wing-tips trailing continuous lightning",
        "devastating thunderstrike attack diving from above, wings releasing massive lightning bolts, body surrounded by storm clouds, supreme thunder-god expression"
    ),
    "aurora_wing": (
        "iridescent rainbow-shimmer feathers shifting through all colors of the aurora, a divine bird body of elegant proportions, large luminous prismatic eyes with a serene transcendent expression, a flowing rainbow crest, magnificent tail feathers displaying aurora patterns, every feather seems to glow with inner light, golden feet",
        "wings fully spread displaying the complete aurora spectrum, hovering in divine radiance, transcendent divine being expression",
        "magnificent prismatic aurora feathers with intensified rainbow light that pulses and flows, large blazing white-gold eyes with a rainbow ring, ornate golden crown with prismatic gems, seven-colored flowing tail streamers each a different aurora hue, wings radiating pure light energy",
        "divine light-burst attack with aurora energy exploding from spread wings, body at the center of a prismatic nova, all colors blazing at maximum intensity, absolute divine aurora goddess expression"
    ),

    # ═══════════════════════════════════════════════════
    # 水族 BASE (32-46)
    # ═══════════════════════════════════════════════════
    "bubble_fish": (
        "round chubby cerulean-blue and white body with transparent bubble-like fin membranes, a cute puffer-fish shape, large round bright blue eyes with a happy bubbly expression, tiny puckered mouth constantly blowing small bubbles, translucent blue-tinted fins, a small round tail fin",
        "body inflated slightly with bubbles streaming from the mouth in a barrage, fins flared for stability, fierce yet adorable bubble-attack expression",
        "shimmering sapphire-blue and pearl-white body with prismatic bubble-patterns on the scales, large blazing sapphire eyes with a teal ring, ornate tiny pearl earrings on the gill covers, magnificent translucent fins with glowing edges, a crown of persistent iridescent bubbles around the head",
        "devastating bubble-storm attack with massive glowing bubbles launching from an open mouth, body surging forward through a wall of prismatic bubbles, fierce ocean warrior expression"
    ),
    "stone_turtle": (
        "warm brown and gray shell with realistic rock-texture and sediment-layer patterns, a small turtle body with sturdy legs, large round gentle amber eyes with a patient calm expression, a rough rocky shell with moss patches, small blunt claws, wrinkled neck skin, a short stubby tail",
        "retreating slightly into shell with head still out and alert, shell angled as a shield, steady unbreakable defense expression",
        "deep granite-brown and golden-veined shell with glowing amber crack-patterns revealing inner strength, large blazing topaz eyes with a golden ring, ornate golden shell-rim with embedded amber gems, magnificent fortress-like enhanced shell, moss replaced by tiny golden crystal formations",
        "shell-slam attack emerging from a spinning shell-charge, golden energy radiating from crack-patterns, earth tremor effect, ancient earth guardian expression"
    ),
    "flame_shrimp": (
        "bright vermilion-red and coral-orange body with a curved shrimp form, long fiery-red antennae that glow like burning wires, large round bright orange eyes on stalks with a feisty snappy expression, small pincer claws with ember-glow tips, segmented body with warm gradient from red to orange, tiny swimmerets",
        "pincers raised and snapping with spark effects, antennae forward like burning whips, body arched in an aggressive attack posture, fierce little warrior expression",
        "magnificent deep crimson and golden-orange body with flowing flame patterns along the segments, large blazing golden-flame eyes with a ruby ring, ornate golden antenna-tips, golden-trimmed pincers with fire-glow, magnificent flame-trail from the tail fan",
        "devastating pincer-strike attack with both claws blazing fire, body lunging forward, antennae whipping flames, explosive fire shrimp warrior expression"
    ),
    "ink_octopus": (
        "deep purple-black and plum body with eight curling tentacles, a round head with large expressive dark violet eyes showing a crafty mischievous expression, color-shifting skin with darker patches, a tiny beak-mouth, suction cups visible on tentacle undersides, one tentacle holding a small ink blob",
        "tentacles spread in all directions creating an intimidating display, body darkening with ink-cloud ready to deploy, cunning tactical expression",
        "magnificent obsidian-purple and deep violet body with flowing shadow-ink patterns, large blazing dark-violet eyes with a purple ring, ornate tiny dark amethyst on the head, golden-tipped tentacle ends, magnificent shadow-ink clouds swirling around, elegant dark presence",
        "devastating ink-storm attack with tentacles whipping and spraying shadow-ink in all directions, body partially hidden in dark cloud, terrifying abyssal predator expression"
    ),
    "jelly_spirit": (
        "translucent pale blue and soft white bell-shaped body with gentle inner glow, flowing transparent tentacles, large round dreamy bright blue eyes visible through the bell, a serene floating pose, bioluminescent dots along the bell edge, ethereal and weightless appearance",
        "bell pulsing with increased luminescence, tentacles trailing in a rhythmic swimming attack pattern, calm but focused battle expression",
        "magnificent crystal-clear and sapphire-blue bell with intricate glowing vein-patterns, large blazing sapphire eyes with a teal ring, ornate tiny pearl at the bell apex, flowing crystalline tentacles with glowing tips, magnificent bioluminescent aurora display within the bell",
        "devastating water-pulse attack with bell releasing shockwaves of luminous energy, tentacles lashing with crystalline force, ethereal water goddess expression"
    ),
    "spark_frog": (
        "bright yellow-green and lime body with electric-yellow lightning-bolt patterns, a round cute frog body with large webbed feet, large round bulging electric-yellow eyes with an alert energetic expression, tiny fingers with suction pads, inflatable throat pouch with yellow glow, smooth moist skin",
        "crouching low with legs coiled for a jumping attack, throat pouch inflating with electrical charge, zapping readiness expression",
        "brilliant golden-green and electric-yellow body with pulsing circuit-like patterns, large blazing electric-white eyes with a golden ring, ornate tiny citrine crystal on the forehead, magnificent crackling energy between the toes, golden lightning patterns along the legs",
        "devastating electric-leap attack with body releasing a discharge mid-jump, legs spread wide with lightning arcing between them, explosive thunder frog expression"
    ),
    "coral_crab": (
        "soft pink and cream body with living coral formations growing from the shell, a small round crab body with mismatched-size claws, large round bright green eyes on stalks with a cheerful determined expression, tiny coral branches and miniature sea-anemones on the back, orange-pink legs",
        "large claw raised in a defensive pinch-threat, small claw braced, body low and sideways in classic crab battle stance, plucky determined expression",
        "magnificent rose-pink and jade-green body with magnificent blooming coral-garden on the shell, large blazing emerald eyes with a jade ring, ornate golden claw-caps, tiny jade gems embedded in the coral, miniature flowering sea-garden creating a living crown",
        "devastating claw-crush attack with massive coral-encrusted claw swinging, coral fragments scattering as projectiles, fierce ocean garden warrior expression"
    ),
    "lantern_fish": (
        "deep dark blue and bioluminescent-orange body with a large glowing lantern-lure on the head, a round deep-sea fish shape, large round glowing orange eyes with an eerie mysterious expression, tiny sharp teeth in a wide grinning mouth, small fins, dark body with scattered bioluminescent spots",
        "lantern-lure blazing bright to blind and attract, mouth open wide showing teeth, lunging forward from the darkness, eerie deep-sea predator expression",
        "magnificent obsidian-blue and brilliant golden-orange body with elaborate glowing patterns like deep-sea constellations, large blazing golden-flame eyes with a vermilion ring, ornate golden lantern-lure with a ruby crystal, magnificent bioluminescent trail patterns, tiny golden fin-edges",
        "devastating lure-blast attack with lantern releasing a blinding explosion of light, body surging from darkness, teeth blazing, terrifying deep-sea dragon expression"
    ),
    "frost_clam": (
        "ice-blue and pearl-white ribbed shell with frost-crystal formations on the ridges, a classic clam shape with the shell slightly open, large round bright pale-blue eyes peeking from inside with a sleepy cozy expression, a soft blue mantle visible inside, tiny ice crystals forming around the shell opening, a small pearl visible within",
        "shell snapping shut rapidly as a trap-attack, ice crystals shooting outward from the closing, cold mist emanating, deceptively dangerous expression",
        "magnificent crystal-ice blue and pearl shell with intricate frost-flower engravings and golden trim, large blazing sapphire eyes with an ice ring, an ornate large iridescent pearl displayed proudly inside, golden shell-edge trim, magnificent ice-crystal formations like a frozen palace",
        "devastating ice-snap attack with shell launching a freezing shockwave, ice crystals exploding outward, pearl blazing with cold energy, fearsome frost fortress expression"
    ),
    "surf_seahorse": (
        "pearl-white and pale cyan body with wave-curl patterns along the tail, a small cute seahorse form with a curled tail, large round bright pale-blue eyes with a carefree happy expression, tiny crown-like head crest, a mane of flowing fin-membranes like ocean foam, a snout-like mouth",
        "tail uncoiled and lashing like a whip, body riding an invisible wave current, fin-mane flaring with speed, adventurous wave-rider expression",
        "shimmering pearl-white and silver-cyan body with flowing wave-and-wind patterns, large blazing diamond-white eyes with a cyan ring, ornate golden crown-crest with tiny moonstones, magnificent flowing fin-mane like crashing waves, elegant golden tail-tip",
        "devastating wave-riding charge attack surfing forward on energy waves, fin-mane creating wind-water hybrid trails, fierce wind-sea warrior expression"
    ),
    "tide_whale": (
        "rich teal-blue and soft white underbelly body with gentle ocean-wave patterns, a cute small whale form, large round bright blue eyes with a gentle wise expression, a small water-spout blowhole that occasionally jets water, smooth curved body, tiny pectoral fins, a broad flat tail fluke",
        "body surging forward with water-spout active, tail fluke raised for a powerful slam, gentle but determined ocean guardian expression",
        "magnificent deep sapphire-blue and pearl-white body with flowing ocean-current patterns, large blazing sapphire eyes with a teal ring, ornate golden markings along the jaw, tiny sapphire gems embedded along the back, magnificent water-aura surrounding the body, golden tail-fluke edges",
        "devastating tidal-wave attack with body creating a massive water surge, tail fluke slamming with ocean force, water energy exploding, supreme ocean guardian expression"
    ),
    "obsidian_turtle": (
        "jet-black and dark gray obsidian-textured shell with volcanic glass sheen, a strong turtle body with muscular legs, large round deep amber eyes with an ancient stoic expression, hexagonal obsidian shell-plates, dark claws, thick wrinkled skin, an impenetrable fortress appearance",
        "fully braced with shell facing the enemy as an absolute shield, eyes steady and unblinking, immovable ancient fortress expression",
        "magnificent polished obsidian-black and golden-veined shell with glowing molten-gold crack patterns, large blazing topaz-gold eyes with an amber ring, ornate golden shell-trim with embedded amber crystals, magnificent volcanic-glass sheen with internal fire-glow, golden claw-caps",
        "devastating shell-charge attack with obsidian shell glowing with inner fire, body unstoppable like a volcanic boulder, golden energy cracking outward, ancient volcanic fortress expression"
    ),
    "abyss_eel": (
        "pitch-black and deep purple elongated eel body with dark shadow tendrils flowing along the length, a sinuous serpentine shape, large round glowing pale violet eyes with a menacing predator expression, wide mouth with sharp teeth, dark fins running along the body, shadow-mist trailing from the tail",
        "body coiled in a striking serpent pose, mouth open showing fangs, shadow energy crackling along the length, terrifying deep-dark predator expression",
        "magnificent obsidian-black and deep violet body with flowing shadow-lightning patterns, large blazing dark-violet eyes with a purple ring, ornate golden jaw-guards, tiny dark amethyst embedded in the forehead, magnificent shadow-storm energy wreathing the entire length, golden fin-edges",
        "devastating shadow-strike attack with body launching like a dark lightning bolt, shadow energy exploding from the jaws, entire length crackling with dark power, terrifying abyssal serpent expression"
    ),
    "thunder_frog": (
        "brilliant golden-yellow and black body with raised electric-pattern warts and markings, a stocky poison-dart-frog shape, large round fierce electric-yellow eyes with gold patterns, vivid warning-coloration stripes, powerful jumping legs with suction-pad toes, inflatable throat pouch pulsing with electric glow",
        "leaping mid-air with legs spread wide and electric discharge arcing between toes, throat pouch blazing, fierce thunder-strike expression",
        "magnificent brilliant gold and obsidian-black body with pulsing electric circuit patterns, large blazing electric-white eyes with a golden ring, ornate tiny golden crown-mark on the head, magnificent crackling electric field around the body, golden lightning patterns along all limbs",
        "devastating thunder-strike leap releasing a massive electric discharge at the apex of the jump, body blazing with golden lightning, legs spread creating a lightning web, supreme thunder amphibian expression"
    ),
    "stardragon_fish": (
        "brilliant golden scales with starlight shimmer and deep red fin-edges, a majestic dragon-fish body with long flowing fins, large luminous golden eyes with star-shaped pupils, barbel whiskers with golden glow, every scale seems to contain a tiny star, magnificent flowing dorsal and tail fins with cosmic patterns",
        "body arched in a majestic display with all fins fully spread, scales blazing with starlight, divine aquatic dragon expression",
        "magnificent prismatic golden and cosmic-blue scales with actual star-pattern constellations across the body, large blazing white-gold eyes with a star ring, ornate golden crown-crest, barbel whiskers with tiny star-gems, magnificent flowing fins like cosmic nebulae, scales pulsing with stellar energy",
        "devastating stellar beam attack with body releasing concentrated starlight, fins spread creating cosmic patterns, every scale blazing, absolute cosmic dragon-fish deity expression"
    ),

    # ═══════════════════════════════════════════════════
    # 植灵族 BASE (47-61)
    # ═══════════════════════════════════════════════════
    "little_mushroom": (
        "a warm brown mushroom-cap creature shaped like a tiny walking toadstool with stubby legs underneath — NOT humanoid, a round oversized mushroom cap on top of a cream-white stalk body, large round bright dark eyes with a shy gentle expression peeking from under the cap, four tiny stubby root-feet at the base, spotted cap with lighter dots, a small cheerful blush on the cheeks, no arms only a round stalk body",
        "cap tilted forward as a shield while releasing pollen-spore clouds, stubby root-feet bracing defensively, determined despite being small expression",
        "magnificent golden-brown and jade-green mushroom-cap creature with luminous spore-patterns on the cap, large blazing emerald eyes with a jade ring, ornate tiny golden crown on the cap, glowing spore-dust halo, golden stalk-body markings, magnificent bioluminescent spots on the cap, four golden root-feet",
        "devastating spore-burst attack with cap releasing a massive cloud of glowing spores, body spinning to spread the attack, fierce mushroom king expression"
    ),
    "dandelion_spirit": (
        "a floating puffball creature shaped like a dandelion seed-head — a round gossamer seed-puff forming the body-head, white and pale green fluffy dandelion-puff with large round bright pale-green eyes with a dreamy whimsical expression, tiny leaf-like fin-wings for hovering, a green stem-tail, seeds gently detaching and floating away, NOT humanoid — looks like a living floating dandelion puffball with eyes",
        "spinning to release a barrage of floating seeds like projectiles, stem-tail leaning into the wind, determined wind-rider expression",
        "magnificent silver-white and golden-green gossamer puff creature with each seed glowing like a tiny star, large blazing diamond-white eyes with a cyan ring, ornate golden stem-crown on top, seeds that trail golden sparkle-trails, elegant wind-borne fairy-puff presence with golden leaf-fins",
        "devastating seed-storm attack with hundreds of glowing seeds launched in a spiral pattern, body at the center of a golden wind-vortex, majestic wind fairy puff expression"
    ),
    "fire_lotus": (
        "deep red and warm coral lotus-flower form with petals as the main body, flame-vein patterns visible in each petal, large round bright orange-amber eyes at the center with a fierce passionate expression, a green lily-pad base as feet, inner glow suggesting a burning core, petals edged with tiny flame-wisps",
        "petals opening wide to release a burst of fire energy from the core, body stance aggressive and open, fierce fire-flower expression",
        "magnificent deep crimson and golden-orange lotus with living flame patterns on each petal, large blazing golden-flame eyes with a vermilion ring, ornate golden stamen-crown at the center, petals with golden-fire edges, magnificent blazing inner core visible, golden lily-pad base",
        "devastating fire-bloom attack with all petals releasing concentrated flames simultaneously, core blazing white-hot, petals spread like a fire-star, supreme fire lotus goddess expression"
    ),
    "vine_child": (
        "a small quadruped creature made of intertwined green vines and tendrils in an animal shape like a small vine-cat, large round bright green eyes with a curious playful expression, leaf-shaped ears, four vine-legs that wiggle, small leaves growing from the back and head, a flower bud on top of the head, vine-tail curling upward",
        "vine-tendrils extending from the back to whip and grapple, body leaning forward aggressively on four legs, tendrils writhing, fierce little plant beast warrior expression",
        "magnificent emerald-green and golden vine-woven cat-beast with blooming flowers throughout the body, large blazing emerald eyes with a jade ring, ornate golden vine-crown with a fully bloomed flower on the head, golden leaf-armor patches on shoulders, magnificent vine-tendrils with golden tips extending from the back",
        "devastating vine-lash attack with massive thorny vines erupting from the ground, body directing the vine assault on four legs, flowers blooming explosively, fierce nature's wrath beast expression"
    ),
    "cactus_ball": (
        "round chubby green cactus body with friendly arranged spines, a perfectly spherical shape with tiny stubby limbs, large round bright amber eyes with a happy goofy expression, a tiny yellow flower blooming on top of the head, rosy blush on green cheeks, soft-looking despite the spines",
        "spinning with spines extended like a spiky ball-attack, flower bouncing on top, surprisingly fierce rolling expression",
        "magnificent deep jade-green and golden-spined spherical body with magnificent blooming crown of flowers, large blazing topaz eyes with an amber ring, ornate golden spine-tips, tiny amber gems among the spines, golden flower crown with multiple blooms",
        "devastating spin-charge attack rolling at high speed with golden spines blazing, flowers trailing petals, earth energy crackling, fierce desert warrior expression"
    ),
    "bamboo_spirit": (
        "a slender bamboo-insect creature shaped like a stick-insect with bamboo-segment joints, tall and thin with emerald-green and pale jade body, large oval bright green eyes with a calm elegant expression, bamboo-leaf antennae flowing upward, six thin graceful bamboo-segment legs, small bamboo-shoot tail, an overall tall willowy insect-plant appearance",
        "body bending like bamboo in wind then snapping back in a whip-strike, leaf-antennae rustling aggressively, flexible yet strong bamboo beast warrior expression",
        "magnificent jade-green and golden bamboo-insect creature with intricate carved-bamboo patterns on every segment, large blazing emerald eyes with a golden-green ring, ornate golden bamboo-joint accents at each node, magnificent bamboo-leaf antennae flowing in an invisible breeze, golden node-rings at each segment joint",
        "devastating bamboo-whip attack with body bending and releasing tremendous stored energy, bamboo-leaf antennae slicing like blades, fierce ancient bamboo sage beast expression"
    ),
    "crystal_bloom": (
        "pale amethyst and crystal-clear flower form growing from a cluster of mineral crystals, geometric crystal petals with inner prismatic light, large round bright pale-purple eyes with a mysterious delicate expression, a crystal stem, tiny gem-like leaves, faceted surfaces catching light",
        "crystal petals rotating and focusing light into a concentrated beam, body resonating with earth energy, precise crystalline warrior expression",
        "magnificent deep amethyst and golden-crystal flower with magnificent faceted petals radiating prismatic light, large blazing topaz eyes with an amber ring, ornate golden crystal-base setting, each petal a different gem-color, magnificent prismatic light display",
        "devastating crystal-beam attack with all petals focusing concentrated prismatic light, body resonating at high frequency, gem-energy explosion, supreme earth crystal expression"
    ),
    "maple_sprite": (
        "a small winged squirrel-shaped creature made of vibrant red-orange maple leaves, main body covered in autumn maple-leaf fur with tiny four legs, large round bright amber-red eyes with an energetic fiery expression, leaf-vein patterns across the body, a bushy tail of layered maple leaves, tiny maple-leaf wings, autumn color gradient from red to gold across the fur",
        "spinning like a leaf in wind creating a fire-whirlwind, body curled with tail spread, fierce autumn beast warrior expression",
        "magnificent deep crimson and brilliant gold maple-leaf squirrel beast with living flame-patterns in the leaf-fur veins, large blazing golden-flame eyes with a vermilion ring, ornate golden vein-patterns on the leaf-wings, tiny golden crown between ears, magnificent autumn-fire aura, tail trailing golden sparks",
        "devastating fire-leaf storm attack with body spinning rapidly scattering hundreds of burning maple leaves in a vortex, each leaf a tiny flame, fierce autumn fire beast expression"
    ),
    "moss_orb": (
        "round green and soft brown moss-ball body that rolls, a perfectly spherical moss-covered creature, large round bright green eyes peeking out from the moss with a calm content expression, tiny moss-tendrils as limbs, small flowers and mushrooms growing in the moss, an overall fluffy green ball appearance",
        "rolling forward at speed with moss-tendrils trailing, body compacted for a tackle-charge, surprisingly determined expression",
        "magnificent emerald and golden-green moss sphere with blooming miniature garden of golden flowers, large blazing emerald eyes with a jade ring, ornate golden vine-crown emerging from the moss, magnificent tiny ecosystem with glowing plants, golden moss-tendrils",
        "devastating rolling-crush attack with body expanding then contracting for impact, garden-energy exploding outward, moss creating entangling waves, fierce living ecosystem expression"
    ),
    "night_orchid": (
        "deep purple-black and pale lavender orchid-flower form with nighttime-bloom petals, an elegant orchid shape with mysterious dark coloring, large round glowing pale violet eyes with a mysterious alluring expression, dark stem body, petals that seem to absorb light, tiny bioluminescent spots on the petal edges, an intoxicating presence",
        "petals flaring open to release a dark pollen cloud, body swaying hypnotically, mysterious dark enchantress expression",
        "magnificent deep violet and obsidian-black orchid with flowing shadow-patterns on iridescent petals, large blazing dark-violet eyes with a purple ring, ornate tiny dark amethyst at the flower center, magnificent shadow-mist emanating from the petals, golden stamen accents",
        "devastating shadow-pollen attack with petals releasing waves of dark energy, body pulsing with shadow power, terrifying dark orchid queen expression"
    ),
    "banyan_elder": (
        "a gnarled ancient tree-tortoise hybrid creature with bark-textured shell and root-beard, a quadruped tree-beast form with four root-like sturdy legs, large oval wise amber-green eyes with a gentle elderly expression, long root-like beard hanging from the face, branch-like antlers with leaf-clusters, shell of living bark with moss, a small bird-nest on the shell, ancient patient demeanor",
        "root-feet digging into ground while branch-antlers extend to grapple, beard-roots writhing defensively, four legs braced, wise but fierce guardian beast expression",
        "magnificent ancient dark-wood and golden-moss bark-shelled tree-tortoise with glowing golden sap-veins, large blazing emerald eyes with a golden ring, ornate golden bark-crown on the shell, magnificent root-beard with golden tips, tiny golden leaf-clusters on antlers, ancient tree beast with centuries of wisdom visible",
        "devastating root-eruption attack with massive roots exploding from the ground, branch-antlers directing the assault, golden sap-energy flowing through the shell, ancient forest god beast expression"
    ),
    "blaze_crystal_lotus": (
        "deep crimson and fire-orange crystal-lotus flower with a blazing inner core of fire, crystal petals with internal flame patterns, large blazing amber-red eyes at the center with an intense passionate expression, a crystal stem with inner fire glow, molten-looking stamen, heat-shimmer around the petals",
        "crystal petals rotating to focus fire into a concentrated blast, inner core blazing intensely, devastating fire-crystal beam expression",
        "magnificent brilliant ruby-red and golden-fire crystal lotus with living flame trapped in each crystalline petal, large blazing golden-flame eyes with a ruby ring, ornate golden crystal-base, magnificent prismatic fire display within the crystals, golden stamen with fire gems",
        "devastating inferno-crystal attack with petals shattering and reforming while releasing concentrated fire-beams, core going white-hot, supreme fire crystal goddess expression"
    ),
    "thunder_bamboo": (
        "a tall bamboo-dragon creature — a serpentine bamboo body charred by lightning with crackling energy at the joints, an Eastern dragon shape made of blackened bamboo segments, large fierce electric-yellow eyes with a stern wise expression, electrified bamboo-leaf mane along the spine standing on end, four short bamboo-stump legs, cracked bark revealing electric inner glow, a charged authoritative serpentine presence",
        "body channeling lightning through bamboo segments while slithering forward on four stumpy legs, leaf-mane crackling with electricity, fierce thunder sage beast expression",
        "magnificent obsidian-green and brilliant electric-gold bamboo-dragon beast with continuous lightning patterns along every segment, large blazing electric-white eyes with a golden ring, ornate golden thunder-crown between bamboo-horns, magnificent electric field around the serpentine body, golden-lightning bamboo segments, crackling authority",
        "devastating thunder-bamboo strike channeling massive lightning through the entire serpentine body, segments blazing with power, supreme thunder bamboo dragon god beast expression"
    ),
    "stone_mushroom_king": (
        "massive gray-brown stone-textured mushroom body with a petrified cap, a large stocky stone-mushroom form, large round deep amber eyes with a stern royal expression, cracks in the stone-cap revealing glowing amber interior, stone-pillar legs, rocky texture throughout, an imposing mountain-like presence",
        "cap tilted forward as a battering-ram shield, stone body braced for impact, unbreakable mountain-king expression",
        "magnificent dark granite and golden-veined stone mushroom with glowing amber crack-patterns, large blazing topaz-gold eyes with an amber ring, ornate golden crown embedded in the stone cap, magnificent amber crystal formations growing from the cap, golden stone-plate armor",
        "devastating earth-shatter attack with stone cap slamming down creating seismic waves, amber energy exploding from the cracks, supreme stone mushroom emperor expression"
    ),
    "heart_blossom": (
        "delicate heart-shaped petals in seven soft pastel rainbow colors radiating gentle healing light, a beautiful flower form with a warm golden center, large luminous golden-pink eyes with a loving compassionate expression, soft glowing stamens, tiny floating petal-hearts around the body, an aura of warmth and healing",
        "petals opening fully to release waves of healing light energy, body radiating warmth, gentle but powerful healer expression",
        "magnificent prismatic heart-flower with intensified seven-color petals each glowing with inner light, large blazing golden-pink eyes with a rainbow ring, ornate golden stamen-crown with rose-quartz center, magnificent healing aura with floating golden heart-petals, divine flower presence",
        "devastating heart-burst attack releasing concentrated healing-and-purifying light, all seven colors blazing simultaneously, body at the center of a love-energy nova, absolute divine heart goddess expression"
    ),

    # ═══════════════════════════════════════════════════
    # 元素族 BASE (62-76)
    # ═══════════════════════════════════════════════════
    "fire_wisp": (
        "a bouncing ball of living flame with a cute face visible in the fire, warm orange-red and yellow flickering body, large round bright amber eyes within the flames with an energetic mischievous expression, tiny flame-tendrils as arms, a flame-tail, the body flickers and dances constantly",
        "body flaring larger with arms spread releasing flame bursts, core blazing brighter, fierce little fire spirit expression",
        "magnificent concentrated blue-white and golden-orange flame form with a visible inner core gem, large blazing golden-flame eyes with a ruby ring, ornate swirling flame patterns with golden streaks, a tiny ruby at the center, more defined elegant fire-form",
        "devastating fire-blast attack with body expanding into a massive fireball then contracting, concentrated flame beam, supreme fire spirit expression"
    ),
    "water_wisp": (
        "a floating sphere of living water with a cute face showing through the surface, translucent cerulean-blue and crystal-clear body, large round bright blue eyes visible through the water with a calm gentle expression, tiny water-tendril arms, gentle ripples constantly moving across the surface",
        "body elongating into a water-jet attack form, surface tension visible, focused water-strike expression",
        "magnificent crystal-clear and sapphire-blue water sphere with swirling inner currents and a visible blue gem core, large blazing sapphire eyes with a teal ring, ornate water-spiral patterns with golden-blue streaks, elegant refined water-form",
        "devastating water-cannon attack with body compressing then releasing a high-pressure blast, golden-blue energy spiraling, supreme water spirit expression"
    ),
    "grass_wisp": (
        "a floating cluster of green leaves and glowing green light forming a cute spirit, emerald-green and soft golden-green body, large round bright green eyes peeking from the leaves with a cheerful friendly expression, tiny leaf-arms, a gentle green glow, small flowers and sprouts appearing and disappearing on the surface",
        "leaves spinning outward like sharp projectiles, core glowing intensely, fierce nature spirit expression",
        "magnificent vibrant emerald and golden-green leaf-cluster with a visible jade gem core, large blazing emerald eyes with a jade ring, ornate blooming flowers and golden-tipped leaves, elegant refined nature-form",
        "devastating leaf-blade storm with hundreds of razor leaves launching outward, core releasing nature energy beam, supreme grass spirit expression"
    ),
    "thunder_wisp": (
        "a crackling ball of electric energy with a face visible in the sparks, bright yellow and electric-blue flickering body, large round electric-yellow eyes within the sparks with a hyperactive excited expression, tiny spark-tendrils as arms, constant small lightning bolts arcing across the surface",
        "body discharging multiple lightning bolts in all directions, core crackling intensely, fierce electrified spirit expression",
        "magnificent concentrated golden-yellow and brilliant white electric sphere with visible citrine gem core, large blazing electric-white eyes with a golden ring, ornate controlled lightning patterns with golden arcs, elegant refined thunder-form",
        "devastating chain-lightning attack with body releasing controlled massive bolts, golden energy web spreading outward, supreme thunder spirit expression"
    ),
    "earth_wisp": (
        "a floating cluster of small stones and pebbles orbiting a glowing amber core with a cute face, brown and amber-gold body, large round gentle amber eyes visible in the stone cluster with a patient steady expression, tiny stone-arms, sand and pebbles gently orbiting, a warm earthy glow",
        "stones compacting into a dense projectile form, amber core blazing, determined earth-strike expression",
        "magnificent polished crystal-stones and golden-veined rocks orbiting a blazing amber gem core, large blazing topaz eyes with an amber ring, ornate golden-veined stone patterns, elegant refined earth-form",
        "devastating earth-shatter attack with stones launching at extreme velocity while core releases seismic pulse, golden earth energy, supreme earth spirit expression"
    ),
    "wind_wisp": (
        "a swirling miniature whirlwind with a cute face visible in the air currents, translucent pale cyan and white body, large round bright pale-cyan eyes visible in the wind with a free-spirited playful expression, tiny wind-tendril arms, constantly spinning and shifting shape, semi-transparent",
        "body tightening into a focused wind-drill attack form, spinning faster and faster, fierce cyclone spirit expression",
        "magnificent concentrated silver-white and pale-cyan whirlwind with visible moonstone gem core, large blazing diamond-white eyes with a cyan ring, ornate controlled spiral patterns with silver streaks, elegant refined wind-form",
        "devastating tornado attack with body expanding into a massive cyclone, core directing the wind force, supreme wind spirit expression"
    ),
    "fire_elemental": (
        "a large salamander-shaped beast made entirely of living flame with a visible red gem embedded in the chest, warm orange-red and white-hot body with four sturdy fire-legs, large blazing amber-red eyes with an intense focused expression, flame-crest ridges running from the head down the spine, long fire-tail, more structured and powerful than a wisp",
        "body crouched low with four legs braced, flame-crest flaring aggressively, mouth opening to release a twin fire-stream, intense fire beast warrior expression",
        "magnificent golden-white and deep vermilion salamander-beast of concentrated fire with intricate fire-scale patterns, a large blazing ruby core-gem embedded in the chest, large blazing golden-flame eyes with a ruby ring, ornate golden fire-crown-crest along the spine, controlled flame-mane, regal fire lord beast form",
        "devastating fire-beam attack with mouth releasing concentrated flame while flame-crest erupts, ruby core blazing, body wreathed in supreme fire, supreme fire elemental beast expression"
    ),
    "water_elemental": (
        "a large serpentine water-dragon beast made entirely of flowing water with a visible blue gem at the chest-core, translucent cerulean and crystal-clear body with a sinuous finned shape, large bright sapphire eyes with a calm wise expression, water-fin crest flowing along the back like a waterfall, four webbed limbs, swirling inner currents visible through the translucent body",
        "body coiling in a serpentine lunge, water-fin crest flaring, mouth directing twin water-jet streams, focused aquatic beast warrior expression",
        "magnificent crystal-clear and deep sapphire serpentine water-beast with intricate current-pattern details, a large blazing sapphire core-gem at the chest, large blazing sapphire eyes with a teal ring, ornate golden-blue fin-crown crest, water-mane in elegant cascading streams, regal water lord beast form",
        "devastating water-cannon attack with body surging forward and mouth directing high-pressure streams, sapphire core blazing, body surrounded by water vortex, supreme water elemental beast expression"
    ),
    "grass_elemental": (
        "a large tortoise-shaped beast made of living vines flowers and leaves with a visible green gem at the chest-core, emerald-green and floral body with a domed shell of woven living branches, large bright emerald eyes with a nurturing gentle expression, flower-and-leaf crest on the head, four sturdy root-like legs, blooming flowers growing across the shell",
        "vine-tendrils extending from the shell while flowers launch pollen projectiles, body stance rooted and strong, four legs firmly planted, fierce nature beast warrior expression",
        "magnificent golden-green and deep emerald tortoise-beast of living nature with intricate vine-pattern shell and golden flowers, a large blazing jade core-gem at the chest, large blazing emerald eyes with a jade ring, ornate golden vine-crown on the shell with blooming golden flowers, regal nature lord beast form",
        "devastating vine-storm attack with massive golden-tipped vines erupting from the shell while flowers release energy bursts, jade core blazing, supreme grass elemental beast expression"
    ),
    "thunder_elemental": (
        "a large wolf-shaped beast made of crackling lightning and electric energy with a visible yellow gem at the chest-core, electric-yellow and white-blue body with four powerful legs, large blazing electric-yellow eyes with an intense charged expression, lightning-bolt mane standing upward along the spine, body crackling with constant discharges, electrified claws",
        "body lunging with four legs in a pounce, lightning-mane blazing, mouth releasing twin chain-lightning streams, fierce thunder beast warrior expression",
        "magnificent golden and brilliant white wolf-beast of living lightning with intricate circuit-pattern fur, a large blazing citrine core-gem at the chest, large blazing electric-white eyes with a golden ring, ornate golden thunder-crown-mane, controlled lightning flowing along all four legs, regal thunder lord beast form",
        "devastating thunder-storm attack with body releasing massive lightning while leaping, citrine core blazing, body at the center of an electrical maelstrom, supreme thunder elemental beast expression"
    ),
    "light_elemental": (
        "a large stag-shaped beast made of pure holy white light with a visible golden-white gem at the chest-core, warm white-gold and pale rose body that radiates gentle light, large luminous white-gold eyes with a serene benevolent expression, antlers of solidified light-rays branching upward, four graceful glowing legs, an angelic sacred beast presence",
        "antlers focusing beams of holy light, body glowing at maximum luminance, four legs braced in a noble stance, divine light beast warrior expression",
        "magnificent brilliant white-gold and pale rose stag-beast of sacred light with intricate sacred-geometry antler patterns, a large blazing sunstone core-gem at the chest, large blazing white-gold eyes with a golden ring, ornate golden divine antler-crown with holy rays, radiant halo effect, supreme light lord beast form",
        "devastating holy-light nova with antlers releasing concentrated divine beams, sunstone core blazing, body radiating blinding sacred energy, supreme divine light beast expression"
    ),
    "shadow_elemental": (
        "a large panther-shaped beast made of living shadow and dark mist with a visible dark purple gem at the chest-core, deep violet and black body with blurred shifting edges, large glowing pale violet eyes with a mysterious enigmatic expression, shadow-smoke mane floating and shifting along the spine, four legs that phase between solid and mist, long shadow-tail",
        "body stalking low with four legs, shadow-mane flaring, mouth directing twin shadow-streams, body flickering between solid and mist, mysterious dark beast warrior expression",
        "magnificent deep violet and obsidian-black panther-beast of living shadow with intricate dark-pattern fur, a large blazing dark amethyst core-gem at the chest, large blazing dark-violet eyes with a purple ring, ornate dark crown with shadow-gems on the head, controlled shadow-tendrils flowing from the mane, regal shadow lord beast form",
        "devastating shadow-nova attack with body phasing through darkness and pouncing, amethyst core blazing, shadow mane erupting into a dark vortex, supreme shadow elemental beast expression"
    ),
    "rock_elemental": (
        "a large bear-shaped beast made of stacked rocks and stone with a visible amber gem at the chest-core, brown and gray stone body with visible sediment layers, large round deep amber eyes with a calm unwavering expression, jagged crystal-cluster ridge along the spine, four massive stone-pillar legs, thick rocky tail, an imposing mountain-beast presence",
        "body rearing up on hind legs then slamming down with four massive stone-paws, earth energy cracking outward, unstoppable earth beast warrior expression",
        "magnificent polished dark-stone and golden-veined bear-beast of living rock with intricate crystal-vein patterns, a large blazing amber core-gem at the chest, large blazing topaz eyes with an amber ring, ornate golden crystal-crown on the head, golden veining throughout four massive legs, regal earth lord beast form",
        "devastating earth-shatter slam with four massive golden-veined paws, amber core blazing, seismic energy cracking outward, supreme earth elemental beast expression"
    ),
    "wind_elemental": (
        "a large eagle-serpent-shaped beast made of swirling wind and air currents with a visible pale gem at the chest-core, translucent pale cyan and white body that constantly shifts, large bright pale-cyan eyes with a free ethereal expression, wind-swept feathered crest and serpentine tail of compressed air-currents, broad wings of solidified wind, semi-transparent beast presence",
        "wings creating twin cyclone vortexes while serpentine tail whips wind-blades, body spinning with increasing velocity, focused wind beast warrior expression",
        "magnificent silver-white and pale cyan eagle-serpent-beast of controlled wind with intricate spiral-pattern plumage, a large blazing moonstone core-gem at the chest, large blazing diamond-white eyes with a cyan ring, ornate silver wind-crown-crest, controlled elegant wind-wings, regal wind lord beast form",
        "devastating cyclone attack with wings generating massive wind funnels and tail creating wind-blades, moonstone core blazing, body at the center of a hurricane, supreme wind elemental beast expression"
    ),
    "chaos_spirit": (
        "a spherical body of swirling light-and-dark energy intertwined in a yin-yang pattern, half brilliant white-gold and half deep violet-black with the two sides constantly flowing into each other, large dual-colored eyes — one white-gold and one dark-violet — with a paradoxical serene-and-intense expression, tiny light and shadow tendrils as arms, a border of prismatic energy where light meets dark",
        "light half and dark half separating slightly then clashing together in an energy burst, both elements surging, paradox warrior expression",
        "magnificent intensified yin-yang sphere of supreme light and supreme darkness with golden border energy where they meet, large blazing dual-colored eyes with golden rings, ornate golden chaos-crown floating above, prismatic lightning at the intersection, profound cosmic presence",
        "devastating chaos-burst attack with light and darkness colliding in a massive explosion, golden energy erupting at the intersection, body releasing both divine and dark power simultaneously, supreme chaos god expression"
    ),

    # ═══════════════════════════════════════════════════
    # 幻灵族 BASE (77-89)
    # ═══════════════════════════════════════════════════
    "stardust_wisp": (
        "a small ethereal spirit made of floating star-dust particles and soft golden light, a round glowing form with sparkling motes orbiting, large luminous warm golden eyes with a gentle wonder-filled expression, tiny star-dust arms, a gentle golden glow, trailing sparkle-dust",
        "body concentrating star-dust into a focused beam, sparkles intensifying, determined little star warrior expression",
        "magnificent concentrated golden and diamond-white star-dust spirit with visible constellations within, large blazing white-gold eyes with a golden ring, ornate golden star-crown, controlled orbiting star-motes, elegant cosmic fairy presence",
        "devastating star-burst attack releasing concentrated stellar energy, body expanding into a miniature supernova, constellation patterns blazing, supreme star spirit expression"
    ),
    "dark_wraith": (
        "a ghostly cat-shaped phantom made of dark purple mist and shadow, a spectral feline form with glowing pale violet eyes and wispy pointed ears, a flowing ghostly body with ragged dark edges that dissolve into smoke, four shadowy paws barely visible, tiny dark fangs, an overall mysterious spooky-cute phantom-cat appearance",
        "body pouncing through shadows with spectral claws extending, dark mist expanding aggressively, fierce phantom-cat warrior expression",
        "magnificent deep violet and obsidian-black spectral feline with ornate dark-golden ear tips and flowing shadow-fur with golden-dark trim, large blazing dark-violet eyes with a purple ring, ornate dark crown between the ghostly ears, controlled shadow-tendrils extending from the tail, regal shadow beast presence",
        "devastating shadow-pounce attack with spectral claws releasing concentrated darkness, body phasing in and out of reality, shadow-storm expanding, terrifying phantom-cat master expression"
    ),
    "dream_tapir": (
        "soft pink-purple and cream tapir body with dreamy cloud-like patterns on the fur, a small cute tapir with a distinctive long snout, large round dreamy rose-pink eyes with a sleepy peaceful expression, tiny star-patterns on the fur, cloud-like tufts of fur, a short fluffy tail, perpetually half-lidded drowsy look",
        "snout extended inhaling visible dream-mist energy, body surrounded by floating dream bubbles, sleepy but focused battle expression",
        "magnificent iridescent lavender and rose-gold tapir with flowing dream-cloud patterns, large blazing golden-pink eyes with a rainbow ring, ornate golden dream-catcher pendant, magnificent constellation-pattern fur, golden snout-tip, floating golden dream-bubbles",
        "devastating dream-devour attack with snout creating a massive vortex pulling in energy, dream-reality warping around the body, golden dream energy, supreme dream guardian expression"
    ),
    "moonbeam_spirit": (
        "a crescent-moon shaped small spirit glowing with soft silvery-white moonlight, a gentle curved lunar form, large luminous pale silver eyes with a calm serene expression, tiny moonbeam-ray arms, a gentle silver aura, small floating moon-fragments orbiting gently",
        "body focusing moonlight into a concentrated silver beam, glow intensifying, serene but focused moon warrior expression",
        "magnificent brilliant silver-white and pale gold crescent spirit with intricate lunar-surface patterns, large blazing white-gold eyes with a silver ring, ornate golden crescent-crown, controlled moonbeam rays extending elegantly, golden moon-dust halo",
        "devastating moon-beam blast with body releasing concentrated silver-gold lunar energy, crescent form blazing at maximum, supreme moon spirit expression"
    ),
    "shade_devourer": (
        "a black foggy amorphous creature with a wide dark mouth visible in the mist, deep black and dark purple shifting body with no fixed shape, large round glowing red-violet eyes with a hungry ominous expression, shadow-tendril arms reaching outward, body absorbing nearby shadows and growing slightly darker",
        "mouth opening wide to inhale shadows and energy, body expanding with consumed darkness, terrifying hunger expression",
        "magnificent controlled obsidian-black and deep violet devourer with golden-dark trim on the edges, large blazing dark-violet eyes with a red ring, ornate dark crown of shadow-thorns, controlled shadow-absorption field, defined elegant form with golden accents",
        "devastating void-consume attack with mouth creating a massive dark vortex, body at the center of a shadow maelstrom, all light being drawn in, supreme void predator expression"
    ),
    "emotion_sprite": (
        "a small heart-shaped spirit that shifts between soft pastel colors based on emotion, currently warm pink and gentle gold, large expressive eyes that change with feelings — currently bright pink with a happy cheerful expression, tiny heart-tendril arms, floating small colored hearts around the body, an emotionally open presence",
        "body flashing through multiple emotion-colors rapidly confusing enemies, hearts launching as projectiles, fierce emotional warrior expression",
        "magnificent prismatic heart-spirit cycling through all emotion-colors in a golden glow, large blazing golden-pink eyes with a rainbow ring, ornate golden heart-crown, controlled emotion-energy field with golden heart-particles, elegant empathic presence",
        "devastating emotion-burst attack releasing a shockwave of all emotional energies simultaneously, body blazing through all colors, heart-energy exploding, supreme empathic spirit expression"
    ),
    "mirror_spirit": (
        "a spirit made of floating mirror-shard fragments arranged in a vaguely humanoid form, reflective silver and prismatic body, large reflective silver-white eyes with a curious analytical expression, tiny mirror-hands, body surfaces reflecting and refracting light creating rainbow sparkles, a crystalline tinkling presence",
        "mirror-shards rotating to focus reflected light into a beam, body reconfiguring for attack, precise analytical warrior expression",
        "magnificent polished silver and prismatic crystal mirror-spirit with golden-trimmed shard edges, large blazing white-gold eyes with a prismatic ring, ornate golden mirror-crown, controlled floating shards creating an armor formation, elegant reflective presence",
        "devastating reflection-beam attack with all shards focusing infinite reflected light into a single point, body creating a prismatic explosion, supreme mirror lord expression"
    ),
    "galaxy_spirit": (
        "a small swirling galaxy-vortex spirit with visible miniature stars and nebulae within, deep cosmic blue-purple and starlight-gold body, large luminous deep blue eyes with tiny stars visible in the pupils, spiral-arms extending as limbs, a gentle cosmic glow, truly containing a miniature galaxy within",
        "spiral arms compressing the inner galaxy then releasing a cosmic-energy blast, stars brightening, focused cosmic warrior expression",
        "magnificent intensified cosmic blue-purple and golden galaxy spirit with brilliant inner star-clusters, large blazing cosmic-blue eyes with a golden star-ring, ornate golden constellation-crown, controlled galaxy-arms with golden spiral patterns, supreme cosmic presence",
        "devastating cosmic-blast attack releasing concentrated stellar energy from the galaxy core, stars going supernova, spiral arms directing the blast, supreme galaxy lord expression"
    ),
    "nether_spirit": (
        "a deep purple-black spectral entity with nether-realm energy wisps, a translucent ghostly form with visible bone-like internal structure, large glowing pale violet eyes with an ancient otherworldly expression, nether-fire wisps floating around, dark chains or bindings partially visible, an underworld presence",
        "nether-fire intensifying and chains rattling aggressively, body expanding with underworld energy, terrifying nether warrior expression",
        "magnificent deep violet and obsidian nether spirit with golden-underworld trim and controlled nether-fire, large blazing dark-violet eyes with a golden-dark ring, ornate dark golden crown, controlled chains now golden, elegant nether-realm lord form",
        "devastating nether-blast attack releasing concentrated underworld energy, chains whipping as weapons, nether-fire erupting, supreme underworld lord expression"
    ),
    "psyche_spirit": (
        "a golden-veined translucent spirit body with visible nerve-like golden pathways, soft golden and pale lavender body, large luminous golden eyes with a deeply perceptive expression, tiny golden-thread arms, a gentle golden pulse running through the veins rhythmically, an empathic sensing presence",
        "golden veins flaring as emotions are sensed and directed as energy, body resonating with psychic power, focused mind-warrior expression",
        "magnificent brilliant golden and rose-gold psyche spirit with intricate golden neural-pathway patterns, large blazing golden-pink eyes with a golden ring, ornate golden psyche-crown, controlled golden energy field, magnificent network of golden light-veins, supreme psychic presence",
        "devastating psyche-blast releasing concentrated golden mental energy, neural pathways all blazing, body at center of a golden mind-wave, supreme psyche lord expression"
    ),
    "divine_illusion": (
        "a shimmering white-platinum and golden spirit that constantly shifts between multiple beautiful forms, an elegant shape-shifting presence, large luminous white-gold eyes with a transcendent serene expression, body outline constantly morphing — sometimes angelic sometimes animal sometimes abstract, golden sparkle trail, divine holy presence",
        "form stabilizing into a powerful attack-shape then shifting rapidly, golden energy focusing, divine illusionist warrior expression",
        "magnificent brilliant white-gold and platinum illusion spirit with golden sacred-geometry patterns visible during shifts, large blazing white-gold eyes with a rainbow ring, ornate golden divine-crown that remains stable, controlled elegant form-shifts with golden trails, supreme divine presence",
        "devastating holy-illusion attack creating multiple divine after-images all attacking simultaneously, golden light everywhere, form at peak divine beauty, supreme divine illusionist expression"
    ),
    "myriad_spirit": (
        "a spherical translucent body containing tiny visions of all creatures and elements in miniature, iridescent and prismatic, large luminous golden-pink eyes with infinite depth, body showing miniature forests oceans mountains and skies rotating within, an all-encompassing presence, tiny arms of pure light",
        "body focusing the inner myriad visions into concentrated energy streams, all elements visible, overwhelming myriad warrior expression",
        "magnificent intensified prismatic and golden myriad sphere with clearer more detailed inner visions, large blazing golden-pink eyes with a rainbow ring, ornate golden cosmic crown, controlled element-energy streams extending outward, supreme all-knowing presence",
        "devastating myriad-burst releasing all elemental energies simultaneously from the inner visions, body expanding with cosmic power, all creation visible, supreme myriad lord expression"
    ),
    "realm_master": (
        "a mysterious multi-eyed floating beast of light shadow and heart energy intertwined, a chimeric creature body combining dragon-serpent and owl features with a cloak of light-and-shadow fabric, large dual-colored luminous eyes — one white-gold one pale-violet — with a commanding all-knowing expression, multiple smaller eyes along the serpentine neck, three floating gem-orbs — light shadow heart — orbiting the horned head, four clawed limbs of mixed light-shadow energy, feathered wings of opposing light and dark",
        "wings flaring as all three energies surge simultaneously, claws directing reality-warping power, all eyes blazing, commanding realm-master beast expression",
        "magnificent supreme light-shadow-heart chimeric beast with golden ornate armor plating on shoulders and chest, large blazing tri-colored eyes, ornate golden triple-crown with three blazing gems between grand horns, controlled reality-warping field with golden borders, feathered wings one light one dark with golden edges, absolute master beast presence",
        "devastating realm-collapse attack warping space with all three energies, claws directing reality itself, all eyes releasing beams, golden border energy containing the chaos, supreme dimension lord beast expression"
    ),

    # ═══════════════════════════════════════════════════
    # 龙族 BASE (90-103)
    # ═══════════════════════════════════════════════════
    "fire_dragonling": (
        "bright red and warm orange small dragon with tiny wings and a chubby body, classic baby dragon proportions, large round bright amber-red eyes with an eager excited expression, small smoke wisps from the nostrils, tiny horns, a pudgy belly, short thick tail with a flame-tip, stubby legs with small claws",
        "mouth open wide breathing a small flame, tiny wings flapping excitedly, stubby legs braced, eager young dragon warrior expression",
        "magnificent deep crimson and golden-orange dragon with grown wings showing flame-patterns, large blazing golden-flame eyes with a vermilion ring, ornate golden horn-crowns, flame-patterned scales, golden claw-tips, a magnificent flame-wreathed tail, proud young fire dragon form",
        "devastating fire-breath attack with mouth releasing concentrated flames, wings spread creating fire-updraft, body surging with fire power, fierce fire dragon expression"
    ),
    "water_serpent": (
        "teal-blue and pearl-white long sinuous Chinese serpent-dragon body with flowing whiskers, an elegant Eastern dragon whelp, large round bright blue eyes with a playful mischievous expression, long barbel whiskers, tiny fin-like legs, flowing mane of water-like tendrils along the spine, a pearl held under the chin",
        "body coiling in a serpentine strike pose, whiskers forward sensing the enemy, water-mane flaring, cunning water serpent expression",
        "magnificent deep sapphire and silver-white serpent dragon with flowing aqua-silk mane, large blazing sapphire eyes with a teal ring, ornate golden whisker-tips, a large luminous pearl at the chin, golden scale-accents along the body, magnificent flowing water-energy aura",
        "devastating water-cyclone attack with body spiraling to create a water-tornado, pearl blazing with ocean power, mane whipping water-blades, supreme water serpent expression"
    ),
    "rock_drake": (
        "gray-brown and sandy stocky lizard-dragon with thick rocky armor plates, a low wide body built like a tank, large round deep amber eyes with a calm stubborn expression, heavy jaw with underbite, thick armored tail, wide flat feet with heavy claws, rocky spine-ridges along the back, a squat powerful build",
        "head lowered with armored skull aimed forward in a charge, tail raised as a counterweight, stubborn unstoppable charge expression",
        "magnificent dark granite and golden-veined armored drake with glowing amber plates, large blazing topaz eyes with an amber ring, ornate golden horn-spikes, massive reinforced armor plates with golden cracks, golden claw-gauntlets, supreme earth-tank form",
        "devastating armored charge with head slamming into the ground creating a seismic wave, golden energy erupting from armor cracks, unstoppable earth drake expression"
    ),
    "wind_wyvern": (
        "green-white and silver sleek young wyvern with large bat-like wings and an elongated body built for flight, large round bright emerald-green eyes with an adventurous excited expression, a pointed snout, thin tail with a small fin, wing-arms with tiny claws, a tiny emerald bead on a cord",
        "large wings fully spread ready for takeoff, body crouched in a launch position, tail fin angled for steering, bright excited flight-ready expression",
        "magnificent pearl-green and silver-white wyvern with shimmering wind-pattern wing membranes, large blazing emerald-green eyes with a golden-green ring, ornate golden wing-claw caps, magnificent expanded wings with golden-wind trails, golden snout-tip, elegant aerodynamic form",
        "devastating dive-bomb attack from extreme height with wings tucked creating sonic wind-blade, body streamlined for maximum impact, fierce wind wyvern expression"
    ),
    "spark_ceratops": (
        "yellow and dark brown young ceratops-dragon with a large triangular head-crest that crackles with electricity, a stocky four-legged body, large round electric-yellow eyes with a fierce brave expression, three small horns on the face, the large bony frill glowing with electric patterns, thick sturdy legs, a short thick tail",
        "head lowered with horns aimed forward and frill crackling with electricity charging for a ram-attack, fierce little thunder-horn expression",
        "magnificent golden-yellow and obsidian-brown ceratops with a magnificent electric-crackling frill displaying lightning patterns, large blazing electric-white eyes with a golden ring, ornate golden horn-tips, electrified golden frill-edge, magnificent lightning crown-crest",
        "devastating thunder-charge attack with horns blazing electricity and frill releasing a massive discharge on impact, body surrounded by thunder, supreme thunder horn expression"
    ),
    "flora_lindworm": (
        "green and floral-pattern limbless serpent-dragon with flowering vines growing along the body, an elegant snake-dragon form, large round bright green eyes with a gentle graceful expression, tiny flower-buds growing from the head as horns, moss and small flowers along the spine, a leaf-shaped tail tip",
        "body coiled and striking forward with vine-whip tail, flowers releasing pollen burst, graceful yet fierce lindworm expression",
        "magnificent deep emerald and golden-green serpent dragon with magnificent flowering vine body, large blazing emerald eyes with a jade ring, ornate golden flower-crown horns, golden vine-patterns, magnificent blooming flower-garden along the entire body, golden tail-leaf",
        "devastating flora-strike with body whipping forward while flowers explode with nature energy, vines lashing, supreme flora serpent expression"
    ),
    "gale_pteranodon": (
        "pale gray and white young pteranodon with an enormous head-crest and vast membrane wings, a lean flying-reptile form, large round bright pale-cyan eyes with a sharp focused expression, long pointed beak, a large curved head-crest, thin body built entirely for flight, clawed wing-tips",
        "wings fully spread catching an updraft, beak open in a diving screech, body angled for an attack dive, fierce sky predator expression",
        "magnificent silver-white and pale cyan pteranodon with wind-pattern membrane wings, large blazing diamond-white eyes with a cyan ring, ornate golden crest-tip, golden beak-tip, magnificent wind-trail wings, elegant supreme flying form",
        "devastating supersonic dive with wings creating shockwave-trails, body at extreme velocity, golden wind energy, supreme sky lord expression"
    ),
    "shadow_dragon": (
        "dark purple and obsidian-black sleek dragon with shadow-mist trailing from the body, an elegant sinister dragon form, large glowing pale violet eyes with a cold calculating expression, curved dark horns, membranous wings with shadow-pattern, shadow tendrils extending from the tail and claws, a dark majestic presence",
        "body partially dissolved into shadow-mist, claws extending from the darkness, wings spread revealing shadow-vortex patterns, terrifying shadow predator expression",
        "magnificent deep violet and obsidian-black shadow dragon with golden-dark ornamental trim, large blazing dark-violet eyes with a purple ring, ornate golden-dark horns with amethyst tips, controlled shadow-field, golden scale-accents piercing through the darkness, dark regal presence",
        "devastating shadow-breath attack releasing concentrated darkness from the jaws, body phasing between shadow and solid, wings creating dark-blade trails, supreme shadow dragon expression"
    ),
    "radiant_dragon": (
        "white-gold and luminous platinum dragon with scales that radiate gentle holy light, an elegant sacred dragon form, large luminous white-gold eyes with a serene dignified expression, elegant swept-back golden horns, crystalline wing-membranes that refract light into rainbows, a sacred presence, golden claws",
        "body glowing with intensified holy light, wings spread creating a halo effect, divine dragon warrior expression",
        "magnificent brilliant white-gold and platinum dragon with blazing sacred-geometry scale patterns, large blazing white-gold eyes with a golden ring, ornate golden divine-crown with sunstone, magnificent crystalline wings radiating prismatic light, golden horn filigree, supreme holy dragon form",
        "devastating holy-breath attack releasing concentrated divine light, wings creating a light-nova, body at the center of sacred radiance, supreme holy dragon god expression"
    ),
    "ocean_dragon": (
        "rich deep blue and teal Eastern-style dragon with flowing ocean-wave mane and whiskers, a classic Chinese dragon form swimming through the air, large bright sapphire-blue eyes with a commanding noble expression, long flowing body with wave-pattern scales, flowing whiskers and mane, a tide-pearl at the chin, fin-lined spine",
        "body spiraling through the air creating water-currents, pearl blazing, mane and whiskers streaming with water energy, majestic ocean lord expression",
        "magnificent deep sapphire and silver-white ocean dragon with golden wave-pattern scales, large blazing sapphire eyes with a teal ring, ornate golden whisker-tips and mane-ornaments, a magnificent large luminous pearl, golden fin-edges, supreme ocean dragon lord form",
        "devastating tidal-wave breath creating a massive wall of water, body spiraling generating a waterspout, pearl directing the ocean's fury, supreme ocean dragon god expression"
    ),
    "ironscale_dragon": (
        "iron-gray and dark steel armored dragon with incredibly thick overlapping plate-scales, a massive heavily-armored dragon form, large round deep amber eyes with a stern unbreakable expression, heavy blunt horns, thick armored wings folded like shields, a mace-like tail, every surface covered in iron-like scales",
        "body lowered into maximum defense posture, tail raised as a weapon, scales hardening with a metallic sheen, immovable fortress expression",
        "magnificent polished dark-iron and golden-veined armored dragon with glowing amber reinforcement patterns, large blazing topaz eyes with an amber ring, ornate golden horn-caps, magnificent golden-reinforced plate armor, golden mace-tail tip, supreme iron fortress dragon form",
        "devastating iron-tail slam with mace-tail crashing down, armor plates expanding with golden energy, seismic force, supreme iron dragon god expression"
    ),
    "heart_dragon": (
        "golden-purple and iridescent scales on an elegant Eastern dragon with heart-pattern markings visible on the scales, a noble Chinese dragon form, large luminous golden-pink eyes with a gentle wise expression, elegant curved horns with heart-shaped tips, flowing silk-like whiskers, a rose-quartz pearl at the chin, gentle warm aura",
        "body undulating gently while projecting heart-energy waves, pearl glowing, whiskers directing the energy, compassionate but powerful expression",
        "magnificent prismatic golden-purple dragon with blazing heart-pattern constellation scales, large blazing golden-pink eyes with a rainbow ring, ornate golden heart-crown, rose-quartz pearl blazing with love-energy, magnificent golden flowing whiskers and mane, supreme heart dragon lord form",
        "devastating heart-wave attack with pearl releasing a massive love-energy shockwave, scales all blazing with heart patterns, body radiating divine compassion-power, supreme heart dragon god expression"
    ),
    "inferno_ancient": (
        "deep crimson-black and molten-gold massive ancient dragon with cracked volcanic scales revealing inner lava, an imposing ancient dragon form, large blazing white-hot eyes with amber cores showing absolute power, grand sweeping horns with molten tips, massive scarred wings, a thick tail with a molten mace-tip, volcanic majesty, ancient scars across the body",
        "jaws opening to reveal a white-hot inferno within, wings spread creating heat-shimmer, body radiating overwhelming volcanic heat, absolute supreme power expression",
        "magnificent obsidian-black and blazing molten-gold ancient dragon with lava-flow scale patterns, large blazing white-gold eyes with a ruby ring, ornate golden-magma crown between grand horns, magnificent volcanic wings with golden-lava edges, every scale-crack blazing with inner fire, supreme ancient fire god form",
        "devastating ancient-fire breath unleashing a volcanic inferno, wings creating firestorm updraft, body erupting with primordial fire, absolute supreme dragon god expression"
    ),
    "cosmos_dragon": (
        "magnificent five-colored shimmering dragon with scales cycling through all elemental colors, a supreme Chinese dragon form of divine proportions, large luminous prismatic eyes with infinite depth showing all elements, grand multi-colored flowing mane and whiskers, every scale a different jewel-color, a massive multi-colored pearl at the chin, absolute dragon majesty, golden claws and horns",
        "body coiling through space displaying all elemental colors, pearl blazing with all elements, supreme cosmic dragon expression showing all-element mastery",
        "magnificent intensified prismatic cosmic dragon with golden-bordered scales each blazing a different element, large blazing prismatic eyes with a golden cosmic ring, ornate golden multi-gem crown, magnificent all-element pearl, golden whiskers trailing cosmic energy, supreme cosmic dragon god form",
        "devastating all-element breath releasing every elemental energy simultaneously, body at the center of a cosmic maelstrom, all colors blazing, absolute supreme cosmic dragon god expression"
    ),

    # ═══════════════════════════════════════════════════
    # 合成宠 — 兽灵族合成 (1-20)
    # ═══════════════════════════════════════════════════
    "steam_beast": (
        "a vapor-shrouded beast with patches of warm cream and cool teal fur, steam constantly rising from the body, a chimeric form blending mammalian features, large round dual-toned blue-and-amber eyes with a restless energetic expression, mist curling from the nostrils, damp fur with condensation droplets",
        "body releasing jets of pressurized steam from vents along the spine, crouched in an aggressive lunge, fierce steam-powered expression",
        "magnificent chrome-silver and golden-steam beast with controlled vapor vents and glowing amber-teal patterns, large blazing dual-toned eyes with golden rings, ornate golden steam-valve accents, magnificent pressurized steam aura, refined powerful form",
        "devastating steam-explosion attack with superheated vapor erupting from all vents, body surging with thermal power, fierce steam titan expression"
    ),
    "char_deer": (
        "a blackened-wood deer with charcoal and ember-orange fur, antlers of smoldering charred branches with tiny glowing ember-tips, large round warm amber eyes with a resilient determined expression, cracked bark-texture skin revealing orange glow beneath, ash particles floating from the body",
        "antlers blazing with renewed fire as it lowers them to charge, body trailing ash and sparks, fierce reborn warrior expression",
        "magnificent obsidian-black and golden-ember deer with blazing golden-fire antler branches, large blazing golden-flame eyes with a vermilion ring, ornate golden bark-armor patches, magnificent ember-trail aura, charred beauty form",
        "devastating charge attack with blazing antlers, ash-storm trailing, body wreathed in renewal fire, supreme charcoal phoenix-deer expression"
    ),
    "lava_armadillo": (
        "iron-gray armored body with glowing orange-red lava visible through cracks in the shell plates, a heavy compact armadillo form, large round fierce amber-red eyes with an intense expression, molten lava seeping between armor segments, heat-shimmer around the body, heavy clawed feet leaving scorch marks",
        "curled into a ball rolling with lava trailing like a meteor, shell plates glowing white-hot, unstoppable lava juggernaut expression",
        "magnificent obsidian and molten-gold armored form with controlled lava-flow patterns between golden plates, large blazing white-gold eyes with a ruby ring, ornate golden armor trim, magnificent magma-core glow, supreme volcanic fortress form",
        "devastating magma-roll attack leaving a trail of molten rock, shell erupting lava on impact, seismic force, supreme volcanic titan expression"
    ),
    "moss_creek_raccoon": (
        "green-tinted teal and cream fur covered in patches of soft moss, a pudgy raccoon-dog body with aquatic moss-garden growing on the back, large round bright green-blue eyes with a peaceful lazy expression, moss-covered mask markings, webbed paws with moss between the toes, tiny flowers growing in the back-moss",
        "shaking body to release a wave of moss-spores and water droplets, crouching in a defensive splash-stance, calm guardian expression",
        "magnificent jade-green and aquamarine fur with a magnificent miniature moss-water-garden on the back, large blazing emerald-teal eyes with a jade ring, ornate golden vine-collar, golden moss-tips, blooming water-flowers, supreme nature-water spirit form",
        "devastating moss-wave attack with water and plant energy erupting together, back-garden expanding explosively, supreme nature guardian expression"
    ),
    "mudstone_badger": (
        "dark brown and gray mud-encrusted heavy body with dried mud armor patches, a stocky powerful badger form, large round deep amber eyes with a grim determined expression, thick mud-caked claws, stone-reinforced spine ridge, permanent mud-splash patterns across the fur",
        "claws dragging through the ground creating mud-wave attacks, body low and braced, stubborn earth warrior expression",
        "magnificent dark granite and golden-mud armored badger with crystallized mud-plates and golden veining, large blazing topaz eyes with an amber ring, ornate golden claw-caps, magnificent crystal-mud armor, supreme earth tank form",
        "devastating mud-avalanche attack with claws ripping the ground open, crystal-mud projectiles launching, supreme earth warrior expression"
    ),
    "gale_hedgehog": (
        "silver-white and green body with wind-blade spines instead of normal quills, a round hedgehog form with razor-sharp wind-hardened spines, large round bright cyan-green eyes with a fierce determined expression, spines that hum with wind-vibration, streamlined for speed despite the round shape",
        "spinning rapidly launching wind-blade spines as projectiles, body becoming a whirling wind-weapon, fierce wind-cutter expression",
        "magnificent pearl-white and jade-green body with magnificent crystalline wind-blade spines, large blazing diamond-green eyes with a cyan ring, ornate golden spine-base accents, magnificent wind-aura, supreme wind-blade hedgehog form",
        "devastating wind-blade storm with all spines launching simultaneously while body spins generating a cyclone, supreme wind warrior expression"
    ),
    "flash_weasel": (
        "electric-yellow and silver sleek body crackling with constant lightning, an extremely elongated weasel form built for impossible speed, large round bright electric-white eyes with a manic excited expression, lightning-bolt fur markings, tail trailing a constant electric arc, blur-lines suggesting perpetual motion",
        "body moving so fast it appears in multiple positions simultaneously, lightning connecting each afterimage, insanely fast expression",
        "magnificent golden-white and electric-blue body with pulsing lightning circuit patterns, large blazing electric-white eyes with a golden ring, ornate golden speed-lines along the body, magnificent electric aura, supreme speed-lightning form",
        "devastating lightning-dash attack appearing everywhere at once, electric explosions at each impact point, supreme speed demon expression"
    ),
    "mist_fox": (
        "warm amber and cool teal-gray fur with mist constantly emanating from the body, a graceful fox form shrouded in warm steam-mist, large round mysterious amber-teal eyes with a cunning mysterious expression, multiple tail-tips visible through the mist, warm breath creating perpetual fog, an elusive misty presence",
        "dissolving partially into mist while striking from multiple angles, tails creating fog screens, cunning illusionist expression",
        "magnificent golden-amber and silver-mist fox with controlled fog-veil and golden sparkle-mist, large blazing golden-teal eyes with dual rings, ornate golden mist-collar, magnificent triple tails trailing golden mist, supreme mist illusionist form",
        "devastating mist-strike attack emerging from fog to deliver a concentrated blow, golden mist exploding, supreme fox spirit expression"
    ),
    "thorn_ox": (
        "deep brown bark-textured hide with living thorny branches growing from the shoulders and head like extra horns, a massive ox form with tree-bark skin, large round deep green-amber eyes with a calm immovable expression, horns wrapped in thorny vines, wooden hooves, thick neck with bark-armor",
        "horns aimed forward with thorns extending aggressively, hooves stamping creating root-tremors, immovable thorn-fortress expression",
        "magnificent dark wood-brown and golden-green bark-armored ox with magnificent blooming thorn-branches, large blazing emerald-amber eyes with a jade ring, ornate golden thorn-crown, golden bark-plate armor, supreme forest titan form",
        "devastating thorn-charge with branches extending into lances, roots erupting underfoot, supreme nature-earth titan expression"
    ),
    "soul_blaze_lion": (
        "golden-cream and ethereal blue-white flame-mane lion with soul-fire burning instead of normal fire, a majestic lion form with ghostly flame aura, large blazing golden-pink eyes with an intense passionate expression, mane of translucent soul-fire that burns pink-gold, spiritual warmth radiating from the body",
        "mane erupting with soul-fire while roaring, body radiating emotional power, passionate soul warrior expression",
        "magnificent white-gold and rose-flame lion with magnificent soul-fire mane burning with love-energy, large blazing golden-pink eyes with a heart-flame ring, ornate golden heart-crown, soul-fire spreading warmth, supreme heart-fire lion king form",
        "devastating soul-fire roar releasing a wave of emotional flame, mane fully ablaze with pink-gold fire, supreme soul lion god expression"
    ),
    "frost_fang_wolf": (
        "ice-blue and silver-white fur with frost crystals forming on the muzzle and paws, a lean powerful wolf form built for cold endurance, large fierce icy-blue eyes with a cold calculating expression, visible breath in cold air, ice-crystal fangs, frost-tipped ears, thick winter fur with ice-crystal patterns",
        "lunging with ice-crystal fangs bared, body radiating freezing cold, paws leaving frost-prints, fierce arctic predator expression",
        "magnificent crystal-ice and silver wolf with magnificent frost-crystal armor and golden-ice accents, large blazing sapphire eyes with an ice ring, ornate golden ice-crown, magnificent frost-crystal mane, golden fang-tips, supreme frost wolf lord form",
        "devastating frost-fang attack with ice-crystal jaws creating a freezing shockwave, body trailing a blizzard, supreme arctic wolf god expression"
    ),
    "thunder_roar_tiger": (
        "dark storm-gray and electric-gold striped fur with continuous lightning crackling between the stripes, a powerful large tiger form with storm energy, large blazing electric-gold eyes with a fierce commanding expression, electrified whiskers, thunder-rumble vibrating from the body, storm-clouds forming around the paws",
        "roaring with visible thunderclap shockwave, body discharging lightning in all directions, supreme thunder beast expression",
        "magnificent obsidian-black and brilliant electric-gold tiger with pulsing storm-patterns, large blazing electric-white eyes with a golden-lightning ring, ornate golden thunder-crown, magnificent electric storm aura, golden lightning-stripes, supreme storm tiger king form",
        "devastating thunder-roar attack with a roar that creates a lightning-storm, body at the center of a thunderstorm, supreme storm tiger god expression"
    ),
    "jade_radiant_deer": (
        "luminous jade-green and warm golden-cream fur with faintly glowing antlers, an elegant deer form radiating gentle green-gold light, large luminous emerald-gold eyes with a serene noble expression, antlers that shine with inner jade light, golden hooves, a jade pendant on a vine cord, gentle nature-light aura",
        "antlers blazing with concentrated jade-light beams, body stance noble and powerful, radiant nature warrior expression",
        "magnificent brilliant jade-green and golden deer with magnificent crystalline jade antlers radiating holy nature-light, large blazing emerald-gold eyes with a golden-jade ring, ornate golden vine-crown, jade-light aura, supreme radiant forest lord form",
        "devastating jade-light beam from antlers with concentrated nature-holy energy, body radiating green-gold light, supreme forest deity expression"
    ),
    "phantom_leopard": (
        "pale silver-white and dark violet fur that phases between solid and shadow, a sleek leopard form that flickers like a mirage, large round glowing violet-cyan eyes with a mysterious elusive expression, shadow-spots that shift and move across the fur, partially transparent body edges, a ghostly silent presence",
        "body phasing in and out of visibility while striking from blind spots, shadow-form attack, elusive phantom warrior expression",
        "magnificent silver and deep-violet phantom leopard with controlled phase-shifting and golden-shadow accents, large blazing violet-cyan eyes with a golden ring, ornate golden shadow-collar, magnificent controlled translucency, supreme phantom hunter form",
        "devastating phase-strike attack appearing and disappearing rapidly while delivering multiple blows, supreme phantom assassin expression"
    ),
    "iron_badger_king": (
        "heavy iron-gray and dark steel fur with visible metal-like plating, a massive badger form armored in iron-hard fur, large fierce deep amber eyes with an indomitable king expression, metal-sheen claws, reinforced head-stripe of steel-gray, every part built for maximum defense, an impregnable presence",
        "claws crossed in a defensive stance creating an iron wall, body completely braced, unyielding iron king expression",
        "magnificent polished dark-iron and golden-steel badger with golden reinforcement patterns, large blazing topaz eyes with a golden ring, ornate golden iron-crown, magnificent golden-reinforced armor plating, supreme iron fortress king form",
        "devastating iron-claw assault with metal-enhanced claws ripping through defenses, golden iron energy, supreme iron badger emperor expression"
    ),
    "inferno_lion_king": (
        "deep crimson and blazing gold mane of heavenly fire, a magnificent lion form wreathed in intense flames, large blazing white-gold eyes with an absolute authority expression, massive burning mane that reaches skyward, golden-fire paws, flame-tail, every hair burning with divine fire, a king-of-all-beasts presence",
        "massive roar with mane erupting into a pillar of fire, body radiating supreme heat, absolute fire king expression",
        "magnificent white-gold and supreme vermilion lion with heavenly flame mane blazing with divine fire, large blazing white-gold eyes with a ruby ring, ornate golden emperor-crown with fire-gems, supreme divine-fire aura, golden flame-armor, absolute fire lion god form",
        "devastating heavenly fire roar creating a firestorm, mane becoming a fire-tornado, supreme fire lion god expression"
    ),
    "qilin_fire_aspect": (
        "golden-crimson qilin with flame-element transformation, warm golden scales with fire-pattern overlay, a majestic qilin form wreathed in gentle flames, large blazing golden-amber eyes with a compassionate fierce expression, flame-wreathed horn, fire-mane, gentle fire-aura that warms but doesn't burn",
        "horn directing concentrated fire-heart energy, body wreathed in compassionate flames, fierce yet gentle fire-qilin expression",
        "magnificent supreme golden-crimson qilin with divine fire-heart patterns, large blazing golden-flame eyes with a heart-fire ring, ornate golden fire-crown with ruby-heart gem, magnificent divine flame-aura, supreme fire-qilin god form",
        "devastating fire-heart beam from horn with divine flames carrying love-energy, body blazing with supreme fire-heart power, absolute fire-qilin deity expression"
    ),
    "qilin_ice_aspect": (
        "golden-sapphire qilin with ice-element transformation, pale golden scales with frost-pattern overlay, a majestic qilin form surrounded by gentle frost, large blazing golden-blue eyes with a compassionate serene expression, ice-crystal horn, frost-mane, gentle cold-aura that soothes",
        "horn directing concentrated ice-heart energy, body surrounded by compassionate frost, serene yet powerful ice-qilin expression",
        "magnificent supreme golden-sapphire qilin with divine ice-heart patterns, large blazing golden-ice eyes with a heart-ice ring, ornate golden ice-crown with sapphire-heart gem, magnificent divine frost-aura, supreme ice-qilin god form",
        "devastating ice-heart beam from horn with divine frost carrying love-energy, body blazing with supreme ice-heart power, absolute ice-qilin deity expression"
    ),
    "purgatory_beast": (
        "obsidian-black and blazing crimson-gold massive beast with fire and lightning intertwined across the body, a terrifying ancient beast form, large blazing white-hot eyes with absolute destructive expression, thunder-fire horns, flame-lightning mane, volcanic and electrical energy merged",
        "body erupting with both fire and lightning simultaneously, earth shaking with each step, absolute destruction expression",
        "magnificent supreme obsidian and golden-magma beast with controlled fire-lightning patterns, large blazing white-gold eyes with a fire-lightning ring, ornate golden purgatory-crown, supreme fire-thunder aura, absolute divine beast form",
        "devastating fire-thunder apocalypse attack with both elements exploding together, reality-shaking power, supreme purgatory god expression"
    ),
    "primordial_qilin": (
        "supreme white-gold and prismatic qilin with all colors shimmering across divine scales, the ultimate qilin form radiating pure benevolent power, large blazing prismatic eyes with golden rings showing infinite wisdom, magnificent spiraling golden horn with all gems, flowing rainbow mane, divine halo of light and heart energy",
        "horn channeling supreme heart-light energy, body radiating absolute divine power, ultimate benevolent deity expression",
        "magnificent supreme prismatic-golden qilin with blazing sacred-geometry scale patterns, large blazing white-gold eyes with a prismatic ring, ornate supreme golden crown with all gem types, magnificent divine aura of all elements, absolute primordial deity form",
        "devastating primordial beam from horn releasing the power of creation itself, all elements and heart energy merged, absolute supreme qilin god expression"
    ),

    # ═══════════════════════════════════════════════════
    # 合成宠 — 羽翼族合成 (21-38)
    # ═══════════════════════════════════════════════════
    "thunderfire_wing": (
        "a striking bird with one wing of crackling lightning and one wing of blazing fire, a medium bird form with asymmetric elemental wings, large round fierce dual-toned amber-and-yellow eyes with an intense expression, thunder-fire plumage mixing gold and red, sparks and embers trailing from the wings",
        "both wings spread releasing simultaneous fire and lightning from each side, fierce dual-element warrior expression",
        "magnificent golden-red and electric-blue asymmetric-winged bird with controlled fire-lightning patterns, large blazing dual-toned eyes with golden rings, ornate golden dual-element crown, supreme fire-thunder bird form",
        "devastating dual-element attack with fire-wing and thunder-wing releasing simultaneously, supreme thunder-fire deity expression"
    ),
    "seafoam_swallow": (
        "ocean-blue and pearl-white sleek swallow with seafoam-mist trailing from the wings, a graceful swift form, large bright teal-blue eyes with a free adventurous expression, long forked tail with water-mist tips, salt-crystal speckles on the feathers, an ocean breeze presence",
        "diving through seafoam spray at high speed, wings cutting water and wind, fierce sea-wind warrior expression",
        "magnificent sapphire and pearl swallow with golden-seafoam wing-trails, large blazing sapphire-cyan eyes with golden rings, ornate golden sea-crown, magnificent seafoam aura, supreme ocean-wind bird form",
        "devastating sea-wind dive creating a combined water-wind shockwave, supreme ocean-wind warrior expression"
    ),
    "pollen_moth": (
        "soft green-gold wings with luminous pollen-dust particles and flower patterns, a beautiful moth form, large round warm golden-green eyes with a gentle nurturing expression, feathery antennae tipped with tiny golden light-pollen, body dusted with glowing pollen",
        "wings releasing massive clouds of glowing pollen that heals allies and damages enemies, gentle healer-warrior expression",
        "magnificent emerald and golden moth with magnificent luminous pollen-cloud wings, large blazing golden-green eyes with jade-gold rings, ornate golden antennae-crowns, supreme nature-light moth form",
        "devastating pollen-light storm with wings creating golden healing-attack energy, supreme nature-light moth deity expression"
    ),
    "sandstorm_owl": (
        "sand-brown and dark stone-gray feathers with swirling sand-dust patterns, a sturdy owl form with intense eyes, large round piercing amber-gold eyes with a vigilant watchful expression, sand particles orbiting slowly, thick feathered talons, gritty desert-storm presence",
        "wings creating sandstorm blasts while eyes lock onto prey through the dust, fierce desert sentinel expression",
        "magnificent golden-sand and dark granite owl with controlled sandstorm aura, large blazing topaz eyes with amber rings, ornate golden desert-crown, supreme sand-storm sentinel form",
        "devastating sandstorm attack with wings generating a massive dust-storm, supreme desert guardian expression"
    ),
    "dark_wing_bat": (
        "obsidian-black and deep violet bat with shadow-infused wing membranes showing void-like depth, a sinister sleek bat form, large round glowing red-violet eyes with a predatory menacing expression, shadow trails from wing-tips, silent dark presence, wind from wingbeats carries cold darkness",
        "swooping with shadow-blades extending from wings, body partially merged with darkness, terrifying shadow predator expression",
        "magnificent deep violet and obsidian bat with golden-shadow wing patterns, large blazing dark-violet eyes with golden-dark rings, ornate dark golden ear-ornaments, supreme shadow-wind bat lord form",
        "devastating shadow-dive with wings releasing concentrated darkness blades, supreme void predator expression"
    ),
    "flame_crane": (
        "brilliant vermilion-red and white plumage with both wings fully ablaze with living fire, a tall elegant crane form, large blazing amber-gold eyes with a regal warrior expression, flame-crown on the head, body surrounded by fire-aura, long legs with golden-fire glow, magnificent burning presence",
        "performing a fire-dance martial art with wings creating flame-arcs, one leg raised in crane-stance, supreme fire dancer expression",
        "magnificent pure white and supreme vermilion crane with golden flame-pattern plumage, large blazing white-gold eyes with a ruby ring, ornate golden flame-crown, supreme divine fire-dance aura, golden leg-bands",
        "devastating fire-dance attack creating a spiral of flame, wings painting fire-calligraphy in the air, supreme fire crane deity expression"
    ),
    "mist_ocean_gull": (
        "translucent pearl-white and ocean-blue feathers that dissolve into sea-mist at the edges, a graceful gull form that seems half-mist, large round bright teal-blue eyes with a free ethereal expression, body phasing between solid and sea-mist, salt-crystal sparkles throughout",
        "body dissolving into mist then reforming to strike, water-mist attacks from all angles, elusive ocean spirit expression",
        "magnificent pearl and sapphire mist-gull with golden-mist accents and controlled phase-shifting, large blazing sapphire eyes with golden rings, ornate golden mist-crown, supreme ocean-mist spirit form",
        "devastating mist-burst attack appearing from sea-fog to deliver concentrated water-strikes, supreme ocean mist deity expression"
    ),
    "emerald_butterfly": (
        "brilliant emerald-green wings made of living jade-colored leaves with intricate vein patterns, a beautiful butterfly form, large round bright emerald eyes with a graceful regal expression, antennae of golden-green vine-curls, body of living jade-crystal, wings that genuinely look like precious jade leaves",
        "wings releasing a storm of razor-sharp jade-leaf projectiles, body spinning elegantly, fierce jade warrior expression",
        "magnificent deep jade and golden butterfly with living crystal-jade wing petals, large blazing emerald eyes with golden-jade rings, ornate golden vine-crown, supreme emerald fairy form",
        "devastating jade-leaf storm with wings shattering and reforming repeatedly launching crystal projectiles, supreme jade fairy deity expression"
    ),
    "storm_eagle": (
        "dark storm-gray and electric-gold feathers with continuous lightning arcing across the body, a massive powerful eagle form wreathed in storm energy, large blazing electric-gold eyes with fierce commanding expression, electrified crest, thunder-rumble wingbeats, storm-cloud aura",
        "diving through self-generated storm with lightning trailing from every feather, devastating thunder warrior expression",
        "magnificent obsidian and brilliant electric-gold storm eagle with supreme lightning patterns, large blazing electric-white eyes with golden rings, ornate golden thunder-crown, supreme storm aura, golden lightning-feather edges",
        "devastating chain-lightning dive releasing multiple bolts from every feather, supreme thunder eagle god expression"
    ),
    "cyclone_moth": (
        "silver-white and pale-cyan massive moth with wings that generate powerful wind vortexes, a large intimidating moth form, large round bright cyan eyes with a calm powerful expression, enormous wings with wind-spiral patterns, body surrounded by constant air currents, antennae like wind-sensors",
        "wings flapping creating a devastating cyclone, body at the calm center, supreme wind controller expression",
        "magnificent pearl-white and silver-cyan moth with golden wind-spiral wing patterns, large blazing diamond-white eyes with cyan rings, ornate golden antennae-spirals, supreme cyclone aura, golden wing-edges",
        "devastating tornado attack with wings generating a massive cyclone, body directing the wind, supreme wind moth deity expression"
    ),
    "stellar_falcon": (
        "silver-white and starlight-gold feathers with tiny twinkling star-points along the wings, an elegant fast falcon form, large luminous golden-cyan eyes with a noble proud expression, wing-tips trailing star-sparkle trails, celestial light emanating from the plumage",
        "diving with starlight-trails streaming from wings, body blazing like a shooting star, supreme star warrior expression",
        "magnificent platinum and golden-star falcon with magnificent starlight wing-patterns, large blazing white-gold eyes with golden-star rings, ornate golden star-crown, supreme stellar aura, golden light-trails",
        "devastating star-dive attack blazing like a comet, leaving a golden starlight trail, supreme stellar falcon deity expression"
    ),
    "nether_raven": (
        "absolute pitch-black feathers with nether-realm purple energy wisps, a large sinister raven form, large glowing pale violet eyes with an ancient knowing expression, nether-fire wisps trailing from wing-tips and tail, an otherworldly death-realm presence, silent as the grave",
        "wings spread releasing nether-fire wave, body partially phasing into the underworld, terrifying nether lord expression",
        "magnificent obsidian and golden-nether raven with controlled underworld energy patterns, large blazing dark-violet eyes with golden-dark rings, ornate dark golden crown, supreme nether aura, golden feather-edges glowing against the absolute darkness",
        "devastating nether-blast with wings releasing concentrated underworld energy, supreme nether raven deity expression"
    ),
    "heart_phoenix": (
        "warm rose-pink and golden feathers with gentle heart-energy flame plumage, a small beautiful phoenix form radiating warmth and love, large luminous golden-pink eyes with a compassionate loving expression, heart-shaped tail feathers, warm aura that heals nearby beings, tiny golden bells on the wing-tips",
        "wings spread releasing waves of warm heart-energy, body glowing with love-fire, gentle healer warrior expression",
        "magnificent rose-gold and warm pink phoenix with supreme heart-fire plumage, large blazing golden-pink eyes with heart rings, ornate golden heart-crown, supreme love-fire aura, golden heart-pattern feathers",
        "devastating heart-fire burst with wings releasing waves of purifying love-flame, supreme heart phoenix deity expression"
    ),
    "divine_sparrow": (
        "brilliant golden-white and sacred-gold feathers radiating holy divine light, a transformed sparrow-to-divine-bird form of supreme beauty, large blazing white-gold eyes with absolute divine serenity, full-body golden sacred glow, every feather a ray of divine light, magnificent crest of pure golden light-rays",
        "body releasing concentrated divine light in all directions, holy presence overwhelming, supreme divine warrior expression",
        "magnificent supreme white-gold sparrow-phoenix with blazing sacred-geometry feather patterns, large blazing white-gold eyes with prismatic rings, ornate supreme golden divine-crown, absolute holy light aura",
        "devastating divine light-burst with entire body becoming a sun of holy energy, supreme divine sparrow god expression"
    ),
    "void_wasp_wing": (
        "obsidian-black and deep void-purple insectoid form with sharp angular wings, a menacing wasp-like creature of the void, large compound-style glowing red-violet eyes with a predatory calculating expression, sharp stinger tail, buzzing void-energy wings, thin segmented body of living darkness",
        "darting with impossible speed stinger-first releasing void-poison, wings buzzing with dark energy, terrifying void predator expression",
        "magnificent deep void-black and golden-dark wasp with controlled void-energy patterns, large blazing dark-violet compound eyes, ornate golden-dark crown, supreme void-sting aura, golden exoskeleton accents",
        "devastating void-sting barrage attacking from multiple angles simultaneously, supreme void wasp deity expression"
    ),
    "aurora_phoenix": (
        "magnificent seven-colored aurora feathers that shift and flow through all spectral colors, the ultimate phoenix form of breathtaking beauty, large luminous prismatic eyes with transcendent divine serenity, flowing seven-colored tail streamers, every feather a different aurora hue, absolute divine bird of light",
        "wings spread creating a full aurora display, body radiating all colors of light, supreme divine aurora expression",
        "magnificent supreme prismatic aurora phoenix with golden sacred-geometry patterns visible through all colors, large blazing prismatic eyes with golden rings, ornate supreme golden aurora-crown with seven gems, absolute divine light aura",
        "devastating aurora-nova with all seven colors exploding in a divine light-storm, supreme aurora phoenix god expression"
    ),
    "tempest_roc_king": (
        "massive dark storm-gray and electric-gold roc with sky-darkening wingspan, a colossal bird form wreathed in perpetual storm, large blazing electric-gold eyes with absolute commanding presence, thunder constantly rumbling from the wingbeats, storm-clouds forming around the body, rain and lightning following",
        "wings creating a full thunderstorm, body at the center of the tempest, absolute sky-lord expression",
        "magnificent obsidian-storm and supreme golden roc with controlled tempest aura, large blazing electric-white eyes with golden-storm rings, ornate golden tempest-crown, supreme storm-god aura, golden lightning-wing patterns",
        "devastating world-storm with wings generating a continental-scale tempest, supreme tempest roc god expression"
    ),
    "soul_crane": (
        "ethereal white-gold and soft rose plumage with soul-light emanating from within, a tall divine crane form that seems partially translucent showing inner light, large luminous golden-pink eyes with absolute serenity and wisdom, flowing soul-ribbons from wings, heart-light halo, guides spirits with gentle presence",
        "wings spread releasing soul-guiding light, body becoming a beacon for spirits, supreme soul guardian expression",
        "magnificent supreme white-gold and rose-light crane with blazing sacred soul-patterns, large blazing golden-pink eyes with heart-light rings, ornate golden soul-crown, supreme soul-light aura, golden ribbon-feathers",
        "devastating soul-light purification with entire body radiating supreme heart-and-holy energy, supreme soul crane deity expression"
    ),

    # ═══════════════════════════════════════════════════
    # 合成宠 — 水族合成 (39-53)
    # ═══════════════════════════════════════════════════
    "armored_fish_turtle": (
        "teal-blue and stone-brown hybrid creature with fish body and turtle-shell armor on top, a unique fusion form, large round bright blue-amber eyes with a sturdy calm expression, fish tail and fins with rocky shell plates, small turtle-like legs underneath, an aquatic tank presence",
        "shell raised as shield while tail whips sideways, body braced for impact, steady aquatic defender expression",
        "magnificent sapphire and golden-stone armored fish-turtle with golden shell-plates and glowing scale patterns, large blazing dual-toned eyes with golden rings, ornate golden shell-crown, supreme aquatic fortress form",
        "devastating shell-charge through water with tail propulsion and shell as battering ram, supreme aquatic tank expression"
    ),
    "venom_flame_shrimp": (
        "dark crimson and toxic purple shrimp with venomous flame-dripping pincers, a dangerous small crustacean form, large round glowing red-violet eyes with a vicious aggressive expression, pincers oozing dark flaming venom, segmented body with poison-fire markings, toxic fumes rising",
        "pincers snapping and spraying venom-fire in an arc, body arched aggressively, fierce toxic warrior expression",
        "magnificent deep crimson and dark-violet shrimp with golden-venom flame patterns, large blazing red-violet eyes with golden-dark rings, ornate golden pincer-caps, supreme toxic-fire aura, golden segmented armor",
        "devastating venom-fire spray attack from both pincers simultaneously, supreme toxic flame warrior expression"
    ),
    "voltaic_jellyfish": (
        "translucent blue and electric-yellow jellyfish with crackling electric tentacles, a large bell-shaped form, large round bright electric-blue eyes visible through the bell with an intense expression, tentacles constantly discharging electricity, internal electric organ visible, shocking on contact",
        "bell pulsing with massive electrical discharge, tentacles creating a web of lightning, fierce electric warrior expression",
        "magnificent crystal-blue and golden-electric jellyfish with controlled lightning patterns, large blazing electric-blue eyes with golden rings, ornate golden bell-crown, supreme electric-ocean aura, golden tentacle-tips",
        "devastating electric-pulse with bell releasing a massive lightning shockwave through water, supreme voltaic deity expression"
    ),
    "flora_coral_crab": (
        "pink-green and floral-coral armored crab with blooming flowers and living coral formations all over the shell, a beautiful garden-crab form, large round bright green-pink eyes with a cheerful protective expression, flower-covered shell creating a miniature reef-garden, claws decorated with sea-flowers",
        "shell-garden releasing a burst of pollen and coral-spore projectiles, claws raised defensively, fierce garden guardian expression",
        "magnificent jade-pink and golden-coral crab with magnificent blooming reef-garden shell, large blazing emerald-pink eyes with golden rings, ornate golden coral-crown, supreme reef-garden aura, golden claw-caps with flower details",
        "devastating coral-bloom attack with shell-garden exploding with nature-water energy, supreme reef deity expression"
    ),
    "deep_lantern_dragon": (
        "dark deep-blue and bioluminescent orange-gold fish-dragon hybrid with a glowing lantern-lure and serpentine body, a deep-sea dragon form, large round glowing amber-blue eyes with an ancient mysterious expression, dragon whiskers and fish fins combined, lantern-lure blazing, elongated body with luminous spots",
        "lantern releasing a concentrated light-blast while body lunges from the deep, fierce deep-sea dragon expression",
        "magnificent obsidian-blue and golden-luminescent deep-sea dragon with magnificent glowing pattern-constellations, large blazing golden-blue eyes with golden rings, ornate golden lantern with ruby, supreme deep-sea dragon lord form",
        "devastating deep-light blast from lantern with body spiraling attack, supreme deep-sea dragon deity expression"
    ),
    "tide_shark": (
        "rich teal-blue and silver sleek shark with tidal-wave energy flowing along the body, a powerful shark form, large fierce sapphire-blue eyes with a predatory intense expression, streamlined body built for speed and power, dorsal fin cutting water like a blade, powerful tail generating currents",
        "body surging forward creating a tidal-wave behind, jaws open showing rows of teeth, fierce ocean predator expression",
        "magnificent deep sapphire and golden-silver shark with tidal-current patterns, large blazing sapphire eyes with golden rings, ornate golden dorsal-fin crown, supreme tidal warrior aura, golden tooth-edges",
        "devastating tidal-rush attack creating a massive wave while striking, supreme tidal shark deity expression"
    ),
    "thunder_shell_king": (
        "dark iron-green and electric-yellow armored turtle with a shell that functions as a lightning capacitor, a massive battle-turtle form, large fierce electric-amber eyes with a stern commanding expression, shell covered in electric circuit-patterns, lightning arcing between shell-plates, thunder-powered presence",
        "shell discharging stored lightning in a massive burst, body braced and immovable, supreme thunder-fortress expression",
        "magnificent obsidian-green and golden-electric turtle with controlled lightning-capacitor shell, large blazing electric-gold eyes with golden rings, ornate golden shell-crown, supreme thunder-fortress aura, golden circuit-plate patterns",
        "devastating thunder-shell blast releasing all stored lightning in a single massive discharge, supreme thunder turtle deity expression"
    ),
    "windsurf_seahorse": (
        "pearl-white and cyan-teal seahorse riding on wind-water hybrid energy, an agile seahorse form surfing invisible waves, large round bright cyan-blue eyes with a joyful adventurous expression, flowing mane of wind-water energy, tail gripping wind-currents, speed-lines suggesting constant motion",
        "surfing a wind-wave at high speed and attacking with a tail-whip, exhilarating wind-surf warrior expression",
        "magnificent pearl and golden-cyan seahorse with wind-wave riding trails, large blazing diamond-cyan eyes with golden rings, ornate golden wave-crown, supreme wind-water surf aura, golden mane-streams",
        "devastating wind-wave charge surfing a massive combined wind-water wave, supreme wind-surf deity expression"
    ),
    "starlight_octopus": (
        "translucent blue-black and starlight-dotted octopus with tentacles tipped in tiny star-lights, a wise intelligent octopus form, large luminous golden-blue eyes with an incredibly intelligent expression, body like a miniature night sky, each tentacle grasping a different tiny glowing star, a cosmic ocean presence",
        "tentacles directing concentrated starlight beams while body coordinates multiple attacks, supreme tactical genius expression",
        "magnificent cosmic-blue and golden-star octopus with constellation-pattern body, large blazing golden-blue eyes with star rings, ornate golden cosmic-crown, supreme stellar-ocean aura, golden star-tipped tentacles",
        "devastating octo-starlight attack with all tentacles releasing concentrated star-beams simultaneously, supreme cosmic ocean deity expression"
    ),
    "heart_dolphin": (
        "warm rose-pink and pearl-white dolphin with heart-pattern markings and a warm healing aura, a gentle graceful dolphin form, large luminous golden-pink eyes with a joyful compassionate expression, heart-shaped markings on the fins, warm glow emanating from the body, a presence that soothes emotions",
        "body releasing waves of heart-energy while performing a healing leap, gentle but powerful healer expression",
        "magnificent rose-gold and warm pearl dolphin with blazing heart-patterns, large blazing golden-pink eyes with heart rings, ornate golden heart-crown, supreme heart-healing aura, golden fin-edges",
        "devastating heart-wave leap releasing a massive pulse of healing-and-purifying energy, supreme heart dolphin deity expression"
    ),
    "crystal_clam_king": (
        "massive ice-blue and crystal shell encrusted with gems and ice-crystal formations, a grand royal clam form, large round blazing pale-blue eyes with a regal cold expression inside, magnificent gem-encrusted shell interior, a crown of crystals, ice-cold aura, a treasury-like presence",
        "shell opening to blast enemies with ice-crystal barrage then snapping shut, supreme ice fortress expression",
        "magnificent crystal-ice and golden clam with magnificent gem-studded golden-trim shell, large blazing sapphire eyes with golden-ice rings, ornate golden shell-crown, supreme ice-crystal treasury aura, magnificent pearl within",
        "devastating ice-gem barrage with shell opening to release concentrated crystal-ice projectiles, supreme ice clam deity expression"
    ),
    "azure_divine_fish": (
        "brilliant azure-blue and sacred-gold fish of divine aquatic beauty, a supreme fish form radiating ocean mastery, large luminous sapphire-gold eyes with a serene commanding expression, every scale shimmering with ocean power, flowing divine fins, a golden aura of ocean authority, a sovereign of all waters presence",
        "body commanding the ocean currents to form a devastating water assault, supreme ocean lord expression",
        "magnificent supreme azure and golden divine fish with sacred ocean-geometry scale patterns, large blazing sapphire-gold eyes with golden rings, ornate golden water-crown, supreme divine ocean aura, golden sacred fins",
        "devastating divine-ocean attack commanding all water to serve, supreme ocean deity expression"
    ),
    "abyss_sea_emperor": (
        "obsidian-black and deep violet massive deep-sea creature combining squid and eel features, a terrifying abyssal emperor form, large glowing pale-violet eyes with absolute dark commanding expression, shadow-tentacles and serpentine body, deep-sea darkness clinging to the form, crushing pressure aura",
        "shadow-tentacles grabbing while serpent-body strikes, abyssal darkness expanding, terrifying deep emperor expression",
        "magnificent obsidian and golden-dark abyssal emperor with controlled shadow-ocean patterns, large blazing dark-violet eyes with golden-dark rings, ornate dark golden crown, supreme abyssal aura, golden accent details against absolute darkness",
        "devastating abyss-crush attack with shadow and water pressure combining to overwhelm, supreme abyss emperor deity expression"
    ),
    "stellar_whale_god": (
        "magnificent cosmic-blue and starlight body containing visible star-clusters within, a divine whale form of cosmic proportions, large luminous golden-blue eyes with stars visible in the depths, body like a living galaxy swimming through cosmic ocean, star-song emanating from the blowhole, absolute stellar majesty",
        "body releasing stellar energy through the blowhole in a cosmic water-spout, stars brightening within, supreme cosmic whale expression",
        "magnificent supreme cosmic-blue and golden-star whale with blazing constellation patterns, large blazing golden-cosmic eyes with star rings, ornate golden cosmic-crown, supreme stellar-ocean aura, golden star-patterns along the body",
        "devastating stellar-spout releasing concentrated cosmic-ocean energy, stars within going supernova, supreme stellar whale god expression"
    ),
    "sovereign_dragonfish": (
        "supreme golden and all-water-blue dragon-fish with scales containing all types of water — ocean river rain mist ice, a divine aquatic dragon form, large luminous golden-blue eyes with absolute water-mastery depth, flowing all-water fins, every scale a different shade of water-blue, supreme aquatic dragon-fish majesty",
        "body commanding all forms of water simultaneously in a devastating multi-water assault, absolute water sovereign expression",
        "magnificent supreme golden and prismatic-blue dragon-fish with sacred water-geometry patterns, large blazing golden-blue eyes with prismatic-water rings, ornate golden supreme water-crown, absolute water deity aura, golden scale-borders",
        "devastating all-water-command releasing every form of water as weapon simultaneously, supreme sovereign dragon-fish deity expression"
    ),

    # ═══════════════════════════════════════════════════
    # 合成宠 — 植灵族合成 (54-68)
    # ═══════════════════════════════════════════════════
    "mushroom_vine": (
        "a symbiotic creature of mushroom cap and vine tendrils intertwined, green vines with a colorful mushroom growing from the body, large round bright green-brown eyes with a content symbiotic expression, vines for arms with tiny mushrooms growing at the joints, a walking ecosystem",
        "vines whipping while mushroom-cap releases spore clouds, combined assault, fierce symbiotic warrior expression",
        "magnificent jade-green and golden-brown mushroom-vine with magnificent blooming symbiosis, large blazing emerald-brown eyes with golden rings, ornate golden spore-crown, supreme nature symbiosis aura",
        "devastating spore-vine attack with combined mushroom-spore and vine-lash assault, supreme symbiotic deity expression"
    ),
    "bloom_cactus": (
        "round green cactus body completely covered in magnificent blooming flowers of all colors, a spectacular flowering cactus form, large round bright amber-green eyes with a proud happy expression, dozens of vibrant flowers covering every surface between the spines, flower-petals constantly drifting off",
        "flowers launching pollen-blasts while spines extend as a barrier, fierce blooming fortress expression",
        "magnificent golden-green and flower-covered cactus with supreme blooming golden flowers, large blazing emerald-amber eyes with golden rings, ornate golden thorn-crown with flower-gems, supreme desert-bloom aura",
        "devastating bloom-burst with all flowers exploding simultaneously releasing nature-earth energy, supreme bloom cactus deity expression"
    ),
    "blaze_maple": (
        "a maple-tree squirrel-spirit beast with permanently burning crimson-orange leaf-fur that never consumes, a small agile squirrel-form with a magnificent fiery maple-leaf tail, large round bright amber-red eyes with a passionate artistic expression, four nimble legs with bark-textured paws, leaves of living fire floating around the body, warm glow from the tail, a beautiful fire-art beast presence",
        "tail-leaves swirling into a fire-vortex while body leaps on all fours directing the flame-art, fierce fire artist beast expression",
        "magnificent deep crimson and golden-fire maple squirrel-beast with supreme flame-leaf patterns on the fur, large blazing golden-flame eyes with vermilion rings, ornate golden fire-leaf crown on the head, supreme fire-nature beast aura, golden bark-paws and magnificent blazing tail",
        "devastating fire-leaf storm creating a tornado of burning golden leaves launched from the tail, supreme fire maple beast deity expression"
    ),
    "gale_dandelion": (
        "pure white and wind-silver dandelion spirit with seeds that fill the sky perpetually, an ethereal wind-fairy form, large round bright cyan-white eyes with a dreamy free expression, body dissolving into floating seeds at the edges, wind-carried presence, fills the air with floating seed-stars",
        "releasing a massive seed-storm that fills the battlefield, seeds cutting like tiny wind-blades, fierce wind-scatter expression",
        "magnificent silver-white and golden-wind dandelion with supreme glowing star-seeds, large blazing diamond-white eyes with cyan rings, ornate golden seed-crown, supreme wind-scatter aura, golden floating seeds everywhere",
        "devastating seed-wind storm filling the entire area with cutting golden seed-projectiles, supreme wind dandelion deity expression"
    ),
    "fire_crystal_lotus": (
        "brilliant ruby-red crystal-lotus blooming from volcanic rock, a magnificent fire-and-earth hybrid flower, large blazing amber-red eyes at the center with an intense expression, crystal petals with trapped fire inside, molten rock base, heat waves visible, a volcanic flower masterpiece",
        "crystal petals focusing fire into devastating beams, volcanic base erupting, supreme fire-earth warrior expression",
        "magnificent supreme ruby and golden-fire crystal lotus with blazing prismatic fire-petals, large blazing white-gold eyes with ruby rings, ornate golden volcanic-crystal base, supreme fire-earth aura, golden crystal-petal edges",
        "devastating magma-crystal beam with all petals focusing supreme fire through crystal, supreme fire-crystal lotus deity expression"
    ),
    "heart_tree": (
        "ancient gnarled tree body with a warm golden glow emanating from a heart-shaped hollow in the trunk, a wise ancient tree form radiating empathy, large luminous golden-pink eyes in the bark with an all-knowing compassionate expression, heart-shaped leaves, golden sap, roots sensing all emotions in the earth",
        "roots extending to touch and heal while golden heart-light radiates outward, supreme empathic healer expression",
        "magnificent supreme ancient tree with blazing golden heart-core and sacred golden-bark patterns, large blazing golden-pink eyes with heart rings, ornate golden heart-hollow crown, supreme empathic-earth aura, golden roots and leaves",
        "devastating heart-root-wave with roots and heart-energy combining in a massive healing-and-protecting burst, supreme heart tree deity expression"
    ),
    "light_bloom": (
        "a flower spirit that blooms with pure holy white-gold light, an elegant sacred flower form, large luminous white-gold eyes with a serene divine expression, petals radiating gentle holy light, illuminating darkness around it, a beacon of hope presence",
        "petals opening fully to release concentrated divine light, body blazing with holy energy, supreme light-nature warrior expression",
        "magnificent supreme golden-white light bloom with sacred-geometry petal patterns, large blazing white-gold eyes with golden rings, ornate golden divine stamen-crown, supreme holy-nature aura, golden light-petal edges",
        "devastating holy-bloom light-burst with petals releasing supreme divine nature energy, supreme light bloom deity expression"
    ),
    "purgatory_lotus": (
        "a lotus that burns with supreme concentrated fire that never goes out, deep crimson and white-hot petals, large blazing white-hot eyes with absolute fierce expression, perpetual flames, the ultimate fire-flower, heat distortion around every petal, an inextinguishable presence",
        "all petals releasing white-hot fire simultaneously, body at the center of an inferno, supreme purgatory expression",
        "magnificent supreme crimson and golden-fire purgatory lotus with controlled white-hot petals, large blazing white-gold eyes with ruby rings, ornate golden fire-crown, supreme purgatory fire aura, golden petal-veins",
        "devastating purgatory-fire eruption with all petals releasing supreme concentrated fire, supreme purgatory lotus deity expression"
    ),
    "thunder_sprout": (
        "bright green bamboo-shoot form crackling with absorbed lightning, a young energetic sprout-spirit charged with electricity, large round bright electric-green eyes with an eager charged expression, electric sparks running along the young bamboo segments, growing rapidly with each lightning charge absorbed",
        "body channeling a lightning strike from above through the tip, electricity flowing through the segments, fierce thunder-growth expression",
        "magnificent golden-green and electric-gold bamboo sprout with supreme lightning patterns, large blazing electric-green eyes with golden rings, ornate golden lightning-tip crown, supreme thunder-growth aura, golden segment-rings",
        "devastating thunder-growth strike channeling massive lightning while rapidly growing, supreme thunder sprout deity expression"
    ),
    "shadow_orchid": (
        "dark purple and black orchid that blooms only in shadow with ghostly bioluminescent edges, a sinister beautiful flower form, large glowing pale violet eyes with a mysterious dark allure, petals that seem to absorb light, shadow-mist emanating, a hauntingly beautiful dark presence",
        "petals releasing waves of shadow-pollen that drains energy, body pulsing with dark beauty, terrifying dark enchantress expression",
        "magnificent deep violet and golden-dark orchid with controlled shadow patterns and golden petal-edges, large blazing dark-violet eyes with golden-dark rings, ornate golden shadow-stamen crown, supreme shadow-nature aura",
        "devastating shadow-drain with petals releasing concentrated darkness that absorbs all light and energy, supreme shadow orchid deity expression"
    ),
    "stone_king_mushroom": (
        "massive petrified mushroom with a fossilized stone cap and crystal growths, an ancient stone-mushroom colossus, large deep amber eyes in the stone with an ancient eternal expression, cap of solid stone with amber crystal veins, pillar-like stone stalk, geological age visible in the layers",
        "stone cap slamming down like a hammer creating seismic waves, body unshakable, supreme earth colossus expression",
        "magnificent dark granite and golden-crystal stone mushroom king with supreme amber crystal growths, large blazing topaz eyes with amber rings, ornate golden stone-crown with amber gems, supreme petrified-earth aura, golden crystal veins throughout",
        "devastating earth-shatter slam with massive stone cap crashing down releasing golden seismic energy, supreme stone mushroom deity expression"
    ),
    "ancient_tree_god": (
        "massive ancient tree body of incredible girth and age with wisdom etched in every ring of bark, a supreme tree-god form, large luminous amber-green eyes in the bark with infinite patience and wisdom, canopy of a thousand leaves, root-system vast, ecosystem of tiny creatures living within, absolute ancient nature majesty",
        "roots erupting everywhere while canopy rains nature-energy, body commanding all plant life, supreme forest god expression",
        "magnificent supreme ancient tree with golden sap-veins and sacred bark-patterns, large blazing emerald-gold eyes with golden rings, ornate golden bark-crown, supreme ancient forest god aura, golden leaves and roots",
        "devastating root-and-canopy assault commanding all nature to attack and defend simultaneously, supreme ancient tree deity expression"
    ),
    "heart_flower_god": (
        "magnificent multi-colored healing flower deity radiating love-energy, a supreme divine flower form of all colors, large luminous golden-pink eyes with absolute compassion, every petal a different healing color, golden heart-core blazing with love, a presence that heals all wounds physical and emotional",
        "body releasing supreme healing-love waves that restore and purify, absolute heart-healer expression",
        "magnificent supreme prismatic flower god with sacred heart-geometry patterns, large blazing golden-pink eyes with prismatic-heart rings, ornate golden heart-flower crown, supreme divine healing aura, golden petals each a different healing color",
        "devastating heart-bloom healing-burst purifying everything with supreme love-and-nature energy, supreme heart flower deity expression"
    ),
    "divine_purgatory_lotus": (
        "supreme nirvana-rebirth lotus combining holy fire and sacred renewal, white-gold and phoenix-fire petals, a transcendent lotus form of rebirth, large blazing white-gold eyes with absolute renewal expression, flames of purification that create rather than destroy, phoenix-fire petals constantly dying and being reborn",
        "petals cycling through death and rebirth while releasing purifying fire, supreme rebirth expression",
        "magnificent supreme white-gold and phoenix-fire nirvana lotus with sacred rebirth-geometry patterns, large blazing white-gold eyes with golden-fire rings, ornate golden nirvana-crown, supreme purification-rebirth aura, golden phoenix-fire petal edges",
        "devastating nirvana-fire purification with entire lotus going through death-rebirth cycle releasing supreme creation-fire, supreme nirvana lotus deity expression"
    ),
    "world_tree_spirit": (
        "supreme colossal tree connecting heaven and earth with roots in the underworld and branches touching the stars, the ultimate tree form containing all elements, large luminous prismatic eyes with absolute cosmic-nature wisdom, every branch a different element, cosmic-nature presence of absolute magnitude, the axis of the world",
        "all elements flowing through roots to branches in a devastating all-element nature assault, absolute world tree expression",
        "magnificent supreme prismatic world tree with sacred golden axis and all-element branches, large blazing prismatic-gold eyes with cosmic rings, ornate golden cosmic-nature crown, supreme world-axis aura, golden bark with all-element veins",
        "devastating all-element nature assault channeling every force of nature simultaneously through the world axis, supreme world tree deity expression"
    ),

    # ═══════════════════════════════════════════════════
    # 合成宠 — 元素族合成 (69-83)
    # ═══════════════════════════════════════════════════
    "steam_spirit": (
        "a badger-lizard hybrid beast of living steam where fire and water energy coexist, warm red and cool blue swirling vapor body with four stocky legs, large round bright amber-blue eyes with an intense unstable expression, steam-vent ridges along the spine, constant steam venting from the back plates, temperature-shimmer visible",
        "body releasing superheated steam blasts from spine-vents while charging on four legs, water and fire energy clashing within, fierce steam beast warrior expression",
        "magnificent golden-steam badger-lizard beast with controlled fire-water balance and golden vapor patterns, large blazing amber-blue eyes with golden rings, ornate golden steam-vent crown-ridge, supreme thermal beast aura, golden vapor trails from armored plates",
        "devastating steam-explosion with superheated blast releasing both fire and water energy from all vents, supreme steam beast deity expression"
    ),
    "flame_grass_spirit": (
        "a paradoxical fox-deer hybrid beast of fire and living plants coexisting, burning flowers growing from antlers and tail, warm red-green furred body with four agile legs, large round bright amber-green eyes with a paradoxical peaceful-intense expression, plants growing through fire on the antlers without burning, fire feeding the tail-flowers, an impossible harmony beast",
        "charging with antlers ablaze with plant-fire while tail scatters burning seed-projectiles, fierce paradox beast warrior expression",
        "magnificent golden fire-flora fox-deer beast with controlled paradox harmony patterns on the fur, large blazing amber-green eyes with golden rings, ornate golden paradox-antler crown, supreme fire-nature beast aura, golden flame-flowers blooming on shoulders",
        "devastating paradox-burst with antler-fire and tail-seeds simultaneously attacking in perfect impossible harmony, supreme fire-flora beast deity expression"
    ),
    "storm_spirit": (
        "a wolf-eagle hybrid beast of combined thunder and wind energy, electric-yellow and pale-cyan swirling body with four powerful legs and broad wind-wings, large blazing electric-cyan eyes with a fierce unstoppable expression, lightning arcing through wind-feathered mane, miniature storm-clouds forming around the paws and wing-tips, thunder-rumble constant",
        "body leaping with wings spread generating a localized thunderstorm, four legs directing lightning and wind strikes, supreme storm beast warrior expression",
        "magnificent golden storm wolf-eagle beast with controlled tempest patterns, large blazing electric-white eyes with golden-cyan rings, ornate golden storm-crown between feathered ears, supreme tempest beast aura, golden lightning-wind trail from wings and tail",
        "devastating full storm-strike with combined wind-and-lightning assault from wings and claws, supreme storm beast deity expression"
    ),
    "quake_thunder_spirit": (
        "a rhinoceros-shaped beast combining seismic earth and electrical energy, amber-brown and electric-yellow armored body with four massive pillar-legs, large blazing amber-electric eyes with an overwhelming expression, body cracking the ground with each step while lightning arcs from the horn upward, combined quake-and-thunder rhino presence",
        "body stomping with massive legs to create earthquakes while horn attracts lightning strikes, supreme quake-thunder beast warrior expression",
        "magnificent golden earth-thunder rhino beast with controlled seismic-electric armor patterns, large blazing topaz-electric eyes with golden rings, ornate golden quake-horn crown, supreme seismic-lightning beast aura, golden armor-crack patterns",
        "devastating quake-thunder attack with ground-shattering stomp releasing upward lightning from horn, supreme quake-thunder beast deity expression"
    ),
    "aqua_flora_spirit": (
        "a turtle-deer hybrid beast of living water and plants in symbiotic harmony, teal-blue and emerald-green body with a shell of woven aquatic plants, large bright blue-green eyes with a nurturing wise expression, water flowing through vine-channels in the shell, aquatic plants growing from antlers, four webbed hooves, a living water-garden beast",
        "antlers releasing water-empowered plant-growth beams while shell sprays plant-filtered water attacks, supreme aqua-flora beast warrior expression",
        "magnificent golden aqua-flora turtle-deer beast with sacred water-plant symbiosis patterns on the shell, large blazing teal-green eyes with golden rings, ornate golden aqua-flora antler-crown, supreme water-garden beast aura, golden shell-vine details",
        "devastating aqua-flora assault with water and plant energy combining from antlers and shell, supreme aqua-flora beast deity expression"
    ),
    "sandwind_spirit": (
        "a desert scorpion-lizard hybrid beast of wind and earth combined, sandy-amber and pale-cyan armored body with four clawed legs and a scorpion-like tail, large round amber-cyan eyes with a weathered harsh expression, sand particles carried by wind-currents forming a storm-cloak around the body, a desert-storm predator incarnate",
        "body disintegrating into a localized sandstorm while tail whips sand-blades, then reforming to strike, supreme desert beast warrior expression",
        "magnificent golden sandwind scorpion-lizard beast with controlled desert-storm armor patterns, large blazing topaz-cyan eyes with golden rings, ornate golden desert-crown on the head, supreme sandstorm beast aura, golden tail-blade and claw-caps",
        "devastating sandstorm assault with body becoming a massive sand-cyclone centered on the beast, supreme sandwind beast deity expression"
    ),
    "chaos_elemental": (
        "supreme yin-yang chimeric beast of perfect light-and-shadow balance with a body that is half brilliant white-gold lion and half deep violet-black wolf, a refined chaos beast with four powerful legs, large dual-colored blazing eyes with an enlightened expression, golden border energy where the two halves meet at the spine, mane half light half dark, tail half light half dark",
        "both halves of the body releasing simultaneous opposing energy beams from the mouth, supreme chaos beast warrior expression",
        "magnificent supreme white-gold and violet-black yin-yang chimeric beast with sacred balance patterns and golden borders down the spine, large blazing dual-colored eyes with golden rings, ornate golden chaos-crown with light-dark gems between opposing horns, supreme perfect-chaos beast aura, golden claws on all four legs",
        "devastating chaos-collision with light and dark beast-halves merging energy in a supreme paradox explosion, supreme chaos elemental beast deity expression"
    ),
    "gale_rock_elemental": (
        "a golem-tortoise beast of stone and wind combined with floating rock-fragments held together by wind-currents around a core body, stone-brown and pale-cyan body with four thick legs, large round amber-cyan eyes with a powerful expression, rocks orbiting in wind-patterns above the shell, a sandstone-storm golem-beast presence",
        "launching wind-propelled rock-projectiles from orbiting stones while charging on four legs, supreme rock-wind beast warrior expression",
        "magnificent golden-stone and wind-silver golem-tortoise beast with controlled geo-wind patterns, large blazing topaz-cyan eyes with golden rings, ornate golden geo-wind crown on the shell, supreme rock-storm beast aura, golden stone-plate armor on legs",
        "devastating geo-wind assault launching golden rocks at hurricane speed from orbiting formations, supreme gale-rock beast deity expression"
    ),
    "blaze_flora_elemental": (
        "a boar-stag hybrid beast of fire and plants in a burning garden form, vermilion and emerald furred body with four strong legs, burning flowers as antlers and mane-crest, large blazing amber-green eyes with a fierce paradoxical expression, fire nourishing the plants while plants fuel the fire on the body, a perpetual burning garden beast incarnate",
        "charging with four legs while antlers of burning flowers release fire-empowered seed projectiles, supreme fire-garden beast warrior expression",
        "magnificent golden fire-flora boar-stag beast with sacred burning-garden patterns on the fur, large blazing golden-green eyes with golden rings, ornate golden fire-garden antler-crown, supreme blaze-flora beast aura, golden hooves and tusk-details",
        "devastating burning-garden eruption with antler-fire and body-plants exploding in supreme paradox harmony, supreme blaze-flora beast deity expression"
    ),
    "mud_elemental": (
        "a hippo-crab hybrid beast of thick living mud combining water and earth, brown-teal slurping body with four squat powerful legs, large round amber-blue eyes with a calm overwhelming expression, shell-like mud-armor plates on the back, body constantly shifting and reforming, mud tendrils extending from the shell, a mire-beast incarnate presence",
        "body surging forward engulfing enemies in waves of thick mud from the shell, reforming instantly, supreme mud beast warrior expression",
        "magnificent golden-brown and teal mud hippo-crab beast with controlled earth-water armor patterns, large blazing amber-teal eyes with golden rings, ornate golden mire-crown on the shell, supreme mud-swamp beast aura, golden shell-plate accents",
        "devastating mud-engulf with body expanding into a massive mud-wave, supreme mud beast deity expression"
    ),
    "light_heart_spirit": (
        "supreme phoenix-qilin hybrid beast of holy light and heart energy merged, warm white-gold and rose-pink feathered-scaled body with four graceful clawed legs, large luminous golden-pink eyes with absolute divine compassion, holy light infused with love-energy creating a warm sacred glow, phoenix-feathered wings and qilin antler-horn, heartbeat visible as a pulse of golden-pink light in the chest",
        "body radiating supreme holy-heart energy from the chest-pulse while charging with four legs, wings spread releasing healing light, absolute divine healer beast expression",
        "magnificent supreme golden-rose light-heart phoenix-qilin beast with sacred geometry patterns on feathered scales, large blazing golden-pink eyes with divine rings, ornate golden light-heart crown between antler-horns, supreme divine-compassion beast aura, golden feathered wings with rose-light edges",
        "devastating holy-heart nova with wings and antler-horn releasing supreme divine love-and-light energy, supreme light-heart beast deity expression"
    ),
    "shadow_heart_spirit": (
        "a wolf-phoenix hybrid beast where shadow and heart energy are unified, deep violet and rose-pink feathered-furred body with four powerful legs, large luminous violet-pink eyes with a mysterious empathic expression, shadow-mist feathered mane infused with emotional warmth creating a comforting darkness, dark wings with rose-heart markings, heart-pulse visible in the shadow-chest",
        "body releasing shadow-heart waves from the chest-pulse while prowling on four legs, dark wings flaring with empathic energy, mysterious empathic beast warrior expression",
        "magnificent deep violet and golden-rose shadow-heart wolf-phoenix beast with sacred dark-heart patterns on the fur, large blazing violet-pink eyes with golden-dark rings, ornate golden dark-heart crown between feathered ears, supreme shadow-compassion beast aura, golden-dark wing edges",
        "devastating shadow-heart wave releasing empathic darkness from wings and chest, supreme shadow-heart beast deity expression"
    ),
    "origin_spirit": (
        "a transcendent dragon-turtle fusion beast tracing back to the origin of all elements, prismatic and golden armored shell containing the source-code of reality, large luminous prismatic eyes with absolute cosmic understanding, four massive clawed legs, the shell displays the fundamental building blocks of all elements as glowing rune-like scale patterns, long dragon tail, a primordial essence beast presence",
        "body channeling the origin-energy of all elements through the shell simultaneously while bracing on all fours, shell blazing with source-patterns, absolute primordial beast warrior expression",
        "magnificent supreme prismatic-golden dragon-turtle origin beast with sacred source-geometry shell patterns, large blazing prismatic eyes with golden cosmic rings, ornate golden origin-crown on the head, supreme primordial beast aura, golden shell-plates each displaying a different element",
        "devastating origin-burst releasing the fundamental energy of all elements from the shell, supreme origin beast deity expression"
    ),
    "soul_spirit": (
        "a celestial deer-bird hybrid beast of pure concentrated heart-soul energy, warm rose-gold feathered-furred body with four slender legs and small wings, large luminous golden-pink eyes with absolute emotional depth, body pulsing with pure emotional energy through the antler-branches, the most concentrated form of heart energy in beast form, a presence that touches the soul directly",
        "body releasing supreme concentrated soul-energy waves from glowing antlers while leaping gracefully, wings fluttering with emotional power, absolute empathic beast warrior expression",
        "magnificent supreme rose-gold and golden-pink soul deer-bird beast with sacred heart-soul geometry antler patterns, large blazing golden-pink eyes with supreme heart rings, ornate golden soul-crown between antlers, supreme pure-soul beast aura, golden feathered wings trailing soul-light",
        "devastating soul-burst releasing the purest possible heart-energy from antlers and wings in a supreme emotional shockwave, supreme soul beast deity expression"
    ),
    "genesis_spirit": (
        "supreme serpent-phoenix fusion beast containing the power of creation itself, prismatic-golden feathered-scaled body with four powerful clawed legs and vast rainbow wings, large luminous white-gold eyes with absolute creative power, body showing all elements being born from the golden core in the chest, a serpentine neck with phoenix plumage, all elements visible flowing across the scales, absolute genesis beast presence",
        "body unleashing the power of creation from open jaws and wings, all elements emerging from the chest-core, four legs bracing against the creative force, absolute genesis beast expression",
        "magnificent supreme white-gold and prismatic genesis serpent-phoenix beast with sacred creation-geometry wing patterns, large blazing white-gold eyes with supreme cosmic rings, ornate golden genesis-crown between phoenix-horns, supreme creation beast aura, golden feather-scales shifting through all element colors",
        "devastating genesis-burst recreating reality with supreme creative power erupting from jaws and wings, all elements born anew, supreme genesis beast deity expression"
    ),

    # ═══════════════════════════════════════════════════
    # 合成宠 — 幻灵族合成 (84-95)
    # ═══════════════════════════════════════════════════
    "dream_fire_beast": (
        "a ghostly tapir-fox hybrid beast of dream-fire, combining a tapir's snout with a fox's bushy tail, translucent rose-pink and warm orange-amber furred body with four agile legs, large dreamy blazing amber-pink eyes with a surreal fierce expression, fox-ears and tapir-snout, flames that dance like dreams on the three tails, body shifting between waking and sleeping states, dream-smoke trailing from the fur",
        "dream-fire erupting from fox-tails while tapir-snout inhales enemy energy, body flickering between reality and dream on all four legs, fierce dream-fire beast warrior expression",
        "magnificent golden-pink and ethereal flame tapir-fox beast with controlled dream-fire patterns on the fur, large blazing golden-amber eyes with dream rings, ornate golden dream-fire crown between fox-ears, supreme dream-flame beast aura, golden ghostly-fire on all three tails",
        "devastating dream-fire blast from tails releasing surreal flames while snout creates dream-vortex, supreme dream-fire beast deity expression"
    ),
    "galaxy_dolphin": (
        "a dolphin-dragonfish hybrid made of galaxy-light swimming through star-fields, cosmic blue-purple and starlight-gold body with dolphin form but long dragon-fish barbel whiskers and flowing dorsal fin, large luminous golden-cosmic eyes with a joyful cosmic expression, body containing visible stars and nebulae, dragon-fish scales shimmering on the belly, starlight trail behind the flowing tail",
        "performing a cosmic leap releasing starlight and water-energy combined, barbel whiskers channeling stellar power, supreme cosmic-aquatic warrior expression",
        "magnificent golden-cosmic dolphin-dragonfish with blazing constellation patterns and golden whiskers, large blazing golden-cosmic eyes with star rings, ornate golden cosmic-crown between dragon-fish horns, supreme stellar-ocean beast aura, golden star-fin patterns and luminous barbels",
        "devastating cosmic-leap attack releasing concentrated stellar-ocean energy from open mouth and whiskers, supreme galaxy dolphin deity expression"
    ),
    "nether_water_lantern": (
        "a floating ghost-lantern drifting in dark waters, deep violet-blue and ghostly green-glow, large round eerie pale green-violet eyes with a haunting mysterious expression, lantern body of dark water containing nether-light, dripping shadow-water, bobbing gently in unseen currents",
        "lantern flaring with nether-light to blind and drain enemies, shadow-water splashing, eerie nether warrior expression",
        "magnificent dark violet and golden-nether water lantern with controlled ghost-light patterns, large blazing pale-green eyes with golden-dark rings, ornate golden lantern-frame, supreme nether-water aura, golden ghost-light accents",
        "devastating nether-light flood releasing combined shadow and dark-water energy, supreme nether water deity expression"
    ),
    "radiant_dream_wing": (
        "a winged owl-phoenix hybrid of pure light and dream-energy, translucent golden-white and soft rainbow feathered body with four taloned legs and magnificent dream-crystal wings, large luminous prismatic owl-like eyes with a transcendent dreaming expression, wings made of crystallized dreams refracting light, phoenix tail-plumes trailing dream-light, owl-face with feathered disc, ethereal celestial bird-beast presence",
        "wings releasing waves of dream-light energy while body ascends on four legs in divine radiance, supreme dream-light beast warrior expression",
        "magnificent supreme golden-white dream-wing owl-phoenix with sacred light-dream geometry wing patterns, large blazing prismatic owl-eyes with golden-dream rings, ornate golden dream-light crown on feathered head, supreme radiant-dream beast aura, golden tail-plumes and talons",
        "devastating dream-light nova with crystal-wings releasing supreme light-dream energy in all directions, supreme radiant dream beast deity expression"
    ),
    "illusion_dream": (
        "a shifting entity of light and shadow that exists only in the space between perception and reality, half-golden half-dark body constantly shifting, large dual-toned luminous eyes with a paradoxical expression, body creating illusions and dreams simultaneously, reality bending around the form",
        "body creating multiple illusory copies all attacking from different dimensions, supreme illusion warrior expression",
        "magnificent golden-prismatic and shadow illusion-dream with controlled reality-shift patterns, large blazing dual-toned eyes with golden rings, ornate golden illusion-crown, supreme reality-bending aura",
        "devastating illusion-collapse with reality itself being weaponized, supreme illusion-dream deity expression"
    ),
    "twin_phantasm": (
        "a pair of connected phantoms — one of pure light one of pure shadow — orbiting each other, white-gold and violet-black twin forms, large dual pairs of luminous eyes with synchronized expressions, light-phantom and shadow-phantom tethered by golden energy, eternal twins of opposing force",
        "both phantasms attacking in coordinated light-and-dark assault, supreme twin warrior expression",
        "magnificent supreme light-shadow twin phantasms with golden tether-energy patterns, large blazing dual-toned eyes on both forms, ornate golden twin-crowns, supreme light-dark duality aura",
        "devastating twin-assault with both phantasms attacking simultaneously from opposite dimensions, supreme twin phantasm deity expression"
    ),
    "divine_heart_fox": (
        "a sacred qilin-fox fusion beast wreathed in holy light and heart-energy — combining the qilin's scaled body and single horn with the fox's pointed ears and multiple bushy tails, white-gold and warm rose-pink celestial beast form with four graceful clawed legs, large luminous golden-pink eyes with absolute divine compassion and ancient wisdom, nine flowing tails of golden light and heart-fire, qilin scales on the chest and horn radiating sacred power, an aura of divine warmth and protection",
        "horn and nine tails directing holy-heart energy beams simultaneously while body radiates divine warmth on all four legs, supreme divine fox-qilin beast warrior expression",
        "magnificent supreme white-gold and rose-pink divine qilin-fox beast with sacred nine-tail and horn patterns, large blazing golden-pink eyes with divine-heart rings, ornate golden celestial crown between qilin-horn and fox-ears, supreme divine-heart beast aura, golden nine-tail patterns and scaled chest-plate",
        "devastating divine-heart nine-tail attack with all tails and horn releasing supreme holy-love energy, supreme divine fox-qilin beast deity expression"
    ),
    "myriad_chaos": (
        "a sphere of all-encompassing chaos containing myriad visions within light-dark-heart swirling energy, prismatic and yin-yang body with golden chaos borders, large luminous tri-colored eyes with absolute cosmic comprehension, all elements and emotions visible within, reality warping around the form",
        "body releasing myriad-chaos energy waves of all elements simultaneously, supreme all-encompassing warrior expression",
        "magnificent supreme prismatic-chaos sphere with golden sacred-chaos geometry, large blazing tri-colored eyes with golden cosmic rings, ornate golden myriad-chaos crown, supreme all-reality aura",
        "devastating myriad-chaos eruption releasing all possible energies in chaotic supreme harmony, supreme myriad chaos deity expression"
    ),
    "realm_deity": (
        "supreme ruler of all phantom-realms — a massive multi-eyed dragon-serpent beast combining the realm_master's chimeric form with greater draconic power, golden-prismatic scaled body with four powerful armored legs and enormous feathered wings of light-shadow-heart energy, large blazing tri-colored luminous eyes with absolute commanding presence, multiple smaller eyes along the serpentine neck, reality itself reshaping around the colossal beast form, dimensional portals visible near the wings and tail",
        "body commanding reality to attack with dimensional weapons, wings creating portals while four legs brace against dimensional stress, supreme realm ruler beast expression",
        "magnificent supreme golden-prismatic realm dragon-beast with sacred dimension-geometry scale patterns, large blazing tri-colored eyes with supreme dimensional rings, ornate golden realm-crown with three supreme gems between massive horns, absolute realm-master beast aura, golden armored wings one light one dark with heart-energy borders",
        "devastating dimension-collapse attack warping all realities simultaneously, all eyes releasing dimensional beams, supreme realm deity beast expression"
    ),
    "heart_realm_dream": (
        "a dreaming tapir-butterfly hybrid guardian of the heart-realm — combining the tapir's snout with butterfly dream-wings, rose-gold and soft-lavender furred body with four small legs and large translucent dream-wings, large luminous golden-pink eyes with infinite compassionate dream-wisdom, tapir snout gently inhaling dream-hearts, body surrounded by floating dream-heart butterflies, a soothing protective dream-cocoon beast presence",
        "dream-heart butterflies mobilizing to protect and heal while tapir body radiates calming energy on all fours, wings pulsing with heart-dreams, supreme dream-heart guardian beast expression",
        "magnificent supreme rose-gold and lavender tapir-butterfly dream-guardian with sacred heart-dream geometry wing patterns, large blazing golden-pink eyes with heart-dream rings, ornate golden dream-heart crown between rounded ears, supreme compassionate dream beast aura, golden dream-wings with heart-butterfly patterns",
        "devastating heart-dream wave engulfing all in a supreme healing protective dream released from wings and snout, supreme heart-dream beast deity expression"
    ),
    "galaxy_whale_spirit": (
        "a colossal phantom-whale swimming through star-fields with galaxies visible within, cosmic blue-purple and starlight body, large luminous golden-cosmic eyes with absolute cosmic serenity, body containing visible galaxies and nebulae, song that resonates across dimensions, absolute cosmic-ocean majesty",
        "body releasing a cosmic whale-song shockwave of stellar and water energy, supreme cosmic whale warrior expression",
        "magnificent supreme cosmic whale with blazing galaxy patterns and golden constellation borders, large blazing golden-cosmic eyes with supreme star rings, ornate golden cosmic-ocean crown, supreme stellar-phantom aura",
        "devastating cosmic whale-song nova releasing supreme stellar-ocean energy across all dimensions, supreme galaxy whale deity expression"
    ),
    "moonlight_spirit": (
        "the purest condensation of moonlight into a spirit form, soft silver-white and pale gold body radiating gentle lunar radiance, large luminous silver-gold eyes with absolute serene purity, crescent-moon shapes forming the body, the gentlest yet most powerful light, a beacon in darkness",
        "body focusing supreme moonlight into a concentrated purifying beam, absolute serene warrior expression",
        "magnificent supreme silver-gold moonlight spirit with sacred lunar-geometry patterns, large blazing silver-gold eyes with supreme moon rings, ornate golden crescent-crown, supreme pure-moon aura",
        "devastating moonlight purification releasing the purest supreme lunar energy, supreme moonlight deity expression"
    ),

    # ═══════════════════════════════════════════════════
    # 合成宠 — 龙族合成 (96-120)
    # ═══════════════════════════════════════════════════
    "steam_serpent": (
        "a Chinese serpent-dragon wreathed in pressurized steam, teal-blue and warm orange body with vapor constantly venting, large round bright amber-blue eyes with a fierce hissing expression, long sinuous body with steam vents along the spine, barbel whiskers trailing steam, a hot-springs dragon presence",
        "body releasing pressurized steam jets while coiling to strike, fierce steam-serpent warrior expression",
        "magnificent golden-steam and teal serpent-dragon with controlled vapor patterns, large blazing amber-blue eyes with golden rings, ornate golden steam-vent horns, supreme thermal-serpent aura, golden scale-accents",
        "devastating steam-coil attack with body spiraling and releasing superheated vapor, supreme steam serpent deity expression"
    ),
    "lava_dragon": (
        "a heavily-armored dragon covered in hardened lava-rock with glowing magma visible through cracks, deep obsidian and molten-orange body, large blazing white-hot eyes with a fierce volcanic expression, thick lava-rock armor plates, magma dripping from the jaws, volcanic heat-shimmer, crushing weight",
        "jaws opening to release a lava stream while body radiates volcanic heat, supreme volcanic warrior expression",
        "magnificent obsidian and golden-magma lava dragon with controlled volcanic patterns, large blazing white-gold eyes with ruby-amber rings, ornate golden magma-crown, supreme volcanic aura, golden lava-flow accents",
        "devastating magma-breath releasing concentrated molten rock and fire, supreme lava dragon deity expression"
    ),
    "aqua_wyvern": (
        "a wyvern with water-membrane wings that can fly and swim equally, teal-blue and silver-white body, large round bright cyan-blue eyes with an agile adventurous expression, water-flow wings, streamlined aquatic-aerodynamic body, water trailing from wing-tips in flight",
        "diving from air into water and back out in a fluid combined attack, supreme aqua-aerial warrior expression",
        "magnificent sapphire and golden-silver aqua wyvern with water-wind wing patterns, large blazing sapphire-cyan eyes with golden rings, ornate golden aqua-wing crown, supreme water-wind dragon aura, golden fin-wing edges",
        "devastating air-water strike diving through both elements in one devastating pass, supreme aqua wyvern deity expression"
    ),
    "quake_bolt_dragon": (
        "a massive heavy-armored dragon that causes earthquakes and summons lightning, dark stone-brown and electric-yellow body, large blazing amber-electric eyes with an overwhelming expression, incredibly thick leg-pillars that crack the earth, lightning-rod horns, seismic and electric dual presence",
        "body stamping to create earthquakes while horns attract lightning strikes, supreme quake-bolt warrior expression",
        "magnificent golden-stone and electric-gold armored dragon with seismic-lightning patterns, large blazing topaz-electric eyes with golden rings, ornate golden quake-bolt crown, supreme seismic-storm aura",
        "devastating quake-bolt attack with ground-shattering stomp releasing upward lightning simultaneously, supreme quake-bolt dragon deity expression"
    ),
    "wind_radiant_dragon": (
        "a majestic dragon riding holy wind-currents with luminous sacred wings, pale gold and silver-white body radiating divine wind-light, large luminous golden-cyan eyes with a noble transcendent expression, crystalline wind-light wings, divine aura of holy wind, elegant aerial sacred presence",
        "body ascending on holy wind while releasing divine light-beams, supreme sacred wind warrior expression",
        "magnificent supreme golden-white and silver wind-radiant dragon with sacred wind-light patterns, large blazing white-gold eyes with divine wind rings, ornate golden divine-wind crown, supreme holy-wind aura, golden crystalline wings",
        "devastating divine wind-light assault from the heavens, supreme wind-radiant dragon deity expression"
    ),
    "lightdark_dragon": (
        "a dragon with one half of pure light and one half of pure shadow, yin-yang body split down the middle, large dual-colored eyes — one white-gold one dark-violet — with a balanced dual expression, wings one light one dark, golden energy border at the division line",
        "both halves releasing simultaneous opposing breath attacks, supreme duality warrior expression",
        "magnificent supreme golden light-dark dragon with sacred yin-yang patterns and golden borders, large blazing dual-colored eyes with golden rings, ornate golden duality-crown, supreme light-dark balance aura",
        "devastating duality-breath with light and darkness colliding into a supreme chaos-blast, supreme lightdark dragon deity expression"
    ),
    "coastal_dragon": (
        "a heavy-armored sea-dragon guarding coastlines with coral-encrusted stone armor, deep blue and stone-brown body, large round deep sapphire-amber eyes with a steadfast guardian expression, coral and barnacle-covered stone plates, water flowing over rock-armor, a living reef-fortress presence",
        "body charging with the force of crashing waves, armor-plates raised as a tidal shield, supreme coastal guardian expression",
        "magnificent sapphire-stone and golden-coral coastal dragon with living reef-fortress armor, large blazing sapphire-amber eyes with golden rings, ornate golden coral-crown, supreme coastal fortress aura, golden reef-plate accents",
        "devastating tidal-fortress charge with combined water-earth force, supreme coastal dragon deity expression"
    ),
    "heart_inferno_ancient": (
        "a supreme ancient dragon with soul-fire burning from a heart-energy core, deep crimson-gold and rose-flame body, large blazing golden-pink-flame eyes with both fury and compassion, ancient scarred body with heart-fire burning through the cracks, a paradox of destructive fire and protective love",
        "ancient fire-breath infused with heart-energy creating compassionate destruction, supreme heart-inferno expression",
        "magnificent supreme golden-crimson and rose-flame ancient dragon with sacred heart-fire patterns, large blazing golden-pink eyes with heart-flame rings, ornate golden heart-inferno crown, supreme soul-fire aura",
        "devastating heart-inferno breath of ancient soul-fire that both destroys and protects, supreme heart-inferno ancient deity expression"
    ),
    "flora_serpent_king": (
        "a magnificent serpent-dragon completely covered in a blooming flower-garden, deep emerald and floral body, large blazing emerald eyes with a regal nature-king expression, flower-crown horns, vine-scale body, every surface blooming with different flowers, a living serpent-garden of supreme beauty",
        "body whipping while flowers launch a barrage of nature-projectiles, supreme flora-serpent warrior expression",
        "magnificent supreme emerald and golden-floral serpent king with sacred garden patterns, large blazing emerald eyes with golden-jade rings, ornate golden flower-crown, supreme living garden aura, golden vine-scale accents",
        "devastating garden-serpent assault with body whipping and flowers exploding with nature energy, supreme flora serpent deity expression"
    ),
    "fire_origin_dragon": (
        "a dragon of pure concentrated fire energy, brilliant vermilion and white-hot body with a visible fire-gem core, large blazing white-gold eyes with absolute fire mastery, body made entirely of controlled living flame in dragon form, ultimate fire-dragon essence",
        "body releasing supreme concentrated fire from the core, absolute fire warrior expression",
        "magnificent supreme golden-fire and white-hot origin dragon with sacred fire-geometry patterns, large blazing white-gold eyes with ruby-fire rings, ornate golden fire-origin crown, supreme pure-fire aura",
        "devastating origin-fire breath of the purest possible fire energy, supreme fire origin dragon deity expression"
    ),
    "water_origin_dragon": (
        "a dragon of pure concentrated water energy, deep sapphire and crystal-clear body with a visible water-gem core, large blazing sapphire eyes with absolute water mastery, body made entirely of controlled living water in dragon form, ultimate water-dragon essence",
        "body releasing supreme concentrated water from the core, absolute water warrior expression",
        "magnificent supreme golden-sapphire and crystal water origin dragon with sacred water-geometry patterns, large blazing sapphire eyes with blue-water rings, ornate golden water-origin crown, supreme pure-water aura",
        "devastating origin-water breath of the purest possible water energy, supreme water origin dragon deity expression"
    ),
    "thunder_origin_dragon": (
        "a dragon of pure concentrated thunder energy, brilliant electric-gold and white-blue body with a visible lightning-gem core, large blazing electric-white eyes with absolute thunder mastery, body made entirely of controlled living lightning in dragon form, ultimate thunder-dragon essence",
        "body releasing supreme concentrated lightning from the core, absolute thunder warrior expression",
        "magnificent supreme golden-electric and brilliant white origin dragon with sacred thunder-geometry patterns, large blazing electric-white eyes with golden-lightning rings, ornate golden thunder-origin crown, supreme pure-thunder aura",
        "devastating origin-thunder breath of the purest possible lightning energy, supreme thunder origin dragon deity expression"
    ),
    "light_origin_dragon": (
        "a dragon of pure concentrated holy light energy, brilliant white-gold body radiating divine light with a visible sunstone core, large blazing white-gold eyes with absolute light mastery, body made entirely of controlled divine light in sacred dragon form, ultimate holy-dragon essence",
        "body releasing supreme holy light from the core, absolute divine warrior expression",
        "magnificent supreme white-gold origin dragon with sacred light-geometry patterns, large blazing white-gold eyes with divine rings, ornate golden light-origin crown, supreme divine-light aura",
        "devastating origin-light breath of the purest divine light, supreme light origin dragon deity expression"
    ),
    "radiant_dream_dragon": (
        "a luminous dream-guardian dragon of light and heart energy, pale gold and rose-dream body, large luminous golden-pink eyes with gentle dream-wisdom, wings of crystallized dream-light, body partially translucent showing a glowing heart-core, a protective dream-light dragon presence",
        "wings releasing waves of dream-light protection energy, supreme dream guardian expression",
        "magnificent supreme golden-rose dream dragon with sacred dream-light patterns, large blazing golden-pink eyes with dream-light rings, ornate golden dream-guardian crown, supreme radiant-dream aura",
        "devastating dream-light wave of supreme protective-healing energy, supreme radiant dream dragon deity expression"
    ),
    "shadow_dream_dragon": (
        "a dark dream-dragon born from nightmares with shadow and heart energy, deep violet and dark rose body, large glowing violet-pink eyes with a haunting wise expression, wings of shadow-dreams, body trailing dark dream-mist, a protector who conquers nightmares from within",
        "wings releasing controlled nightmare-energy that subdues enemies, supreme shadow-dream warrior expression",
        "magnificent deep violet and golden-dark dream dragon with sacred shadow-dream patterns, large blazing violet-pink eyes with golden-dark rings, ornate golden nightmare-crown, supreme shadow-dream aura",
        "devastating nightmare-wave releasing controlled dark-dream energy that overwhelms, supreme shadow dream dragon deity expression"
    ),
    "heart_dream_dragon": (
        "a dragon of pure heart-dream energy that exists in the deepest heart-realm, rose-gold and warm lavender body, large luminous golden-pink eyes with absolute emotional wisdom, body made of crystallized heart-dreams, the most loving of all dragons, a soothing protective presence",
        "body radiating supreme heart-dream energy, emotions becoming shields and weapons, supreme heart-dream guardian expression",
        "magnificent supreme rose-gold and golden-lavender heart-dream dragon with sacred heart-dream geometry, large blazing golden-pink eyes with supreme heart-dream rings, ornate golden heart-dream crown, supreme emotional-dream aura",
        "devastating heart-dream wave creating a supreme emotional reality-shield, supreme heart dream dragon deity expression"
    ),
    "thunder_fire_dragon": (
        "a fierce dragon of intertwined fire and lightning energy, deep crimson and electric-gold body, large blazing amber-electric eyes with a furious berserker expression, fire and lightning constantly arcing across the scales, volatile and explosive energy, a dragon of rage and power",
        "body erupting with simultaneous fire and lightning from every scale, supreme fire-thunder berserker expression",
        "magnificent supreme crimson and electric-gold thunder-fire dragon with controlled fire-lightning patterns, large blazing white-gold eyes with fire-thunder rings, ornate golden thunder-fire crown, supreme volcanic-storm aura",
        "devastating fire-thunder eruption with both elements exploding simultaneously, supreme thunder-fire dragon deity expression"
    ),
    "tempest_dragon": (
        "a storm-dragon of combined wind and lightning energy, storm-gray and electric-cyan body, large blazing electric-cyan eyes with a fierce commanding expression, body surrounded by a perpetual tempest, wind and lightning merging around the wings, a living thunderstorm in dragon form",
        "body generating a massive localized tempest around itself, supreme storm warrior expression",
        "magnificent supreme storm-gray and golden-electric tempest dragon with controlled storm patterns, large blazing electric-white eyes with golden-storm rings, ornate golden tempest-crown, supreme thunderstorm aura",
        "devastating full-tempest attack generating a massive wind-lightning storm, supreme tempest dragon deity expression"
    ),
    "radiant_flora_dragon": (
        "a beautiful dragon of holy light and living plants, pale gold and emerald body with blooming flowers growing along sacred-light scales, large luminous golden-green eyes with a nurturing divine expression, wings of golden-green light-leaves, holy nature aura, a divine forest-dragon of healing",
        "wings releasing holy-nature healing light and protective plant-barriers, supreme radiant-flora guardian expression",
        "magnificent supreme golden-emerald radiant-flora dragon with sacred light-nature patterns, large blazing golden-green eyes with divine-nature rings, ornate golden nature-light crown, supreme holy-garden aura",
        "devastating radiant-flora burst of supreme divine nature-light energy, supreme radiant flora dragon deity expression"
    ),
    "sea_purgatory_dragon": (
        "a terrifying dragon that burns the ocean itself, deep crimson-blue body with fire and water warring across the scales creating perpetual steam, large blazing white-hot amber-blue eyes with absolute devastating expression, wings of fire over ocean, seawater boiling at the touch, apocalyptic ocean-fire presence",
        "body releasing fire into the sea creating a steam-apocalypse, supreme sea-purgatory warrior expression",
        "magnificent supreme crimson-blue and golden sea-purgatory dragon with sacred fire-water apocalypse patterns, large blazing white-gold eyes with fire-water rings, ornate golden sea-fire crown, supreme ocean-inferno aura",
        "devastating sea-fire apocalypse setting the ocean ablaze, supreme sea purgatory dragon deity expression"
    ),
    "yin_yang_dragon_god": (
        "supreme yin-yang dragon god of perfect light-shadow balance, half brilliant white-gold half absolute dark-violet, a divine dragon form, large blazing dual-colored eyes with absolute cosmic balance, golden energy at the division, wings one of light one of shadow, the ultimate balance embodied",
        "both halves releasing supreme divine power in perfect opposing harmony, absolute balance-god expression",
        "magnificent supreme golden-bordered yin-yang dragon god with sacred balance-geometry patterns, large blazing dual-colored eyes with supreme golden rings, ornate golden balance-crown with light-dark gems, supreme cosmic-balance aura",
        "devastating supreme balance-blast with light and darkness merging into transcendent golden power, supreme yin-yang dragon god expression"
    ),
    "heart_shadow_dragon_god": (
        "supreme dragon god where heart-energy unifies and commands both light and shadow, golden-rose and prismatic body with controlled light-dark energy, large blazing tri-colored luminous eyes with absolute heart-mastery over all forces, heart-energy bridging and commanding light and shadow, supreme triune dragon presence",
        "heart-energy directing light and shadow simultaneously in perfect harmony, supreme triune commander expression",
        "magnificent supreme golden-rose and prismatic dragon god with sacred triune-geometry, large blazing tri-colored eyes with supreme golden rings, ornate golden triune-crown with three divine gems, supreme heart-light-shadow aura",
        "devastating triune-blast with heart commanding light and shadow in supreme unified attack, supreme heart-shadow dragon god expression"
    ),
    "magma_ancient_dragon": (
        "supreme ancient dragon of volcanic fury with magma-core body and stone-armor plates, obsidian and molten-gold massive ancient form, large blazing white-hot eyes with absolute volcanic might, lava flowing through every crack in the ancient stone-scales, the volcano incarnate as a dragon, tectonic presence",
        "body erupting like a volcano with magma breath and seismic stomps, supreme volcanic ancient expression",
        "magnificent supreme obsidian and golden-magma ancient dragon with sacred volcanic-geometry patterns, large blazing white-gold eyes with magma rings, ornate golden volcanic-crown, supreme tectonic-fire aura",
        "devastating volcanic eruption-breath with body itself erupting with magma, supreme magma ancient dragon deity expression"
    ),
    "ocean_heart_dragon_god": (
        "supreme ocean-guardian dragon god with heart-energy protecting all seas, deep sapphire and warm rose-gold body, large luminous sapphire-pink eyes with absolute oceanic compassion, body flowing with ocean-heart currents, guardian of all marine life, the heart of the ocean in dragon form",
        "body commanding compassionate ocean-currents to protect and heal, supreme ocean-heart guardian expression",
        "magnificent supreme sapphire-rose and golden ocean-heart dragon god with sacred ocean-heart geometry, large blazing sapphire-pink eyes with supreme ocean-heart rings, ornate golden ocean-heart crown, supreme oceanic-compassion aura",
        "devastating ocean-heart wave of supreme protective oceanic love-energy, supreme ocean heart dragon god expression"
    ),
    "sovereign_dragon_god": (
        "absolute supreme dragon god ruling all elements and all dragon-kind, prismatic-golden body displaying all elements simultaneously, a divine dragon form of absolute cosmic proportions, large blazing prismatic eyes with absolute sovereign authority, every scale a different element, supreme crown of all gems, absolute ruler of the dragon realm",
        "body commanding all elements and all draconic power simultaneously, absolute sovereign expression",
        "magnificent supreme prismatic-golden sovereign dragon god with sacred all-element geometry, large blazing prismatic eyes with supreme golden-cosmic rings, ornate supreme golden sovereign-crown with all element gems, absolute dragon-sovereign aura",
        "devastating all-element sovereign breath commanding every force simultaneously, supreme sovereign dragon god expression"
    ),

    # ═══════════════════════════════════════════════════
    # 跨种族终极合成 (121-125)
    # ═══════════════════════════════════════════════════
    "radiant_qilin_dragon": (
        "a divine fusion of qilin and fire-dragon with holy-fire essence, white-gold and crimson-flame body with both qilin grace and dragon power, large blazing golden-amber eyes with divine-fire intensity, qilin horn fused with dragon horns, fire-scaled body with qilin markings, divine beast of supreme fire-and-light",
        "horn and horns channeling supreme holy-fire breath, body surging with qilin-dragon fusion power, supreme divine-fire warrior expression",
        "magnificent supreme golden-crimson qilin-dragon with sacred fire-light fusion geometry, large blazing white-gold eyes with divine-fire rings, ornate golden fusion-crown, supreme holy-fire beast aura",
        "devastating holy-fire fusion breath of supreme qilin-dragon power, supreme radiant qilin dragon deity expression"
    ),
    "shadow_sea_serpent_king": (
        "a massive dark serpent-dragon of abyssal ocean and shadow energy, obsidian-blue and deep violet colossal serpent form, large glowing pale-violet-blue eyes with absolute abyssal authority, shadow-ocean flowing along the body, darkness and deep water merged, king of the lightless depths",
        "body creating a vortex of shadow-ocean that drags enemies into the abyss, supreme abyssal king expression",
        "magnificent supreme obsidian-blue and golden-dark serpent king with sacred abyss-shadow geometry, large blazing violet-blue eyes with golden-dark rings, ornate dark golden abyss-crown, supreme shadow-ocean aura",
        "devastating abyss-vortex with shadow and ocean combining to create an inescapable void, supreme shadow sea serpent deity expression"
    ),
    "heart_flora_dragon_deer": (
        "a beautiful dragon-deer fusion with heart energy and nature power, jade-green and rose-gold graceful body combining deer elegance with dragon majesty, large luminous golden-green-pink eyes with compassionate noble expression, branching antler-horns with blooming flowers and dragon scales, vine-and-scale body, a nature-heart divine beast",
        "antler-horns channeling heart-nature energy beams, body radiating healing nature-love, supreme nature-heart guardian expression",
        "magnificent supreme jade-rose and golden nature-heart dragon-deer with sacred flora-heart geometry, large blazing golden-green-pink eyes with nature-heart rings, ornate golden blooming-antler crown, supreme flora-heart aura",
        "devastating heart-nature fusion burst of supreme healing and protective flora-love energy, supreme heart flora dragon deity expression"
    ),
    "magma_bear_dragon": (
        "a colossal bear-dragon fusion of earth and fire, massive obsidian-brown and molten-gold body combining bull-power with dragon-might, large blazing white-hot amber eyes with unstoppable force, massive horns and thick magma-armored body, earthquake with every step, volcanic titan of supreme strength",
        "charging with earth-shattering force while breathing magma, supreme tectonic berserker expression",
        "magnificent supreme obsidian and golden-magma bear-dragon titan with sacred volcanic-force geometry, large blazing white-gold eyes with magma-earth rings, ornate golden volcanic-titan crown, supreme tectonic-fire aura",
        "devastating magma-charge with continental-shaking force and volcanic breath, supreme magma bear dragon deity expression"
    ),
    "storm_tiger_wyvern": (
        "a winged tiger-dragon fusion of wind and thunder, storm-gray and electric-gold powerful flying-tiger body with wyvern wings, large blazing electric-gold eyes with fierce predatory sky-king expression, tiger body with dragon wings, lightning-striped fur-scales, airborne storm predator of supreme speed and power",
        "diving from storm-clouds with lightning and wind combined in a devastating aerial pounce, supreme storm sky-predator expression",
        "magnificent supreme storm and golden-electric tiger-wyvern with sacred storm-beast geometry, large blazing electric-white eyes with golden-storm rings, ornate golden storm-beast crown, supreme aerial-thunder aura",
        "devastating storm-dive with wind-lightning tiger-pounce from the clouds, supreme storm tiger wyvern deity expression"
    ),

    # ═══════════════════════════════════════════════════
    # 神级终极合成 (126-133)
    # ═══════════════════════════════════════════════════
    "divine_wing_dragon": (
        "supreme divine bird-dragon fusion of aurora light and dragon power, prismatic-gold and white-platinum winged dragon with seven-colored aurora wings, large blazing prismatic eyes with absolute divine sky-sovereignty, aurora-wing feathers on dragon body, supreme aerial divine presence",
        "aurora wings releasing supreme divine light while dragon form adds devastating power, absolute sky-god expression",
        "magnificent supreme prismatic-golden divine wing dragon with sacred aurora-dragon geometry, large blazing prismatic eyes with supreme golden rings, ornate golden divine-wing crown, supreme aurora-dragon aura",
        "devastating aurora-dragon breath combining supreme divine light with draconic power, supreme divine wing dragon deity expression"
    ),
    "starfish_heart_dragon": (
        "a dragon with stellar scales and heart-energy core, cosmic-gold and warm rose body, large luminous golden-cosmic-pink eyes with both stellar wisdom and emotional depth, star-pattern scales with heart-light emanating from within, starlight-heart fusion dragon of cosmic love",
        "body releasing stellar-heart energy combining cosmic power with emotional force, supreme stellar-heart warrior expression",
        "magnificent supreme cosmic-gold and rose star-heart dragon with sacred stellar-heart geometry, large blazing golden-cosmic-pink eyes with star-heart rings, ornate golden star-heart crown, supreme cosmic-love aura",
        "devastating star-heart nova releasing supreme cosmic-emotional energy, supreme star heart dragon deity expression"
    ),
    "heart_bloom_dragon": (
        "a divine dragon fused with the heart-flower god essence, emerald-gold and warm rose-pink body with blooming flowers growing from dragon-scales, large luminous golden-green-pink eyes with absolute nurturing divine expression, flower-horn crown, vine-scale body with heart-flowers, supreme healing nature-dragon",
        "body releasing supreme heart-nature healing energy, flowers blooming with divine power, supreme heart-nature guardian expression",
        "magnificent supreme emerald-rose and golden heart-bloom dragon with sacred nature-heart-dragon geometry, large blazing golden-green-pink eyes with nature-heart rings, ornate golden bloom-dragon crown, supreme divine-garden aura",
        "devastating heart-bloom wave of supreme divine nature-healing energy, supreme heart bloom dragon deity expression"
    ),
    "chaos_dragon_god": (
        "supreme dragon god of controlled chaos with perfect light-dark balance in draconic form, yin-yang body of white-gold and deep violet with golden chaos borders, large blazing dual-colored eyes with absolute chaos mastery, wings one light one dark, chaos-fire breath, the dragon of ordered disorder",
        "breath of chaotic dual-energy combining creation and destruction, supreme chaos-dragon expression",
        "magnificent supreme golden-bordered yin-yang chaos dragon with sacred chaos-dragon geometry, large blazing dual-colored eyes with supreme chaos rings, ornate golden chaos-dragon crown, supreme ordered-chaos aura",
        "devastating chaos-breath combining supreme light and dark in a reality-shaking explosion, supreme chaos dragon god expression"
    ),
    "realm_dragon_god": (
        "supreme dimensional dragon god combining phantom-realm mastery with draconic power, golden-prismatic and tri-colored body, large blazing tri-colored eyes with absolute dimensional-dragon sovereignty, reality warping around the draconic form, master of all dimensions and all dragon power combined",
        "body warping dimensions while releasing supreme draconic breath, absolute dimension-dragon expression",
        "magnificent supreme golden-prismatic realm dragon with sacred dimension-dragon geometry, large blazing tri-colored eyes with supreme dimensional rings, ornate golden realm-dragon crown with tri-gems, supreme dimension-sovereign aura",
        "devastating dimension-dragon breath warping reality while releasing supreme all-force draconic energy, supreme realm dragon god expression"
    ),
    "genesis_deity": (
        "a colossal qilin-phoenix fusion beast of supreme elemental creation, prismatic-golden scales and luminous feathered mane flowing with all elemental colors, massive qilin antler-horns crackling with genesis energy, large blazing white-gold eyes with vertical beast pupils radiating creation-force, four powerful clawed legs with phoenix-feathered fetlocks, long sweeping feathered tail trailing prismatic sparks, muscular divine beast body covered in iridescent scales",
        "body crouching low with all four legs braced, qilin horns channeling explosive genesis energy forward, feathered mane billowing with creation power, fierce primal beast battle-roar expression",
        "magnificent supreme prismatic-golden qilin-phoenix god-beast with elaborate golden armor plates on shoulders and chest, massive ornate antler-horns wreathed in creation-fire, large blazing white-gold eyes with supreme prismatic rings in vertical beast pupils, flowing prismatic feathered mane and tail with golden filigree ornaments, four powerful armored clawed legs, iridescent scales shifting through all element colors",
        "devastating genesis-burst erupting from massive open jaws and antler-horns simultaneously, body surging forward with all four legs in powerful charge, prismatic creation-energy exploding outward, supreme genesis beast war-cry expression"
    ),
    "purgatory_deity_dragon": (
        "a supreme fire-dragon of colossal size combining the greatest beast-fire with dragon-fire, massive vermilion-gold and white-hot scaled body with four powerful dragon legs, enormous bat-like wings wreathed in purgatory flames, large blazing white-hot dragon eyes with vertical slit pupils of absolute fire authority, thick armored neck with layered fire-scales, massive horned dragon head with fangs dripping molten flame, long powerful tail ending in a flame-blade",
        "body rearing up with wings spread wide, jaws open releasing supreme concentrated purgatory-fire breath, tail lashing with flame, fierce dragon war-god expression",
        "magnificent supreme white-gold and vermilion purgatory dragon god with ornate golden flame-armor plating on chest and shoulders, massive horns wreathed in supreme sacred fire, large blazing white-hot dragon eyes with golden-fire rings in vertical pupils, enormous wings with golden-edged flame membranes, four powerful armored dragon legs with golden claws, layered supreme fire-scales radiating intense heat",
        "devastating supreme purgatory-fire breath erupting from massive dragon jaws, wings fully spread creating a wall of sacred flame, body surging forward with four legs in devastating charge, supreme purgatory dragon god expression"
    ),
    "primordial_deity": (
        "a titanic dragon-qilin fusion beast of absolute supreme power, the largest and most majestic of all creatures, massive prismatic-golden-white scaled body with four colossal clawed legs, enormous multi-layered wings combining dragon membranes with prismatic feathers, great qilin antler-horns fused with dragon horns on a massive bestial head, large blazing white-gold prismatic eyes with vertical beast pupils containing all elemental colors, thick armored neck with flowing prismatic mane, long powerful dragon tail wreathed in all-element energy, every scale shifting through all colors of creation",
        "body in devastating four-legged charge with wings spread wide, massive jaws open releasing prismatic all-element breath, antler-horns channeling supreme unified power, absolute primordial titan war-beast expression",
        "magnificent supreme prismatic-white-gold primordial titan dragon-beast with elaborate golden divine armor covering chest shoulders and legs, colossal ornate antler-dragon-horns wreathed in all-element sacred fire, large blazing supreme white-gold eyes with all-encompassing prismatic rings in vertical beast pupils, enormous wings with golden-armored edges and prismatic feather-membranes, flowing prismatic mane with golden ornaments, four massive golden-armored clawed legs, supreme golden tail-blade crackling with all forces, the absolute apex beast of all creation",
        "devastating primordial unity-burst erupting from massive open jaws and colossal horns simultaneously, enormous wings creating a prismatic storm, body charging forward on four powerful legs with earth-shaking force, every element every force combined in one transcendent supreme beast attack, absolute primordial titan war-god expression"
    ),
}
