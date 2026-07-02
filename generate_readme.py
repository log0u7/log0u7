#!/usr/bin/env python3
"""Generate manpage-style README.md from profile.yaml"""

import yaml
import datetime
import textwrap
import subprocess
import re
import random
from pathlib import Path

PROFILE = "profile.yaml"
BANNER_SOURCE = "assets/banner.txt"
README = "README.md"
WIDTH = 78
MAN_NAME = "LOG0U7(1)"
MAN_SECTION = "User Commands"


BADGE_GROUPS = [
    ("Languages", [
        "Python", "Ruby", "Perl", "PHP", "C", "C++", "R",
        "JavaScript", "Node.js", "Bash",
        "awk", "lex/yacc/bison", "Markdown",
    ]),
    ("Environment", [
        "tmux", "GNU Screen", "Starship",
    ]),
    ("AI / ML", [
        "Anthropic", "Claude", "OpenAI", "Ollama",
        "PyTorch", "pandas", "NumPy",
    ]),
    ("Infra / Containers", [
        "Linux", "GNU", "systemd", "Make", "CMake", "Arduino",
        "Vagrant", "Packer", "Docker", "Podman", "LXC", "libvirt", "QEMU",
        "KVM", "VirtualBox", "Kubernetes", "Nomad", "Proxmox",
    ]),
    ("IaC / Automation", [
        "Ansible", "Salt", "Puppet", "Chef", "OpenTofu", "Foreman", "Consul",
    ]),
    ("Observability / Monitoring", [
        "Prometheus", "Grafana", "VictoriaMetrics", "VictoriaLogs",
        "OpenTelemetry", "Loki", "Tempo", "Jaeger",
    ]),
    ("Databases", [
        "MariaDB", "MySQL", "Postgres", "Redis", "SQLite", "CouchDB",
    ]),
    ("Security", [
        "OpenSSH", "GPG", "OpenSSL", "OpenBao",
        "nmap", "netcat", "OpenVAS",
        "Wireshark", "Metasploit", "Burp Suite", "Hashcat",
    ]),
    ("Reverse Engineering / Debugging", [
        "radare2", "Ghidra", "GDB", "DDD", "Metasm", "Scapy", "binwalk",
    ]),
    ("Networking / VPN / Firewall", [
        "WireGuard", "OpenVPN",
        "iptables", "nftables", "pf",
        "m0n0wall", "pfSense", "OPNsense", "OpenWrt", "PowerDNS",
    ]),
    ("Proxy / LB / Web", [
        "Traefik", "Apache", "Nginx", "HAProxy", "Varnish", "Squid",
        "GlusterFS",
    ]),
    ("Cloud", [
        "AWS", "Google Cloud", "OVHcloud", "Alibaba Cloud", "Yandex Cloud",
        "Vultr", "DigitalOcean", "Hetzner", "Scaleway",
        "Selectel", "IBM Cloud", "Oracle Cloud",
    ]),
    ("VCS / CI", [
        "Git", "GitLab", "GitHub", "GitHub Actions", "GitLab CI",
    ]),
    ("Editors / IDEs", [
        "Vim", "Neovim", "VSCodium", "OpenCode",
    ]),
    ("Distributions", [
        "Debian", "Ubuntu", "AlmaLinux", "Alpine Linux",
        "Arch Linux", "Gentoo", "NixOS", "OpenBSD", "POSIX",
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


SPARKLINE_CHARS = "▁▂▃▄▅▆▇█"


def render_uptime(since_year: int) -> str:
    today = datetime.date.today()
    start = datetime.date(since_year, 1, 1)
    delta = today - start
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = delta.days % 30
    return f"{years}y {months}m {days}d"


def render_sparkline(seed: int, length: int = 32) -> str:
    rng = random.Random(seed)
    # Generate smooth-ish values with a walk to look like activity
    values = []
    v = rng.randint(2, 5)
    for _ in range(length):
        v = max(0, min(7, v + rng.randint(-1, 1)))
        values.append(v)
    return "".join(SPARKLINE_CHARS[v] for v in values)


def render_fortune(fortunes: list, seed: int) -> str:
    if not fortunes:
        return ""
    idx = seed % len(fortunes)
    return fortunes[idx]


def render_status(p: dict) -> str:
    today = datetime.date.today()
    iso_year, iso_week, _ = today.isocalendar()
    seed = iso_year * 100 + iso_week

    since_year = int(p["identity"].get("since", 1984))
    uptime = render_uptime(since_year)
    sparkline = render_sparkline(seed)
    fortune_text = render_fortune(p.get("fortunes", []), seed)

    # Neofetch-style block
    col_w = 16
    lines = []

    def row(label: str, value: str) -> str:
        return f"  {label:<{col_w}}{value}"

    lines.append(row("handle:", p["identity"]["handle"]))
    lines.append(row("uptime:", uptime))
    lines.append(row("location:", p["identity"]["location"]))
    lines.append(row("domain:", p["identity"].get("domain", "")))
    lines.append(row("week:", f"W{iso_week:02d} {iso_year}"))
    lines.append("")
    lines.append(row("activity:", sparkline))
    lines.append("")
    if fortune_text:
        wrapped = textwrap.fill(
            fortune_text,
            width=WIDTH - 2,
            initial_indent="  ",
            subsequent_indent="  ",
            break_long_words=False,
            break_on_hyphens=False,
        )
        lines.append(wrapped)

    return "\n".join(lines)


def load_profile() -> dict:
    raw = Path(PROFILE).read_text()
    return yaml.safe_load(raw)


def render(p: dict) -> str:
    parts = []
    id_ = p["identity"]

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

    # --- NAME ---
    parts.append("## NAME")
    parts.append("")
    parts.append(f"**{id_['handle']}** - {id_['title']}")
    parts.append("")

    # --- SYNOPSIS ---
    parts.append("## SYNOPSIS")
    parts.append("")
    parts.append("```bash")
    for line in p.get("synopsis", []):
        parts.append(f"    {line.format(handle=id_['handle'])}")
    parts.append("```")
    parts.append("")

    # --- DESCRIPTION ---
    parts.append("## DESCRIPTION")
    parts.append("")
    parts.append(wrap(p["summary"]))
    parts.append("")
    parts.append(f"**Name:** {id_['name']}  ")
    parts.append("")

    # --- STATUS (neofetch-style + sparkline + fortune) ---
    parts.append("## STATUS")
    parts.append("")
    parts.append("```text")
    parts.append(render_status(p))
    parts.append("```")
    parts.append("")

    # --- ORIGIN (bio) ---
    if "bio" in p and p["bio"]:
        parts.append("## ORIGIN")
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

    return "\n".join(parts)


def main():
    profile = load_profile()
    readme = render(profile)
    Path(README).write_text(readme)
    print("README.md generated")


if __name__ == "__main__":
    main()
