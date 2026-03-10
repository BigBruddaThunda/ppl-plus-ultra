import type { Metadata } from "next";
import { Inter, JetBrains_Mono } from "next/font/google";
import { HomeButton } from "@/components/nav/HomeButton";
import "./globals.css";

const inter = Inter({
  variable: "--font-body",
  subsets: ["latin"],
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "PPL± | 1,680 Rooms",
  description: "Semantic training language. 61 emojis. 1,680 workouts.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} ${jetbrainsMono.variable} antialiased`}>
        {children}
        <HomeButton />
      </body>
    </html>
  );
}
