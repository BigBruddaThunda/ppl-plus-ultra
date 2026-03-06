#!/usr/bin/env python3
"""
build-exercise-registry.py — CX-36: Exercise Identity Registry

Reads middle-math/exercise-library.json (2,085 exercises, per-section sequential IDs)
and produces middle-math/exercise-registry.json with:
  - Globally unique IDs: EX-0001 through EX-2085
  - Standardized movement patterns (16-pattern vocabulary from template-spec.md)
  - Inferred anatomy: primary/secondary/stabilizer movers + joint actions
  - Family linkage (8 explicit families + pattern-grouped families for rest)
  - Axis affinity and Order affinity scores (octave scale -8 to +8)
  - Equipment list (inferred from name + tier)
  - Knowledge file path (exercise-content/{type}/{slug}.md)
  - External ref dock (null — populated by CX-39 pipeline)
  - Status: REGISTERED

Usage:
  python scripts/build-exercise-registry.py
  python scripts/build-exercise-registry.py --stats
  python scripts/build-exercise-registry.py --validate
  python scripts/build-exercise-registry.py --dry-run
"""

import argparse
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).parent.parent
SOURCE_PATH = REPO_ROOT / "middle-math" / "exercise-library.json"
OUTPUT_PATH = REPO_ROOT / "middle-math" / "exercise-registry.json"

# ─────────────────────────────────────────────────────────────────────────────
# PATTERN MAP — source movement_pattern → standardized 16-pattern vocabulary
# ─────────────────────────────────────────────────────────────────────────────
PATTERN_MAP: dict = {
    "Hip Hinge": "hip-hinge", "Squat": "squat", "Lunge": "lunge",
    "Horizontal Press": "horizontal-press", "Vertical Press": "vertical-press",
    "Horizontal Pull": "horizontal-pull", "Vertical Pull": "vertical-pull",
    "Isolation Curl": "isolation-curl", "Isolation Extension": "isolation-extension",
    "Leg Isolation": "leg-isolation", "Carry": "carry", "Anti-Rotation": "anti-rotation",
    "Core Stability": "core-stability", "Olympic": "olympic",
    "Conditioning": "conditioning", "Plyometric": "plyometric",
    "Neck Flexion": "core-stability", "Neck Extension": "core-stability",
    "Neck Lateral Flexion": "core-stability", "Neck Rotation": "core-stability",
    "Neck Isometric": "core-stability", "Cervical Flexion": "core-stability",
    "Cervical Extension": "core-stability",
    "Lateral Raise": "vertical-press", "Front Raise": "vertical-press",
    "Shoulder Rotation": "anti-rotation", "Shoulder Flexion": "vertical-press",
    "Rear Delt": "horizontal-pull", "Rear Delt Fly": "horizontal-pull",
    "Shrug": "vertical-pull", "Upright Row": "vertical-pull",
    "Face Pull": "horizontal-pull",
    "Chest Fly": "horizontal-press", "Chest Flye": "horizontal-press",
    "Chest Isolation": "horizontal-press", "Cable Fly": "horizontal-press",
    "Cable Flye": "horizontal-press", "Pullover": "vertical-pull",
    "Hip Extension": "hip-hinge", "Back Extension": "hip-hinge",
    "Glute Bridge": "hip-hinge", "Hip Thrust": "hip-hinge",
    "Superman": "core-stability", "Hyperextension": "hip-hinge",
    "Wrist Curl": "isolation-curl", "Wrist Extension": "isolation-extension",
    "Forearm Rotation": "anti-rotation", "Forearm Curl": "isolation-curl",
    "Hammer Curl": "isolation-curl", "Preacher Curl": "isolation-curl",
    "Concentration Curl": "isolation-curl", "Tricep Extension": "isolation-extension",
    "Tricep Kickback": "isolation-extension", "Tricep Pushdown": "isolation-extension",
    "Dips": "isolation-extension", "Push-Down": "isolation-extension",
    "Overhead Extension": "isolation-extension",
    "Crunch": "core-stability", "Sit-Up": "core-stability",
    "Leg Raise": "core-stability", "Plank": "core-stability",
    "Hollow Hold": "core-stability", "Dead Bug": "core-stability",
    "Bird Dog": "core-stability", "V-Up": "core-stability",
    "Russian Twist": "anti-rotation", "Pallof Press": "anti-rotation",
    "Landmine Rotation": "anti-rotation", "Woodchop": "anti-rotation",
    "Side Bend": "anti-rotation", "Ab Wheel": "core-stability",
    "Rollout": "core-stability", "Mountain Climber": "core-stability",
    "Hip Abduction": "leg-isolation", "Hip Adduction": "leg-isolation",
    "Clamshell": "leg-isolation", "Donkey Kick": "leg-isolation",
    "Fire Hydrant": "leg-isolation", "Monster Walk": "leg-isolation",
    "Glute Kickback": "leg-isolation",
    "Calf Raise": "leg-isolation", "Tibialis Raise": "leg-isolation",
    "Step-Up": "lunge", "Split Squat": "lunge",
    "Bulgarian Split Squat": "lunge", "Leg Press": "squat",
    "Hack Squat": "squat", "Leg Curl": "leg-isolation",
    "Leg Extension": "leg-isolation", "Nordic Curl": "leg-isolation",
    "Hamstring Curl": "leg-isolation", "Seated Leg Curl": "leg-isolation",
    "Clean": "olympic", "Snatch": "olympic", "Jerk": "olympic",
    "Power Clean": "olympic", "Power Snatch": "olympic",
    "Hang Clean": "olympic", "Hang Snatch": "olympic",
    "Clean and Jerk": "olympic", "Push Jerk": "olympic", "Split Jerk": "olympic",
    "Jump": "plyometric", "Box Jump": "plyometric", "Broad Jump": "plyometric",
    "Depth Jump": "plyometric", "Bound": "plyometric", "Hop": "plyometric",
    "Jump Squat": "plyometric", "Tuck Jump": "plyometric",
    "Kettlebell Swing": "hip-hinge", "Turkish Get-Up": "anti-rotation",
    "Kettlebell Clean": "olympic", "Kettlebell Snatch": "olympic",
    "Kettlebell Press": "vertical-press", "Kettlebell Row": "horizontal-pull",
    "Kettlebell Carry": "carry", "Windmill": "anti-rotation",
    "Steady State": "conditioning", "Interval": "conditioning",
    "HIIT": "conditioning", "Running": "conditioning",
    "Cycling": "conditioning", "Rowing": "conditioning",
    "Swimming": "conditioning", "Jump Rope": "conditioning",
    "Sprint": "conditioning", "Bike": "conditioning",
    "Stone Lift": "olympic", "Tire Flip": "olympic",
    "Atlas Stone": "olympic", "Yoke Walk": "carry",
    "Sled Push": "conditioning", "Sled Pull": "conditioning",
    "Log Press": "vertical-press", "Axle Press": "vertical-press",
    "Sandbag Carry": "carry", "Farmer's Walk": "carry", "Farmers Walk": "carry",
    "Agility": "conditioning", "Ladder Drill": "conditioning",
    "Cone Drill": "conditioning", "Footwork": "conditioning",
    "Shuffle": "conditioning", "Throwing": "anti-rotation",
    "Medicine Ball": "anti-rotation", "Rotational": "anti-rotation",
    "Stretch": "core-stability", "Mobility": "core-stability",
    "Flexibility": "core-stability", "Foam Roll": "core-stability",
    "SMR": "core-stability", "Isometric": "core-stability",
    "Balance": "core-stability", "Coordination": "core-stability",
    "Cat-Cow": "core-stability", "Hip Circle": "core-stability",
    "Shoulder CAR": "core-stability", "Hip CAR": "core-stability",
}

PATTERN_KEYWORDS: dict = {
    "hip-hinge": ["hinge", "deadlift", "rdl", "good morning", "back extension",
                  "hip thrust", "glute bridge", "hyperextension", "swing", "stiff-leg"],
    "squat": ["squat", "leg press", "hack squat"],
    "lunge": ["lunge", "split squat", "step-up", "step up", "walking lunge",
              "reverse lunge", "lateral lunge", "curtsy"],
    "horizontal-press": ["bench press", "push-up", "pushup", "chest press",
                         "flye", "fly", "pec deck"],
    "vertical-press": ["overhead press", "shoulder press", "lateral raise",
                       "front raise", "arnold press", "push press", "ohp",
                       "log press", "axle press", "military press"],
    "horizontal-pull": ["row", "face pull", "pull-apart", "band pull"],
    "vertical-pull": ["pull-up", "pullup", "chin-up", "chinup", "lat pulldown",
                      "pulldown", "pull down", "shrug"],
    "isolation-curl": ["curl", "hammer curl"],
    "isolation-extension": ["tricep", "skull crusher", "pushdown", "push-down",
                             "dips", "kickback", "overhead extension"],
    "leg-isolation": ["leg curl", "leg extension", "calf raise", "tibialis",
                      "hip abduction", "hip adduction", "clamshell",
                      "donkey kick", "glute kickback", "nordic"],
    "carry": ["carry", "farmer", "suitcase", "rack walk", "yoke", "loaded walk"],
    "anti-rotation": ["pallof", "rotation", "woodchop", "wood chop", "twist",
                      "chop", "landmine rotation", "anti-rotation", "side bend",
                      "windmill", "turkish"],
    "core-stability": ["plank", "hollow", "dead bug", "bird dog", "sit-up",
                       "crunch", "rollout", "ab wheel", "neck", "cervical",
                       "mountain climber", "flutter kick", "leg raise",
                       "cat-cow", "car", "mobility", "stretch", "foam",
                       "bear crawl", "superman", "world's greatest"],
    "olympic": ["clean", "snatch", "jerk", "stone", "tire flip", "atlas"],
    "conditioning": ["run", "sprint", "bike", "cycle", "swim", "jump rope",
                     "sled", "agility", "footwork", "drill", "treadmill",
                     "rowing machine", "assault bike", "rower", "hiit",
                     "interval", "steady state", "walk"],
    "plyometric": ["box jump", "broad jump", "bound", "hop", "depth jump",
                   "jump squat", "tuck jump", "plyometric"],
}

# ─────────────────────────────────────────────────────────────────────────────
# ANATOMY DATABASE
# ─────────────────────────────────────────────────────────────────────────────
ANATOMY_BY_PATTERN: dict = {
    "hip-hinge": {
        "primary_movers": ["hamstrings", "gluteus_maximus", "erector_spinae"],
        "secondary_movers": ["adductors", "quadratus_lumborum", "gluteus_medius"],
        "stabilizers": ["core", "latissimus_dorsi", "trapezius_upper", "rhomboids"],
        "joint_actions": ["hip_extension", "knee_flexion_isometric", "spinal_extension"],
    },
    "squat": {
        "primary_movers": ["quadriceps", "gluteus_maximus"],
        "secondary_movers": ["hamstrings", "adductors", "gluteus_medius"],
        "stabilizers": ["erector_spinae", "core", "gastrocnemius"],
        "joint_actions": ["knee_extension", "hip_extension", "ankle_dorsiflexion"],
    },
    "lunge": {
        "primary_movers": ["quadriceps", "gluteus_maximus"],
        "secondary_movers": ["hamstrings", "gluteus_medius", "adductors"],
        "stabilizers": ["core", "erector_spinae", "tibialis_anterior"],
        "joint_actions": ["knee_extension", "hip_extension", "hip_flexion"],
    },
    "horizontal-press": {
        "primary_movers": ["pectoralis_major"],
        "secondary_movers": ["anterior_deltoid", "triceps_brachii"],
        "stabilizers": ["rotator_cuff", "serratus_anterior", "core"],
        "joint_actions": ["shoulder_horizontal_adduction", "elbow_extension"],
    },
    "vertical-press": {
        "primary_movers": ["deltoids_anterior", "deltoids_lateral"],
        "secondary_movers": ["triceps_brachii", "upper_trapezius"],
        "stabilizers": ["rotator_cuff", "serratus_anterior", "core"],
        "joint_actions": ["shoulder_flexion", "elbow_extension", "shoulder_abduction"],
    },
    "horizontal-pull": {
        "primary_movers": ["latissimus_dorsi", "rhomboids", "trapezius_middle"],
        "secondary_movers": ["biceps_brachii", "rear_deltoid", "teres_major"],
        "stabilizers": ["rotator_cuff", "core", "erector_spinae"],
        "joint_actions": ["shoulder_horizontal_abduction", "elbow_flexion", "scapular_retraction"],
    },
    "vertical-pull": {
        "primary_movers": ["latissimus_dorsi"],
        "secondary_movers": ["biceps_brachii", "rear_deltoid", "rhomboids", "teres_major"],
        "stabilizers": ["rotator_cuff", "core", "trapezius_lower"],
        "joint_actions": ["shoulder_adduction", "elbow_flexion", "scapular_depression"],
    },
    "isolation-curl": {
        "primary_movers": ["biceps_brachii"],
        "secondary_movers": ["brachialis", "brachioradialis"],
        "stabilizers": ["core", "rotator_cuff"],
        "joint_actions": ["elbow_flexion", "forearm_supination"],
    },
    "isolation-extension": {
        "primary_movers": ["triceps_brachii"],
        "secondary_movers": ["anconeus"],
        "stabilizers": ["core", "rotator_cuff", "anterior_deltoid"],
        "joint_actions": ["elbow_extension"],
    },
    "leg-isolation": {
        "primary_movers": ["quadriceps"],
        "secondary_movers": ["hamstrings", "gastrocnemius"],
        "stabilizers": ["core", "gluteus_medius"],
        "joint_actions": ["knee_extension", "knee_flexion"],
    },
    "carry": {
        "primary_movers": ["trapezius", "core", "gluteus_maximus"],
        "secondary_movers": ["quadriceps", "hamstrings", "forearm_flexors"],
        "stabilizers": ["erector_spinae", "gluteus_medius", "rotator_cuff"],
        "joint_actions": ["hip_extension", "knee_extension", "scapular_depression"],
    },
    "anti-rotation": {
        "primary_movers": ["core", "obliques"],
        "secondary_movers": ["gluteus_maximus", "hip_flexors"],
        "stabilizers": ["erector_spinae", "transversus_abdominis", "multifidus"],
        "joint_actions": ["spinal_rotation", "anti_rotation", "hip_stabilization"],
    },
    "core-stability": {
        "primary_movers": ["core", "transversus_abdominis", "rectus_abdominis"],
        "secondary_movers": ["obliques", "erector_spinae", "hip_flexors"],
        "stabilizers": ["multifidus", "quadratus_lumborum", "diaphragm"],
        "joint_actions": ["spinal_flexion", "spinal_stabilization", "intra_abdominal_pressure"],
    },
    "olympic": {
        "primary_movers": ["quadriceps", "gluteus_maximus", "hamstrings", "trapezius"],
        "secondary_movers": ["deltoids", "triceps_brachii", "gastrocnemius"],
        "stabilizers": ["core", "erector_spinae", "rotator_cuff"],
        "joint_actions": ["hip_extension", "knee_extension", "ankle_plantarflexion", "shoulder_flexion"],
    },
    "conditioning": {
        "primary_movers": ["quadriceps", "hamstrings", "gluteus_maximus"],
        "secondary_movers": ["gastrocnemius", "core", "hip_flexors"],
        "stabilizers": ["erector_spinae", "tibialis_anterior", "gluteus_medius"],
        "joint_actions": ["hip_extension", "knee_extension", "ankle_plantarflexion"],
    },
    "plyometric": {
        "primary_movers": ["quadriceps", "gluteus_maximus", "gastrocnemius"],
        "secondary_movers": ["hamstrings", "hip_flexors"],
        "stabilizers": ["core", "erector_spinae", "tibialis_anterior"],
        "joint_actions": ["hip_extension", "knee_extension", "ankle_plantarflexion"],
    },
}

SECTION_ANATOMY_OVERRIDES: dict = {
    "HEAD & NECK": {
        "primary_movers": ["sternocleidomastoid", "scalenes", "splenius_capitis", "suboccipitals"],
        "secondary_movers": ["upper_trapezius", "levator_scapulae"],
        "stabilizers": ["deep_cervical_flexors", "multifidus"],
        "joint_actions": ["cervical_flexion", "cervical_extension", "cervical_rotation", "cervical_lateral_flexion"],
    },
    "FOREARMS & WRISTS": {
        "primary_movers": ["forearm_flexors", "forearm_extensors"],
        "secondary_movers": ["brachioradialis", "pronator_teres"],
        "stabilizers": ["biceps_brachii", "triceps_brachii"],
        "joint_actions": ["wrist_flexion", "wrist_extension", "forearm_pronation", "forearm_supination"],
    },
    "LOWER LEG & FOOT": {
        "primary_movers": ["gastrocnemius", "soleus"],
        "secondary_movers": ["tibialis_anterior", "peroneus_longus"],
        "stabilizers": ["flexor_digitorum_longus", "tibialis_posterior"],
        "joint_actions": ["ankle_plantarflexion", "ankle_dorsiflexion", "ankle_inversion", "ankle_eversion"],
    },
}

LEG_ISO_REFINEMENTS: list = [
    ("leg curl", {"primary_movers": ["hamstrings"], "secondary_movers": ["gastrocnemius"], "joint_actions": ["knee_flexion"]}),
    ("nordic", {"primary_movers": ["hamstrings"], "secondary_movers": ["gastrocnemius"], "joint_actions": ["knee_flexion"]}),
    ("leg extension", {"primary_movers": ["quadriceps"], "secondary_movers": [], "joint_actions": ["knee_extension"]}),
    ("calf raise", {"primary_movers": ["gastrocnemius", "soleus"], "secondary_movers": ["tibialis_posterior"], "joint_actions": ["ankle_plantarflexion"]}),
    ("tibialis", {"primary_movers": ["tibialis_anterior"], "secondary_movers": [], "joint_actions": ["ankle_dorsiflexion"]}),
    ("hip abduction", {"primary_movers": ["gluteus_medius", "gluteus_minimus", "tensor_fasciae_latae"], "secondary_movers": ["gluteus_maximus"], "joint_actions": ["hip_abduction"]}),
    ("hip adduction", {"primary_movers": ["adductors", "gracilis"], "secondary_movers": ["pectineus"], "joint_actions": ["hip_adduction"]}),
    ("glute bridge", {"primary_movers": ["gluteus_maximus", "hamstrings"], "secondary_movers": ["gluteus_medius"], "joint_actions": ["hip_extension"]}),
    ("hip thrust", {"primary_movers": ["gluteus_maximus"], "secondary_movers": ["hamstrings", "quadriceps"], "joint_actions": ["hip_extension"]}),
    ("clamshell", {"primary_movers": ["gluteus_medius", "gluteus_minimus"], "secondary_movers": ["hip_external_rotators"], "joint_actions": ["hip_external_rotation", "hip_abduction"]}),
    ("donkey kick", {"primary_movers": ["gluteus_maximus"], "secondary_movers": ["hamstrings"], "joint_actions": ["hip_extension"]}),
    ("fire hydrant", {"primary_movers": ["gluteus_medius", "tensor_fasciae_latae"], "secondary_movers": [], "joint_actions": ["hip_abduction", "hip_external_rotation"]}),
]

NECK_REFINEMENTS: list = [
    ("flexion", {"joint_actions": ["cervical_flexion"], "primary_movers": ["sternocleidomastoid", "scalenes", "deep_cervical_flexors"]}),
    ("extension", {"joint_actions": ["cervical_extension"], "primary_movers": ["splenius_capitis", "semispinalis_capitis", "upper_trapezius"]}),
    ("lateral", {"joint_actions": ["cervical_lateral_flexion"], "primary_movers": ["sternocleidomastoid", "scalenes", "splenius_cervicis"]}),
    ("rotation", {"joint_actions": ["cervical_rotation"], "primary_movers": ["sternocleidomastoid", "splenius_capitis", "obliquus_capitis"]}),
]

# ─────────────────────────────────────────────────────────────────────────────
# FAMILY TREE MEMBERS
# ─────────────────────────────────────────────────────────────────────────────
def _fam(family, role, parent=None, ratio=None):
    return {"family": family, "role": role, "parent": parent, "ratio": ratio}

FAMILY_MEMBERS: dict = {
    "conventional barbell deadlift": _fam("hip-hinge", "root", ratio=1.0),
    "deadlift (conventional)": _fam("hip-hinge", "root", ratio=1.0),
    "deadlift": _fam("hip-hinge", "root", ratio=1.0),
    "romanian deadlift (rdl)": _fam("hip-hinge", "variant", "deadlift", 0.90),
    "romanian deadlift": _fam("hip-hinge", "variant", "deadlift", 0.90),
    "single-leg romanian deadlift": _fam("hip-hinge", "variant", "romanian deadlift", 0.70),
    "dumbbell romanian deadlift": _fam("hip-hinge", "equipment-swap", "romanian deadlift", 0.85),
    "sumo deadlift": _fam("hip-hinge", "variant", "deadlift", 0.92),
    "trap bar deadlift": _fam("hip-hinge", "variant", "deadlift", 0.95),
    "hex bar deadlift": _fam("hip-hinge", "equipment-swap", "deadlift", 0.95),
    "stiff-leg deadlift": _fam("hip-hinge", "variant", "deadlift", 0.85),
    "deficit deadlift": _fam("hip-hinge", "progression", "deadlift", 0.80),
    "rack pull": _fam("hip-hinge", "variant", "deadlift", 1.05),
    "dumbbell deadlift": _fam("hip-hinge", "equipment-swap", "deadlift", 0.75),
    "kettlebell deadlift": _fam("hip-hinge", "equipment-swap", "deadlift", 0.80),
    "good morning": _fam("hip-hinge", "variant", "deadlift", 0.70),
    "barbell back squat": _fam("squat", "root", ratio=1.0),
    "barbell front squat": _fam("squat", "variant", "barbell back squat", 0.85),
    "high-bar squat": _fam("squat", "variant", "barbell back squat", 0.95),
    "low-bar squat": _fam("squat", "variant", "barbell back squat", 1.00),
    "safety bar squat": _fam("squat", "equipment-swap", "barbell back squat", 0.92),
    "box squat": _fam("squat", "variant", "barbell back squat", 0.90),
    "pause squat": _fam("squat", "progression", "barbell back squat", 0.80),
    "dumbbell goblet squat": _fam("squat", "regression", "barbell back squat", 0.65),
    "goblet squat (dumbbell)": _fam("squat", "regression", "barbell back squat", 0.65),
    "goblet squat": _fam("squat", "regression", "barbell back squat", 0.65),
    "kettlebell goblet squat": _fam("squat", "equipment-swap", "goblet squat", 0.65),
    "bulgarian split squat": _fam("squat", "variant", "barbell back squat", 0.75),
    "weighted bulgarian split squat (dumbbells)": _fam("squat", "variant", "barbell back squat", 0.75),
    "barbell bulgarian split squat": _fam("squat", "variant", "barbell back squat", 0.75),
    "pistol squat": _fam("squat", "progression", "barbell back squat", 0.60),
    "leg press": _fam("squat", "equipment-swap", "barbell back squat", 0.80),
    "barbell bench press": _fam("horizontal-press", "root", ratio=1.0),
    "close-grip bench press": _fam("horizontal-press", "variant", "barbell bench press", 0.85),
    "wide-grip bench press": _fam("horizontal-press", "variant", "barbell bench press", 0.90),
    "incline barbell bench press": _fam("horizontal-press", "variant", "barbell bench press", 0.85),
    "decline barbell bench press": _fam("horizontal-press", "variant", "barbell bench press", 0.88),
    "pause bench press": _fam("horizontal-press", "progression", "barbell bench press", 0.82),
    "dumbbell bench press": _fam("horizontal-press", "equipment-swap", "barbell bench press", 0.80),
    "incline dumbbell press": _fam("horizontal-press", "variant", "dumbbell bench press", 0.78),
    "decline dumbbell press": _fam("horizontal-press", "variant", "dumbbell bench press", 0.78),
    "dumbbell flye": _fam("horizontal-press", "variant", "barbell bench press", 0.55),
    "cable flye": _fam("horizontal-press", "equipment-swap", "dumbbell flye", 0.55),
    "cable fly": _fam("horizontal-press", "equipment-swap", "dumbbell flye", 0.55),
    "machine chest press": _fam("horizontal-press", "equipment-swap", "barbell bench press", 0.80),
    "push-up": _fam("horizontal-press", "equipment-swap", "barbell bench press", 0.60),
    "scapular push-up": _fam("horizontal-press", "regression", "push-up", 0.40),
    "archer push-up": _fam("horizontal-press", "progression", "push-up", 0.70),
    "weighted push-up": _fam("horizontal-press", "progression", "push-up", 0.70),
    "barbell overhead press (standing)": _fam("vertical-press", "root", ratio=1.0),
    "barbell overhead press": _fam("vertical-press", "root", ratio=1.0),
    "overhead press (barbell)": _fam("vertical-press", "root", ratio=1.0),
    "seated barbell overhead press": _fam("vertical-press", "variant", "barbell overhead press", 0.93),
    "barbell push press": _fam("vertical-press", "variant", "barbell overhead press", 1.05),
    "dumbbell overhead press": _fam("vertical-press", "equipment-swap", "barbell overhead press", 0.82),
    "seated dumbbell overhead press": _fam("vertical-press", "variant", "dumbbell overhead press", 0.82),
    "arnold press": _fam("vertical-press", "variant", "dumbbell overhead press", 0.78),
    "dumbbell lateral raise": _fam("vertical-press", "variant", "barbell overhead press", 0.35),
    "cable lateral raise": _fam("vertical-press", "equipment-swap", "dumbbell lateral raise", 0.35),
    "machine shoulder press": _fam("vertical-press", "equipment-swap", "barbell overhead press", 0.80),
    "landmine press": _fam("vertical-press", "variant", "barbell overhead press", 0.75),
    "single-arm dumbbell press": _fam("vertical-press", "variant", "dumbbell overhead press", 0.82),
    "barbell bent-over row": _fam("horizontal-pull", "root", ratio=1.0),
    "pendlay row": _fam("horizontal-pull", "variant", "barbell bent-over row", 0.90),
    "underhand barbell row": _fam("horizontal-pull", "variant", "barbell bent-over row", 0.92),
    "dumbbell row": _fam("horizontal-pull", "equipment-swap", "barbell bent-over row", 0.85),
    "single-arm dumbbell row": _fam("horizontal-pull", "variant", "dumbbell row", 0.85),
    "chest-supported dumbbell row": _fam("horizontal-pull", "variant", "dumbbell row", 0.85),
    "cable row": _fam("horizontal-pull", "equipment-swap", "barbell bent-over row", 0.78),
    "cable seated row": _fam("horizontal-pull", "equipment-swap", "barbell bent-over row", 0.78),
    "single-arm cable row": _fam("horizontal-pull", "variant", "cable row", 0.78),
    "face pull": _fam("horizontal-pull", "variant", "cable row", 0.45),
    "machine row": _fam("horizontal-pull", "equipment-swap", "barbell bent-over row", 0.78),
    "meadows row": _fam("horizontal-pull", "variant", "barbell bent-over row", 0.82),
    "inverted row": _fam("horizontal-pull", "equipment-swap", "barbell bent-over row", 0.60),
    "t-bar row": _fam("horizontal-pull", "variant", "barbell bent-over row", 0.88),
    "weighted pull-up": _fam("vertical-pull", "root", ratio=1.0),
    "pull-up": _fam("vertical-pull", "regression", "weighted pull-up", 1.0),
    "pull-up (bodyweight)": _fam("vertical-pull", "regression", "weighted pull-up", 1.0),
    "chin-up": _fam("vertical-pull", "variant", "pull-up", 1.05),
    "wide-grip pull-up": _fam("vertical-pull", "variant", "pull-up", 0.92),
    "neutral-grip pull-up": _fam("vertical-pull", "variant", "pull-up", 1.00),
    "archer pull-up": _fam("vertical-pull", "progression", "pull-up", 0.80),
    "scapular pull-up": _fam("vertical-pull", "regression", "pull-up", 0.60),
    "assisted pull-up": _fam("vertical-pull", "regression", "pull-up", 1.20),
    "lat pulldown": _fam("vertical-pull", "equipment-swap", "weighted pull-up", 0.85),
    "wide-grip lat pulldown": _fam("vertical-pull", "variant", "lat pulldown", 0.85),
    "close-grip lat pulldown": _fam("vertical-pull", "variant", "lat pulldown", 0.85),
    "single-arm lat pulldown": _fam("vertical-pull", "variant", "lat pulldown", 0.82),
    "band pull-down": _fam("vertical-pull", "regression", "pull-up", 0.55),
    "band pull-apart": _fam("vertical-pull", "regression", "pull-up", 0.30),
    "barbell curl": _fam("isolation-curl", "root", ratio=1.0),
    "ez-bar curl": _fam("isolation-curl", "variant", "barbell curl", 0.95),
    "dumbbell curl": _fam("isolation-curl", "equipment-swap", "barbell curl", 0.88),
    "hammer curl": _fam("isolation-curl", "variant", "dumbbell curl", 0.90),
    "incline dumbbell curl": _fam("isolation-curl", "variant", "dumbbell curl", 0.80),
    "concentration curl": _fam("isolation-curl", "variant", "dumbbell curl", 0.75),
    "cable curl": _fam("isolation-curl", "equipment-swap", "barbell curl", 0.85),
    "cable hammer curl": _fam("isolation-curl", "variant", "cable curl", 0.85),
    "single-arm cable curl": _fam("isolation-curl", "variant", "cable curl", 0.85),
    "preacher curl": _fam("isolation-curl", "variant", "barbell curl", 0.82),
    "machine curl": _fam("isolation-curl", "equipment-swap", "barbell curl", 0.80),
    "skull crusher": _fam("isolation-extension", "variant", "close-grip bench press", 0.75),
    "ez-bar skull crusher": _fam("isolation-extension", "variant", "skull crusher", 0.75),
    "dumbbell skull crusher": _fam("isolation-extension", "equipment-swap", "skull crusher", 0.72),
    "tricep pushdown": _fam("isolation-extension", "equipment-swap", "close-grip bench press", 0.65),
    "rope pushdown": _fam("isolation-extension", "variant", "tricep pushdown", 0.65),
    "single-arm pushdown": _fam("isolation-extension", "variant", "tricep pushdown", 0.63),
    "overhead tricep extension": _fam("isolation-extension", "variant", "close-grip bench press", 0.68),
    "dumbbell overhead tricep extension": _fam("isolation-extension", "equipment-swap", "overhead tricep extension", 0.68),
    "cable overhead tricep extension": _fam("isolation-extension", "equipment-swap", "overhead tricep extension", 0.68),
    "diamond push-up": _fam("isolation-extension", "equipment-swap", "close-grip bench press", 0.55),
    "dips": _fam("isolation-extension", "variant", "close-grip bench press", 0.80),
    "weighted dips": _fam("isolation-extension", "progression", "dips", 0.90),
    "tricep dips": _fam("isolation-extension", "variant", "close-grip bench press", 0.75),
}

EQUIPMENT_KEYWORDS: list = [
    ("rowing machine", ["rowing_machine"]),
    ("assault bike", ["assault_bike"]),
    ("resistance band", ["band"]),
    ("trap bar", ["trap_bar"]),
    ("hex bar", ["trap_bar"]),
    ("safety bar", ["safety_bar"]),
    ("ez-bar", ["ez_bar"]),
    ("ez bar", ["ez_bar"]),
    ("pull-up bar", ["pull_up_bar"]),
    ("foam roll", ["foam_roller"]),
    ("treadmill", ["treadmill"]),
    ("kettlebell", ["kettlebell"]),
    ("dumbbell", ["dumbbell"]),
    ("barbell", ["barbell"]),
    ("cable", ["cable"]),
    ("machine", ["machine"]),
    ("band", ["band"]),
    ("trx", ["trx"]),
    ("suspension", ["trx"]),
    ("rings", ["gymnastic_rings"]),
    ("sled", ["sled"]),
    ("plate", ["plate"]),
    ("box", ["box"]),
    ("rower", ["rowing_machine"]),
    ("bike", ["bike"]),
    ("bodyweight", ["bodyweight"]),
]

SPORT_TAGS_BY_PATTERN: dict = {
    "hip-hinge": ["strength_sports", "powerlifting", "team_sports_lower"],
    "squat": ["strength_sports", "powerlifting", "team_sports_lower", "olympic_weightlifting"],
    "lunge": ["team_sports_lower", "sprinting", "general_fitness"],
    "horizontal-press": ["powerlifting", "bodybuilding", "team_sports_upper"],
    "vertical-press": ["powerlifting", "bodybuilding", "team_sports_upper", "throwing"],
    "horizontal-pull": ["bodybuilding", "rowing_sport", "climbing", "team_sports_upper"],
    "vertical-pull": ["bodybuilding", "climbing", "gymnastics", "team_sports_upper"],
    "isolation-curl": ["bodybuilding", "general_fitness"],
    "isolation-extension": ["bodybuilding", "general_fitness"],
    "leg-isolation": ["bodybuilding", "rehabilitation", "general_fitness"],
    "carry": ["strongman", "functional_fitness", "team_sports_lower"],
    "anti-rotation": ["functional_fitness", "wrestling", "martial_arts", "throwing"],
    "core-stability": ["general_fitness", "rehabilitation", "gymnastics"],
    "olympic": ["olympic_weightlifting", "strength_sports", "functional_fitness"],
    "conditioning": ["distance_running", "cycling", "rowing_sport", "general_fitness"],
    "plyometric": ["sprinting", "jumping", "team_sports_lower", "youth_athletics"],
}

VALID_PATTERNS = {
    "hip-hinge", "vertical-pull", "horizontal-pull", "isolation-curl",
    "horizontal-press", "vertical-press", "isolation-extension", "squat",
    "lunge", "leg-isolation", "carry", "anti-rotation", "core-stability",
    "olympic", "conditioning", "plyometric",
}


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def normalize(name: str) -> str:
    return re.sub(r'\s+', ' ', name.lower().strip())

def make_slug(name: str) -> str:
    s = name.lower()
    s = re.sub(r"['\"/\\()\[\]{}]", "", s)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")

def standardize_pattern(raw: str) -> tuple:
    if raw in PATTERN_MAP:
        std = PATTERN_MAP[raw]
        return std, (raw if std != raw else None)
    raw_lower = raw.lower()
    for key, val in PATTERN_MAP.items():
        if key.lower() == raw_lower:
            return val, raw
    for std_pat, keywords in PATTERN_KEYWORDS.items():
        for kw in keywords:
            if kw in raw_lower:
                return std_pat, raw
    return "core-stability", raw

def infer_anatomy(name: str, std_pattern: str, muscle_groups: str) -> dict:
    name_lower = name.lower()
    for section_key, override in SECTION_ANATOMY_OVERRIDES.items():
        if section_key in muscle_groups.upper():
            if section_key == "HEAD & NECK":
                for kw, refinement in NECK_REFINEMENTS:
                    if kw in name_lower:
                        result = dict(override)
                        result.update(refinement)
                        return result
            return dict(override)
    if std_pattern == "leg-isolation":
        base = dict(ANATOMY_BY_PATTERN["leg-isolation"])
        for kw, refinement in LEG_ISO_REFINEMENTS:
            if kw in name_lower:
                base.update(refinement)
                return base
    return dict(ANATOMY_BY_PATTERN.get(std_pattern, ANATOMY_BY_PATTERN["core-stability"]))

def find_family(name: str):
    norm = normalize(name)
    if norm in FAMILY_MEMBERS:
        return FAMILY_MEMBERS[norm]
    for known, info in FAMILY_MEMBERS.items():
        if len(known) >= 8 and known in norm:
            role = info["role"] if info["role"] != "root" else "variant"
            return {**info, "role": role}
    return None

def compute_axis_affinity(entry: dict, std_pattern: str) -> dict:
    compound = entry.get("compound", False)
    bilateral = entry.get("bilateral", True)
    tier_max = entry.get("equipment_tier", [0, 3])[-1]
    gold_gated = entry.get("gold_gated", False)
    axis_emphasis = entry.get("axis_emphasis", [])
    axis_name_map = {"Basics": "classic", "Functional": "functional",
                     "Aesthetic": "aesthetic", "Challenge": "challenge",
                     "Time": "time", "Partner": "partner"}
    scores = {"classic": 0, "functional": 0, "aesthetic": 0, "challenge": 0, "time": 0, "partner": 0}
    for ax in axis_emphasis:
        key = axis_name_map.get(ax)
        if key:
            scores[key] += 3
    if compound and bilateral and tier_max >= 3:
        scores["classic"] += 5
    elif compound and bilateral:
        scores["classic"] += 3
    if not bilateral:
        scores["functional"] += 5
    elif compound:
        scores["functional"] += 2
    if not compound:
        scores["aesthetic"] += 5
    if tier_max >= 4:
        scores["aesthetic"] += 2
    if gold_gated:
        scores["challenge"] = 8
    elif std_pattern in ("olympic", "plyometric"):
        scores["challenge"] += 5
    if std_pattern in ("conditioning", "plyometric"):
        scores["time"] += 5
    scores["partner"] += 2
    return {k: max(-8, min(8, v)) for k, v in scores.items()}

def compute_order_affinity(entry: dict, std_pattern: str) -> dict:
    order_relevance = entry.get("order_relevance", [])
    compound = entry.get("compound", False)
    tier_max = entry.get("equipment_tier", [0, 3])[-1]
    gold_gated = entry.get("gold_gated", False)
    order_key_map = {"Foundation": "foundation", "Strength": "strength",
                     "Hypertrophy": "hypertrophy", "Performance": "performance",
                     "Full Body": "full_body", "Balance": "balance",
                     "Restoration": "restoration"}
    scores = {k: 0 for k in order_key_map.values()}
    for o in order_relevance:
        key = order_key_map.get(o)
        if key:
            scores[key] += 3
    if compound and tier_max >= 3:
        scores["strength"] += 4
        scores["performance"] += 3
        scores["foundation"] += 2
    if not compound:
        scores["hypertrophy"] += 4
        scores["balance"] += 3
    if gold_gated:
        scores["performance"] += 5
    if std_pattern == "conditioning":
        scores["full_body"] += 3
        scores["restoration"] += 2
    if std_pattern == "core-stability":
        scores["restoration"] += 3
        scores["balance"] += 4
    return {k: max(-8, min(8, v)) for k, v in scores.items()}

def infer_equipment(name: str, tier_min: int) -> list:
    name_lower = name.lower()
    found = []
    for keyword, equip in EQUIPMENT_KEYWORDS:
        if keyword in name_lower:
            for e in equip:
                if e not in found:
                    found.append(e)
    if tier_min == 0 and not found:
        found.append("bodyweight")
    return found

def knowledge_file_path(entry: dict) -> str:
    scl_types = entry.get("scl_types", ["Plus"])
    type_dir = scl_types[0].lower() if scl_types else "plus"
    slug = make_slug(entry.get("name", "unknown"))
    return f"exercise-content/{type_dir}/{slug}.md"


# ─────────────────────────────────────────────────────────────────────────────
# BUILD
# ─────────────────────────────────────────────────────────────────────────────

def build_registry() -> list:
    with open(SOURCE_PATH, encoding="utf-8") as f:
        exercises = json.load(f)

    registry = []
    name_to_id = {}

    for global_idx, src in enumerate(exercises, start=1):
        ex_id = f"EX-{global_idx:04d}"
        name = src.get("name", f"Unknown-{global_idx}")
        name_to_id[normalize(name)] = ex_id

        raw_pattern = src.get("movement_pattern", "")
        std_pattern, subpattern = standardize_pattern(raw_pattern)
        muscle_groups = src.get("muscle_groups", "")

        anatomy = infer_anatomy(name, std_pattern, muscle_groups)
        family_info = find_family(name)

        if family_info:
            family_id = family_info["family"]
            family_role = family_info["role"]
            parent_name = family_info.get("parent")
            transfer_ratio = family_info.get("ratio")
        else:
            family_id = std_pattern
            family_role = "unlinked"
            parent_name = None
            transfer_ratio = None

        tier = src.get("equipment_tier", [0, 3])
        tier_min = tier[0] if isinstance(tier, list) and len(tier) >= 1 else 0

        entry = {
            "exercise_id": ex_id,
            "source_id": src.get("id"),
            "source_section": src.get("section"),
            "name": name,
            "canonical_name": name,
            "scl_types": src.get("scl_types", []),
            "order_relevance": src.get("order_relevance", []),
            "axis_emphasis": src.get("axis_emphasis", []),
            "equipment_tier": tier if isinstance(tier, list) else [0, 3],
            "gold_gated": src.get("gold_gated", False),
            "movement_pattern": std_pattern,
            "movement_subpattern": subpattern if subpattern and subpattern != std_pattern else None,
            "muscle_groups": muscle_groups,
            "bilateral": src.get("bilateral", True),
            "compound": src.get("compound", False),
            "primary_movers": anatomy.get("primary_movers", []),
            "secondary_movers": anatomy.get("secondary_movers", []),
            "stabilizers": anatomy.get("stabilizers", []),
            "joint_actions": anatomy.get("joint_actions", []),
            "equipment": infer_equipment(name, tier_min),
            "family_id": family_id,
            "family_role": family_role,
            "_parent_name": parent_name,
            "parent_id": None,
            "transfer_ratio": transfer_ratio,
            "axis_affinity": compute_axis_affinity(src, std_pattern),
            "order_affinity": compute_order_affinity(src, std_pattern),
            "sport_tags": SPORT_TAGS_BY_PATTERN.get(std_pattern, ["general_fitness"]),
            "external_ref": None,
            "knowledge_file": knowledge_file_path(src),
            "status": "REGISTERED",
        }
        registry.append(entry)

    # Second pass: resolve parent names to IDs
    for entry in registry:
        parent_name = entry.pop("_parent_name", None)
        entry["parent_id"] = name_to_id.get(normalize(parent_name)) if parent_name else None

    return registry


# ─────────────────────────────────────────────────────────────────────────────
# STATS & VALIDATION
# ─────────────────────────────────────────────────────────────────────────────

def print_stats(registry: list) -> None:
    total = len(registry)
    type_counts = defaultdict(int)
    section_counts = defaultdict(int)
    pattern_counts = defaultdict(int)
    family_counts = defaultdict(int)

    for e in registry:
        for t in e.get("scl_types", []):
            type_counts[t] += 1
        section_counts[e.get("source_section", "?")] += 1
        pattern_counts[e.get("movement_pattern", "?")] += 1
        family_counts[e.get("family_id", "?")] += 1

    with_primary = sum(1 for e in registry if e.get("primary_movers"))
    explicit_fam = sum(1 for e in registry if e.get("family_role") != "unlinked")

    print(f"\n{'='*52}")
    print(f"Exercise Registry Stats — {total} total")
    print(f"{'='*52}")
    print(f"\nBy SCL Type:")
    for t, c in sorted(type_counts.items()):
        print(f"  {t:15} {c:5d}")
    print(f"\nBy Section ({len(section_counts)} sections):")
    for s, c in sorted(section_counts.items()):
        print(f"  Section {s:3}  {c:5d}")
    print(f"\nBy Movement Pattern:")
    for p, c in sorted(pattern_counts.items(), key=lambda x: -x[1]):
        print(f"  {p:32} {c:5d}")
    print(f"\nFamily Coverage:")
    print(f"  Explicit linkage:    {explicit_fam:5d} / {total} ({100*explicit_fam//total}%)")
    print(f"  Unlinked:            {total - explicit_fam:5d}")
    print(f"\nAnatomy Coverage:")
    print(f"  With primary movers: {with_primary:5d} / {total} ({100*with_primary//total}%)")
    print(f"\nTop 5 Families:")
    for fam, cnt in sorted(family_counts.items(), key=lambda x: -x[1])[:5]:
        print(f"  {fam:32} {cnt:5d}")


def validate_registry(registry: list) -> bool:
    errors = []

    ids = [e["exercise_id"] for e in registry]
    dups = [i for i in set(ids) if ids.count(i) > 1]
    if dups:
        errors.append(f"FAIL: Duplicate IDs: {dups}")
    else:
        print("PASS: No duplicate exercise_id values")

    missing = [e["name"] for e in registry if not e.get("primary_movers")]
    if missing:
        errors.append(f"FAIL: {len(missing)} exercises missing primary_movers")
    else:
        print("PASS: All exercises have primary_movers")

    invalid_pat = [e["name"] for e in registry if e.get("movement_pattern") not in VALID_PATTERNS]
    if invalid_pat:
        errors.append(f"FAIL: {len(invalid_pat)} invalid movement_patterns (first 3: {invalid_pat[:3]})")
    else:
        print("PASS: All movement_patterns in 16-pattern vocabulary")

    no_fam = [e["name"] for e in registry if not e.get("family_id")]
    if no_fam:
        errors.append(f"FAIL: {len(no_fam)} exercises missing family_id")
    else:
        print("PASS: All exercises have family_id")

    first_id = registry[0]["exercise_id"] if registry else None
    last_id = registry[-1]["exercise_id"] if registry else None
    expected_last = f"EX-{len(registry):04d}"
    if first_id != "EX-0001" or last_id != expected_last:
        errors.append(f"FAIL: ID range {first_id}..{last_id}, expected EX-0001..{expected_last}")
    else:
        print(f"PASS: ID range EX-0001 through {expected_last}")

    if errors:
        print()
        for err in errors:
            print(err, file=sys.stderr)
        return False
    print("\nAll validation checks passed.")
    return True


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Build exercise-registry.json (CX-36)")
    parser.add_argument("--stats", action="store_true", help="Print statistics")
    parser.add_argument("--validate", action="store_true", help="Run validation checks")
    parser.add_argument("--dry-run", action="store_true", help="Build without writing output")
    args = parser.parse_args()

    print(f"Reading {SOURCE_PATH} ...")
    registry = build_registry()
    print(f"Built {len(registry)} registry entries.")

    if args.stats:
        print_stats(registry)

    if args.validate:
        print("\n=== Validation ===")
        ok = validate_registry(registry)
        if not ok:
            sys.exit(1)

    if not args.dry_run:
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2, ensure_ascii=False)
        size_kb = OUTPUT_PATH.stat().st_size // 1024
        print(f"\nWrote {OUTPUT_PATH} ({len(registry)} entries, ~{size_kb} KB)")
    else:
        print("Dry run — output not written.")


if __name__ == "__main__":
    main()
