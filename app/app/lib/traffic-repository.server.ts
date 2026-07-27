import {
  diagnoseTraffic,
  type TrafficDiagnosticsResult,
} from "@mcfly/mer-core";
import type { SpendChannel } from "@prisma/client";
import prisma from "../db.server";
import type { DateRange } from "./periods";

const CHANNEL_DISPLAY: Record<SpendChannel, string> = {
  meta: "Meta",
  google: "Google",
  other: "Other / Manual",
};

export async function getLinkClicksByChannel(
  shopId: string,
  range: DateRange,
): Promise<{ channel: SpendChannel; clicks: number }[]> {
  const entries = await prisma.linkClickEntry.findMany({
    where: {
      shopId,
      periodStart: { lte: range.end },
      periodEnd: { gte: range.start },
    },
  });

  const totals: Record<SpendChannel, number> = {
    meta: 0,
    google: 0,
    other: 0,
  };

  for (const entry of entries) {
    totals[entry.channel as SpendChannel] += entry.clicks;
  }

  return (["meta", "google", "other"] as const).map((channel) => ({
    channel,
    clicks: totals[channel],
  }));
}

export async function getSessionsTotal(
  shopId: string,
  range: DateRange,
): Promise<number> {
  const entries = await prisma.sessionEntry.findMany({
    where: {
      shopId,
      periodStart: { lte: range.end },
      periodEnd: { gte: range.start },
    },
  });

  return entries.reduce(
    (sum: number, entry: { sessions: number }) => sum + entry.sessions,
    0,
  );
}

export async function buildTrafficDiagnostics(
  shopId: string,
  range: DateRange,
): Promise<TrafficDiagnosticsResult> {
  const [sessions, clicks] = await Promise.all([
    getSessionsTotal(shopId, range),
    getLinkClicksByChannel(shopId, range),
  ]);

  return diagnoseTraffic({
    sessions,
    channels: clicks
      .filter((row) => row.clicks > 0)
      .map((row) => ({
        name: CHANNEL_DISPLAY[row.channel],
        linkClicks: row.clicks,
      })),
  });
}
