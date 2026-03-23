import type { Metadata } from "next";
import localFont from "next/font/local";
import { HomeButton } from "@/components/nav/HomeButton";
import "./globals.css";

const inter = localFont({
  src: [
    { path: "./fonts/inter-var.woff2", style: "normal" },
  ],
  variable: "--font-body",
  display: "swap",
  fallback: ["system-ui", "-apple-system", "Segoe UI", "Roboto", "Helvetica Neue", "sans-serif"],
});

const mono = localFont({
  src: [
    { path: "./fonts/jetbrains-mono-var.woff2", style: "normal" },
  ],
  variable: "--font-mono",
  display: "swap",
  fallback: ["Menlo", "Consolas", "Monaco", "Liberation Mono", "monospace"],
});

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
      <body className={`${inter.variable} ${mono.variable} antialiased`}>
        {children}
        <HomeButton />
      </body>
    </html>
  );
}
