"""Baut die fertigen HTML-Seiten aus src/: ersetzt {{icon:name}} durch das Phosphor-SVG aus assets/icons
(inline, damit keine externen Anfragen nötig sind). Impressum und Datenschutz liegen direkt im Hauptordner."""
import pathlib, re

root = pathlib.Path(__file__).parent
icons = root / "assets" / "icons"

def inline_icon(match):
    svg = (icons / f"{match.group(1)}.svg").read_text().strip()
    return svg.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)

for src in (root / "src").glob("*.html"):
    html = re.sub(r"\{\{icon:([a-z0-9-]+)\}\}", inline_icon, src.read_text())
    (root / src.name).write_text(html)
    print("gebaut:", src.name)
