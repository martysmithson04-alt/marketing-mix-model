import type {
  ActionFunctionArgs,
  HeadersFunction,
  LoaderFunctionArgs,
} from "react-router";
import { Form, useActionData, useLoaderData, useNavigation } from "react-router";
import { boundary } from "@shopify/shopify-app-react-router/server";
import { authenticate } from "../shopify.server";
import { ensureShop } from "../lib/mer-dashboard.server";
import { resolvePeriod, type PeriodPreset } from "../lib/periods";
import prisma from "../db.server";

const CHANNELS = [
  { value: "meta", label: "Meta" },
  { value: "google", label: "Google" },
  { value: "other", label: "Other" },
] as const;

export const loader = async ({ request }: LoaderFunctionArgs) => {
  const { session } = await authenticate.admin(request);
  const shop = await ensureShop(session.shop);
  const [linkClicks, sessions] = await Promise.all([
    prisma.linkClickEntry.findMany({
      where: { shopId: shop.id },
      orderBy: { periodStart: "desc" },
      take: 20,
    }),
    prisma.sessionEntry.findMany({
      where: { shopId: shop.id },
      orderBy: { periodStart: "desc" },
      take: 20,
    }),
  ]);
  return { linkClicks, sessions };
};

export const action = async ({ request }: ActionFunctionArgs) => {
  const { session } = await authenticate.admin(request);
  const shop = await ensureShop(session.shop);
  const form = await request.formData();
  const intent = String(form.get("intent") ?? "");
  const period = (String(form.get("period") ?? "mtd") as PeriodPreset) || "mtd";
  const note = String(form.get("note") ?? "").trim() || null;
  const range = resolvePeriod(period);

  if (intent === "sessions") {
    const sessions = parseInt(String(form.get("sessions") ?? "0"), 10);
    if (!Number.isFinite(sessions) || sessions < 0) {
      return { error: "Enter a non-negative session count", success: false };
    }
    await prisma.sessionEntry.create({
      data: {
        shopId: shop.id,
        sessions,
        periodStart: range.start,
        periodEnd: range.end,
        note,
      },
    });
    return { error: null, success: true, kind: "sessions" as const };
  }

  if (intent === "link_clicks") {
    const channel = String(form.get("channel") ?? "other");
    const clicks = parseInt(String(form.get("clicks") ?? "0"), 10);
    if (!["meta", "google", "other"].includes(channel)) {
      return { error: "Invalid channel", success: false };
    }
    if (!Number.isFinite(clicks) || clicks < 0) {
      return { error: "Enter a non-negative link click count", success: false };
    }
    await prisma.linkClickEntry.create({
      data: {
        shopId: shop.id,
        channel: channel as "meta" | "google" | "other",
        clicks,
        periodStart: range.start,
        periodEnd: range.end,
        note,
      },
    });
    return { error: null, success: true, kind: "link_clicks" as const };
  }

  return { error: "Unknown action", success: false };
};

export default function TrafficEntryPage() {
  const { linkClicks, sessions } = useLoaderData<typeof loader>();
  const actionData = useActionData<typeof action>();
  const navigation = useNavigation();
  const isSubmitting = navigation.state === "submitting";

  return (
    <s-page heading="Traffic (clicks & sessions)">
      <s-section heading="How Mcfly uses this">
        <s-paragraph>
          Upload paid <strong>link clicks</strong> (Ads Manager) and store{" "}
          <strong>sessions</strong>. We show paid click share and estimate organic
          as sessions − total paid link clicks. This is mix pressure — not path
          attribution or “who got the sale.”
        </s-paragraph>
      </s-section>

      <s-section heading="Add store sessions">
        <Form method="post">
          <input type="hidden" name="intent" value="sessions" />
          <s-stack direction="block" gap="base">
            <label>
              <s-text>Sessions</s-text>
              <input
                name="sessions"
                type="number"
                step="1"
                min="0"
                required
                placeholder="5000"
                style={{ display: "block", marginTop: 4, width: "100%", maxWidth: 240 }}
              />
            </label>
            <PeriodSelect />
            <NoteInput placeholder="e.g. Shopify analytics MTD sessions" />
            <Feedback actionData={actionData} expect="sessions" />
            <s-button type="submit" variant="primary" {...(isSubmitting ? { loading: true } : {})}>
              Save sessions
            </s-button>
          </s-stack>
        </Form>
      </s-section>

      <s-section heading="Add paid link clicks">
        <Form method="post">
          <input type="hidden" name="intent" value="link_clicks" />
          <s-stack direction="block" gap="base">
            <label>
              <s-text>Channel</s-text>
              <select name="channel" defaultValue="meta" style={{ display: "block", marginTop: 4 }}>
                {CHANNELS.map(({ value, label }) => (
                  <option key={value} value={value}>
                    {label}
                  </option>
                ))}
              </select>
            </label>
            <label>
              <s-text>Link clicks</s-text>
              <input
                name="clicks"
                type="number"
                step="1"
                min="0"
                required
                placeholder="2200"
                style={{ display: "block", marginTop: 4, width: "100%", maxWidth: 240 }}
              />
            </label>
            <PeriodSelect />
            <NoteInput placeholder="e.g. Meta Ads Manager link clicks" />
            <Feedback actionData={actionData} expect="link_clicks" />
            <s-button type="submit" variant="primary" {...(isSubmitting ? { loading: true } : {})}>
              Save link clicks
            </s-button>
          </s-stack>
        </Form>
      </s-section>

      <s-section heading="Recent sessions">
        {sessions.length === 0 ? (
          <s-paragraph>
            <s-text tone="neutral">No session entries yet.</s-text>
          </s-paragraph>
        ) : (
          <s-stack direction="block" gap="base">
            {sessions.map((entry) => (
              <s-box key={entry.id} padding="base" borderWidth="base" borderRadius="base">
                <s-stack direction="inline" gap="base">
                  <s-text>{entry.sessions.toLocaleString()} sessions</s-text>
                  <s-text tone="neutral">
                    {entry.periodStart.toLocaleDateString()} –{" "}
                    {entry.periodEnd.toLocaleDateString()}
                  </s-text>
                  {entry.note && <s-text tone="neutral">{entry.note}</s-text>}
                </s-stack>
              </s-box>
            ))}
          </s-stack>
        )}
      </s-section>

      <s-section heading="Recent link clicks">
        {linkClicks.length === 0 ? (
          <s-paragraph>
            <s-text tone="neutral">No link click entries yet.</s-text>
          </s-paragraph>
        ) : (
          <s-stack direction="block" gap="base">
            {linkClicks.map((entry) => (
              <s-box key={entry.id} padding="base" borderWidth="base" borderRadius="base">
                <s-stack direction="inline" gap="base">
                  <s-text>{entry.channel}</s-text>
                  <s-text>{entry.clicks.toLocaleString()} clicks</s-text>
                  <s-text tone="neutral">
                    {entry.periodStart.toLocaleDateString()} –{" "}
                    {entry.periodEnd.toLocaleDateString()}
                  </s-text>
                  {entry.note && <s-text tone="neutral">{entry.note}</s-text>}
                </s-stack>
              </s-box>
            ))}
          </s-stack>
        )}
      </s-section>

      <s-section slot="aside" heading="Organic estimate">
        <s-paragraph>
          Estimated organic sessions ≈ store sessions − Σ paid link clicks
          (floored at 0). One click is not one session — treat this as a
          directional cash-desk diagnostic.
        </s-paragraph>
      </s-section>
    </s-page>
  );
}

function PeriodSelect() {
  return (
    <label>
      <s-text>Period</s-text>
      <select name="period" defaultValue="mtd" style={{ display: "block", marginTop: 4 }}>
        <option value="mtd">Month to date</option>
        <option value="qtd">Quarter to date</option>
        <option value="ytd">Year to date</option>
      </select>
    </label>
  );
}

function NoteInput({ placeholder }: { placeholder: string }) {
  return (
    <label>
      <s-text>Note (optional)</s-text>
      <input
        name="note"
        type="text"
        placeholder={placeholder}
        style={{ display: "block", marginTop: 4, width: "100%", maxWidth: 400 }}
      />
    </label>
  );
}

function Feedback({
  actionData,
  expect,
}: {
  actionData: Awaited<ReturnType<typeof action>> | undefined;
  expect: "sessions" | "link_clicks";
}) {
  if (!actionData) return null;
  if (actionData.error) {
    return <s-text tone="critical">{actionData.error}</s-text>;
  }
  if (actionData.success && actionData.kind === expect) {
    return (
      <s-text tone="success">
        {expect === "sessions" ? "Sessions saved." : "Link clicks saved."}
      </s-text>
    );
  }
  return null;
}

export const headers: HeadersFunction = (headersArgs) => {
  return boundary.headers(headersArgs);
};
