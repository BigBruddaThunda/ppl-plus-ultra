import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Dynamic routes (/zip/[code]) require server rendering.
  // Static export removed — will deploy to Vercel with server functions.
};

export default nextConfig;
