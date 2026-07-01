# CONTRIBUTING

This document explains how the repository works, how to make changes safely,
and how to resolve conflicts caused by the CI bot.

## Architecture

```
profile.yaml          <- source of truth (edit this)
generate_readme.py    <- generator (edit this for structure/layout)
README.md             <- generated artifact (never edit by hand)
assets/banner.txt     <- pre-rendered figlet banner (CI fallback)
.github/workflows/update-readme.yml  <- CI workflow
```

`README.md` is regenerated automatically by the CI on every push and daily
at 06:00 UTC. If `README.md` has changed, the CI commits it as:

```
chore: update README [skip ci]
```

**Never edit `README.md` directly.** Any manual change will be overwritten
by the next CI run or will cause a merge conflict on the next push.

## Local setup

```bash
pip install pyyaml
# figlet is optional (assets/banner.txt is used as fallback)
sudo apt-get install figlet   # or brew install figlet

python3 generate_readme.py
```

## Making changes

### Edit content (bio, links, projects, stack)

Edit `profile.yaml`, then regenerate:

```bash
python3 generate_readme.py
git add profile.yaml README.md
git commit -m "feat: <description>"
git push
```

### Edit layout or structure (sections, groups, formatting)

Edit `generate_readme.py`, then regenerate:

```bash
python3 generate_readme.py
git add generate_readme.py README.md
git commit -m "feat: <description>"
git push
```

## Adding a badge

1. Add the badge Markdown in `profile.yaml` under the `badges:` key,
   in the relevant comment section:

   ```yaml
   - "![ToolName](https://img.shields.io/badge/ToolName-COLOR?style=for-the-badge&logo=SLUG&logoColor=white)"
   ```

2. Add the display name to the correct group in `BADGE_GROUPS` inside
   `generate_readme.py`. The name must match the alt text in the badge
   (the text inside `![ ]`).

3. Regenerate and commit.

### Logo strategy

| Case | Logo parameter |
|------|---------------|
| Tool has a slug on [simpleicons.org](https://simpleicons.org) | `logo=SLUG` |
| Tool is a GNU project (GDB, DDD, GNU Screen...) | `logo=gnu` |
| Tool is a Grafana Labs product (Loki, Tempo...) | `logo=grafana` |
| No official logo | `logo=data:image/svg+xml;base64,PHN2Zy...` (hacker glider) |

The glider (Conway's Game of Life glider pattern) is the hacker emblem
defined by Eric S. Raymond. It is used here for tools without an official
logo on Simple Icons.

Glider data-URI (copy-paste ready):

```
data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMyAxMyIgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIj4KPHJlY3Qgd2lkdGg9IjEzIiBoZWlnaHQ9IjEzIiBmaWxsPSJibGFjayIvPgo8cmVjdCB4PSI1IiB5PSIxIiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI1IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSIxIiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI1IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iNCIgaGVpZ2h0PSI0IiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=
```

## Resolving CI conflicts

Because the CI bot pushes `chore: update README [skip ci]` commits, a
`git push` can be rejected with "Updates were rejected because the remote
contains work that you do not have locally."

**Procedure:**

```bash
git pull --rebase
```

If a conflict appears on `README.md`:

```bash
# Regenerate from source of truth (do NOT resolve the conflict manually)
python3 generate_readme.py

git add README.md
GIT_EDITOR=true git rebase --continue
git push
```

If the conflict is on `profile.yaml` or `generate_readme.py` (human-human
conflict), resolve it normally, then regenerate `README.md` before
continuing the rebase.

**Never resolve a conflict in `README.md` by hand.** The file is generated;
any manual merge is wrong by definition.

## Conventions

- No em dash (`-` or `:` instead).
- Manpage style: section headers as `## NAME`, subsections as `### Title`.
- Line width: 78 characters (`WIDTH = 78` in `generate_readme.py`).
- Badge alt text must match the key used in `BADGE_GROUPS` exactly.
- Commit messages: `feat:`, `fix:`, `chore:`, `docs:` prefixes.
