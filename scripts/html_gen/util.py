import re
import html


def slugify(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = re.sub(r"^-|-$", "", name)
    return name


def escape(s: str) -> str:
    return html.escape(s, quote=True)