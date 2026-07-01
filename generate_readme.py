#!/usr/bin/env python3
"""Generate manpage-style README.md from profile.yaml"""

import yaml
import datetime
import textwrap
import subprocess
from pathlib import Path

PROFILE = "profile.yaml"
BANNER_SOURCE = "assets/banner.txt"
README = "README.md"
WIDTH = 78


def figlet(text: str) -> str:
    try:
        result = subprocess.check_output(
            ["figlet", "-f", "slant", text], text=True, stderr=subprocess.DEVNULL
        )
        return result.rstrip("\n")
    except (FileNotFoundError, subprocess.CalledProcessError):
        banner_path = Path(BANNER_SOURCE)
        if banner_path.exists():
            return banner_path.read_text().rstrip("\n")
        return text


def wrap(text: str, indent: str = "") -> str:
    return textwrap.fill(
        text, width=WIDTH, initial_indent=indent, subsequent_indent=indent
    )


def tag(text: str) -> str:
    return f"`{text}`"


def render_badges(badges: list) -> str:
    return "\n".join(badges) if badges else ""


def load_profile() -> dict:
    raw = Path(PROFILE).read_text()
    return yaml.safe_load(raw)


def render(p: dict) -> str:
    parts = []
    id_ = p["identity"]
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now().isoformat(timespec="seconds")

    # --- ASCII banner ---
    parts.append("```text")
    parts.append("")
    parts.append(figlet(id_["handle"]))
    parts.append("```")
    parts.append("")

    # --- Title ---
    parts.append(f'`{id_["handle"]}` - {id_["title"]}')
    parts.append("")
    parts.append(f"*Updated: {today}*")
    parts.append("")

    # --- NAME ---
    parts.append("## NAME")
    parts.append("")
    parts.append(f"**{id_['handle']}** - {p['summary']}")
    parts.append("")

    # --- SYNOPSIS ---
    parts.append("## SYNOPSIS")
    parts.append("")
    parts.append("```bash")
    parts.append(f"$ {id_['handle']} [OPTIONS] [PROJECT]")
    parts.append("```")
    parts.append("")

    # --- DESCRIPTION ---
    parts.append("## DESCRIPTION")
    parts.append("")
    parts.append(wrap(p["summary"]))
    parts.append("")

    details = [
        ("Handle", f'`{id_["handle"]}`'),
        ("Name", id_["name"]),
        ("Email", f'`{id_["email"]}`'),
        ("Location", id_["location"]),
        ("Since", id_["since"]),
        ("Domain", "Platform Engineering / AI/ML / Security Tooling"),
    ]
    for label, value in details:
        parts.append(f"**{label}:** {value}  ")
    parts.append("")

    # --- STACK (badges) ---
    if "badges" in p and p["badges"]:
        parts.append("## STACK")
        parts.append("")
        parts.append(render_badges(p["badges"]))
        parts.append("")

    # --- OPTIONS (skills as flags) ---
    parts.append("## OPTIONS")
    parts.append("")

    skill_groups = p.get("stack", {})
    group_map = {
        "languages": ("Languages", "-l", "--lang"),
        "platforms": ("Platforms", "-p", "--platform"),
        "ai_ml": ("AI/ML", "-a", "--ai"),
        "security": ("Security", "-s", "--sec"),
        "observability": ("Observability", "-o", "--obs"),
        "tooling": ("Tooling", "-t", "--tool"),
    }

    for key, (title, short_flag, long_flag) in group_map.items():
        items = skill_groups.get(key, [])
        if not items:
            continue
        parts.append(f"### {title}")
        parts.append("")
        for item in items:
            flag_name = item.split("(")[0].strip().lower().replace(" ", "-")
            dots = "." * max(2, 26 - len(flag_name))
            parts.append(f"  `{short_flag} {flag_name}`{dots}{item}")
        parts.append("")

    # --- EXAMPLES (projects) ---
    parts.append("## EXAMPLES")
    parts.append("")

    for proj in p.get("projects", []):
        emoji = "\U0001f7e2" if proj["status"] == "active" else "\U0001f534"
        parts.append(f"### {emoji} {proj['name']}")
        parts.append("")
        parts.append(wrap(proj["desc"]))
        parts.append("")
        parts.append(f'**Tags:** {", ".join(tag(t) for t in proj["tags"])}  ')
        parts.append(f'**Lines:** ~{proj["lines"]:,}  ')
        if proj.get("tests"):
            parts.append(f'**Tests:** {proj["tests"]}  ')
        parts.append(f'**Repo:** [{proj["url"]}]({proj["url"]})')
        parts.append("")

    # --- SEE ALSO ---
    parts.append("## SEE ALSO")
    parts.append("")
    for key, value in p.get("links", {}).items():
        label = key.title()
        parts.append(f"* **{label}:** [{value}]({value})")
    parts.append("")

    # --- BUGS ---
    parts.append("## BUGS")
    parts.append("")
    parts.append("Report issues via GitHub Issues on the relevant project repository.")
    parts.append("")
    if "email" in p.get("links", {}):
        email = p["links"]["email"]
        parts.append(f"Contact: [{email}]({email})")
    parts.append("")

    # --- FOOTER ---
    parts.append("---")
    parts.append(f"*Generated on {now} from `profile.yaml`*")
    parts.append("")

    return "\n".join(parts)


def main():
    profile = load_profile()
    readme = render(profile)
    Path(README).write_text(readme)
    print("README.md generated")


if __name__ == "__main__":
    main()
