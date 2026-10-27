"""Baut die fertigen HTML-Seiten aus src/: ersetzt {{icon:name}} durch das Phosphor-SVG aus assets/icons
(inline, damit keine externen Anfragen nötig sind). Impressum und Datenschutz liegen direkt im Hauptordner."""
import hashlib, pathlib, re

root = pathlib.Path(__file__).parent
icons = root / "assets" / "icons"

def inline_icon(match):
    svg = (icons / f"{match.group(1)}.svg").read_text().strip()
    return svg.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)

# Versionsnummer an style.css hängen, damit Browser nach jeder Änderung die neue Datei laden
# (GitHub Pages lässt Dateien sonst bis zu 10 Minuten im Browser-Zwischenspeicher)
stil = hashlib.md5((root / "style.css").read_bytes()).hexdigest()[:8]

for src in (root / "src").glob("*.html"):
    html = re.sub(r"\{\{icon:([a-z0-9-]+)\}\}", inline_icon, src.read_text())
    html = html.replace('href="style.css"', f'href="style.css?v={stil}"')
    (root / src.name).write_text(html)
    print("gebaut:", src.name)

# Impressum und Datenschutz (ohne Quelle in src/) bekommen dieselbe Versionsnummer
for name in ("impressum.html", "datenschutz.html"):
    seite = root / name
    seite.write_text(re.sub(r'href="style\.css(\?v=[a-f0-9]+)?"', f'href="style.css?v={stil}"', seite.read_text()))
