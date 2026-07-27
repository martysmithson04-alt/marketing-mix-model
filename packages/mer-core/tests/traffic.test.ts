import { describe, expect, it } from "vitest";
import {
  computeClickShare,
  diagnoseTraffic,
  sumLinkClicks,
} from "../src/traffic.js";

describe("sumLinkClicks", () => {
  it("sums non-negative clicks", () => {
    expect(
      sumLinkClicks([
        { name: "Meta", linkClicks: 1000 },
        { name: "Google", linkClicks: 400 },
      ]),
    ).toBe(1400);
  });

  it("floors negatives and ignores non-finite", () => {
    expect(
      sumLinkClicks([
        { name: "Meta", linkClicks: -10 },
        { name: "Google", linkClicks: Number.NaN },
        { name: "Other", linkClicks: 50 },
      ]),
    ).toBe(50);
  });
});

describe("computeClickShare", () => {
  it("returns share of paid link clicks by channel", () => {
    const rows = computeClickShare([
      { name: "Meta", linkClicks: 750 },
      { name: "Google", linkClicks: 250 },
    ]);
    expect(rows[0]?.clickShare).toBe(0.75);
    expect(rows[1]?.clickShare).toBe(0.25);
  });

  it("returns zero shares when no clicks", () => {
    const rows = computeClickShare([{ name: "Meta", linkClicks: 0 }]);
    expect(rows[0]?.clickShare).toBe(0);
  });
});

describe("diagnoseTraffic", () => {
  it("estimates organic as sessions minus paid link clicks", () => {
    const result = diagnoseTraffic({
      sessions: 5000,
      channels: [
        { name: "Meta", linkClicks: 2000 },
        { name: "Google", linkClicks: 1000 },
      ],
    });

    expect(result.totalPaidLinkClicks).toBe(3000);
    expect(result.estimatedOrganicSessions).toBe(2000);
    expect(result.estimatedOrganicShare).toBe(0.4);
    expect(result.estimatedPaidShare).toBe(0.6);
    expect(result.paidClicksExceedSessions).toBe(false);
    expect(result.clickShare.find((c) => c.name === "Meta")?.clickShare).toBe(
      roundish(2000 / 3000),
    );
    expect(result.why).toMatch(/organic/i);
    expect(result.assumptions.length).toBeGreaterThanOrEqual(3);
  });

  it("floors organic at 0 when paid clicks exceed sessions", () => {
    const result = diagnoseTraffic({
      sessions: 1000,
      channels: [{ name: "Meta", linkClicks: 1500 }],
    });

    expect(result.estimatedOrganicSessions).toBe(0);
    expect(result.paidClicksExceedSessions).toBe(true);
    expect(result.estimatedPaidShare).toBe(1.5);
    expect(result.why).toMatch(/exceed/i);
  });

  it("treats all sessions as organic when no paid clicks", () => {
    const result = diagnoseTraffic({
      sessions: 800,
      channels: [],
    });

    expect(result.estimatedOrganicSessions).toBe(800);
    expect(result.estimatedOrganicShare).toBe(1);
    expect(result.why).toMatch(/no paid link clicks/i);
  });
});

function roundish(value: number): number {
  return Math.round(value * 10000) / 10000;
}
