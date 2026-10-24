# schuehler-apps.de

Übersichtsseite aller Apps von Benjamin Schühler mit zentralem Support (support@schuehler-apps.de), Impressum und Datenschutz.
Statisches HTML ohne Build, ohne Cookies und ohne externe Anfragen. Hosting: GitHub Pages, Domain bei Hostinger.
Keine Gedankenstriche in sichtbaren Texten. App-Icons liegen unter `assets/` (aus dem App Store, 256 px).

## Bauen

Die Startseite wird in `src/index.html` bearbeitet. Danach `python3 build.py` ausführen: Das Skript setzt die Icons aus `assets/icons` direkt ein und schreibt `index.html` in den Hauptordner. Impressum und Datenschutz werden direkt im Hauptordner bearbeitet.
