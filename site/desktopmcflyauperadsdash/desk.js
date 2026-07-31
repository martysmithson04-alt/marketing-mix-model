/**
 * desktopmcflyauperadsdash — browser-only operator desk UI.
 * localStorage only. No Fly. No Cloudflare Workers. No Shopify app calls.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "desktopmcflyauperadsdash.v1";
  var Mer = window.McflyDeskMer;

  var state = {
    period: "mtd",
    marginPct: 0.35,
    currency: "USD",
    mode: "services",
    spend: [],
    revenue: [],
  };

  function $(sel) {
    return document.querySelector(sel);
  }

  function loadState() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return;
      var parsed = JSON.parse(raw);
      if (parsed.period) state.period = parsed.period;
      if (typeof parsed.marginPct === "number") state.marginPct = parsed.marginPct;
      if (parsed.currency) state.currency = parsed.currency;
      if (parsed.mode) state.mode = parsed.mode;
      if (Array.isArray(parsed.spend)) state.spend = parsed.spend;
      if (Array.isArray(parsed.revenue)) state.revenue = parsed.revenue;
    } catch (e) {
      /* ignore corrupt storage */
    }
  }

  function saveState() {
    localStorage.setItem(
      STORAGE_KEY,
      JSON.stringify({
        period: state.period,
        marginPct: state.marginPct,
        currency: state.currency,
        mode: state.mode,
        spend: state.spend,
        revenue: state.revenue,
      }),
    );
  }

  function parseCsvLine(line) {
    var fields = [];
    var current = "";
    var inQuotes = false;
    for (var i = 0; i < line.length; i++) {
      var ch = line[i];
      if (inQuotes) {
        if (ch === '"') {
          if (line[i + 1] === '"') {
            current += '"';
            i++;
          } else {
            inQuotes = false;
          }
        } else {
          current += ch;
        }
      } else if (ch === '"') {
        inQuotes = true;
      } else if (ch === ",") {
        fields.push(current.trim());
        current = "";
      } else {
        current += ch;
      }
    }
    fields.push(current.trim());
    return fields;
  }

  function parseSpendCsv(text) {
    var lines = text
      .split(/\r?\n/)
      .map(function (l) {
        return l.trim();
      })
      .filter(Boolean);
    var imported = [];
    var errors = [];
    if (!lines.length) {
      return { imported: imported, errors: [{ line: 0, reason: "Empty file" }] };
    }
    var start = 0;
    var header = parseCsvLine(lines[0]).map(function (h) {
      return h.toLowerCase();
    });
    if (header[0] === "date" && header.indexOf("channel") !== -1) start = 1;

    for (var i = start; i < lines.length; i++) {
      var lineNum = i + 1;
      var raw = lines[i];
      var cols = parseCsvLine(raw);
      var dateStr = cols[0] || "";
      var channel = cols[1] || "";
      var amountStr = cols[2] || "";
      var currency = (cols[3] || state.currency).toUpperCase();
      var note = cols[4] ? cols[4] : null;
      if (!/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
        errors.push({ line: lineNum, reason: "Bad date — expected YYYY-MM-DD", raw: raw });
        continue;
      }
      if (!channel.trim()) {
        errors.push({ line: lineNum, reason: "Missing channel", raw: raw });
        continue;
      }
      var amount = Number(amountStr);
      if (!isFinite(amount) || amount <= 0) {
        errors.push({
          line: lineNum,
          reason: "Bad amount — must be a positive number",
          raw: raw,
        });
        continue;
      }
      if (currency !== state.currency.toUpperCase()) {
        errors.push({
          line: lineNum,
          reason:
            "Currency " +
            currency +
            " ≠ desk currency " +
            state.currency +
            " (no conversion)",
          raw: raw,
        });
        continue;
      }
      imported.push({
        date: dateStr,
        channel: channel.trim(),
        amount: amount,
        currency: currency,
        note: note,
      });
    }
    return { imported: imported, errors: errors };
  }

  function parseRevenueCsv(text) {
    var lines = text
      .split(/\r?\n/)
      .map(function (l) {
        return l.trim();
      })
      .filter(Boolean);
    var imported = [];
    var errors = [];
    if (!lines.length) {
      return { imported: imported, errors: [{ line: 0, reason: "Empty file" }] };
    }
    var start = 0;
    var header = parseCsvLine(lines[0]).map(function (h) {
      return h.toLowerCase();
    });
    if (header[0] === "date" && header.indexOf("amount") !== -1) start = 1;

    for (var i = start; i < lines.length; i++) {
      var lineNum = i + 1;
      var raw = lines[i];
      var cols = parseCsvLine(raw);
      var dateStr = cols[0] || "";
      var amountStr = cols[1] || "";
      var currency = (cols[2] || state.currency).toUpperCase();
      var note = cols[3] ? cols[3] : null;
      if (!/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
        errors.push({ line: lineNum, reason: "Bad date — expected YYYY-MM-DD", raw: raw });
        continue;
      }
      var amount = Number(amountStr);
      if (!isFinite(amount) || amount <= 0) {
        errors.push({
          line: lineNum,
          reason: "Bad amount — must be a positive number",
          raw: raw,
        });
        continue;
      }
      if (currency !== state.currency.toUpperCase()) {
        errors.push({
          line: lineNum,
          reason: "Currency mismatch — no conversion in this desk",
          raw: raw,
        });
        continue;
      }
      imported.push({
        date: dateStr,
        amount: amount,
        currency: currency,
        note: note,
      });
    }
    return { imported: imported, errors: errors };
  }

  function inRange(dateStr, range) {
    var t = Date.parse(dateStr + "T12:00:00.000Z");
    if (!isFinite(t)) return false;
    return t >= range.start.getTime() && t <= range.end.getTime();
  }

  function money(n) {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: state.currency,
      maximumFractionDigits: 0,
    }).format(n);
  }

  function moneyExact(n) {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: state.currency,
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    }).format(n);
  }

  function formatMer(v) {
    if (v === null || !isFinite(v)) return "—";
    return v.toFixed(2);
  }

  function showError(msg) {
    var el = $("#desk-error");
    if (!msg) {
      el.hidden = true;
      el.textContent = "";
      return;
    }
    el.hidden = false;
    el.textContent = msg;
  }

  function render() {
    var range = Mer.periodRange(state.period, new Date());
    var spendRows = state.spend.filter(function (r) {
      return inRange(r.date, range);
    });
    var revRows = state.revenue.filter(function (r) {
      return inRange(r.date, range);
    });

    var totalSpend = spendRows.reduce(function (s, r) {
      return s + r.amount;
    }, 0);
    var revenueIn = revRows.reduce(function (s, r) {
      return s + r.amount;
    }, 0);

    var byChannel = {};
    spendRows.forEach(function (r) {
      byChannel[r.channel] = (byChannel[r.channel] || 0) + r.amount;
    });
    var channels = Object.keys(byChannel).map(function (name) {
      return { name: name, spend: byChannel[name] };
    });

    var merValue = Mer.mer(revenueIn, totalSpend);
    var beMer = Mer.breakEvenMer(state.marginPct);
    var above = beMer !== null ? Mer.isAboveBreakEven(merValue, beMer) : null;
    var allocation = Mer.allocationAction({
      channels: channels,
      revenueIn: revenueIn,
      totalSpend: totalSpend,
      contributionMargin: state.marginPct,
      periodLabel: range.label,
    });

    $("#period-label").textContent = range.label;
    $("#rev-label").textContent =
      state.mode === "ecommerce"
        ? "Net sales (uploaded)"
        : "Closed / booked revenue";
    $("#rev-help").textContent =
      state.mode === "ecommerce"
        ? "Cash in from orders this period — uploaded, not Shopify live."
        : "Cash closed or booked this period — not lead-source credit.";

    var empty = totalSpend === 0 && revenueIn === 0;
    $("#desk-empty").hidden = !empty;
    $("#desk-main").hidden = empty;

    document.querySelectorAll("[data-period]").forEach(function (btn) {
      btn.setAttribute(
        "aria-pressed",
        btn.getAttribute("data-period") === state.period ? "true" : "false",
      );
    });

    $("#margin-input").value = (state.marginPct * 100).toFixed(1);
    $("#be-preview").textContent =
      beMer !== null
        ? (state.marginPct * 100).toFixed(0) +
          "% margin → break-even MER " +
          formatMer(beMer)
        : "Enter a margin between 1 and 100.";

    if (empty) return;

    $("#mer-value").textContent = formatMer(merValue);
    $("#mer-meta").textContent =
      money(revenueIn) + " revenue ÷ " + money(totalSpend) + " spend";
    $("#be-value").textContent = formatMer(beMer);
    $("#be-meta").textContent =
      "You keep " + (state.marginPct * 100).toFixed(0) + "% of each sale";

    var verdictEl = $("#verdict-value");
    var gapEl = $("#verdict-meta");
    verdictEl.className = "desk-card__value";
    if (above === true) {
      verdictEl.textContent = "Above break-even";
      verdictEl.classList.add("desk-verdict--above");
      gapEl.textContent =
        "+" + (merValue - beMer).toFixed(2) + " above BE";
    } else if (above === false) {
      verdictEl.textContent = "Below break-even";
      verdictEl.classList.add("desk-verdict--below");
      gapEl.textContent =
        (merValue - beMer).toFixed(2) + " below BE";
    } else {
      verdictEl.textContent = "—";
      gapEl.textContent = "Add spend to compute MER";
    }

    var tbody = $("#channel-body");
    tbody.innerHTML = "";
    allocation.inputs.channelEfficiencies.forEach(function (c) {
      var action =
        allocation.actions.find(function (a) {
          return a.channel === c.name;
        }) || null;
      var tr = document.createElement("tr");
      var rowAbove =
        c.effectiveMer !== null && beMer !== null && c.effectiveMer >= beMer;
      tr.className = rowAbove ? "desk-row--above" : "desk-row--below";
      tr.innerHTML =
        "<td>" +
        escapeHtml(c.name) +
        "</td>" +
        "<td>" +
        moneyExact(c.spend) +
        "</td>" +
        "<td>" +
        (c.spendShare * 100).toFixed(1) +
        "%</td>" +
        "<td>" +
        moneyExact(c.assumedSales) +
        "</td>" +
        "<td>" +
        formatMer(c.effectiveMer) +
        "</td>" +
        "<td>" +
        (action
          ? '<span class="desk-badge desk-badge--' +
            action.type +
            '">' +
            action.type +
            "</span>"
          : "—") +
        "</td>";
      tbody.appendChild(tr);
    });

    $("#rec-text").textContent = allocation.recommendation;
    $("#audit-block").textContent = formatAudit(allocation);

    $("#teaser").textContent = allocation.recommendation;
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function formatAudit(allocation) {
    var lines = [];
    var inp = allocation.inputs;
    lines.push("INPUTS USED (audit trail)");
    lines.push("period: " + inp.periodLabel);
    lines.push("revenueIn: " + inp.revenueIn);
    lines.push("totalSpend: " + inp.totalSpend);
    lines.push("blendedMer: " + (inp.blendedMer == null ? "—" : inp.blendedMer));
    lines.push(
      "breakEvenMer: " + (inp.breakEvenMer == null ? "—" : inp.breakEvenMer),
    );
    lines.push("contributionMargin: " + inp.contributionMargin);
    lines.push("minSpendShareFloor: " + inp.minSpendShareFloor);
    lines.push("shiftRelativeGap: " + inp.shiftRelativeGap);
    lines.push("shiftSizePct: " + inp.shiftSizePct);
    lines.push("suggestedTestDays: " + inp.suggestedTestDays);
    lines.push("");
    lines.push("CHANNELS");
    inp.channelEfficiencies.forEach(function (c) {
      lines.push(
        "- " +
          c.name +
          " spend=" +
          c.spend +
          " share=" +
          c.spendShare +
          " assumedSales=" +
          c.assumedSales +
          " (" +
          c.assumedSalesBasis +
          ") effMER=" +
          (c.effectiveMer == null ? "—" : c.effectiveMer) +
          " qualifies=" +
          c.qualifies,
      );
    });
    lines.push("");
    lines.push("ACTIONS");
    allocation.actions.forEach(function (a) {
      lines.push(
        "- " +
          a.type +
          " · " +
          a.channel +
          (a.toChannel ? " → " + a.toChannel : "") +
          " · " +
          a.detail,
      );
      (a.reasons || []).forEach(function (r) {
        lines.push("    reason: " + r);
      });
    });
    return lines.join("\n");
  }

  function mergeImported(kind, rows) {
    if (kind === "spend") {
      state.spend = state.spend.concat(rows);
    } else {
      state.revenue = state.revenue.concat(rows);
    }
    saveState();
    render();
  }

  function reportErrors(errors) {
    if (!errors.length) {
      showError(null);
      return;
    }
    showError(
      errors
        .slice(0, 12)
        .map(function (e) {
          return "Line " + e.line + ": " + e.reason;
        })
        .join(" · ") +
        (errors.length > 12 ? " · +" + (errors.length - 12) + " more" : ""),
    );
  }

  async function loadSample(which) {
    showError(null);
    var spendPath =
      which === "ecommerce"
        ? "samples/ecommerce-spend.csv"
        : "samples/services-spend.csv";
    var revPath =
      which === "ecommerce"
        ? "samples/ecommerce-revenue.csv"
        : "samples/services-revenue.csv";
    try {
      var spendText = await fetch(spendPath).then(function (r) {
        if (!r.ok) throw new Error("Could not load " + spendPath);
        return r.text();
      });
      var revText = await fetch(revPath).then(function (r) {
        if (!r.ok) throw new Error("Could not load " + revPath);
        return r.text();
      });
      var spend = parseSpendCsv(spendText);
      var rev = parseRevenueCsv(revText);
      reportErrors(spend.errors.concat(rev.errors));
      state.mode = which === "ecommerce" ? "ecommerce" : "services";
      state.spend = spend.imported;
      state.revenue = rev.imported;
      saveState();
      render();
    } catch (err) {
      showError(err instanceof Error ? err.message : "Sample load failed");
    }
  }

  function exportCsv() {
    var range = Mer.periodRange(state.period, new Date());
    var spendRows = state.spend.filter(function (r) {
      return inRange(r.date, range);
    });
    var revByDate = {};
    state.revenue
      .filter(function (r) {
        return inRange(r.date, range);
      })
      .forEach(function (r) {
        revByDate[r.date] = (revByDate[r.date] || 0) + r.amount;
      });

    var dates = {};
    spendRows.forEach(function (r) {
      dates[r.date] = true;
    });
    Object.keys(revByDate).forEach(function (d) {
      dates[d] = true;
    });

    var lines = ["date,channel,spend,currency,revenueIn,blendedMer"];
    Object.keys(dates)
      .sort()
      .forEach(function (date) {
        var daySpend = spendRows.filter(function (r) {
          return r.date === date;
        });
        var dayRev = revByDate[date] || 0;
        var dayTotal = daySpend.reduce(function (s, r) {
          return s + r.amount;
        }, 0);
        var dayMer = Mer.mer(dayRev, dayTotal);
        if (!daySpend.length) {
          lines.push(
            [
              date,
              "",
              "0",
              state.currency,
              dayRev,
              dayMer == null ? "" : dayMer.toFixed(4),
            ].join(","),
          );
          return;
        }
        daySpend.forEach(function (r) {
          lines.push(
            [
              date,
              csvEscape(r.channel),
              r.amount,
              r.currency,
              dayRev,
              dayMer == null ? "" : dayMer.toFixed(4),
            ].join(","),
          );
        });
      });

    var blob = new Blob([lines.join("\n")], { type: "text/csv;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = "desktopmcflyauperadsdash-" + state.period + ".csv";
    a.click();
    URL.revokeObjectURL(url);
  }

  function csvEscape(s) {
    if (/[",\n]/.test(s)) return '"' + s.replace(/"/g, '""') + '"';
    return s;
  }

  function clearAll() {
    if (!confirm("Clear all local desk data on this browser?")) return;
    state.spend = [];
    state.revenue = [];
    saveState();
    showError(null);
    render();
  }

  function bind() {
    document.querySelectorAll("[data-period]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        state.period = btn.getAttribute("data-period");
        saveState();
        render();
      });
    });

    $("#margin-input").addEventListener("input", function (e) {
      var pct = parseFloat(e.target.value);
      if (!isFinite(pct)) return;
      state.marginPct = pct / 100;
      saveState();
      render();
    });

    $("#mode-select").addEventListener("change", function (e) {
      state.mode = e.target.value;
      saveState();
      render();
    });

    $("#spend-file").addEventListener("change", function (e) {
      var file = e.target.files && e.target.files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function () {
        var result = parseSpendCsv(String(reader.result || ""));
        reportErrors(result.errors);
        if (result.imported.length) mergeImported("spend", result.imported);
        else render();
      };
      reader.readAsText(file);
      e.target.value = "";
    });

    $("#revenue-file").addEventListener("change", function (e) {
      var file = e.target.files && e.target.files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function () {
        var result = parseRevenueCsv(String(reader.result || ""));
        reportErrors(result.errors);
        if (result.imported.length) mergeImported("revenue", result.imported);
        else render();
      };
      reader.readAsText(file);
      e.target.value = "";
    });

    document.querySelectorAll("[data-sample]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        loadSample(btn.getAttribute("data-sample"));
      });
    });
    $("#btn-export").addEventListener("click", exportCsv);
    $("#btn-print").addEventListener("click", function () {
      window.print();
    });
    $("#btn-clear").addEventListener("click", clearAll);
  }

  document.addEventListener("DOMContentLoaded", function () {
    loadState();
    $("#mode-select").value = state.mode;
    bind();
    render();
  });
})();
