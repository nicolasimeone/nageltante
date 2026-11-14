#!/usr/bin/env python3
"""Erzeugt index.html und alle Unterseiten für nageltante.ch (statisches HTML)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent
import time
VERSION = time.strftime("%Y%m%d%H%M")  # verhindert alte Versionen im Browser-Cache

PAGES = [
    ("ueber-uns",        "Über uns"),
    ("preise",           "Preise"),
    ("termin",           "Termin"),
    ("team",             "Team"),
    ("studio",           "Studio"),
    ("werde-nageltante", "Werde Nageltante"),
    ("geschenkkarte",    "Geschenkkarte"),
    ("kontakt",          "Kontakt"),
]

ARROW = '<span class="menu-arrow" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>'

HEAD = """<!DOCTYPE html>
<html lang="de-CH" class="is-loading {cls}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#f7f6f4">
  <script>try{{if(sessionStorage.getItem("nt_seen"))document.documentElement.classList.remove("is-loading")}}catch(e){{}}</script>
  <link rel="icon" href="assets/logos/nageltante_emblem_positiv.svg" type="image/svg+xml">
  <link rel="preload" href="assets/logos/nageltante_emblem_positiv.svg" as="image">
  <link rel="preload" href="assets/fonts/NeueHaasDisplayRoman.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="css/style.css?v={v}">
</head>
<body>

  <!-- Ladescreen -->
  <div class="loader" aria-hidden="true">
    <img src="assets/logos/nageltante_emblem_positiv.svg" alt="" class="loader-emblem" width="71" height="57">
  </div>
"""

TAIL = """
  <script src="js/site.js?v=__V__"></script>
</body>
</html>
"""


def home():
    items = "\n".join(
        f"""      <a class="menu-item" href="{slug}.html">
        <span class="menu-num">{i}</span>
        <span class="menu-label">{label}</span>
        {ARROW}
      </a>""" for i, (slug, label) in enumerate(PAGES, 1))
    body = f"""
  <main class="home">

    <!-- Navigation links -->
    <nav class="menu" aria-label="Hauptnavigation">
{items}
    </nav>

    <!-- Info-Panel -->
    <aside class="panel">
      <div class="panel-top">
        <h1 class="brand">
          <img src="assets/logos/nageltante_logo.svg" alt="Nageltante" width="1000" height="266">
        </h1>
        <div class="contact-lines">
          <address>[Strasse Nr.], [PLZ Ort]</address>
          <a href="tel:+41000000000">+41 00 000 00 00</a>
        </div>
      </div>

      <div class="info-grid">
        <div class="info">
          <span class="info-key">A</span>
          <div>
            <h2>Termin</h2>
            <a href="#" data-booking>Online buchen</a>
          </div>
        </div>
        <div class="info">
          <span class="info-key">B</span>
          <div>
            <h2>Karriere</h2>
            <a href="werde-nageltante.html">Werde Nageltante</a>
          </div>
        </div>
        <div class="info">
          <span class="info-key">C</span>
          <div>
            <h2>Social</h2>
            <a href="#" data-instagram>Instagram</a>
          </div>
        </div>
        <div class="info">
          <span class="info-key">D</span>
          <div>
            <h2>Rechtliches</h2>
            <a href="impressum.html">Impressum</a>
            <a href="datenschutz.html">Datenschutz</a>
          </div>
        </div>
      </div>

      <div class="panel-bottom">
        <span>*Nagelstudio</span>
        <span>©<span data-year></span> Alle Rechte vorbehalten</span>
      </div>
    </aside>

  </main>
  <div class="edge-tint" aria-hidden="true"></div>
"""
    html = HEAD.format(cls="is-home", v=VERSION, title="Nageltante — Nagelstudio",
                       desc="Nageltante – ehrliches Handwerk, Ästhetik ohne Kitsch.") + body + TAIL.replace("__V__", VERSION)
    (OUT / "index.html").write_text(html)


def block(label, inner):
    return f"""
    <section class="block">
      <h2 class="block-label">{label}</h2>
      <div class="block-body">
{inner}
      </div>
    </section>
"""


def rows(items):
    lis = "\n".join(
        f'          <li><span class="r-num">{i:02d}</span><span class="r-name">{name}'
        + (f"<small>{sub}</small>" if sub else "")
        + f'</span><span class="r-price">{price}</span></li>'
        for i, (name, sub, price) in enumerate(items, 1))
    return f'        <ol class="rows">\n{lis}\n        </ol>'


TEAM = [
    ("meli", "Meli", "Nail Artist &amp; Gründerin",
     "Nageltante ist aus Leidenschaft, Umwegen und Hingabe entstanden. Ich glaube an ehrliches Handwerk, Ästhetik ohne Kitsch und daran, dass Schönheit dann entsteht, wenn man sich Zeit nimmt und sich selbst sein kann."),
    ("nanji", "Nanji", "Nail Artist",
     "Mit viel Ruhe und einem Blick fürs Detail kreiere ich gepflegte und elegante Nägel, die deine Persönlichkeit unterstreichen. Bei mir darfst du abschalten und ganz du selbst sein."),
    ("yoshi", "Yoshi", "Feel-Good Manager",
     "Ich heisse Yoshi. Ich mache keine Nägel, aber ohne mich wäre es hier nur halb so cool."),
]


def team_html():
    cards = "\n".join(f"""          <article class="member">
            <div class="media">
              <video src="assets/videos/{slug}.mp4" poster="assets/images/{slug}.jpg" autoplay muted loop playsinline preload="metadata"
                     onerror="this.replaceWith(Object.assign(document.createElement('img'),{{src:'assets/logos/nageltante_emblem_positiv.svg',className:'fallback',alt:''}}))"></video>
            </div>
            <h3>{name}</h3>
            <p class="role">{role}</p>
            <p>{text}</p>
          </article>""" for slug, name, role, text in TEAM)
    return f'        <div class="team">\n{cards}\n        </div>'


FACTS = """        <div class="facts">
          <div>
            <h3>Adresse</h3>
            <p>Nageltante<br>[Strasse Nr.]<br>[PLZ Ort]</p>
          </div>
          <div>
            <h3>Öffnungszeiten</h3>
            <p>[Di–Fr 09–19 Uhr]<br>[Sa 09–15 Uhr]<br>[So–Mo geschlossen]</p>
          </div>
          <div>
            <h3>Kontakt</h3>
            <p><a href="tel:+41000000000">+41 00 000 00 00</a><br>
            <a href="mailto:hallo@nageltante.ch">hallo@nageltante.ch</a><br>
            <a href="#" data-instagram>Instagram</a></p>
          </div>
        </div>"""

CONTENT = {
    "ueber-uns": dict(
        intro="Ehrliches Handwerk, Ästhetik ohne Kitsch – und Zeit für dich.",
        body=block("Geschichte", """        <p class="lead">Nageltante ist aus Leidenschaft, Umwegen und Hingabe entstanden.</p>
        <p class="placeholder">[Text: Wie alles angefangen hat, wann das Studio eröffnet wurde, was euch antreibt.]</p>""")
        + block("Haltung", """        <ul class="list">
          <li>[Qualität vor Tempo – wir nehmen uns Zeit]</li>
          <li>[Hochwertige Produkte, sauber verarbeitet]</li>
          <li>[Ein Ort, an dem du ganz du selbst sein darfst]</li>
        </ul>""")),
    "preise": dict(
        intro="Alle Preise in CHF. Nail Art und Extras rechnen wir nach Aufwand ab.",
        body=block("Hände", rows([
            ("Maniküre", "[Form, Pflege, Nagelhaut]", "CHF —"),
            ("Neumodellage Gel", "[inkl. Farbe]", "CHF —"),
            ("Auffüllen", "[nach 3–4 Wochen]", "CHF —"),
            ("Shellac / Gel-Lack", "", "CHF —"),
            ("Ablösen", "", "CHF —"),
        ])) + block("Füsse", rows([
            ("Pediküre", "[Fussbad, Pflege, Lack]", "CHF —"),
            ("Gel-Lack Füsse", "", "CHF —"),
        ])) + block("Extras", rows([
            ("Nail Art", "[pro Nagel / Set]", "ab CHF —"),
            ("French", "", "CHF —"),
            ("Reparatur", "[pro Nagel]", "CHF —"),
        ]))),
    "termin": dict(
        intro="Termine buchst du ganz einfach online – rund um die Uhr.",
        body=block("Online buchen", """        <p class="lead">Wähle Behandlung, Nageltante und Zeit – fertig.</p>
        <p><a href="#" class="btn" data-booking>Termin buchen ↗</a></p>""")
        + block("Gut zu wissen", """        <ul class="list">
          <li>[Bitte komm ohne Lack oder sag uns vorher Bescheid, falls etwas abgelöst werden muss.]</li>
          <li>[Absagen bitte mindestens 24 Stunden vorher, sonst verrechnen wir den Termin.]</li>
          <li>[Bei Verspätung über 15 Minuten müssen wir den Termin evtl. kürzen.]</li>
        </ul>""")),
    "team": dict(
        intro="Die Gesichter hinter Nageltante.",
        body=block("Wir sind", team_html())),
    "studio": dict(
        intro="Ein ruhiger Ort zum Abschalten – mitten in [Ort].",
        body=block("Einblicke", """        <div class="gallery">
          <div class="ph">Bild 1</div>
          <div class="ph">Bild 2</div>
          <div class="ph">Bild 3</div>
          <div class="ph">Bild 4</div>
          <div class="ph">Bild 5</div>
          <div class="ph">Bild 6</div>
        </div>""")
        + block("Besuch uns", FACTS)),
    "werde-nageltante": dict(
        intro="Du liebst Nägel, Details und gute Stimmung? Wir suchen Verstärkung.",
        body=block("Wen wir suchen", """        <p class="lead">[Nail Artist, Pensum 40–100 %]</p>
        <p class="placeholder">[Text: Erfahrung, Arbeitsweise, Start.]</p>""")
        + block("Was wir bieten", """        <ul class="list">
          <li>[Schönes Studio und ein herzliches Team]</li>
          <li>[Faire Bedingungen und flexible Zeiten]</li>
          <li>[Weiterbildungen]</li>
        </ul>""")
        + block("Bewerben", """        <p>Schick uns ein paar Zeilen über dich und Bilder deiner Arbeiten.</p>
        <p><a href="mailto:hallo@nageltante.ch?subject=Bewerbung%20Nageltante" class="btn">hallo@nageltante.ch</a></p>""")),
    "geschenkkarte": dict(
        intro="Schöne Nägel verschenken – für jeden Anlass.",
        body=block("Beträge", """        <div class="chips">
          <span>CHF 50</span><span>CHF 80</span><span>CHF 100</span><span>Wunschbetrag</span>
        </div>""")
        + block("So geht’s", """        <ul class="list">
          <li>[Im Studio kaufen oder per E-Mail bestellen]</li>
          <li>[Wir senden dir die Karte per Post oder als PDF]</li>
          <li>[Gültig während 2 Jahren]</li>
        </ul>
        <p><a href="mailto:hallo@nageltante.ch?subject=Geschenkkarte" class="btn">Geschenkkarte bestellen</a></p>""")),
    "kontakt": dict(
        intro="Fragen, Wünsche oder einfach Hallo sagen – wir freuen uns.",
        body=block("Studio", FACTS)
        + block("Anfahrt", """        <p class="placeholder">[Hinweis zu ÖV, Parkplätzen, Eingang.]</p>
        <p><a href="https://maps.google.com/?q=Nageltante" class="btn">In Google Maps öffnen ↗</a></p>""")),
}


def subpage(i, slug, label):
    nxt_i = i % len(PAGES) + 1
    nxt_slug, nxt_label = PAGES[nxt_i - 1]
    c = CONTENT[slug]
    body = f"""
  <div class="page">

    <header class="page-header">
      <a href="index.html" class="home-link" aria-label="Zur Startseite">
        <img src="assets/logos/nageltante_emblem_positiv.svg" alt="" width="71" height="57">
        <span>Nageltante</span>
      </a>
      <div class="page-header-right">
        <a href="index.html" class="menu-link">Menü</a>
        <a href="#" class="btn btn-dark" data-booking>Termin buchen</a>
      </div>
    </header>

    <main>
      <section class="page-hero">
        <span class="page-num">{i}</span>
        <h1>{label}</h1>
        <p class="intro">{c['intro']}</p>
      </section>
{c['body']}
    </main>

    <footer class="page-footer">
      <a href="{nxt_slug}.html" class="next-link">
        <span class="menu-num">{nxt_i}</span>
        <span class="next-text">
          <span class="next-kicker">Weiter</span>
          <span class="menu-label">{nxt_label}</span>
        </span>
        {ARROW}
      </a>
      <div class="footer-meta">
        <a href="index.html" aria-label="Zur Startseite"><img src="assets/logos/nageltante_logo.svg" alt="Nageltante" width="1000" height="266"></a>
        <nav>
          <a href="#" data-instagram>Instagram</a>
          <a href="impressum.html">Impressum</a>
          <a href="datenschutz.html">Datenschutz</a>
          <span>©<span data-year></span> Nageltante</span>
        </nav>
      </div>
    </footer>

  </div>
"""
    html = HEAD.format(cls="is-sub", v=VERSION, title=f"{label} — Nageltante", desc=f"{label} – Nageltante Nagelstudio.") + body + TAIL.replace("__V__", VERSION)
    (OUT / f"{slug}.html").write_text(html)


if __name__ == "__main__":
    home()
    for i, (slug, label) in enumerate(PAGES, 1):
        subpage(i, slug, label)
    print("ok")
