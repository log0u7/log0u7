```text
LOG0U7(1)                       User Commands                        LOG0U7(1)

    __            ____       _____
   / /___  ____ _/ __ \__  _/__  /
  / / __ \/ __ `/ / / / / / / / / 
 / / /_/ / /_/ / /_/ / /_/ / / /  
/_/\____/\__, /\____/\__,_/ /_/   
        /____/                    
```

`log0u7` - Staff/Principal Platform Engineer AI/ML Security Tooling

*Updated: 2026-07-01*

## NAME

**log0u7** - Staff/Principal Platform Engineer AI/ML Security Tooling

## SYNOPSIS

```bash
    log0u7 [--skills] [--format man] [--section <section>]
    log0u7 --ai orchestration --platform kubernetes
    log0u7 --skills --filter languages
```

## DESCRIPTION

Self-taught platform engineer designing and operating infrastructure, AI/ML
and developer experience platforms. Multi-language stack (Python, Ruby, Perl,
PHP, C/C++, Java, R, Prolog, VimScript).

**Handle:** `log0u7`  
**Name:** G.K.E.  
**Location:** France  
**Since:** 1984  
**Domain:** Platform Engineering / AI/ML / Security Tooling  

### Origin

Born in 1984. The fascination started before any keyboard. TV commercials for
home computers, the director's machine at nursery school glimpsed through a
half-open door, NES and MasterSystem controllers at friends' houses: the
screens were already there, doing things, long before I knew how to make them
do anything I wanted.

First actual contact came around 1990-91 at primary school: Thomson TO7/MO5
units, the "Informatique pour Tous" plan, mostly sticking tape on the
keyboards rather than shipping code, but BASIC snuck in anyway.

The real thing came a year or two later. My father brought home a VTech Laser
500: cassette deck, fifteen-minute load times, a Scheidegger BASIC course in a
grey briefcase. My first machine. Still have it. Between eight and ten years
old I wrote agenda apps, calculators, text games, fractal generators, all in
BASIC, none of it useful, all of it mine.

1993, age nine: DOOM on a 486DX2/66 with 4 MB RAM and a Sound Blaster, at
school, because at home I still had the Laser 500. That demo rewired something
permanently. A machine building 3D worlds in real time. Game over for every
other hobby.

1994, age ten: my aunt passed me her Amstrad CPC 6128+ with Locomotive BASIC,
CP/M, a 3-inch floppy drive, and a stack of listing books riddled with
publisher typos. You typed pages of code, hit RUN, got a syntax error on line
340, and debugged it for hours. That was the curriculum. No Stack Overflow. No
forums. Just the listing and the machine.

Around 1995-96, while everyone else was on PlayStation, I was on Super
Nintendo with an Action Replay 2. Not to cheat, or not only: to understand
what the codes actually did, which memory addresses they patched, what
happened when you changed a byte. Freeze the game, inspect the value, modify
it, see what broke. That was the first real taste of reverse engineering,
before I had a word for it, before I had a PC, before I had x86 assembly. Just
a cartridge, a code device, and a question.

1996-97: first personal PC, Pentium then AMD K6. Warcraft 1 and 2, C, x86
assembly, Quake, Quake 2. BBS and newsgroups slowly dissolving into the web.
The Action Replay habit followed onto PlayStation and then the PC: same
instinct, better tools. 1998: StarCraft and Brood War, three perfectly
balanced races, entire nights of micro-management. 1999: Quake 3, Unreal
Tournament, Counter-Strike on the Half-Life engine, the tactical FPS online,
invented in a garage. 2000: organized CS with a clan, LAN parties, Linux
install parties, then PHP, Python, Ruby.

Post-2001: the MMO era hit hard. T4C (The 4th Coming), then DAoC, nights of
farming and PvP in persistent worlds that kept turning when you logged off. No
WoW yet, but the addiction was already wired in.

2007-2008: a second track started quietly alongside the gaming. A Perl harness
strapped to GDB, automating the tedious parts of exploit development: fuzz the
offset, resolve the JMP ESP gadget, build the payload, fire. Stack overflows,
format strings, ret2libc, each technique abstracted behind a common interface.
Not impressive by any standard. At the time, watching it land a shell on its
own for the first time was enough.

2009: SWI-Prolog replaced the hardcoded if/else dispatch. Target properties
became facts, exploitation preconditions became rules, and the engine could
reason about which technique to apply instead of just iterating. At the time I
was working as a self-taught sysadmin at the Universite de Provence, campus
Saint-Charles in Marseille, where Alain Colmerauer (creator of Prolog, 1972,
Luminy, ten minutes away) was retired but still around. He talked about his
language to a sysadmin who did not know what logic programming was. That
conversation was enough.

2009-2012 ran on two tracks simultaneously. One was the WoW server: MaNGOS on
a VPS, CMake compiles pegging every core, MySQL with accounts and quest
templates, a launcher, a signup system, game masters, a community, all self-
taught, zero budget. The other track was the Prolog inference engine growing
into a genetic algorithm: populations of strategy configurations evaluated in
parallel via Parallel::ForkManager, fitness measured as exploitation success
rate, generations converging on weight inversions that human intuition had
never found. Both tracks ran on the same Core 2 Duo, in the same Marseille
apartment.

2010: discovered Metasm, Yoann Guillot's pure-Ruby binary analysis suite, via
an exploitation tutorial on the Sogeti ESEC lab blog. Where the Perl/GDB
system orchestrated external tools, Metasm internalized everything: assembler,
disassembler, debugger interface, ELF/PE parsers, all in one library. Learning
Ruby through Metasm's codebase opened an entire ecosystem: Puppet, Foreman,
early GitLab. The exploitation framework became an infrastructure career.
Funny how that works.

Post-2012: industrialized deployments of TeamSpeak and Mumble servers, Steam
game servers for CS:GO and ARK. Ran a cross-server ARK community with plugins,
synchronized wipes, GM events, and centralized configs. Ops at scale, still
for fun. In parallel, a separate R/ML track: neural networks, predictive
models, weather first, then forex and crypto. Same pattern as the exploit
engine (profile, predict, act, learn), different domain.

Around 2018, Python unified both lines. pwntools for binary profiling,
z3-solver for numerical constraints, PyTorch replacing R for the models. Ruby
stayed for the exploitation layer; Python became the orchestrator. 2019: first
contextual bandits (Thompson sampling) replacing the static GA weights. 2023:
LLM integration (GPT, then Ollama for local inference).

2024-2026: the architecture settled into six layers (fuzzing, profiling,
Datalog/Souffle, Bitwuzla/Z3, LLM, bandit/MCTS), validated on three public CTF
suites (24/24) and a documented kernel exploit chain. Three articles written
up, describing fifteen years of evolution from a Perl script and a Prolog
query to a hybrid neuro-symbolic pipeline.

The machines got bigger, the stack got deeper, the instinct never changed:
figure it out, build it, run it.

## STACK

### Languages / Runtimes

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Ruby](https://img.shields.io/badge/ruby-%23CC342D.svg?style=for-the-badge&logo=ruby&logoColor=white) ![Perl](https://img.shields.io/badge/perl-%2339457E.svg?style=for-the-badge&logo=perl&logoColor=white) ![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white) ![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white) ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=cplusplus&logoColor=white) ![R](https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Node.js](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=nodedotjs&logoColor=white) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Markdown](https://img.shields.io/badge/markdown-083FA1?style=for-the-badge&logo=markdown&logoColor=white)

### Shell / Terminal

![Bash](https://img.shields.io/badge/bash-%23121011.svg?style=for-the-badge&logo=gnubash&logoColor=white) ![POSIX sh](https://img.shields.io/badge/POSIX_sh-333333?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![tmux](https://img.shields.io/badge/tmux-1BB91F?style=for-the-badge&logo=tmux&logoColor=white) ![GNU Screen](https://img.shields.io/badge/GNU_Screen-A42E2B?style=for-the-badge&logo=gnu&logoColor=white) ![Starship](https://img.shields.io/badge/starship-DD0B78?style=for-the-badge&logo=starship&logoColor=white)

### AI / ML

![Anthropic](https://img.shields.io/badge/anthropic-191919?style=for-the-badge&logo=anthropic&logoColor=white) ![Claude](https://img.shields.io/badge/claude-D97757?style=for-the-badge&logo=claude&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![Ollama](https://img.shields.io/badge/ollama-000000?style=for-the-badge&logo=ollama&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=pytorch&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikitlearn&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

### Infra / Containers

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![GNU](https://img.shields.io/badge/GNU-A42E2B?style=for-the-badge&logo=gnu&logoColor=white) ![systemd](https://img.shields.io/badge/systemd-000000?style=for-the-badge&logo=systemd&logoColor=white) ![Make](https://img.shields.io/badge/make-6D00CC?style=for-the-badge&logo=make&logoColor=white) ![CMake](https://img.shields.io/badge/cmake-064F8C?style=for-the-badge&logo=cmake&logoColor=white) ![Arduino](https://img.shields.io/badge/arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white) ![PlatformIO](https://img.shields.io/badge/PlatformIO-F5822A?style=for-the-badge&logo=platformio&logoColor=white) ![Vagrant](https://img.shields.io/badge/vagrant-%231563FF.svg?style=for-the-badge&logo=vagrant&logoColor=white) ![Packer](https://img.shields.io/badge/packer-%23E7EEF0.svg?style=for-the-badge&logo=packer&logoColor=%2302A8EF) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Podman](https://img.shields.io/badge/Podman-8929D0?style=for-the-badge&logo=podman&logoColor=white) ![LXC](https://img.shields.io/badge/LXC-009688?style=for-the-badge&logo=linuxcontainers&logoColor=white) ![libvirt](https://img.shields.io/badge/libvirt-FF6600?style=for-the-badge&logo=libvirt&logoColor=white) ![QEMU](https://img.shields.io/badge/QEMU-FF5733?style=for-the-badge&logo=qemu&logoColor=white) ![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white) ![Nomad](https://img.shields.io/badge/Nomad-00A3E0?style=for-the-badge&logo=nomad&logoColor=white) ![Proxmox](https://img.shields.io/badge/Proxmox-E57000?style=for-the-badge&logo=proxmox&logoColor=white)

### IaC / Automation

![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white) ![OpenTofu](https://img.shields.io/badge/OpenTofu-7B42BC?style=for-the-badge&logo=opentofu&logoColor=white) ![OpenBao](https://img.shields.io/badge/OpenBao-1D3557?style=for-the-badge&logo=hashicorp&logoColor=white)

### Observability / Monitoring

![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white) ![VictoriaMetrics](https://img.shields.io/badge/VictoriaMetrics-3F8CE0?style=for-the-badge&logo=victoriametrics&logoColor=white) ![VictoriaLogs](https://img.shields.io/badge/VictoriaLogs-3F8CE0?style=for-the-badge&logo=victoriametrics&logoColor=white) ![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-3D348B?style=for-the-badge&logo=opentelemetry&logoColor=white) ![Loki](https://img.shields.io/badge/Loki-F46800?style=for-the-badge&logo=grafana&logoColor=white) ![Tempo](https://img.shields.io/badge/Tempo-F46800?style=for-the-badge&logo=grafana&logoColor=white) ![Jaeger](https://img.shields.io/badge/Jaeger-66CFE1?style=for-the-badge&logo=jaeger&logoColor=white) ![CouchDB](https://img.shields.io/badge/CouchDB-447E9B?style=for-the-badge&logo=couchdb&logoColor=white)

### Databases

![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### Security

![SSH](https://img.shields.io/badge/SSH-4E9A06?style=for-the-badge&logo=openssh&logoColor=white) ![GPG](https://img.shields.io/badge/GPG-0093DD?style=for-the-badge&logo=gnuprivacyguard&logoColor=white) ![OpenSSL](https://img.shields.io/badge/OpenSSL-721412?style=for-the-badge&logo=openssl&logoColor=white) ![nmap](https://img.shields.io/badge/nmap-4682B4?style=for-the-badge&logo=nmap&logoColor=white) ![OpenVAS](https://img.shields.io/badge/OpenVAS-4CAF50?style=for-the-badge&logo=openvas&logoColor=white) ![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white) ![Metasploit](https://img.shields.io/badge/Metasploit-2596CD?style=for-the-badge&logo=metasploit&logoColor=white) ![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white) ![Hashcat](https://img.shields.io/badge/Hashcat-2B2B2B?style=for-the-badge&logo=hashcat&logoColor=white)

### Reverse Engineering / Debugging

![radare2](https://img.shields.io/badge/radare2-1F2A44?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![Ghidra](https://img.shields.io/badge/Ghidra-FF6600?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![GDB](https://img.shields.io/badge/GDB-A42E2B?style=for-the-badge&logo=gnu&logoColor=white) ![DDD](https://img.shields.io/badge/DDD-A42E2B?style=for-the-badge&logo=gnu&logoColor=white) ![binwalk](https://img.shields.io/badge/binwalk-333333?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=)

### Networking / VPN / Firewall

![WireGuard](https://img.shields.io/badge/WireGuard-88171A?style=for-the-badge&logo=wireguard&logoColor=white) ![OpenVPN](https://img.shields.io/badge/OpenVPN-EA7E20?style=for-the-badge&logo=openvpn&logoColor=white) ![iptables](https://img.shields.io/badge/iptables-333333?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![nftables](https://img.shields.io/badge/nftables-333333?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![pf](https://img.shields.io/badge/pf_(BSD)-333333?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![m0n0wall](https://img.shields.io/badge/m0n0wall-1A237E?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![pfSense](https://img.shields.io/badge/pfSense-212121?style=for-the-badge&logo=pfsense&logoColor=white) ![OPNsense](https://img.shields.io/badge/OPNsense-D94F00?style=for-the-badge&logo=opnsense&logoColor=white) ![OpenWrt](https://img.shields.io/badge/OpenWrt-00B5E2?style=for-the-badge&logo=openwrt&logoColor=white) ![PowerDNS](https://img.shields.io/badge/PowerDNS-333333?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=)

### Proxy / LB / Storage

![HAProxy](https://img.shields.io/badge/HAProxy-1F3A8F?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![Varnish](https://img.shields.io/badge/Varnish-4B9CD3?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![Squid](https://img.shields.io/badge/Squid-CE2027?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![Traefik](https://img.shields.io/badge/Traefik-249EA6?style=for-the-badge&logo=traefik&logoColor=white) ![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![GlusterFS](https://img.shields.io/badge/GlusterFS-CE3226?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=) ![Consul](https://img.shields.io/badge/Consul-F24C53?style=for-the-badge&logo=consul&logoColor=white) ![Foreman](https://img.shields.io/badge/Foreman-333333?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=)

### Cloud

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

### VCS / CI

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![GitLab CI](https://img.shields.io/badge/gitlab%20ci-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)

### Editors / IDEs

![Neovim](https://img.shields.io/badge/Neovim-57A143?style=for-the-badge&logo=neovim&logoColor=white) ![Vim](https://img.shields.io/badge/Vim-019733?style=for-the-badge&logo=vim&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![OpenCode](https://img.shields.io/badge/OpenCode-000000?style=for-the-badge&logo=opencode&logoColor=white)

### Distributions

![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white) ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![AlmaLinux](https://img.shields.io/badge/AlmaLinux-10B981?style=for-the-badge&logo=almalinux&logoColor=white) ![Alpine Linux](https://img.shields.io/badge/Alpine_Linux-%230D597F.svg?style=for-the-badge&logo=alpine-linux&logoColor=white) ![Arch Linux](https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white) ![Gentoo](https://img.shields.io/badge/Gentoo-5A3D8F?style=for-the-badge&logo=gentoo&logoColor=white) ![NixOS](https://img.shields.io/badge/NixOS-5277C3?style=for-the-badge&logo=nixos&logoColor=white)


## OPTIONS

### Languages

```text
  -l python
       Python (async, FastAPI, Starlette, Pydantic, Textual, multithreaded
       client/server, web scraping)

  -l ruby
       Ruby (scripting, tooling, Metasm)

  -l perl
       Perl (systems, network, multithreaded client/server, IRC bots)

  -l php
       PHP (systems, network, MVC, custom CMF framework)

  -l r
       R (data mining, machine learning, predictive modeling)

  -l vimscript
       VimScript (async jobs, submodules, 2k+ lines)

  -l bash
       Bash (modular frameworks, Mise/Fnox)

  -l ansible
       Ansible (roles, collections, Mitogen)

  -l c
       C/C++ (systems programming, network internals, embedded Arduino/ESP)

  -l java
       Java / Groovy (Jenkins pipelines, CI automation)

  -l prolog
       Prolog / Datalog (declarative logic programming)

  -l z3-solver
       Z3 solver (SMT, verification, constraint solving)

  -l x86-assembly
       x86 assembly (DOS, basic reverse engineering)

  -l basic
       BASIC (Thomson TO7/MO5, Laser 500, Amstrad CPC 6128+, QBasic)

  -l javascript
       JavaScript / Node.js
```

### Platforms

```text
  -p docker-swarm
       Docker Swarm (multi-stack, TLS, MACVLAN, bare-metal PXE)

  -p kubernetes
       Kubernetes (CKA level, operators)

  -p nomad
       Nomad

  -p podman
       Podman, LXC, libvirt, QEMU/KVM

  -p proxmox
       Proxmox

  -p traefik
       Traefik

  -p nixos
       NixOS, Arch Linux, Gentoo, AlmaLinux
```

### AI/ML

```text
  -a multi-agent-llm-orchestration
       Multi-agent LLM orchestration (coder panel consensus lead)

  -a rag
       RAG (pgvector, sqlite-vec), Docker sandbox, streaming SSE

  -a quota
       Quota/governance, TUI (Textual), CI/CD

  -a predictive-modeling
       Predictive modeling (weather, forex, crypto)
```

### Security

```text
  -s docker-sandbox
       Docker sandbox (--network none --read-only, caps drop)

  -s zip-slip-protection
       Zip-slip protection, mTLS, secrets management (age, fnox)

  -s bug-hunting-platform
       Bug hunting platform (GraphQL, WebSocket shell, Traefik API)

  -s ssh
       SSH, GPG, OpenSSL, nmap, OpenVAS
```

### Observability

```text
  -o victoriametrics
       VictoriaMetrics, VictoriaLogs, Grafana, OpenTelemetry, ARA

  -o couchdb
       CouchDB
```

### Tooling

```text
  -t mise
       Mise, Fnox, Starship, Textual, pytest, GitLab CI, GitHub Actions

  -t opentofu
       OpenTofu, OpenBao

  -t vim
       Vim
```

## EXAMPLES

### 🟢 consensus

Orchestration multi-agents LLM production-grade (coder panel consensus lead),
RAG (pgvector/sqlite-vec), sandbox Docker securise, quota management, TUI
Textual, 6k+ lignes Python async

**Tags:** `AI/ML`, `Python`, `FastAPI`, `Docker`, `RAG`, `Textual`  
**Lines:** ~3,883  
**Tests:** 21  
**Repo:** [https://github.com/log0u7/consensus](https://github.com/log0u7/consensus)

### 🟢 myflec

Shell framework modulaire (Bash + Mise + Fnox + Starship), SSH identity model
(gitdir + host alias), validation shellcheck/bash -n, CI multi-forge

**Tags:** `DevX`, `Bash`, `Mise`, `Fnox`, `Shell`, `Starship`  
**Lines:** ~16,000  
**Repo:** [https://github.com/log0u7/myflec](https://github.com/log0u7/myflec)

### 🟢 vim-plugin-manager

Gestionnaire plugins Vim (Git submodules + packages natifs), async jobs avec
queue de concurrence, 20 tests Vader, CI multi-distro
(Alma/Debian/Ubuntu/Arch/Gentoo)

**Tags:** `VimScript`, `DevTools`, `Async`, `Testing`, `Git`  
**Lines:** ~2,507  
**Tests:** 20  
**Repo:** [https://github.com/log0u7/vim-plugin-manager](https://github.com/log0u7/vim-plugin-manager)

### 🟢 calvin

Platform IaC Docker Swarm 11 stacks (Traefik, Foreman PXE, PowerDNS/DHCP,
VictoriaMetrics/Logs, Grafana, ARA), TLS 4 modes, MACVLAN, Makefile 25k
lignes, CI GitLab

**Tags:** `IaC`, `Docker Swarm`, `Bare-metal`, `Observability`, `Foreman`, `Traefik`  
**Lines:** ~50,000  
**Repo:** [https://github.com/log0u7/calvin](https://github.com/log0u7/calvin)

### 🟢 fluolight

Controleur NeoPixel embarque (Arduino/C++), Ethernet DHCP, proxy, watchdog,
architecture modulaire 5 fichiers, 920 lignes

**Tags:** `Embedded`, `C++`, `Arduino`, `NeoPixel`, `Ethernet`  
**Lines:** ~920  
**Repo:** [https://github.com/log0u7/fluolight](https://github.com/log0u7/fluolight)

## SEE ALSO

* **Github:** [https://github.com/log0u7](https://github.com/log0u7)
* **Website:** [https://www.6admin.io](https://www.6admin.io)

## BUGS

Report issues via GitHub Issues on the relevant project repository.

Contact: [https://www.6admin.io](https://www.6admin.io)

---
*Generated on 2026-07-01T23:22:06 from `profile.yaml`*
