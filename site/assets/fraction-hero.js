(function () {
  var root = document.getElementById("roas-fraction");
  if (!root) return;
  var sales = Number(root.getAttribute("data-sales"));
  var spend = Number(root.getAttribute("data-spend"));
  var quotEl = root.querySelector("[data-quot]");
  var beVal = root.querySelector("[data-be-val]");
  var beLine = root.querySelector("[data-be-line]");
  var statusEl = root.querySelector("[data-status]");
  var range = document.querySelector("[data-margin-range]");
  var marginLabel = document.querySelector("[data-margin-label]");
  if (!range || !quotEl) return;

  var quot = spend > 0 ? sales / spend : 0;

  function formatX(n) {
    return (Math.round(n * 100) / 100).toFixed(2) + "×";
  }

  function update() {
    var margin = Number(range.value) / 100;
    var be = margin > 0 ? 1 / margin : 0;
    var maxScale = Math.max(quot, be, 1) * 1.15;
    var bePct = Math.min(100, (be / maxScale) * 100);
    beVal.textContent = formatX(be);
    beLine.style.left = bePct + "%";
    var above = quot >= be;
    statusEl.textContent = above ? "Above" : "Below";
    statusEl.classList.toggle("above", above);
    statusEl.classList.toggle("below", !above);
    quotEl.classList.toggle("is-above", above);
    quotEl.classList.toggle("is-below", !above);
    if (marginLabel) marginLabel.textContent = range.value + "%";
    range.setAttribute("aria-valuenow", range.value);
    range.setAttribute("aria-valuetext", "break-even " + formatX(be));
  }

  quotEl.textContent = formatX(quot);
  range.addEventListener("input", update);
  update();
})();
