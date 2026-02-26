# Exercise Family Trees

Status: DRAFT — Major movement patterns covered. Full family trees for all ~2,185 exercises are a future task.

Movement families group exercises by pattern. The family defines transfer relationships: if you know a user's performance at the root exercise, you can project their likely performance at any variant in the family.

---

## Data Structure

```
Family:
  id:          unique string identifier ("hip-hinge")
  root:        the canonical baseline exercise
  children:    list of exercises with:
                 - parent_id
                 - relationship_type: "variant" | "progression" | "regression" | "equipment-swap"
                 - transfer_ratio: 0.xx (from transfer-ratios.md)
                 - equipment_tier: integer
                 - axis_affinity: {🏛: x, 🔨: x, 🌹: x, 🪐: x, ⌛: x, 🐬: x}
                 - bilateral: true/false
```

---

## Hip Hinge Family

Root: Conventional Barbell Deadlift (equipment tier 3, bilateral, 🏛+8)

```
Conventional Barbell Deadlift [ROOT / T3 / bilateral / 🏛+8 🪐+5]
├─ Romanian Deadlift [variant / T3 / bilateral / 🏛+7 🌹+4] ratio: 0.90
│   ├─ Dumbbell Romanian Deadlift [equipment-swap / T2 / bilateral / 🏛+5 🔨+4] ratio: 0.85
│   └─ Single-Leg Romanian Deadlift [variant / T2 / unilateral / 🔨+8 🌹+5] ratio: 0.70
├─ Sumo Deadlift [variant / T3 / bilateral / 🏛+6 🪐+4] ratio: 0.92
├─ Trap Bar Deadlift [variant / T3 / bilateral / 🏛+5 🔨+5] ratio: 0.95
├─ Hex Bar Deadlift [equipment-swap / T3 / bilateral] ratio: 0.95
├─ Stiff-Leg Deadlift [variant / T3 / bilateral / 🌹+5] ratio: 0.85
├─ Deficit Deadlift [progression / T3 / bilateral / 🪐+7] ratio: 0.80
├─ Rack Pull [variant / T3 / bilateral / 🪐+4] ratio: 1.05 (easier ROM)
├─ Deadlift with Bands [progression / T3 / bilateral / 🪐+6] ratio: 0.90
├─ Dumbbell Deadlift [equipment-swap / T2 / bilateral / 🏛+4 🔨+3] ratio: 0.75
├─ Kettlebell Deadlift [equipment-swap / T2 / bilateral / 🔨+5] ratio: 0.80
└─ Good Morning [variant / T3 / bilateral / 🌹+5 🏛+4] ratio: 0.70
```

---

## Squat Family

Root: Barbell Back Squat (equipment tier 3, bilateral, 🏛+8)

```
Barbell Back Squat [ROOT / T3 / bilateral / 🏛+8 🪐+5]
├─ Barbell Front Squat [variant / T3 / bilateral / 🏛+7 🪐+6] ratio: 0.85
│   └─ Barbell Front Squat with Straps [variant / T3 / bilateral] ratio: 0.85
├─ High-Bar Squat [variant / T3 / bilateral / 🏛+7] ratio: 0.95
├─ Low-Bar Squat [variant / T3 / bilateral / 🏛+7 🔨+3] ratio: 1.00
├─ Safety Bar Squat [equipment-swap / T3 / bilateral / 🏛+5] ratio: 0.92
├─ Box Squat [variant / T3 / bilateral / 🪐+5] ratio: 0.90
├─ Pause Squat [progression / T3 / bilateral / 🪐+7] ratio: 0.80
├─ Squat with Bands [progression / T3 / bilateral / 🪐+6] ratio: 0.88
├─ Dumbbell Goblet Squat [regression / T2 / bilateral / 🏛+4 🔨+4] ratio: 0.65
├─ Dumbbell Squat [equipment-swap / T2 / bilateral / 🔨+4] ratio: 0.70
├─ Kettlebell Goblet Squat [equipment-swap / T2 / bilateral / 🔨+5] ratio: 0.65
├─ Bulgarian Split Squat [variant / T2 / unilateral / 🔨+8 🪐+5] ratio: 0.75
├─ Barbell Bulgarian Split Squat [variant / T3 / unilateral / 🔨+7 🪐+5] ratio: 0.75
├─ Pistol Squat [progression / T0 / unilateral / 🪐+8 🟢+8] ratio: 0.60
├─ Hack Squat [equipment-swap / T4 / bilateral / 🏛+4] ratio: 0.85
└─ Leg Press [equipment-swap / T4 / bilateral / 🏛+3 🌹+4] ratio: 0.80
```

---

## Horizontal Press Family

Root: Barbell Bench Press (equipment tier 3, bilateral, 🏛+8)

```
Barbell Bench Press [ROOT / T3 / bilateral / 🏛+8 🪐+4]
├─ Close-Grip Bench Press [variant / T3 / bilateral / 🏛+7] ratio: 0.85 (triceps shift)
├─ Wide-Grip Bench Press [variant / T3 / bilateral / 🏛+6] ratio: 0.90 (chest shift)
├─ Incline Barbell Bench Press [variant / T3 / bilateral / 🏛+7] ratio: 0.85
├─ Decline Barbell Bench Press [variant / T3 / bilateral / 🏛+6] ratio: 0.88
├─ Pause Bench Press [progression / T3 / bilateral / 🪐+7] ratio: 0.82
├─ Bench with Bands [progression / T3 / bilateral / 🪐+6] ratio: 0.87
├─ Dumbbell Bench Press [equipment-swap / T2 / bilateral / 🏛+5 🔨+4] ratio: 0.80
│   ├─ Incline Dumbbell Press [variant / T2 / bilateral / 🏛+5 🔨+4] ratio: 0.78
│   └─ Decline Dumbbell Press [variant / T2 / bilateral] ratio: 0.78
├─ Dumbbell Flye [variant / T2 / bilateral / 🌹+7] ratio: 0.55 (isolation shift)
├─ Cable Flye [equipment-swap / T4 / bilateral / 🌹+8] ratio: 0.55
├─ Machine Chest Press [equipment-swap / T4 / bilateral / 🌹+5] ratio: 0.80
└─ Push-Up [equipment-swap / T0 / bilateral / 🟢+8 🔨+5] ratio: 0.60
    ├─ Archer Push-Up [progression / T0 / bilateral / 🪐+7] ratio: 0.70
    └─ Weighted Push-Up [progression / T0-1 / bilateral / 🪐+4] ratio: 0.70
```

---

## Vertical Press Family

Root: Barbell Overhead Press (equipment tier 3, bilateral, 🏛+8)

```
Barbell Overhead Press (OHP) [ROOT / T3 / bilateral / 🏛+8 🪐+4]
├─ Seated Barbell OHP [variant / T3 / bilateral / 🏛+6] ratio: 0.93
├─ Barbell Push Press [variant / T3 / bilateral / 🏛+6 🔨+4] ratio: 1.05 (leg drive)
├─ Dumbbell Overhead Press [equipment-swap / T2 / bilateral / 🏛+5 🔨+5] ratio: 0.82
│   ├─ Seated Dumbbell OHP [variant / T2 / bilateral / 🏛+4] ratio: 0.82
│   └─ Arnold Press [variant / T2 / bilateral / 🌹+5] ratio: 0.78
├─ Dumbbell Lateral Raise [variant / T2 / bilateral / 🌹+7] ratio: 0.35 (isolation)
├─ Cable Lateral Raise [equipment-swap / T4 / bilateral / 🌹+8] ratio: 0.35
├─ Machine Shoulder Press [equipment-swap / T4 / bilateral / 🌹+5] ratio: 0.80
├─ Landmine Press [variant / T3 / unilateral / 🔨+6] ratio: 0.75
└─ Single-Arm Dumbbell Press [variant / T2 / unilateral / 🔨+7] ratio: 0.82
```

---

## Horizontal Pull Family

Root: Barbell Bent-Over Row (equipment tier 3, bilateral, 🏛+8)

```
Barbell Bent-Over Row [ROOT / T3 / bilateral / 🏛+8 🪐+4]
├─ Pendlay Row [variant / T3 / bilateral / 🏛+7 🪐+5] ratio: 0.90
├─ Underhand Barbell Row [variant / T3 / bilateral / 🏛+6] ratio: 0.92
├─ Dumbbell Row [equipment-swap / T2 / unilateral / 🔨+7 🏛+5] ratio: 0.85
│   └─ Chest-Supported Dumbbell Row [variant / T2 / bilateral / 🌹+4] ratio: 0.85
├─ Cable Row [equipment-swap / T4 / bilateral / 🌹+6 🏛+4] ratio: 0.78
│   ├─ Single-Arm Cable Row [variant / T4 / unilateral / 🔨+6 🌹+5] ratio: 0.78
│   └─ Face Pull [variant / T4 / bilateral / 🌹+7] ratio: 0.45 (rear delt isolation)
├─ Machine Row [equipment-swap / T4 / bilateral / 🌹+5] ratio: 0.78
├─ Meadows Row [variant / T3 / unilateral / 🔨+6 🏛+4] ratio: 0.82
└─ Inverted Row [equipment-swap / T0 / bilateral / 🟢+6 🔨+5] ratio: 0.60
```

---

## Vertical Pull Family

Root: Weighted Pull-Up (equipment tier 2–3, bilateral, 🏛+7)

```
Weighted Pull-Up [ROOT / T2-3 / bilateral / 🏛+7 🪐+6]
├─ Pull-Up (bodyweight) [regression / T0 / bilateral / 🟢+7 🏛+6] ratio: 1.00 (reference)
│   ├─ Chin-Up [variant / T0 / bilateral / 🏛+6] ratio: 1.05 (biceps assist)
│   ├─ Wide-Grip Pull-Up [variant / T0 / bilateral / 🏛+6 🌹+4] ratio: 0.92
│   ├─ Neutral-Grip Pull-Up [variant / T0 / bilateral] ratio: 1.00
│   └─ Archer Pull-Up [progression / T0 / bilateral / 🪐+7] ratio: 0.80
├─ Assisted Pull-Up [regression / T4 / bilateral] ratio: varies (bodyweight reduction)
├─ Lat Pulldown [equipment-swap / T4 / bilateral / 🏛+4 🌹+5] ratio: 0.85
│   ├─ Wide-Grip Lat Pulldown [variant / T4 / bilateral / 🏛+4] ratio: 0.85
│   ├─ Close-Grip Lat Pulldown [variant / T4 / bilateral / 🌹+4] ratio: 0.85
│   └─ Single-Arm Lat Pulldown [variant / T4 / unilateral / 🔨+5] ratio: 0.82
└─ Band Pull-Down [regression / T1 / bilateral / 🟢+4] ratio: 0.55
```

---

## Isolation Curl Family (Biceps)

Root: Barbell Curl (equipment tier 3, bilateral, 🏛+5)

```
Barbell Curl [ROOT / T3 / bilateral / 🏛+5 🌹+5]
├─ EZ-Bar Curl [variant / T3 / bilateral / 🏛+5] ratio: 0.95 (wrist comfort)
├─ Dumbbell Curl [equipment-swap / T2 / bilateral / 🌹+6 🔨+3] ratio: 0.88
│   ├─ Hammer Curl [variant / T2 / bilateral / 🌹+5 🔨+4] ratio: 0.90 (brachialis)
│   ├─ Incline Dumbbell Curl [variant / T2 / bilateral / 🌹+7] ratio: 0.80
│   └─ Concentration Curl [variant / T2 / unilateral / 🌹+8] ratio: 0.75
├─ Cable Curl [equipment-swap / T4 / bilateral / 🌹+7] ratio: 0.85
│   ├─ Cable Hammer Curl [variant / T4 / bilateral / 🌹+6] ratio: 0.85
│   └─ Single-Arm Cable Curl [variant / T4 / unilateral / 🔨+5 🌹+6] ratio: 0.85
├─ Preacher Curl [variant / T4 / bilateral / 🌹+8] ratio: 0.82 (peak isolation)
└─ Machine Curl [equipment-swap / T4 / bilateral / 🌹+7] ratio: 0.80
```

---

## Isolation Extension Family (Triceps)

Root: Close-Grip Bench Press (equipment tier 3, bilateral, 🏛+6)

```
Close-Grip Bench Press [ROOT / T3 / bilateral / 🏛+6 🌹+4]
├─ Skull Crusher [variant / T3 / bilateral / 🌹+6] ratio: 0.75 (isolation shift)
│   ├─ EZ-Bar Skull Crusher [variant / T3 / bilateral / 🌹+6] ratio: 0.75
│   └─ Dumbbell Skull Crusher [equipment-swap / T2 / bilateral / 🌹+6] ratio: 0.72
├─ Tricep Pushdown [equipment-swap / T4 / bilateral / 🌹+7] ratio: 0.65
│   ├─ Rope Pushdown [variant / T4 / bilateral / 🌹+8] ratio: 0.65
│   └─ Single-Arm Pushdown [variant / T4 / unilateral / 🔨+4 🌹+7] ratio: 0.63
├─ Overhead Tricep Extension [variant / T2 / bilateral / 🌹+7] ratio: 0.68
│   ├─ Dumbbell Overhead Extension [equipment-swap / T2 / bilateral] ratio: 0.68
│   └─ Cable Overhead Extension [equipment-swap / T4 / bilateral / 🌹+7] ratio: 0.68
├─ Diamond Push-Up [equipment-swap / T0 / bilateral / 🟢+5 🌹+4] ratio: 0.55
└─ Dips [variant / T0-3 / bilateral / 🏛+5 🟢+4] ratio: 0.80
    └─ Weighted Dips [progression / T2-3 / bilateral / 🪐+4] ratio: 0.90
```

---

## Notes on Transfer Ratios

Transfer ratios in this document are first-pass estimates based on movement biomechanics and established exercise science conventions. They will be refined in future sessions as the transfer-ratios.md specification matures and empirical data from user ledgers becomes available.

See `transfer-ratios.md` for the complete specification of ratio types and derivation methodology.

The complete family trees for all 2,185 exercises in the library is a future task. This document establishes the format and populates the most important families for the initial procedural engine build.

---

🧮
