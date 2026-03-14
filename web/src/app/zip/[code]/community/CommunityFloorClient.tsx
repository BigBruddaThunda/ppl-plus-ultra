"use client";

import { CommunityFeed } from "@/components/community/CommunityFeed";

interface Props {
  zipCode: string;
  userTier: number;
  userId: string;
}

export function CommunityFloorClient({ zipCode, userTier, userId }: Props) {
  return (
    <CommunityFeed
      zipCode={zipCode}
      userTier={userTier}
      userId={userId}
    />
  );
}
