#!/usr/bin/env python3
"""Generate manpage-style README.md from profile.yaml"""

import yaml
import datetime
import textwrap
import subprocess
import re
from pathlib import Path

PROFILE = "profile.yaml"
BANNER_SOURCE = "assets/banner.txt"
README = "README.md"
WIDTH = 78
MAN_NAME = "LOG0U7(1)"
MAN_SECTION = "User Commands"


BADGE_GROUPS = [
    ("Languages / Runtimes", [
        "Python", "Ruby", "Perl", "PHP", "C", "C++", "R",
        "JavaScript", "Node.js", "Shell Script", "Markdown",
    ]),
    ("Shell / Terminal", [
        "Bash", "POSIX sh", "tmux", "GNU Screen", "Starship",
    ]),
    ("AI / ML", [
        "Anthropic", "Claude", "OpenAI", "Ollama",
        "PyTorch", "scikit-learn", "pandas", "NumPy",
    ]),
    ("Infra / Containers", [
        "Linux", "GNU", "systemd", "Make", "CMake",
        "Arduino", "PlatformIO",
        "Vagrant", "Packer", "Docker", "Podman", "LXC", "libvirt", "QEMU",
        "Kubernetes", "Nomad", "Proxmox",
    ]),
    ("IaC / Automation", [
        "Ansible", "OpenTofu", "OpenBao",
    ]),
    ("Observability / Monitoring", [
        "Prometheus", "Grafana", "VictoriaMetrics", "VictoriaLogs",
        "OpenTelemetry", "Loki", "Tempo", "Jaeger", "CouchDB",
    ]),
    ("Databases", [
        "MariaDB", "MySQL", "Postgres", "Redis", "SQLite",
    ]),
    ("Security", [
        "SSH", "GPG", "OpenSSL", "nmap", "OpenVAS",
        "Wireshark", "Metasploit", "Burp Suite", "Hashcat",
    ]),
    ("Reverse Engineering / Debugging", [
        "radare2", "Ghidra", "GDB", "DDD", "binwalk",
    ]),
    ("Networking / VPN / Firewall", [
        "WireGuard", "OpenVPN",
        "iptables", "nftables", "pf",
        "m0n0wall", "pfSense", "OPNsense", "OpenWrt", "PowerDNS",
    ]),
    ("Proxy / LB / Storage", [
        "HAProxy", "Varnish", "Squid",
        "Traefik", "Apache", "Nginx",
        "GlusterFS", "Consul", "Foreman",
    ]),
    ("Cloud", [
        "AWS", "Google Cloud",
    ]),
    ("VCS / CI", [
        "Git", "GitLab", "GitHub", "GitHub Actions", "GitLab CI",
    ]),
    ("Editors / IDEs", [
        "Neovim", "Vim", "Visual Studio Code", "OpenCode",
    ]),
    ("Distributions", [
        "Debian", "Ubuntu", "AlmaLinux", "Alpine Linux",
        "Arch Linux", "Gentoo", "NixOS",
    ]),
]


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


def parse_badges_flat(badges: list) -> dict:
    result = {}
    for entry in badges:
        m = re.match(r"!\[(.+?)\]\(.+?\)", entry)
        if m:
            name = m.group(1)
            result[name] = entry
    return result


def render_badge_groups(badges: list) -> str:
    if not badges:
        return ""
    flat = parse_badges_flat(badges)
    assigned = set()
    lines = []

    for group_title, tech_list in BADGE_GROUPS:
        found = []
        for tech in tech_list:
            if tech in flat:
                found.append(flat[tech])
                assigned.add(tech)
        if found:
            lines.append(f"### {group_title}")
            lines.append("")
            lines.append(" ".join(found))
            lines.append("")

    remaining = [v for k, v in flat.items() if k not in assigned]
    if remaining:
        lines.append("### Other")
        lines.append("")
        lines.append(" ".join(remaining))
        lines.append("")

    return "\n".join(lines)


def load_profile() -> dict:
    raw = Path(PROFILE).read_text()
    return yaml.safe_load(raw)


def render(p: dict) -> str:
    parts = []
    id_ = p["identity"]
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now().isoformat(timespec="seconds")

    # --- ASCII BANNER (includes manpage header) ---
    header_left = MAN_NAME
    header_center = MAN_SECTION
    header_right = MAN_NAME
    pad = WIDTH - len(header_left) - len(header_center) - len(header_right)
    header_line = f"{header_left}{' ' * (pad // 2)}{header_center}{' ' * (pad - pad // 2)}{header_right}"
    parts.append("```text")
    parts.append(header_line)
    parts.append("")
    parts.append(figlet(id_["handle"]))
    parts.append("```")
    parts.append("")
    parts.append(f"`{id_['handle']}` - {id_['title']}")
    parts.append("")
    parts.append(f"*Updated: {today}*")
    parts.append("")

    # --- NAME ---
    parts.append("## NAME")
    parts.append("")
    parts.append(f"**{id_['handle']}** - {id_['title']}")
    parts.append("")

    # --- SYNOPSIS ---
    parts.append("## SYNOPSIS")
    parts.append("")
    parts.append("```bash")
    parts.append(f"    {id_['handle']} [--skills] [--format man] [--section <section>]")
    parts.append(f"    {id_['handle']} --ai orchestration --platform kubernetes")
    parts.append(f"    {id_['handle']} --skills --filter languages")
    parts.append("```")
    parts.append("")

    # --- DESCRIPTION ---
    parts.append("## DESCRIPTION")
    parts.append("")
    parts.append(wrap(p["summary"]))
    parts.append("")
    for label, value in [
        ("Handle", f'`{id_["handle"]}`'),
        ("Name", id_["name"]),
        ("Location", id_["location"]),
        ("Since", id_["since"]),
        ("Domain", "Platform Engineering / AI/ML / Security Tooling"),
    ]:
        parts.append(f"**{label}:** {value}  ")
    parts.append("")

    # --- BIO (origin story) ---
    if "bio" in p and p["bio"]:
        parts.append("### Origin")
        parts.append("")
        paragraphs = []
        current = []
        for line in p["bio"].strip().split("\n"):
            line = line.strip()
            if line == "":
                if current:
                    paragraphs.append(" ".join(current))
                    current = []
            else:
                current.append(line)
        if current:
            paragraphs.append(" ".join(current))
        for para in paragraphs:
            parts.append(wrap(para))
            parts.append("")

    # --- STACK (badges grouped) ---
    if "badges" in p and p["badges"]:
        parts.append("## STACK")
        parts.append("")
        groups = render_badge_groups(p["badges"])
        if groups:
            parts.append(groups)
        parts.append("")

    # --- OPTIONS (skills as flags) ---
    parts.append("## OPTIONS")
    parts.append("")

    skill_groups = p.get("stack", {})
    group_map = [
        ("Languages", "-l", "languages"),
        ("Platforms", "-p", "platforms"),
        ("AI/ML", "-a", "ai_ml"),
        ("Security", "-s", "security"),
        ("Observability", "-o", "observability"),
        ("Tooling", "-t", "tooling"),
    ]

    for title, short_flag, key in group_map:
        items = skill_groups.get(key, [])
        if not items:
            continue
        parts.append(f"### {title}")
        parts.append("")
        parts.append("```text")
        desc_indent = "       "
        for i, item in enumerate(items):
            raw = item.split("(")[0].strip()
            raw = raw.split(",")[0].strip()
            raw = raw.split(" /")[0].strip()
            raw = raw.split("/")[0].strip()
            flag_name = raw.lower().replace(" ", "-")
            parts.append(f"  {short_flag} {flag_name}")
            wrapped = textwrap.fill(
                item,
                width=WIDTH,
                initial_indent=desc_indent,
                subsequent_indent=desc_indent,
                break_long_words=False,
                break_on_hyphens=False,
            )
            parts.append(wrapped)
            if i < len(items) - 1:
                parts.append("")
        parts.append("```")
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
    website = p.get("links", {}).get("website", "")
    if website:
        parts.append(f"Contact: [{website}]({website})")
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
