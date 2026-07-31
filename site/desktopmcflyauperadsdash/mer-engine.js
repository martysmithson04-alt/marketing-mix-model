/**
 * desktopmcflyauperadsdash — pure Cash MER math (browser only).
 * Mirror of @mcfly/mer-core religion. No I/O. No attribution.
 */
(function (global) {
  "use strict";

  var MIN_SPEND_SHARE_FLOOR = 0.05;
  var SHIFT_RELATIVE_GAP = 0.25;
  var SHIFT_SIZE_PCT = 15;
  var DEFAULT_TEST_DAYS = 7;

  function mer(revenueIn, adSpend) {
    if (adSpend === 0) return null;
    return revenueIn / adSpend;
  }

  function breakEvenMer(contributionMargin) {
    if (!(contributionMargin > 0) || contributionMargin > 1) return null;
    return 1 / contributionMargin;
  }

  function isAboveBreakEven(merValue, beMer) {
    if (merValue === null) return null;
    return merValue >= beMer;
  }

  function channelShare(channelSpend, totalSpend) {
    if (totalSpend === 0) return 0;
    return channelSpend / totalSpend;
  }

  function assumedChannelSales(share, revenueIn) {
    return share * revenueIn;
  }

  function channelEffectiveMer(assumedSales, channelSpend) {
    if (channelSpend === 0) return null;
    return assumedSales / channelSpend;
  }

  function round(value, digits) {
    var f = Math.pow(10, digits == null ? 2 : digits);
    return Math.round(value * f) / f;
  }

  function relativeGap(leaderMer, laggardMer) {
    if (laggardMer <= 0) return Infinity;
    return (leaderMer - laggardMer) / laggardMer;
  }

  /**
   * @param {{ channels: Array<{name:string,spend:number,salesContribution?:number}>, revenueIn:number, totalSpend:number, contributionMargin:number, periodLabel?:string }} ctx
   */
  function allocationAction(ctx) {
    var channels = ctx.channels || [];
    var revenueIn = ctx.revenueIn;
    var totalSpend = ctx.totalSpend;
    var contributionMargin = ctx.contributionMargin;
    var periodLabel = ctx.periodLabel || "current period";
    var suggestedTestDays = DEFAULT_TEST_DAYS;
    var minShare = MIN_SPEND_SHARE_FLOOR;
    var shiftGap = SHIFT_RELATIVE_GAP;
    var shiftPct = SHIFT_SIZE_PCT;

    var beMer = breakEvenMer(contributionMargin);
    var overallMer = mer(revenueIn, totalSpend);
    var above =
      beMer !== null ? isAboveBreakEven(overallMer, beMer) : null;

    var efficiencies = channels
      .filter(function (c) {
        return c.spend >= 0;
      })
      .map(function (channel) {
        var share = channelShare(channel.spend, totalSpend);
        var hasSplit = channel.salesContribution !== undefined;
        var assumed = hasSplit
          ? channel.salesContribution
          : assumedChannelSales(share, revenueIn);
        var eff = channelEffectiveMer(assumed, channel.spend);
        return {
          name: channel.name,
          spend: channel.spend,
          spendShare: round(share, 4),
          assumedSales: round(assumed, 2),
          assumedSalesBasis: hasSplit ? "operator_split" : "cash_share",
          effectiveMer: eff !== null ? round(eff, 4) : null,
          qualifies: share >= minShare && channel.spend > 0,
        };
      });

    var inputs = {
      revenueIn: round(revenueIn, 2),
      totalSpend: round(totalSpend, 2),
      blendedMer: overallMer !== null ? round(overallMer, 4) : null,
      breakEvenMer: beMer !== null ? round(beMer, 4) : null,
      contributionMargin: contributionMargin,
      periodLabel: periodLabel,
      suggestedTestDays: suggestedTestDays,
      minSpendShareFloor: minShare,
      shiftRelativeGap: shiftGap,
      shiftSizePct: shiftPct,
      channelEfficiencies: efficiencies,
    };

    var actions = [];

    if (totalSpend <= 0 || channels.length === 0) {
      var why0 =
        "No ad spend recorded for this period. Add spend before allocation advice applies.";
      return {
        overallMer: null,
        breakEvenMer: beMer !== null ? round(beMer, 4) : null,
        isAboveBreakEven: null,
        overallState: "unknown",
        suggestedTestDays: suggestedTestDays,
        actions: [
          {
            type: "watch",
            channel: "—",
            detail: "Enter channel spend to unlock mix suggestions.",
            reasons: ["totalSpend === 0"],
          },
        ],
        recommendation: why0,
        why: why0,
        inputs: inputs,
      };
    }

    if (beMer === null) {
      var whyM = "Contribution margin must be greater than 0% and at most 100%.";
      return {
        overallMer: overallMer !== null ? round(overallMer, 4) : null,
        breakEvenMer: null,
        isAboveBreakEven: null,
        overallState: "unknown",
        suggestedTestDays: suggestedTestDays,
        actions: efficiencies.map(function (c) {
          return {
            type: "watch",
            channel: c.name,
            detail: "Fix margin before actions apply.",
            reasons: ["invalid contributionMargin"],
          };
        }),
        recommendation: whyM,
        why: whyM,
        inputs: inputs,
      };
    }

    var thin = efficiencies.filter(function (c) {
      return !c.qualifies;
    });
    var qualifying = efficiencies.filter(function (c) {
      return c.qualifies;
    });

    thin.forEach(function (c) {
      actions.push({
        type: "watch",
        channel: c.name,
        detail:
          "Spend share " +
          round(c.spendShare * 100, 1) +
          "% is below the " +
          round(minShare * 100, 0) +
          "% floor — watch, do not cut or shift on thin data.",
        reasons: [
          "spendShare " + c.spendShare + " < minSpendShareFloor " + minShare,
        ],
      });
    });

    if (above === false) {
      var worst = qualifying
        .slice()
        .sort(function (a, b) {
          var ma = a.effectiveMer == null ? Infinity : a.effectiveMer;
          var mb = b.effectiveMer == null ? Infinity : b.effectiveMer;
          if (ma !== mb) return ma - mb;
          return b.spend - a.spend;
        })[0];

      var whyBelow =
        "Overall MER (" +
        round(overallMer || 0) +
        ") is below break-even (" +
        round(beMer) +
        "). Cash view: cut the weakest qualifying channel.";
      var recommendation = whyBelow;

      qualifying.forEach(function (c) {
        if (worst && c.name === worst.name) {
          actions.push({
            type: "cut",
            channel: c.name,
            percentChange: -shiftPct,
            detail:
              "Lowest effective MER among qualifying channels — test a " +
              shiftPct +
              "% cut over " +
              suggestedTestDays +
              " days.",
            reasons: [
              "blendedMer < breakEvenMer",
              "effectiveMer " + c.effectiveMer,
              "qualifies: spendShare >= " + minShare,
            ],
          });
          recommendation =
            "Cut ~" +
            shiftPct +
            "% of " +
            c.name +
            " spend — " +
            suggestedTestDays +
            "-day test. Re-check blended MER vs break-even after.";
        } else if (c.effectiveMer !== null && c.effectiveMer < beMer) {
          actions.push({
            type: "watch",
            channel: c.name,
            detail: "Below break-even on assumed cash-share MER — watch.",
            reasons: [
              "blendedMer < breakEvenMer",
              "not the worst channel",
            ],
          });
        } else {
          actions.push({
            type: "hold",
            channel: c.name,
            detail: "At or above break-even on assumed sales — hold.",
            reasons: ["blendedMer < breakEvenMer"],
          });
        }
      });

      return {
        overallMer: overallMer !== null ? round(overallMer, 4) : null,
        breakEvenMer: round(beMer, 4),
        isAboveBreakEven: false,
        overallState: "below_break_even",
        suggestedTestDays: suggestedTestDays,
        actions: actions,
        recommendation: recommendation,
        why: whyBelow,
        inputs: inputs,
      };
    }

    var sorted = qualifying
      .filter(function (c) {
        return c.effectiveMer !== null;
      })
      .slice()
      .sort(function (a, b) {
        return (b.effectiveMer || 0) - (a.effectiveMer || 0);
      });
    var leader = sorted[0] || null;
    var laggard = sorted[sorted.length - 1] || null;

    if (
      leader &&
      laggard &&
      leader.name !== laggard.name &&
      leader.effectiveMer !== null &&
      laggard.effectiveMer !== null
    ) {
      var gap = relativeGap(leader.effectiveMer, laggard.effectiveMer);
      if (gap >= shiftGap) {
        qualifying.forEach(function (c) {
          if (c.name === laggard.name) {
            actions.push({
              type: "shift",
              channel: c.name,
              toChannel: leader.name,
              percentChange: -shiftPct,
              detail:
                "Shift ~" +
                shiftPct +
                "% of " +
                c.name +
                " spend to " +
                leader.name +
                " — " +
                suggestedTestDays +
                "-day test (effective MER gap " +
                round(gap * 100, 0) +
                "%).",
              reasons: [
                "blendedMer >= breakEvenMer",
                "relativeGap " + round(gap * 100, 1) + "% >= " + shiftGap * 100 + "%",
              ],
            });
          } else {
            actions.push({
              type: "hold",
              channel: c.name,
              detail:
                c.name === leader.name
                  ? "Leader — receive shift test from " + laggard.name + "."
                  : "Within band — hold.",
              reasons: ["blendedMer >= breakEvenMer"],
            });
          }
        });
        var recShift =
          "Shift ~" +
          shiftPct +
          "% of " +
          laggard.name +
          " spend to " +
          leader.name +
          " — " +
          suggestedTestDays +
          "-day test.";
        return {
          overallMer: overallMer !== null ? round(overallMer, 4) : null,
          breakEvenMer: round(beMer, 4),
          isAboveBreakEven: true,
          overallState: "above_break_even",
          suggestedTestDays: suggestedTestDays,
          actions: actions,
          recommendation: recShift,
          why:
            "Overall MER (" +
            round(overallMer || 0) +
            ") is at or above break-even (" +
            round(beMer) +
            ").",
          inputs: inputs,
        };
      }
    }

    qualifying.forEach(function (c) {
      actions.push({
        type: "hold",
        channel: c.name,
        detail: "Above break-even and within the shift band — hold.",
        reasons: [
          "blendedMer >= breakEvenMer",
          "no pair with relativeGap >= " + shiftGap,
        ],
      });
    });

    var whyHold =
      "Overall MER (" +
      round(overallMer || 0) +
      ") is at or above break-even (" +
      round(beMer) +
      "). Channels are within band — hold.";
    return {
      overallMer: overallMer !== null ? round(overallMer, 4) : null,
      breakEvenMer: round(beMer, 4),
      isAboveBreakEven: true,
      overallState: "above_break_even",
      suggestedTestDays: suggestedTestDays,
      actions: actions,
      recommendation: whyHold,
      why: whyHold,
      inputs: inputs,
    };
  }

  function periodRange(preset, now) {
    now = now || new Date();
    var y = now.getUTCFullYear();
    var m = now.getUTCMonth();
    var d = now.getUTCDate();
    var end = new Date(Date.UTC(y, m, d, 23, 59, 59, 999));
    var start;
    var label;
    if (preset === "qtd") {
      var q = Math.floor(m / 3) * 3;
      start = new Date(Date.UTC(y, q, 1, 0, 0, 0, 0));
      label = "Quarter to date";
    } else if (preset === "ytd") {
      start = new Date(Date.UTC(y, 0, 1, 0, 0, 0, 0));
      label = "Year to date";
    } else {
      start = new Date(Date.UTC(y, m, 1, 0, 0, 0, 0));
      label = "Month to date";
    }
    return { start: start, end: end, label: label, preset: preset };
  }

  global.McflyDeskMer = {
    mer: mer,
    breakEvenMer: breakEvenMer,
    isAboveBreakEven: isAboveBreakEven,
    channelShare: channelShare,
    assumedChannelSales: assumedChannelSales,
    channelEffectiveMer: channelEffectiveMer,
    allocationAction: allocationAction,
    periodRange: periodRange,
    MIN_SPEND_SHARE_FLOOR: MIN_SPEND_SHARE_FLOOR,
    SHIFT_RELATIVE_GAP: SHIFT_RELATIVE_GAP,
    SHIFT_SIZE_PCT: SHIFT_SIZE_PCT,
    DEFAULT_TEST_DAYS: DEFAULT_TEST_DAYS,
  };
})(typeof window !== "undefined" ? window : globalThis);
