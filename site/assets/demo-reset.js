
(function () {
  var btn = document.querySelector("[data-demo-reset]");
  if (!btn) return;
  btn.addEventListener("click", function () {
    window.location.reload();
  });
})();
