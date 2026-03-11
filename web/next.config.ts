import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Dynamic routes (/zip/[code]) require server rendering.
  // Static export removed — deploy to Vercel with server functions.

  // Security headers
  headers: async () => [
    {
      source: "/(.*)",
      headers: [
        { key: "X-Frame-Options", value: "DENY" },
        { key: "X-Content-Type-Options", value: "nosniff" },
        { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
        { key: "Permissions-Policy", value: "camera=(), microphone=(self), geolocation=()" },
      ],
    },
    {
      // Cache compiled JSON card data aggressively
      source: "/api/resolve/:path*",
      headers: [
        { key: "Cache-Control", value: "public, s-maxage=86400, stale-while-revalidate=604800" },
      ],
    },
  ],
};

export default nextConfig;
