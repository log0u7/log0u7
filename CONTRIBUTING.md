# CONTRIBUTING

`README.md` is the GitHub profile page. It is written and maintained by hand,
with no generator and no CI step.

## Making changes

1. Edit `README.md` directly.
2. Preview the Markdown in GitHub or through the API:

   ```bash
   gh api markdown -f mode=gfm -F text=@README.md --jq '.'
   ```

3. Commit with a `feat:`, `fix:`, `docs:` or `chore:` prefix.

## Conventions

- English content.
- No em dash. Use `:`, `,`, parentheses or a plain hyphen.
- One project entry: linked name, one-line outcome, then four badges.
- Badges use shields.io `flat-square`: language first, then three key technologies.
- Use a known Simple Icons slug when available. Otherwise use a label-only badge
  with a neutral dark color.
- Project links must point to public repositories.
- Keep the page scannable on mobile: short descriptions, no wide tables.
