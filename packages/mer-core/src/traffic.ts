/**
 * Traffic diagnostics from store sessions + paid link clicks.
 *
 * Religion: this is click-share and a rough organic estimate — not path
 * attribution or “who got credit for the sale.”
 *
 * Organic estimate (founder heuristic):
 *   organicSessions ≈ max(0, storeSessions − Σ paid link clicks)
 */

export type TrafficChannelInput = {
  name: string;
  linkClicks: number;
};

export type ClickShareRow = {
  name: string;
  linkClicks: number;
  clickShare: number;
};

export type TrafficDiagnosticsInput = {
  /** Store sessions for the period (Shopify / analytics). */
  sessions: number;
  /** Paid channel link clicks (Ads Manager link clicks, etc.). */
  channels: TrafficChannelInput[];
};

export type TrafficDiagnosticsResult = {
  sessions: number;
  totalPaidLinkClicks: number;
  /** max(0, sessions − totalPaidLinkClicks) */
  estimatedOrganicSessions: number;
  /** organic / sessions when sessions > 0; else null */
  estimatedOrganicShare: number | null;
  /** paid clicks / sessions when sessions > 0; else null (can exceed 1) */
  estimatedPaidShare: number | null;
  /** True when paid link clicks exceed sessions — estimate is floored / weak. */
  paidClicksExceedSessions: boolean;
  clickShare: ClickShareRow[];
  assumptions: string[];
  why: string;
};

function round(value: number, digits = 4): number {
  const factor = 10 ** digits;
  return Math.round(value * factor) / factor;
}

export function sumLinkClicks(channels: TrafficChannelInput[]): number {
  return channels.reduce((sum, channel) => {
    const clicks = Number.isFinite(channel.linkClicks) ? channel.linkClicks : 0;
    return sum + Math.max(0, clicks);
  }, 0);
}

/**
 * Paid click share by channel. Shares sum to 1 when total clicks > 0.
 */
export function computeClickShare(
  channels: TrafficChannelInput[],
): ClickShareRow[] {
  const total = sumLinkClicks(channels);
  return channels.map((channel) => {
    const linkClicks = Math.max(
      0,
      Number.isFinite(channel.linkClicks) ? channel.linkClicks : 0,
    );
    return {
      name: channel.name,
      linkClicks,
      clickShare: total > 0 ? round(linkClicks / total) : 0,
    };
  });
}

/**
 * Estimate organic traffic pressure from sessions minus paid link clicks.
 * Not attribution — an auditable mix heuristic for operators.
 */
export function diagnoseTraffic(
  input: TrafficDiagnosticsInput,
): TrafficDiagnosticsResult {
  const sessions = Math.max(
    0,
    Number.isFinite(input.sessions) ? input.sessions : 0,
  );
  const clickShare = computeClickShare(input.channels);
  const totalPaidLinkClicks = sumLinkClicks(input.channels);
  const paidClicksExceedSessions =
    sessions > 0 && totalPaidLinkClicks > sessions;
  const estimatedOrganicSessions = Math.max(0, sessions - totalPaidLinkClicks);
  const estimatedOrganicShare =
    sessions > 0 ? round(estimatedOrganicSessions / sessions) : null;
  const estimatedPaidShare =
    sessions > 0 ? round(totalPaidLinkClicks / sessions) : null;

  const assumptions = [
    "Organic estimate = store sessions − total paid link clicks (floored at 0).",
    "One link click ≠ one session; multi-click visits and non-click landings make this a directional estimate.",
    "Click share shows where paid clicks came from — not which channel caused the sale.",
  ];

  if (paidClicksExceedSessions) {
    assumptions.push(
      "Paid link clicks exceed sessions for this period — organic estimate floors at 0; treat paid share as overstated vs sessions.",
    );
  }

  let why: string;
  if (sessions <= 0 && totalPaidLinkClicks <= 0) {
    why =
      "Add store sessions and paid link clicks for this period to unlock click share and the organic estimate.";
  } else if (sessions <= 0) {
    why =
      "Paid link clicks are recorded, but store sessions are missing — enter sessions to estimate organic.";
  } else if (totalPaidLinkClicks <= 0) {
    why =
      "Sessions are recorded with no paid link clicks — organic estimate equals all sessions until paid clicks are entered.";
  } else if (paidClicksExceedSessions) {
    why = `Paid link clicks (${totalPaidLinkClicks}) exceed sessions (${sessions}). Organic estimate floors at 0; use click share for mix, not as a hard session split.`;
  } else {
    const organicPct =
      estimatedOrganicShare !== null
        ? Math.round(estimatedOrganicShare * 1000) / 10
        : 0;
    why = `Estimated organic ≈ ${estimatedOrganicSessions} sessions (${organicPct}% of ${sessions}) after subtracting ${totalPaidLinkClicks} paid link clicks. Click share shows paid mix only — not sale credit.`;
  }

  return {
    sessions,
    totalPaidLinkClicks,
    estimatedOrganicSessions,
    estimatedOrganicShare,
    estimatedPaidShare,
    paidClicksExceedSessions,
    clickShare,
    assumptions,
    why,
  };
}
