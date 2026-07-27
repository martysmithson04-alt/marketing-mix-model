import type { ActionFunctionArgs, LoaderFunctionArgs } from "react-router";
import {
  PostTrafficBodySchema,
  TrafficQuerySchema,
} from "@mcfly/api-contract";
import prisma from "../db.server";
import { authenticateApiRequest, jsonError } from "../lib/api-auth.server";
import { ensureShop } from "../lib/mer-dashboard.server";
import { buildTrafficDiagnostics } from "../lib/traffic-repository.server";

function dayBounds(date: string): { start: Date; end: Date } {
  const [y, m, d] = date.split("-").map(Number);
  return {
    start: new Date(y, m - 1, d),
    end: new Date(y, m - 1, d, 23, 59, 59, 999),
  };
}

function mapChannel(channel: string) {
  const normalized = channel.toLowerCase();
  if (normalized.includes("meta") || normalized.includes("facebook")) {
    return "meta" as const;
  }
  if (normalized.includes("google")) return "google" as const;
  return "other" as const;
}

export const loader = async ({ request }: LoaderFunctionArgs) => {
  const auth = await authenticateApiRequest(request);
  if (!auth.ok) {
    return jsonError(auth.message, auth.status);
  }

  const url = new URL(request.url);
  const parsed = TrafficQuerySchema.safeParse({
    from: url.searchParams.get("from"),
    to: url.searchParams.get("to"),
  });
  if (!parsed.success) {
    return jsonError(parsed.error.message, 400, "invalid_query");
  }

  const shop = await ensureShop(auth.shopDomain);
  const traffic = await buildTrafficDiagnostics(shop.id, {
    start: new Date(`${parsed.data.from}T00:00:00`),
    end: new Date(`${parsed.data.to}T23:59:59.999`),
    label: `${parsed.data.from} → ${parsed.data.to}`,
  });
  return Response.json({
    from: parsed.data.from,
    to: parsed.data.to,
    ...traffic,
  });
};

export const action = async ({ request }: ActionFunctionArgs) => {
  const auth = await authenticateApiRequest(request);
  if (!auth.ok) {
    return jsonError(auth.message, auth.status);
  }

  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return jsonError("Invalid JSON body", 400);
  }

  const parsed = PostTrafficBodySchema.safeParse(body);
  if (!parsed.success) {
    return jsonError(parsed.error.message, 400, "invalid_body");
  }

  const shop = await ensureShop(auth.shopDomain);
  let acceptedLinkClicks = 0;
  let acceptedSessions = 0;

  for (const entry of parsed.data.linkClicks ?? []) {
    const channel = mapChannel(entry.channel);
    const { start, end } = dayBounds(entry.date);
    await prisma.linkClickEntry.create({
      data: {
        shopId: shop.id,
        channel,
        clicks: entry.clicks,
        periodStart: start,
        periodEnd: end,
        note: "api:link_clicks",
      },
    });
    acceptedLinkClicks += 1;
  }

  for (const entry of parsed.data.sessions ?? []) {
    const { start, end } = dayBounds(entry.date);
    await prisma.sessionEntry.create({
      data: {
        shopId: shop.id,
        sessions: entry.sessions,
        periodStart: start,
        periodEnd: end,
        note: "api:sessions",
      },
    });
    acceptedSessions += 1;
  }

  return Response.json(
    {
      acceptedLinkClicks,
      acceptedSessions,
      shopId: shop.id,
    },
    { status: 201 },
  );
};
