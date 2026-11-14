# nageltante.ch

Statische Website, kein Build-Schritt. Läuft direkt auf GitHub Pages.

## Struktur

```
index.html              Startseite (Menü links, Info-Panel rechts)
ueber-uns.html          1 Über uns
preise.html             2 Preise
termin.html             3 Termin
team.html               4 Team (Videos)
studio.html             5 Studio
werde-nageltante.html   6 Werde Nageltante
geschenkkarte.html      7 Geschenkkarte
kontakt.html            8 Kontakt
css/style.css           Design (Farben, Schrift, 4 Schriftgrössen oben in :root)
js/site.js              Hairlist- und Instagram-Link, Ladescreen
assets/fonts/           Hausschrift Neue Haas Grotesk Display (woff2 + ttf)
assets/logos/           Logos und Emblem (SVG)
assets/videos/          Team-Videos (meli.mp4, nanji.mp4, yoshi.mp4)
assets/images/          Bilder, Vorschaubilder für Videos
```

## Anpassen

- **Termin- und Instagram-Link:** in `js/site.js` bei `BOOKING_URL` und `INSTAGRAM_URL` (gilt für alle Seiten).
- **Adresse, Telefon:** in `index.html` im Bereich `panel-top`. Platzhalter stehen in `[eckigen Klammern]`.
- **Farben, Schrift:** in `css/style.css` ganz oben.

## Videos

Kurz, ohne Ton, quadratisch. Vor dem Hochladen komprimieren (Ziel: 2–4 MB pro Clip):

```
ffmpeg -i original.mp4 -an -vf "scale=720:720" -c:v libx264 -crf 26 -preset slow -movflags +faststart meli.mp4
ffmpeg -i meli.mp4 -frames:v 1 -q:v 3 ../images/meli.jpg
```

## Veröffentlichen (GitHub Pages)

1. Settings → Pages → Source: «Deploy from a branch», Branch `main`, Ordner `/ (root)`.
2. Nach ca. 1 Minute ist die Seite unter `https://nicolasimeone.github.io/nageltante/` erreichbar.
3. Domain am Schluss: unter Settings → Pages bei «Custom domain» `nageltante.ch` eintragen und beim Domain-Anbieter die DNS-Einträge auf GitHub Pages setzen.
