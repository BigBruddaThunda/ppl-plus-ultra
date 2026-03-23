import type { Metadata } from "next";
import { HomeButton } from "@/components/nav/HomeButton";
import "./globals.css";

export const metadata: Metadata = {
  title: "Ppl± | 1,680 Rooms",
  description: "Semantic training language. 61 emojis. 1,680 workouts.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased" style={{ fontFamily: 'system-ui, -apple-system, "Segoe UI", Roboto, sans-serif' }}>
        {children}
        <HomeButton />
      </body>
    </html>
  );
}
