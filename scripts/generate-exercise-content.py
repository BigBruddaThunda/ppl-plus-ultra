#!/usr/bin/env python3
"""
generate-exercise-content.py — CX-37: Exercise Knowledge Template Generator
Reads middle-math/exercise-registry.json and writes exercise-content/{type}/{slug}.md

CLI flags:
  --exercise EX-0001        Single exercise by ID
  --section A               All exercises in a source section
  --type Push               All exercises of a SCL type (Push/Pull/Legs/Plus/Ultra)
  --batch N                 First N exercises by priority order
  --priority-first          Sort by usage frequency before sequential (default for --batch)
  --overwrite               Overwrite existing files (default: skip)
  --stats                   Print coverage stats and exit
  --dry-run                 Print what would be generated without writing

Usage:
  python scripts/generate-exercise-content.py --batch 200 --priority-first
  python scripts/generate-exercise-content.py --exercise EX-0571
  python scripts/generate-exercise-content.py --type Pull
  python scripts/generate-exercise-content.py --stats
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REGISTRY   = Path("middle-math/exercise-registry.json")
FAMILY_TREES = Path("middle-math/exercise-engine/family-trees.json")
USAGE_REPORT = Path("reports/exercise-usage-2026-03-06.md")
OUTPUT_DIR = Path("exercise-content")
GENERATED  = date.today().isoformat()

# ---------------------------------------------------------------------------
# Priority exercise list (from exercise-usage-2026-03-06.md — exercises with
# 10+ appearances across 120 generated cards)
# ---------------------------------------------------------------------------
PRIORITY_NAMES = [
    "Dead Bug (Back Stability)",
    "Rowing Machine (Steady State)",
    "Child's Pose (Shoulder Stretch)",
    "Scapular Push-Up",
    "Glute Bridge (Bodyweight)",
    "Scapular Pull-Up",
    "Barbell Bench Press",
    "Bear Crawl (Shoulder Stability)",
    "Jump Rope Intervals (1 minute on/off)",
    "Barbell Overhead Press (Standing)",
    "Rowing Intervals (500m)",
    "Suitcase Carry (Single-Arm)",
    "Romanian Deadlift (RDL)",
    "World's Greatest Stretch (Back Focus)",
    "Single-Arm Dumbbell Row",
    "Treadmill Incline Walk",
    "Shoulder CARs (Controlled Articular Rotations)",
    "Weighted Bulgarian Split Squat (Dumbbells)",
    "Single-Leg Romanian Deadlift",
    "Assault Bike (Steady State)",
    "Band Pull-Apart",
    "Farmer's Carry (Heavy)",
    "Mountain Climber",
    "Cat-Cow (Chest Expansion)",
    "Deadlift (Conventional)",
]

# ---------------------------------------------------------------------------
# PPL± Order voice templates (per movement pattern × order)
# ---------------------------------------------------------------------------
ORDER_TEMPLATES: dict[str, dict[str, str]] = {
    "hip-hinge": {
        "foundation": "Hinge mechanics take priority over load. Sub-65% means you have room to focus on the hip push-back, the hamstring load, and the neutral spine position. This is where the pattern is encoded.",
        "strength":   "The hinge is a force-production pattern. At 75–85%, every rep is a neural event. Full setup before each pull. The bar doesn't move until the lats are locked and the floor is about to break.",
        "hypertrophy":"Drive hamstring tension through the full range. The concentric is deliberate — not explosive. Time under tension through the hip extension is what produces posterior chain adaptation here.",
        "restoration":"Hip-hinge patterns at restoration load (≤55%) become positional resets. RDL variations, light good mornings, or cable pull-throughs. If loading this pattern causes soreness the next day at restoration intensity, something else is wrong.",
    },
    "squat": {
        "foundation": "Foot width, bracing, and descent rate are the lesson. Load is irrelevant. The goal is groove — the same position rep after rep. Sub-65% gives you 8–15 reps to get it right.",
        "strength":   "High CNS demand. The squat earns its intensity. 75–85% with a 3–4 minute rest is not optional — it is the mechanism. Cut the rest and you are no longer training strength.",
        "hypertrophy":"Quad emphasis through full depth and controlled descent. Pause at the bottom to eliminate the stretch reflex and force the quads to do the work. Pump is information — not the goal, but a signal.",
        "restoration":"Goblet squat or bodyweight box squat. Mobility work masquerading as strength. The joint is being asked to move, not loaded. Any squat in restoration should leave the tissues better than you found them.",
    },
    "horizontal-press": {
        "foundation": "Scapular position before bar position. The shoulder blade must be set before the chest is loaded. Foundation load means you have time to find the position without chasing a number.",
        "strength":   "Leg drive is not optional at 75–85%. The press is a full-body movement at strength intensity. The bar path is straight. The wrists are stacked. The arch is earned, not cheated.",
        "hypertrophy":"Full pec stretch at the bottom. Controlled descent. No bounce. The tricep finishes, but the pec drives. Accumulated sets of 8–12 with genuine tension throughout — not just moving through range.",
        "restoration":"Light cable flyes, band chest presses, or low-incline machine press. The chest is active, not loaded. Restoration context means no heavy press variation — the tissue needs circulation, not stimulus.",
    },
    "vertical-press": {
        "foundation": "Overhead position demands shoulder mobility that most people have to earn. Foundation load lets you find the path before you fight the load. Lockout position is the cue — stack the joint.",
        "strength":   "The strict press is an honesty test. At 75–85%, the body wants to use the legs. Keep them out. The movement starts at the chest and finishes with ears through the arms. Each rep is its own event.",
        "hypertrophy":"Partial range presses and lateral raise variations accumulate shoulder volume effectively. The medial delt responds to mechanical tension, not just metabolic stress. 8–12 reps with genuine shoulder isolation.",
        "restoration":"Face pulls, band YTWLs, or light lateral raises. The shoulder girdle at restoration intensity is being mobilized and maintained, not developed. Any pain here is signal — not to be pushed through.",
    },
    "horizontal-pull": {
        "foundation": "Row mechanics: shoulders set first, pull to the lower rib, squeeze the shoulder blade at the top. Foundation load is pattern acquisition — the groove before the grind.",
        "strength":   "Heavy rows are a grip and lat event. 75–85% loads the lats, rhomboids, and rear delts heavily. The row is not a bicep exercise at this intensity. Brace the core. The torso does not rotate.",
        "hypertrophy":"Full stretch at the dead hang, full retraction at the top. The back gets its stimulus from range, not just load. Slow eccentric on cable and dumbbell rows amplifies this.",
        "restoration":"Face pulls, band rows, or TRX rows at low angle. The posterior chain of the shoulder needs circulation after heavy pressing and pulling. This is maintenance, not development.",
    },
    "vertical-pull": {
        "foundation": "Scapular depression before arm pull. The lat initiates — not the bicep. Foundation load means you can practice the activation pattern before load makes it irrelevant.",
        "strength":   "Weighted pull-ups and heavy lat pulldowns demand full spinal extension at the top and controlled descent. The negative is strength work. Dropping the weight after the pull is waste.",
        "hypertrophy":"Full dead hang to chin-over-bar. The stretch at the bottom is the stimulus. Partial range pulldowns accumulate volume but not the full stretch reflex that drives lat hypertrophy.",
        "restoration":"Band-assisted pull-up or light cable pulldown. The lat is a respiratory muscle. Easy vertical pulls in restoration decompress the spine and restore shoulder girdle mobility.",
    },
    "isolation-curl": {
        "foundation": "Supination through the full range of motion — this is the lesson at foundation load. Elbow position does not change. The weight is a prop for practicing the contraction.",
        "strength":   "Heavy curls are not conventional strength work, but preacher curls and incline curls at challenging loads (relatively) develop the long head of the bicep through stretch-mediated hypertrophy.",
        "hypertrophy":"The bicep responds to peak contraction and full stretch. Incline dumbbell curls, preacher curls, and cross-body variations each bias a different part of the range. Accumulated sets with controlled tempo.",
        "restoration":"Light band curls or light cable curls at full extension. The elbow flexors are maintained, not loaded. Any restoration curl is about joint health and circulation, not development.",
    },
    "isolation-extension": {
        "foundation": "Full elbow extension is the lesson. The tricep must fire through its full mechanical range. Foundation load is an education in lockout — not a strength stimulus.",
        "strength":   "Close-grip bench, JM press, and weighted dips at 75–85% develop the tricep as a pressing muscle. The lateral head is built by these compound extension patterns more than by isolation work.",
        "hypertrophy":"Overhead extensions bias the long head through a position of stretch. The long head is responsible for upper arm mass. Accumulate volume here with controlled eccentrics.",
        "restoration":"Band tricep pressdowns or light cable extensions. The elbow joint needs extension range, not load. Restoration tricep work is for the tendon, not the muscle.",
    },
    "lunge": {
        "foundation": "Single-leg stability is the entry fee. Foundation load means the hip, knee, and ankle stack must be established before load amplifies any deviation. Slow, controlled descent.",
        "strength":   "Barbell reverse lunge and Bulgarian split squat at 75–85% are genuine strength movements. The posterior chain drives the return. The front foot stays planted through the full rep.",
        "hypertrophy":"Walking lunges, dumbbell lunges, and split squat variations accumulate quad and glute volume through range. The hip flexor stretch in the rear position is part of the stimulus.",
        "restoration":"Bodyweight reverse lunge or assisted split squat. Single-leg hip stability with no load. The pattern is maintained, not developed.",
    },
    "leg-isolation": {
        "foundation": "Isolation exercises at foundation load establish the muscle-mind connection. Quad extensions, hamstring curls, and calf raises need to be felt — not just performed.",
        "strength":   "Leg press and hack squat at 75–85% qualify as strength work in the leg isolation context. Standard isolation machines peak at 3/5 difficulty regardless of load.",
        "hypertrophy":"Full range of motion through calf raises, leg curls, and leg extensions. The stretch reflex at the bottom of leg press and leg extension drives hypertrophy. Controlled tempo, no bouncing.",
        "restoration":"Light leg curl, light calf raise, or unloaded ankle mobility work. The knee extensors and flexors benefit from circulation at restoration intensity.",
    },
    "carry": {
        "foundation": "The loaded carry teaches bracing under ambulation. Foundation load: rib cage down, shoulders packed, gait uncompromised. The weight is light enough to maintain form for the full distance.",
        "strength":   "Farmer's carry and yoke carry at near-maximal loads are strength events. The goal is not conditioning — it is spinal loading under locomotion. Short distances, heavy loads, full recovery.",
        "hypertrophy":"Loaded carries at moderate weight for longer distances accumulate trap, grip, and core stimulus. The suitcase carry biases quadratus lumborum. The overhead carry biases thoracic stability.",
        "restoration":"Light suitcase carry or unloaded plate pinch. Restoration carries are grip and gait maintenance, not development.",
    },
    "anti-rotation": {
        "foundation": "The anti-rotation pattern is always a stability event. Foundation load: learn to resist, not to produce. Pallof press, landmine anti-rotation, and bird-dog are all pattern-acquisition tools here.",
        "strength":   "Rotational strength does not follow standard loading protocols cleanly. At strength intent, anti-rotation work becomes harder variation selection — longer levers, less stability, higher load.",
        "hypertrophy":"Core hypertrophy through anti-rotation is a secondary outcome. The obliques and quadratus lumborum adapt through repeated stabilization. Higher reps and accumulated sets drive this.",
        "restoration":"Dead bug, bird-dog, and supine anti-rotation holds. Restoration anti-rotation work is parasympathetic-compatible and appropriate for every session.",
    },
    "core-stability": {
        "foundation": "Bracing mechanics are the lesson. Foundation load in core-stability work is often bodyweight. The goal is teaching the nervous system to generate intra-abdominal pressure on demand.",
        "strength":   "Weighted core stability — heavy rollouts, loaded planks, or cable anti-rotation with added load — extends the core stability pattern into strength territory. Limited exercises qualify.",
        "hypertrophy":"Core exercises at 8–15 rep ranges with intentional time under tension produce endurance-hypertrophy. The deep core structures respond to duration, not load.",
        "restoration":"Diaphragmatic breathing, supine dead bug, and child's pose spinal decompression. Restoration core work is nervous system regulation, not muscular development.",
    },
    "olympic": {
        "foundation": "Olympic lifts at foundation load are technique drills. 65% or below means the bar speed is deliberate, not explosive. The catch position is the lesson — not the pull.",
        "strength":   "Olympic lifts are power-strength movements. The strength zone (75–85%) is where bar speed and position integrity are both present. This is competition-adjacent training.",
        "hypertrophy":"Olympic lifts are not hypertrophy tools. If this exercise appears in a 🦋 context, it is serving a power-endurance or conditioning function, not structural adaptation.",
        "restoration":"Olympic lifts do not belong in 🖼 Restoration. Substitute a hip-hinge or vertical pull variation for the same muscle groups.",
    },
    "plyometric": {
        "foundation": "Plyometrics at foundation intent are jumping and landing mechanics. Stick the landing, stabilize, reset. Load is absent or minimal. The goal is ground contact quality and joint position.",
        "strength":   "Plyometric work in a strength context means max-effort single-rep jumps, depth jumps, or bounds with full recovery between reps. Not conditioning. Not circuits. One effort. Full rest.",
        "hypertrophy":"Plyometrics do not produce direct hypertrophy. In a hypertrophy context, they serve as CNS primers between loaded sets or as volume-based conditioning accessories.",
        "restoration":"Plyometrics do not belong in 🖼 Restoration. Substitute a leg-isolation or mobility exercise for the same muscle groups.",
    },
    "conditioning": {
        "foundation": "Conditioning at foundation load is aerobic base development. Zone 2 — the pace you can hold for 30+ minutes while still holding a conversation. Not recovery, not intensity. Base.",
        "strength":   "Conditioning does not follow strength periodization cleanly. In a strength block, conditioning volume is reduced. Short, intense conditioning work (sprints, ergometer intervals) preserves capacity without adding fatigue.",
        "hypertrophy":"Conditioning in a hypertrophy block serves recovery and metabolic health. Steady-state aerobic work 2–3x/week at ≤70% HR max does not interfere with hypertrophy when kept below 30 minutes.",
        "restoration":"Steady-state low-intensity aerobic work is the primary content of 🖼 Restoration conditioning. The heart rate stays below zone 2. The purpose is tissue perfusion and parasympathetic activation.",
    },
}

# Fallback for any pattern not in templates
ORDER_TEMPLATES_DEFAULT: dict[str, str] = {
    "foundation": "Foundation load establishes the movement pattern. Sub-65% means the quality of each rep is the metric — not the weight.",
    "strength":   "At 75–85%, this movement becomes a force-production event. Full setup before each rep. Full rest between sets.",
    "hypertrophy":"Accumulated volume with controlled tempo. The stimulus is mechanical tension through a full range of motion.",
    "restoration":"At restoration intensity (≤55%), this exercise serves circulation and maintenance. It should leave the joints better than it found them.",
}

COLOR_TEMPLATES: dict[str, dict[str, str]] = {
    "hip-hinge": {
        "technical":"Lower volume, longer rest, spotter or camera for form review. Every rep is a recorded event. The technical lens demands lockout position be perfect before adding load.",
        "intense":  "Deadlift clusters, rest-pause sets, or heavy RDL dropsets. High mechanical demand combined with reduced rest — used sparingly. The hip-hinge earns intensity cautiously.",
        "mindful":  "4-second eccentric on every rep. The bar moves down with control, not gravity. Breath pattern: brace on the descent, exhale through the extension. The hamstring load is the cue.",
    },
    "squat": {
        "technical":"Tempo squats, pause squats, or single-leg progressions. The technical lens strips load and demands position. Every deviation is information.",
        "intense":  "Drop sets, cluster sets, or squat supersets (squat → leg press → hack squat). The quad accumulates work across multiple angles with reduced rest.",
        "mindful":  "4-second descent, 2-second pause at the bottom, controlled rise. Breath pattern: brace before descent, exhale past parallel. The hip crease below parallel is the cue.",
    },
    "horizontal-press": {
        "technical":"Paused press, tempo press, or board press. The technical lens exposes bar path deviation. Quality is the only metric.",
        "intense":  "Bench press supersets or tri-sets (flat → incline → cable fly). High volume, reduced rest, accumulated chest work across three planes.",
        "mindful":  "4-second eccentric to the chest. The bar does not bounce. Exhale on the press. Feel the pec stretch at the bottom — that stretch is the point.",
    },
    "vertical-press": {
        "technical":"Strict press with submaximal load. No leg drive. The technical standard here is ears through the arms at lockout. Anything less is a partial rep.",
        "intense":  "Press superset with lateral raise or face pull. Shoulder volume accumulated across planes with reduced rest.",
        "mindful":  "4-second eccentric from lockout to rack position. Exhale on the press. The shoulder joint is stacked — the wrist is over the elbow is over the shoulder.",
    },
    "horizontal-pull": {
        "technical":"Pause at full contraction. Hold the blade together for 1 second at the top of every rep. The technical lens exposes retraction quality.",
        "intense":  "Row superset with face pull or rear delt fly. Posterior shoulder volume accumulated across angles.",
        "mindful":  "4-second eccentric to full dead-hang or full cable stretch. Exhale on the pull. Feel the scapula move before the arm.",
    },
    "vertical-pull": {
        "technical":"Dead-hang start. Full lockout extension before the next rep. The technical standard: the lat must engage before the elbow bends.",
        "intense":  "Pull-up cluster sets or lat pulldown drop sets. Accumulate vertical pull volume with reduced rest.",
        "mindful":  "4-second descent to full dead hang. No kipping. No swinging. Exhale on the pull. The lat drives — not the bicep.",
    },
    "isolation-curl": {
        "technical":"Strict supination. Elbow stays pinned. The weight is secondary to the quality of the curl path.",
        "intense":  "Bicep superset: incline curl into preacher curl into standing curl. Three angles, minimal rest, full pump.",
        "mindful":  "4-second eccentric from peak contraction to full extension. Pause at the bottom before the next rep. Exhale on the curl.",
    },
    "isolation-extension": {
        "technical":"Full lockout on every rep. No partial reps. The technical standard: elbow position does not change, only the forearm moves.",
        "intense":  "Tricep tri-set: overhead extension into pressdown into dip. High volume, reduced rest, accumulated tricep work.",
        "mindful":  "4-second eccentric from lockout to full stretch position. Exhale on the extension. The elbow joint stays stable.",
    },
    "default": {
        "technical":"Lower volume, longer rest, quality over speed. The technical lens means every rep is examined and every deviation is corrected.",
        "intense":  "Higher volume, reduced rest, possible supersets. The intensity lens means accumulating work — not just completing it.",
        "mindful":  "4-second eccentric phase. Deliberate breathing. Extended rest. The mindful lens turns outward effort inward.",
    },
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[''`]", "", s)
    s = re.sub(r"[()[\]{}]", "", s)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def type_dir(scl_types: list) -> str:
    t = (scl_types[0] if scl_types else "plus").lower()
    return t


def output_filename(ex: dict, primary_slug_ids: dict[tuple[str, str], str]) -> str:
    """
    Return deterministic filename for an exercise.

    Most exercises map to {slug}.md. If multiple exercise IDs share the same
    type+slug pair, keep the first ID on the canonical slug and suffix all
    subsequent IDs with their EX number to guarantee one file per exercise.
    """
    tdir = type_dir(ex.get("scl_types", ["plus"]))
    slug = slugify(ex["name"])
    key = (tdir, slug)

    if primary_slug_ids.get(key) == ex["exercise_id"]:
        return f"{slug}.md"

    ex_num = ex["exercise_id"].split("-")[-1]
    return f"{slug}-ex{ex_num}.md"


def format_list(items: list, default: str = "—") -> str:
    if not items:
        return default
    return ", ".join(items)


MAJOR_PATTERNS = set(ORDER_TEMPLATES.keys())


def resolve_template_pattern(ex: dict) -> str:
    """
    Resolve the best template pattern for an exercise.
    If movement_pattern is 'core-stability' (the catch-all) but family_id
    is a known major pattern, prefer the family_id for richer templates.
    """
    pattern = ex.get("movement_pattern", "core-stability")
    family_id = ex.get("family_id", "")
    if pattern == "core-stability" and family_id in MAJOR_PATTERNS and family_id != "core-stability":
        return family_id
    return pattern


def get_order_text(pattern: str, order_key: str) -> str:
    tmpl = ORDER_TEMPLATES.get(pattern, {})
    if order_key in tmpl:
        return tmpl[order_key]
    return ORDER_TEMPLATES_DEFAULT.get(order_key, "")


def get_color_text(pattern: str, color_key: str) -> str:
    tmpl = COLOR_TEMPLATES.get(pattern, COLOR_TEMPLATES["default"])
    return tmpl.get(color_key, COLOR_TEMPLATES["default"].get(color_key, ""))


def build_coaching_notes(ex: dict) -> str:
    """Generate a PPL± voice coaching paragraph."""
    name = ex["name"]
    pattern = ex.get("movement_pattern", "core-stability")
    role = ex.get("family_role", "unlinked")
    fid = ex.get("family_id", pattern)
    gold = ex.get("gold_gated", False)
    compound = ex.get("compound", False)
    bilateral = ex.get("bilateral", True)

    lines = []

    if gold:
        lines.append(f"{name} is a GOLD-gated exercise — available only under 🟣 Technical or 🔴 Intense colors. This is a gate for experience and context, not elitism.")

    if role == "root":
        lines.append(f"This is the root of the {fid.replace('-', ' ')} family. Other exercises in this family are measured against it.")
    elif role == "progression":
        lines.append(f"A progression within the {fid.replace('-', ' ')} family — harder than the root, higher transfer requirements.")
    elif role == "regression":
        lines.append(f"A regression within the {fid.replace('-', ' ')} family — accessible entry point for those building toward the root pattern.")
    elif role == "equipment-swap":
        lines.append(f"An equipment-swap variant within the {fid.replace('-', ' ')} family — same mechanics, different implement.")

    if compound and not bilateral:
        lines.append("Unilateral compound work. Side-to-side asymmetry will be exposed here — that is the point, not a problem.")
    elif not compound:
        lines.append("Isolation work. The goal is accumulated tension in the target muscle — not global strength development.")

    # Pattern-specific closing
    pattern_notes = {
        "hip-hinge":       "The hinge is non-negotiable infrastructure. Every athlete benefits from a well-grooved deadlift pattern regardless of their primary sport.",
        "squat":           "The squat is the most contested movement in strength training. Every variation has a rationale. Know which one applies to this session.",
        "horizontal-press":"The press is as much a shoulder exercise as a chest exercise. The shoulder position matters more than the load.",
        "vertical-press":  "Overhead strength is a shoulder health indicator. Stiffness in the overhead position is a mobility gap, not a strength gap.",
        "horizontal-pull": "The row is the counterpart to the press. The horizontal pulling:pressing ratio is a shoulder health metric.",
        "vertical-pull":   "The vertical pull is the measure of body ownership. The ability to move one's own weight is not optional.",
        "isolation-curl":  "The curl is not vanity work — it is elbow flexor health maintenance for anyone who rows, pulls, or carries.",
        "isolation-extension":"The tricep is 2/3 of upper arm mass. Isolation extension work maintains elbow health and pressing strength.",
        "lunge":           "The single-leg pattern exposes what bilateral work hides. Asymmetry here is real, not relative.",
        "core-stability":  "Core stability work is the foundation that makes everything else transferable. No ceiling on value here.",
        "conditioning":    "Conditioning is infrastructure. A strong, poorly conditioned athlete is a timed release mechanism for injury.",
        "olympic":         "Olympic lifts require technical preparation. These are not exercises to stumble into under fatigue.",
        "plyometric":      "Plyometrics are CNS work. Landing quality defines the rep, not the height or distance of the jump.",
        "carry":           "Loaded carries are the most underused tool in training. The body integrating strength through locomotion.",
        "anti-rotation":   "Anti-rotation is what the spine does during every compound lift. Training it directly is maintenance, not specialty work.",
        "leg-isolation":   "Isolation work in the legs addresses the gaps that compound movements miss — the knee, ankle, and hip isolation angles.",
    }
    note = pattern_notes.get(pattern, "This exercise earns its place through honest mechanical demand and clear training transfer.")
    lines.append(note)

    return " ".join(lines)


def build_setup_cues(ex: dict) -> list[str]:
    """Generate setup cues based on movement pattern and equipment."""
    name = ex["name"]
    pattern = ex.get("movement_pattern", "core-stability")
    equip = ex.get("equipment") or []
    bilateral = ex.get("bilateral", True)

    cues = {
        "hip-hinge": [
            "Set the bar at mid-shin or pick up the implement from the floor.",
            "Push hips back until hamstrings load — shins vertical or slightly forward.",
            "Chest up, eyes neutral, lats braced against the ribcage.",
            "Take a full breath into the belly — 360-degree expansion before the pull.",
        ],
        "squat": [
            "Bar position: high bar below traps or low bar across rear delts (barbell variations).",
            "Foot width at hip to shoulder width, toes out 15–30°.",
            "Brace: ribcage down, core pressurized — like absorbing a punch.",
            "Unrack with purpose: step back in 2–3 steps, feet set before descent.",
        ],
        "horizontal-press": [
            "Shoulders retracted and depressed against the pad — create tension before you touch the bar.",
            "5-point contact: feet on floor, glutes on pad, upper back on pad, head on pad.",
            "Grip just outside shoulder width (flat press) or shoulder width (close grip).",
            "Air in before unrack. Hold through the descent.",
        ],
        "vertical-press": [
            "Grip just outside shoulder width — bar rests on the heels of the hand, not the palm.",
            "Elbows slightly in front of the bar — not flared wide.",
            "Create full-body tension: glutes, quads, core all engaged.",
            "Bar path: chin back on the press up, chin through at lockout.",
        ],
        "horizontal-pull": [
            "Chest to the pad or overhand grip engaged before initiating the pull.",
            "Shoulders down and back before the elbow bends.",
            "Core braced — the torso does not rotate.",
            "Dead stop or controlled stretch at the bottom on each rep.",
        ],
        "vertical-pull": [
            "Grip slightly wider than shoulder width, hands pronated or neutral.",
            "Arms fully extended, shoulders elevated — start from a dead hang.",
            "Depress the scapulae before the first movement — lat engagement before arm pull.",
            "Look forward, not up — cervical spine neutral.",
        ],
        "isolation-curl": [
            "Upper arms pinned to the torso — they do not move.",
            "Grip the handle or bar with a supinated (underhand) grip.",
            "Stand tall or seated with core braced.",
            "Full extension at the bottom before each rep.",
        ],
        "isolation-extension": [
            "Upper arms stay vertical or slightly back — elbows do not flare.",
            "Full extension at lockout before the eccentric.",
            "Grip the bar or handle with hands shoulder-width or narrower.",
            "Core braced throughout — no lower back compensation.",
        ],
        "lunge": [
            "Step forward (or back) to a distance where the front shin stays vertical or close.",
            "Rear knee tracks down — not crashing into the floor.",
            "Torso upright — do not lean forward over the lead leg.",
            "Full foot contact on the front foot through the push-back.",
        ],
        "core-stability": [
            "Find neutral spine — not flat back, not excessive arch.",
            "360-degree brace: belly out, back wide, pelvic floor engaged.",
            "Shoulders packed and away from the ears.",
            "Breath: in through the nose, brace, move. Exhale on the effort or hold.",
        ],
        "olympic": [
            "Hook grip if load allows — thumb wrapped under the fingers.",
            "Starting position: bar over mid-foot, hips above knees, shoulders over bar.",
            "Lats on, shoulders forward of the bar — no slack in the system.",
            "Feet at hip width, toes out slightly — receiving position matches jumping stance.",
        ],
        "plyometric": [
            "Landing position first: athletic stance, knees soft, hips back.",
            "No twisting or buckling at the knee on landing.",
            "Full reset between reps for max-effort plyometrics.",
            "Soft landing: ball of foot first, heel absorbs, hips sink.",
        ],
        "conditioning": [
            "Set target pace or intensity zone before starting.",
            "Posture check: upright, relaxed grip, rhythmic breathing.",
            "Heart rate monitor optional but useful for zone-based work.",
            "Water and clock in view.",
        ],
        "carry": [
            "Load the implement and check grip before lifting.",
            "Standing tall: ribs down, shoulders packed, hips under.",
            "Gait is the exercise — do not waddle or lean.",
            "Eyes forward, not down.",
        ],
        "anti-rotation": [
            "Cable or band at mid-torso height for Pallof variations.",
            "Stance shoulder-width, knees soft, hips square to the anchor.",
            "The movement is pressing away and returning — the spine does not move.",
            "Exhale during the press-away. The core is the movement, not the arms.",
        ],
        "leg-isolation": [
            "Seat position: thigh pad just above the knee (leg extension) or ankle pad just above heel (leg curl).",
            "No grip death: hands rest lightly on handles.",
            "Full range available: do not limit ROM artificially.",
            "Slow enough to feel the target muscle — not just moving the weight.",
        ],
    }

    base = cues.get(pattern, [
        "Set position before adding load.",
        "Brace the core before each rep.",
        "Full range of motion on every rep.",
        "Rest between sets as prescribed.",
    ])

    # Add bilateral modifier if unilateral
    if not bilateral and "Unilateral" not in base[0]:
        base = [f"Unilateral: complete all reps on one side before switching."] + base

    return base[:6]


def build_execution_cues(ex: dict) -> list[str]:
    """Generate execution cues based on movement pattern."""
    pattern = ex.get("movement_pattern", "core-stability")

    cues = {
        "hip-hinge": [
            "Drive the floor away — not pull the bar up.",
            "Hips and shoulders rise at the same rate out of the bottom.",
            "Lockout: glutes squeeze, hips through, ribs down.",
            "Eccentric: hinge first, then bend the knees as bar passes them.",
            "Control the descent — do not drop the weight.",
        ],
        "squat": [
            "Break at the hips and knees simultaneously.",
            "Knees track the toes — not caving in.",
            "Hip crease below parallel: the standard (unless variation specifies otherwise).",
            "Drive through the whole foot on the ascent — not just the heel.",
            "Lock out at the top: glutes engaged, ribs down.",
        ],
        "horizontal-press": [
            "Bar path slightly diagonal: touch lower chest, press to over the face.",
            "Elbows at 45–75° to the torso — not flared perpendicular.",
            "Touch the chest: controlled, not bounced.",
            "Press through the heel of the hand.",
            "Lockout: elbow slightly soft, not hyperextended.",
        ],
        "vertical-press": [
            "Press in a straight line — bar travels over the head, not forward.",
            "Chin back on the way up, chin through at lockout.",
            "Full lockout: elbow fully extended, shoulder packed.",
            "Eccentric: reverse the path, chin back as bar descends.",
            "Rib cage stays down throughout — no hyperextension.",
        ],
        "horizontal-pull": [
            "Lead with the elbow — not the hand.",
            "Squeeze the shoulder blade at the top of every rep.",
            "Lower the weight under control — the eccentric is half the stimulus.",
            "No torso rocking for momentum.",
            "Full stretch at the bottom: let the shoulder blade move forward.",
        ],
        "vertical-pull": [
            "Initiate with scapular depression — shoulder blades pull down before arms pull.",
            "Chest moves toward the bar — not the bar to the chin.",
            "Elbows drive toward the hips in the bottom position.",
            "Full dead hang between reps (strict style).",
            "Controlled descent — not dropping.",
        ],
        "isolation-curl": [
            "Supinate through the full arc — pinky rotates up at the top.",
            "Peak contraction at the top: hold briefly before lowering.",
            "Slow eccentric: 2–3 seconds down.",
            "Full extension at the bottom without hyperextension.",
            "No swinging — the movement comes from the elbow joint only.",
        ],
        "isolation-extension": [
            "Press to full lockout — do not stop short.",
            "Elbows stay in position throughout.",
            "Slow eccentric: 2–3 seconds of controlled return.",
            "Feel the tricep lengthen on the way down.",
            "No shoulder compensation — only the forearm moves.",
        ],
        "lunge": [
            "Step and sink — hip descends vertically, not forward.",
            "Front shin stays vertical or close to it.",
            "Rear knee almost touches the floor on deep lunges.",
            "Drive through the whole front foot to return.",
            "Stand fully upright at the top of each rep.",
        ],
        "core-stability": [
            "Build pressure before moving — brace first, move second.",
            "Maintain neutral spine throughout — no spinal flexion/extension under load.",
            "Breathe: in through the nose, brace, move. Exhale on the effort.",
            "If position is lost, reset before continuing.",
            "Quality over time: a 20-second perfect plank beats a 60-second sagging one.",
        ],
        "olympic": [
            "First pull: leg press the floor, hips and shoulders rise together.",
            "Second pull: bar at thigh level, aggressive hip extension, shrug.",
            "Third pull (clean/snatch): pull under the bar, meet it in the rack position.",
            "Catch: active, not passive — load the position aggressively.",
            "Stand up fully before resetting.",
        ],
        "plyometric": [
            "Intent drives power: every takeoff is maximal.",
            "Land softly — knees track toes, hips absorb the impact.",
            "Stick the landing for 2 seconds before resetting.",
            "Full extension at takeoff: hips, knees, ankles.",
            "Reset fully between reps for power-focused work.",
        ],
        "conditioning": [
            "Establish pace in the first quarter — do not sprint and fade.",
            "Breathe rhythmically with the movement pattern.",
            "Check form at the halfway point — fatigue degrades mechanics.",
            "Pacing over performance in steady-state work.",
            "Cool-down begins when the target time or distance is reached.",
        ],
        "carry": [
            "Walk at a controlled pace — not shuffling.",
            "Grip does not need to be white-knuckle — firm and relaxed.",
            "Turn with the whole body, not just the upper torso.",
            "Set the load down under control at the end of each pass.",
            "Shake out grip between sets.",
        ],
        "anti-rotation": [
            "Press away from the anchor at a controlled pace.",
            "Hold at full extension for 1–2 seconds.",
            "Return under control — do not let the cable pull you.",
            "The spine does not rotate. That is the entire point.",
            "Exhale on the press. Inhale on the return.",
        ],
        "leg-isolation": [
            "Drive through the full range — full extension on leg extension, full curl on leg curl.",
            "Slow eccentric: 2–3 seconds down.",
            "No bouncing at the end range.",
            "Hold at the peak for 1 second to maximize muscular contraction.",
            "Keep the non-target segments still.",
        ],
    }

    base = cues.get(pattern, [
        "Maintain form from first rep to last.",
        "Controlled concentric and eccentric.",
        "No momentum unless the exercise requires it.",
        "Log the set.",
    ])

    return base[:8]


def build_common_faults(ex: dict) -> list[dict]:
    """Generate common fault/correction pairs."""
    pattern = ex.get("movement_pattern", "core-stability")

    faults = {
        "hip-hinge": [
            {"fault": "Lumbar rounding under load", "correction": "Brace before unracking. If you lose position at the bottom, reduce load until bracing holds."},
            {"fault": "Hips shooting up first out of the bottom", "correction": "Hips and shoulders must rise at the same rate. Think: chest up, hips forward."},
            {"fault": "Bar drifting away from the body", "correction": "Lats on before the pull. The bar stays in contact with or close to the leg."},
            {"fault": "Hyperextension at lockout", "correction": "Glutes squeeze at lockout, not a back arch. Ribs stay down at the top."},
        ],
        "squat": [
            {"fault": "Knee cave on the descent or ascent", "correction": "Drive the knees out actively — cue: spread the floor apart with your feet."},
            {"fault": "Forward lean excessive for the variation", "correction": "Chest up, brace hard. If the lean is structural, ankle mobility is the gap — elevate heels temporarily."},
            {"fault": "Rising on the toes", "correction": "Weight through the whole foot. Cue: feel the heel throughout the movement."},
            {"fault": "Shallow depth", "correction": "Hip crease must reach knee level minimum. Box squats are a training tool for depth awareness."},
        ],
        "horizontal-press": [
            {"fault": "Elbows flaring perpendicular to the torso", "correction": "45–75° is the healthy angle. Flared elbows load the anterior shoulder capsule."},
            {"fault": "Bar bouncing off the chest", "correction": "Touch and go is a technique choice — not a compensation. Control the descent."},
            {"fault": "Wrists breaking back under load", "correction": "Bar in the heel of the hand, not the palm. Thumbs around the bar."},
            {"fault": "Butt coming off the pad", "correction": "Foot position and leg drive may be excessive. Re-establish 5-point contact."},
        ],
        "vertical-press": [
            {"fault": "Pressing forward instead of straight up", "correction": "The bar moves over the head — not in front of it. Pull the chin back to give the bar a clear path."},
            {"fault": "No lockout", "correction": "Full elbow extension at the top. The shoulder stacks under the bar. Incomplete lockout is a partial rep."},
            {"fault": "Lower back arch", "correction": "Rib cage down. Glutes engaged. The trunk is a rigid post, not a ramp."},
        ],
        "horizontal-pull": [
            {"fault": "Pulling with the bicep instead of the back", "correction": "Think: elbow to hip, not hand to chest. The lat drives, the bicep assists."},
            {"fault": "Torso rocking for momentum", "correction": "The torso position is fixed. All movement comes from the shoulder blade and arm."},
            {"fault": "Shrugging the shoulder at the top", "correction": "Shoulder stays depressed. The blade retracts, not elevates."},
        ],
        "vertical-pull": [
            {"fault": "Chin-up instead of chest-up", "correction": "The chest moves toward the bar — not the chin. This changes the shoulder position entirely."},
            {"fault": "Kipping without intent", "correction": "Strict reps first. If kipping is in the plan, it must be controlled and intentional."},
            {"fault": "Partial range of motion", "correction": "Dead hang start is mandatory for lat stimulus. No half reps."},
        ],
        "isolation-curl": [
            {"fault": "Swinging to complete reps", "correction": "Reduce load. The movement comes from the elbow, not the shoulder. Pinned upper arms."},
            {"fault": "No supination at the top", "correction": "The pinky rotates up and in at peak contraction. This is the point of the exercise."},
            {"fault": "Cutting the range short at the bottom", "correction": "Full extension. The bicep must stretch to train its full length."},
        ],
        "isolation-extension": [
            {"fault": "Elbows drifting out and back", "correction": "Upper arm position is fixed. Only the forearm moves."},
            {"fault": "Stopping short of lockout", "correction": "Full extension is the stimulus. Incomplete reps mean the tricep is never fully contracted."},
            {"fault": "Lower back compensation on overhead variations", "correction": "Core braced, rib cage down. If the back arches, the load is too heavy."},
        ],
        "lunge": [
            {"fault": "Front knee past the toes excessively", "correction": "Step length determines shin angle. Longer step = more vertical shin = more glute. Shorter step = more knee forward = more quad."},
            {"fault": "Torso leaning forward", "correction": "Chest up, shoulder stacked over hip. The lean is usually hip flexor tightness — note it."},
            {"fault": "Lateral drift on the return", "correction": "Hip stability is the gap. Single-leg work exposes bilateral imbalances — do not compensate your way through them."},
        ],
        "core-stability": [
            {"fault": "Holding breath instead of bracing", "correction": "Brace first, breathe into the brace. They are separate actions. Holding breath is a Valsalva choice for max effort, not the default."},
            {"fault": "Hips hiking in plank or dead bug", "correction": "Find neutral pelvis first. The low back should have a slight natural curve, not flatten completely."},
            {"fault": "Arms/legs moving before core is set", "correction": "Setup order: position, brace, breathe, move. Never the reverse."},
        ],
        "olympic": [
            {"fault": "Early arm bend in the pull", "correction": "Arms are ropes. They do not bend until the second pull is complete. Early arm bend loses bar speed."},
            {"fault": "Missing the catch position", "correction": "The catch is an active receiving position — not a passive one. Pull yourself under the bar aggressively."},
            {"fault": "Looking down during the lift", "correction": "Eyes forward or slightly up throughout the movement. Looking down breaks the cervical spine position."},
        ],
        "plyometric": [
            {"fault": "Soft landing with knees caving", "correction": "Land with knees tracking toes. Soft landing means controlled absorption, not collapsed joints."},
            {"fault": "No reset between reps on max-effort work", "correction": "Full reset = full power on the next rep. Rebound plyometrics are a different protocol."},
        ],
        "conditioning": [
            {"fault": "Going out too fast", "correction": "First quarter pace should feel sustainable. Fade-out in the second half signals pacing error."},
            {"fault": "Form degradation under fatigue", "correction": "Slow down rather than compromise mechanics. Injury risk spikes when form breaks."},
        ],
        "carry": [
            {"fault": "Leaning away from the load (suitcase carry)", "correction": "Stay upright. The point is to resist the lateral pull, not accommodate it."},
            {"fault": "Short stride, shuffling gait", "correction": "Full stride. Carry weight should not change your normal walking pattern."},
        ],
        "anti-rotation": [
            {"fault": "Rotating the spine to complete the press", "correction": "If the spine rotates, the load is too heavy or the setup is wrong."},
            {"fault": "Pressing with the arms, not resisting with the core", "correction": "Think: the arms follow the core. The core drives — the arms hold the cable."},
        ],
        "leg-isolation": [
            {"fault": "Partial range — not extending fully", "correction": "Full extension is the stimulus for the quad. Half reps train the middle of the range only."},
            {"fault": "Bouncing at end range", "correction": "Control the return. The eccentric is the muscle-building component."},
        ],
    }

    return faults.get(pattern, [
        {"fault": "Reduced range of motion under fatigue", "correction": "Reduce load before reducing range. Partial reps in most movements are not a valid substitution."},
        {"fault": "Rushing between reps", "correction": "Establish position before every rep. Speed is earned through form, not assumed."},
        {"fault": "Breath-holding for non-maximal efforts", "correction": "Breathe with the movement. Brace for effort, release after."},
    ])


def get_family_context(ex: dict, exercises_by_id: dict) -> dict:
    """Get family context: regressions, progressions, swaps."""
    fid = ex.get("family_id", "")
    role = ex.get("family_role", "unlinked")
    parent_id = ex.get("parent_id")
    eid = ex["exercise_id"]

    # Find siblings
    siblings = [e for e in exercises_by_id.values()
                if e["family_id"] == fid and e["exercise_id"] != eid]

    regressions = [e["name"] for e in siblings if e.get("family_role") == "regression"][:3]
    progressions = [e["name"] for e in siblings if e.get("family_role") == "progression"][:3]
    swaps = [e["name"] for e in siblings if e.get("family_role") == "equipment-swap"][:3]

    parent_name = exercises_by_id.get(parent_id, {}).get("name", None) if parent_id else None

    return {
        "family_id": fid,
        "role": role,
        "parent_name": parent_name,
        "regressions": regressions or ["—"],
        "progressions": progressions or ["—"],
        "swaps": swaps or ["—"],
    }


def generate_knowledge_file(ex: dict, exercises_by_id: dict) -> str:
    """Generate the full markdown knowledge file for an exercise."""
    eid = ex["exercise_id"]
    name = ex["name"]
    pattern = resolve_template_pattern(ex)
    scl_types = ex.get("scl_types", ["Plus"])
    ex_type = scl_types[0] if scl_types else "Plus"
    primary_movers = ex.get("primary_movers") or []
    secondary_movers = ex.get("secondary_movers") or []
    joint_actions = ex.get("joint_actions") or []
    gold = ex.get("gold_gated", False)

    setup_cues = build_setup_cues(ex)
    exec_cues = build_execution_cues(ex)
    faults = build_common_faults(ex)
    fam = get_family_context(ex, exercises_by_id)
    coaching = build_coaching_notes(ex)

    # PPL± Context per Order
    found = get_order_text(pattern, "foundation")
    strength = get_order_text(pattern, "strength")
    hyp = get_order_text(pattern, "hypertrophy")
    rest = get_order_text(pattern, "restoration")

    # Color modifiers
    tech = get_color_text(pattern, "technical")
    intense = get_color_text(pattern, "intense")
    mindful = get_color_text(pattern, "mindful")

    # What It Is
    muscle_str = format_list(primary_movers)
    what_it_is = (
        f"{name} is a {pattern.replace('-', ' ')} movement "
        f"that primarily trains {muscle_str}. "
        f"It sits in the {ex_type} type of the SCL system and is classified as "
        f"{'a compound' if ex.get('compound') else 'an isolation'} movement. "
    )
    if gold:
        what_it_is += "This exercise is GOLD-gated: available only under 🟣 Technical and 🔴 Intense colors."

    # Format faults
    faults_md = "\n".join(f"- **{f['fault']}:** {f['correction']}" for f in faults)

    # Format setup/exec
    setup_md = "\n".join(f"- {c}" for c in setup_cues)
    exec_md = "\n".join(f"- {c}" for c in exec_cues)

    # Family section
    parent_line = f"**Parent:** {fam['parent_name']}" if fam['parent_name'] else ""
    fam_section = f"""**Pattern:** {fam['family_id']} | **Role:** {fam['role']}
{parent_line + chr(10) if parent_line else ""}**Regressions:** {', '.join(fam['regressions'])}
**Progressions:** {', '.join(fam['progressions'])}
**Equipment swaps:** {', '.join(fam['swaps'])}""".strip()

    content = f"""---
exercise_id: {eid}
name: {name}
type: {ex_type}
movement_pattern: {pattern}
status: GENERATED
generated: {GENERATED}
---

# {name}

## What It Is

{what_it_is}

## Setup

{setup_md}

## Execution

{exec_md}

## Common Faults

{faults_md}

## What It Trains

**Primary:** {format_list(primary_movers)}
**Secondary:** {format_list(secondary_movers)}
**Joint actions:** {format_list(joint_actions)}

## PPL± Context

**In Foundation (🐂):** {found}

**In Strength (⛽):** {strength}

**In Hypertrophy (🦋):** {hyp}

**In Restoration (🖼):** {rest}

**Color modifiers:**
- Technical (🟣): {tech}
- Intense (🔴): {intense}
- Mindful (⚪): {mindful}

## Family

{fam_section}

## Coaching Notes

{coaching}
"""
    return content


def get_priority_order(exercises: list) -> list:
    """Return exercises ordered: priority list first, then by EX-ID."""
    priority_set = set(PRIORITY_NAMES)
    priority = [e for e in exercises if e["name"] in priority_set]
    rest_sorted = sorted(
        [e for e in exercises if e["name"] not in priority_set],
        key=lambda x: int(x["exercise_id"].split("-")[1])
    )
    return priority + rest_sorted


def build_primary_slug_ids(exercises: list[dict]) -> dict[tuple[str, str], str]:
    """Map each (type, slug) to the first exercise_id that claims it."""
    primary: dict[tuple[str, str], str] = {}
    for ex in sorted(exercises, key=lambda x: int(x["exercise_id"].split("-")[1])):
        key = (type_dir(ex.get("scl_types", ["plus"])), slugify(ex["name"]))
        primary.setdefault(key, ex["exercise_id"])
    return primary


def main():
    parser = argparse.ArgumentParser(description="Generate PPL± exercise knowledge files.")
    parser.add_argument("--exercise", help="Single exercise ID (e.g. EX-0001)")
    parser.add_argument("--section",  help="Source section (e.g. A)")
    parser.add_argument("--type",     help="SCL type (Push/Pull/Legs/Plus/Ultra)")
    parser.add_argument("--batch",    type=int, help="Generate first N exercises")
    parser.add_argument("--priority-first", action="store_true",
                        help="Sort by usage frequency before sequential (default with --batch)")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run",  action="store_true", help="Print paths without writing")
    parser.add_argument("--stats",    action="store_true", help="Print coverage stats and exit")
    args = parser.parse_args()

    # Load registry
    exercises = json.loads(REGISTRY.read_text())
    by_id = {e["exercise_id"]: e for e in exercises}
    primary_slug_ids = build_primary_slug_ids(exercises)

    if args.stats:
        total = len(exercises)
        expected_paths = {
            OUTPUT_DIR / type_dir(ex.get("scl_types", ["plus"])) / output_filename(ex, primary_slug_ids)
            for ex in exercises
        }
        written = sum(1 for p in expected_paths if p.exists())
        print(f"Registry entries: {total}")
        print(f"Files written:    {written}")
        print(f"Coverage:         {written/total*100:.1f}%")
        for t in ["push", "pull", "legs", "plus", "ultra"]:
            d = OUTPUT_DIR / t
            count = sum(1 for p in expected_paths if p.parent == d and p.exists())
            print(f"  {t}/: {count} files")
        return

    # Filter
    target = exercises[:]
    if args.exercise:
        target = [e for e in exercises if e["exercise_id"] == args.exercise]
        if not target:
            print(f"ERROR: {args.exercise} not found in registry.", file=sys.stderr)
            sys.exit(1)
    elif args.section:
        target = [e for e in exercises if e.get("source_section") == args.section.upper()]
    elif args.type:
        target = [e for e in exercises if args.type.capitalize() in (e.get("scl_types") or [])]

    # Priority ordering for batch
    if args.batch or args.priority_first:
        target = get_priority_order(target)

    if args.batch:
        target = target[:args.batch]

    # Generate
    written = skipped = errors = 0
    total_words = 0
    for ex in target:
        tdir = type_dir(ex.get("scl_types", ["plus"]))
        filename = output_filename(ex, primary_slug_ids)
        out_path = OUTPUT_DIR / tdir / filename

        if out_path.exists() and not args.overwrite:
            skipped += 1
            continue

        try:
            content = generate_knowledge_file(ex, by_id)
        except Exception as e:
            print(f"ERROR generating {ex['exercise_id']} {ex['name']}: {e}", file=sys.stderr)
            errors += 1
            continue

        if args.dry_run:
            print(f"[DRY-RUN] {ex['exercise_id']} → {out_path}")
            written += 1
        else:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            word_count = len(content.split())
            total_words += word_count
            print(f"  {ex['exercise_id']} {ex['name']} → {out_path} ({word_count}w)")
            written += 1

    print(f"\nDone. Written: {written} | Skipped: {skipped} | Errors: {errors}")
    if written > 0 and not args.dry_run:
        print(f"Avg words/file: {total_words // max(written, 1)}")


if __name__ == "__main__":
    main()
