// ==========================================================
// Nageltante – zentrale Einstellungen
// ==========================================================
const BOOKING_URL = "#";    // Hairlist-Link, z.B. https://xyz.hairlist.ch
const INSTAGRAM_URL = "#";  // z.B. https://instagram.com/nageltante

(function () {
  function setLink(selector, url) {
    document.querySelectorAll(selector).forEach(a => {
      a.href = url;
      if (url !== "#") { a.target = "_blank"; a.rel = "noopener"; }
    });
  }
  setLink("[data-booking]", BOOKING_URL);
  setLink("[data-instagram]", INSTAGRAM_URL);
  document.querySelectorAll("[data-year]").forEach(el => el.textContent = new Date().getFullYear());

  // Ladescreen: wartet auf Seite + Schrift, mind. 700 ms, höchstens 4 s.
  // Pro Besuch nur einmal (danach sofort weg, siehe Inline-Script im <head>).
  const root = document.documentElement;
  if (!root.classList.contains("is-loading")) return;
  const minTime = new Promise(r => setTimeout(r, 700));
  const loaded = document.readyState === "complete"
    ? Promise.resolve()
    : new Promise(r => window.addEventListener("load", r, { once: true }));
  const fonts = document.fonts ? document.fonts.ready : Promise.resolve();
  const done = () => {
    root.classList.remove("is-loading");
    try { sessionStorage.setItem("nt_seen", "1"); } catch (e) {}
  };
  Promise.all([minTime, loaded, fonts]).then(done);
  setTimeout(done, 4000);
})();
