# nageltante.ch

Statische Website auf GitHub Pages. GitHub baut die Seite bei jeder Änderung automatisch neu (Jekyll, ca. 1 Minute).

## Inhalte bearbeiten (CMS)

1. [app.pagescms.org](https://app.pagescms.org) öffnen und mit GitHub anmelden.
2. Repository `nageltante` wählen.
3. Links die Seite wählen (z.B. «2 Preise»), Felder ändern, **Save**.

Nach ca. 1 Minute ist die Änderung online. Jede Änderung ist in der GitHub-History gespeichert und lässt sich rückgängig machen.

## Struktur

```
_data/*.yml             INHALTE: eine Datei pro Seite + allgemein.yml (Adresse, Links)
.pages.yml              Formulare für das CMS
index.html              Startseite (Menü + Info-Panel)
ueber-uns.html …        Aufbau der 8 Unterseiten (Texte kommen aus _data/)
_layouts/               Gemeinsamer Rahmen (Kopf, Fusszeile, Ladescreen)
_includes/              Wiederverwendete Teile (Adresse/Öffnungszeiten)
css/style.css           Design (Farben, Schrift, 4 Schriftgrössen oben in :root)
js/site.js              Ladescreen, Links
assets/fonts/           Hausschrift Neue Haas Grotesk Display
assets/logos/           Logos und Emblem (SVG)
assets/images/          Bilder (Upload übers CMS)
assets/videos/          Team-Videos (Upload übers CMS)
```

## Videos

Kurz, ohne Ton, quadratisch. Vor dem Hochladen komprimieren (Ziel: 2–4 MB pro Clip):

```
ffmpeg -i original.mp4 -an -vf "scale=720:720" -c:v libx264 -crf 26 -preset slow -movflags +faststart meli.mp4
```

## Domain

Unter Settings → Pages bei «Custom domain» `nageltante.ch` eintragen und beim Domain-Anbieter die DNS-Einträge auf GitHub Pages setzen.
