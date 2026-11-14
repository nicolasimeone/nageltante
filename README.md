# nageltante.ch

Statische Website, kein Build-Schritt. Läuft direkt auf GitHub Pages.

## Struktur

```
index.html              Startseite (Menü links, Info-Panel rechts)
angebot.html            Unterseite (folgt)
team.html               Unterseite mit Team-Videos (folgt)
werde-nageltante.html   Unterseite (folgt)
kontakt.html            Unterseite (folgt)
impressum.html          Rechtliches (folgt)
datenschutz.html        Rechtliches (folgt)
css/style.css           Design (Farben und Schrift oben in :root)
assets/videos/          Team-Videos (meli.mp4, nanji.mp4, yoshi.mp4)
assets/images/          Bilder, Vorschaubilder für Videos
```

## Anpassen

- **Termin- und Instagram-Link:** unten in `index.html` bei `BOOKING_URL` und `INSTAGRAM_URL`.
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
