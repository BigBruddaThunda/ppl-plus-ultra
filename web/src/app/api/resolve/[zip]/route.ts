import { resolveZip } from "@/lib/city-compiler";
import { NextResponse } from "next/server";

export async function GET(
  _request: Request,
  { params }: { params: Promise<{ zip: string }> }
) {
  const { zip } = await params;

  // Validate: must be 4-digit numeric zip
  if (!/^\d{4}$/.test(zip)) {
    return NextResponse.json(
      { error: "Invalid zip code. Expected 4-digit numeric code (e.g., 2123)." },
      { status: 400 }
    );
  }

  const compiled = resolveZip(zip);
  if (!compiled) {
    return NextResponse.json(
      { error: `Zip code ${zip} not found.` },
      { status: 404 }
    );
  }

  return NextResponse.json(compiled);
}
