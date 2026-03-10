"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

const EQUIPMENT_TIERS = [
  { tier: 0, name: "Bodyweight" },
  { tier: 1, name: "Bands & Sliders" },
  { tier: 2, name: "Dumbbells & Kettlebells" },
  { tier: 3, name: "Barbell & Rack" },
  { tier: 4, name: "Machines & Cables" },
  { tier: 5, name: "Specialty" },
];

const REGIONS = [
  "Northeast US", "Southeast US", "Midwest US", "Southwest US",
  "West Coast US", "Pacific NW US", "Canada", "UK & Ireland",
  "Western Europe", "Northern Europe", "Australia & NZ", "Other",
];

export default function SettingsPage() {
  const [selectedTiers, setSelectedTiers] = useState<number[]>([]);
  const [region, setRegion] = useState("");
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const supabase = getSupabaseClient();
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) return;

      // Load equipment
      const { data: equipment } = await supabase
        .from("user_equipment")
        .select("tier")
        .eq("user_id", user.id)
        .eq("available", true);

      if (equipment) {
        setSelectedTiers(equipment.map((e: { tier: number }) => e.tier));
      }

      // Load region
      const { data: profile } = await supabase
        .from("profiles")
        .select("region")
        .eq("id", user.id)
        .single();

      if (profile?.region) setRegion(profile.region);
      setLoading(false);
    }
    load();
  }, []);

  function toggleTier(tier: number) {
    setSelectedTiers((prev) =>
      prev.includes(tier) ? prev.filter((t) => t !== tier) : [...prev, tier]
    );
    setSaved(false);
  }

  async function handleSave() {
    setSaving(true);
    const supabase = getSupabaseClient();
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) return;

    // Delete old equipment, insert new
    await supabase.from("user_equipment").delete().eq("user_id", user.id);

    if (selectedTiers.length > 0) {
      await supabase.from("user_equipment").insert(
        selectedTiers.map((tier) => ({
          user_id: user.id,
          tier,
          available: true,
        }))
      );
    }

    // Update region
    await supabase
      .from("profiles")
      .update({ region: region || null, updated_at: new Date().toISOString() })
      .eq("id", user.id);

    setSaving(false);
    setSaved(true);
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-[var(--ppl-background)]">
        <main className="mx-auto max-w-2xl px-6 py-12">
          <p className="text-sm opacity-40">Loading settings...</p>
        </main>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[var(--ppl-background)]">
      <main className="mx-auto max-w-2xl px-6 py-12">
        <div className="mb-2">
          <Link href="/me" className="text-xs opacity-40 hover:opacity-70">
            Dashboard
          </Link>
        </div>

        <header className="mb-8">
          <h1 className="text-2xl font-semibold">Settings</h1>
        </header>

        {/* Equipment */}
        <section className="mb-6 rounded-xl border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-6">
          <p className="text-xs font-medium uppercase tracking-widest opacity-50">
            Equipment Profile
          </p>
          <p className="mt-1 text-sm opacity-50">
            Select all equipment tiers you have access to.
          </p>
          <div className="mt-4 space-y-2">
            {EQUIPMENT_TIERS.map((eq) => (
              <button
                key={eq.tier}
                onClick={() => toggleTier(eq.tier)}
                className={`w-full rounded-lg border px-4 py-3 text-left text-sm transition-colors ${
                  selectedTiers.includes(eq.tier)
                    ? "border-[var(--ppl-accent)] bg-[var(--ppl-background)]"
                    : "border-[var(--ppl-border)] opacity-60 hover:opacity-100"
                }`}
              >
                <span className="font-medium">Tier {eq.tier}:</span> {eq.name}
              </button>
            ))}
          </div>
        </section>

        {/* Region */}
        <section className="mb-6 rounded-xl border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-6">
          <p className="text-xs font-medium uppercase tracking-widest opacity-50">
            Region
          </p>
          <p className="mt-1 text-sm opacity-50">
            Optional. Used for seasonal content only.
          </p>
          <select
            value={region}
            onChange={(e) => { setRegion(e.target.value); setSaved(false); }}
            className="mt-4 w-full rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-background)] px-4 py-2.5 text-sm outline-none focus:border-[var(--ppl-accent)]"
          >
            <option value="">Not set</option>
            {REGIONS.map((r) => (
              <option key={r} value={r}>{r}</option>
            ))}
          </select>
        </section>

        {/* Subscription link */}
        <section className="mb-6 rounded-xl border border-[var(--ppl-border)] p-5">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs font-medium uppercase tracking-widest opacity-50">
                Subscription
              </p>
              <p className="mt-1 text-sm opacity-70">Manage your plan</p>
            </div>
            <Link
              href="/subscribe"
              className="rounded-lg border border-[var(--ppl-accent)] px-4 py-2 text-xs font-medium text-[var(--ppl-accent)]"
            >
              Manage
            </Link>
          </div>
        </section>

        {/* Save */}
        <button
          onClick={handleSave}
          disabled={saving}
          className="w-full rounded-lg bg-[var(--ppl-accent)] px-5 py-2.5 text-sm font-medium text-[var(--ppl-background)] disabled:opacity-50"
        >
          {saving ? "Saving..." : saved ? "Saved" : "Save Changes"}
        </button>
      </main>
    </div>
  );
}
