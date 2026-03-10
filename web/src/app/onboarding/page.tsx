"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

const EQUIPMENT_TIERS = [
  { tier: 0, name: "Bodyweight", description: "No equipment. Floor, wall, gravity." },
  { tier: 1, name: "Bands & Sliders", description: "Resistance bands, sliders, foam rollers." },
  { tier: 2, name: "Dumbbells & Kettlebells", description: "Free weights, plates, medicine balls." },
  { tier: 3, name: "Barbell & Rack", description: "Barbell, squat rack, bench." },
  { tier: 4, name: "Machines & Cables", description: "Cable stacks, leg press, lat pulldown." },
  { tier: 5, name: "Specialty", description: "Stones, sleds, GHD, competition equipment." },
];

const REGIONS = [
  "Northeast US",
  "Southeast US",
  "Midwest US",
  "Southwest US",
  "West Coast US",
  "Pacific NW US",
  "Canada",
  "UK & Ireland",
  "Western Europe",
  "Northern Europe",
  "Australia & NZ",
  "Other",
];

export default function OnboardingPage() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [selectedTiers, setSelectedTiers] = useState<number[]>([0]);
  const [region, setRegion] = useState("");
  const [loading, setLoading] = useState(false);

  function toggleTier(tier: number) {
    setSelectedTiers((prev) =>
      prev.includes(tier) ? prev.filter((t) => t !== tier) : [...prev, tier]
    );
  }

  async function handleComplete() {
    setLoading(true);
    const supabase = getSupabaseClient();
    const { data: { user } } = await supabase.auth.getUser();

    if (!user) {
      router.push("/login");
      return;
    }

    // Save equipment tiers
    const equipmentRows = selectedTiers.map((tier) => ({
      user_id: user.id,
      tier,
      available: true,
    }));

    await supabase.from("user_equipment").upsert(equipmentRows, {
      onConflict: "user_id,tier",
    });

    // Update profile
    await supabase
      .from("profiles")
      .update({
        region: region || null,
        onboarding_complete: true,
        updated_at: new Date().toISOString(),
      })
      .eq("id", user.id);

    router.push("/me");
    router.refresh();
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-[var(--ppl-background)]">
      <div className="w-full max-w-md px-6">
        {/* Progress */}
        <div className="mb-8 flex gap-2">
          {[1, 2, 3].map((s) => (
            <div
              key={s}
              className={`h-1 flex-1 rounded-full ${
                s <= step ? "bg-[var(--ppl-accent)]" : "bg-[var(--ppl-border)]"
              }`}
            />
          ))}
        </div>

        {/* Step 1: Equipment */}
        {step === 1 && (
          <div>
            <h1 className="text-2xl font-semibold">Your Equipment</h1>
            <p className="mt-1 text-sm opacity-50">
              Select all equipment tiers you have access to.
            </p>

            <div className="mt-6 space-y-2">
              {EQUIPMENT_TIERS.map((eq) => (
                <button
                  key={eq.tier}
                  onClick={() => toggleTier(eq.tier)}
                  className={`w-full rounded-lg border p-4 text-left transition-colors ${
                    selectedTiers.includes(eq.tier)
                      ? "border-[var(--ppl-accent)] bg-[var(--ppl-surface)]"
                      : "border-[var(--ppl-border)] opacity-60 hover:opacity-100"
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-sm font-medium">
                        Tier {eq.tier}: {eq.name}
                      </p>
                      <p className="mt-0.5 text-xs opacity-50">{eq.description}</p>
                    </div>
                    <div
                      className={`flex h-5 w-5 items-center justify-center rounded border ${
                        selectedTiers.includes(eq.tier)
                          ? "border-[var(--ppl-accent)] bg-[var(--ppl-accent)]"
                          : "border-[var(--ppl-border)]"
                      }`}
                    >
                      {selectedTiers.includes(eq.tier) && (
                        <span className="text-xs text-[var(--ppl-background)]">+</span>
                      )}
                    </div>
                  </div>
                </button>
              ))}
            </div>

            <button
              onClick={() => setStep(2)}
              className="mt-6 w-full rounded-lg bg-[var(--ppl-accent)] px-5 py-2.5 text-sm font-medium text-[var(--ppl-background)]"
            >
              Next
            </button>
          </div>
        )}

        {/* Step 2: Region */}
        {step === 2 && (
          <div>
            <h1 className="text-2xl font-semibold">Region</h1>
            <p className="mt-1 text-sm opacity-50">
              Optional. Used for seasonal content only. No tracking.
            </p>

            <div className="mt-6 space-y-2">
              {REGIONS.map((r) => (
                <button
                  key={r}
                  onClick={() => setRegion(r)}
                  className={`w-full rounded-lg border px-4 py-3 text-left text-sm transition-colors ${
                    region === r
                      ? "border-[var(--ppl-accent)] bg-[var(--ppl-surface)]"
                      : "border-[var(--ppl-border)] opacity-60 hover:opacity-100"
                  }`}
                >
                  {r}
                </button>
              ))}
            </div>

            <div className="mt-6 flex gap-2">
              <button
                onClick={() => setStep(1)}
                className="flex-1 rounded-lg border border-[var(--ppl-border)] px-5 py-2.5 text-sm font-medium opacity-70 hover:opacity-100"
              >
                Back
              </button>
              <button
                onClick={() => setStep(3)}
                className="flex-1 rounded-lg bg-[var(--ppl-accent)] px-5 py-2.5 text-sm font-medium text-[var(--ppl-background)]"
              >
                {region ? "Next" : "Skip"}
              </button>
            </div>
          </div>
        )}

        {/* Step 3: Summary */}
        {step === 3 && (
          <div>
            <h1 className="text-2xl font-semibold">Ready</h1>
            <p className="mt-1 text-sm opacity-50">
              Your profile is set. You can change these anytime in settings.
            </p>

            <div className="mt-6 rounded-xl border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-5">
              <div className="mb-4">
                <p className="text-xs font-medium uppercase tracking-widest opacity-50">
                  Equipment
                </p>
                <div className="mt-2 flex flex-wrap gap-1.5">
                  {selectedTiers.sort().map((t) => (
                    <span
                      key={t}
                      className="rounded-md border border-[var(--ppl-border)] px-2 py-1 text-xs"
                    >
                      Tier {t}: {EQUIPMENT_TIERS[t].name}
                    </span>
                  ))}
                </div>
              </div>
              <div>
                <p className="text-xs font-medium uppercase tracking-widest opacity-50">
                  Region
                </p>
                <p className="mt-1 text-sm">{region || "Not set"}</p>
              </div>
            </div>

            <div className="mt-6 flex gap-2">
              <button
                onClick={() => setStep(2)}
                className="flex-1 rounded-lg border border-[var(--ppl-border)] px-5 py-2.5 text-sm font-medium opacity-70 hover:opacity-100"
              >
                Back
              </button>
              <button
                onClick={handleComplete}
                disabled={loading}
                className="flex-1 rounded-lg bg-[var(--ppl-accent)] px-5 py-2.5 text-sm font-medium text-[var(--ppl-background)] disabled:opacity-50"
              >
                {loading ? "Saving..." : "Enter the Building"}
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
