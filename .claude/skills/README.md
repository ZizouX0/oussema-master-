# Bundled Claude Code skills

60 skills installed as **project skills**. Claude Code loads every directory
here that contains a `SKILL.md` when a session starts in this repo.

To use them everywhere instead of just in this repo, copy or symlink them into
your personal skills directory:

```bash
cp -r .claude/skills/<name> ~/.claude/skills/
```

Skill names here are unique within this repo, but several (`docx`, `pdf`,
`pptx`, `xlsx`, `canvas-design`, `algorithmic-art`, `skill-creator`,
`theme-factory`, `web-artifacts-builder`) also exist as claude.ai-synced
skills. Copying those to `~/.claude/skills/` creates a duplicate name — prefer
keeping them project-scoped.

## Dependencies

Most skills are pure instructions and need nothing installed. The ones that
ship scripts need system and language packages:

```bash
bash .claude/skills/setup-dependencies.sh
```

Two things the script can't do for you:

| Skill | Needs |
|---|---|
| `firecrawl*` | `firecrawl login`, or `FIRECRAWL_API_KEY` in the environment |
| `skill-creator` evals, `mcp-builder` evaluation | `ANTHROPIC_API_KEY` |

## Verified

Every skill was checked for a loadable `SKILL.md` (frontmatter name matching
the directory, description present), and `claude plugin validate --strict`
passes over the whole tree. Skills with executable tooling were run end to end:

| Skill | What was exercised |
|---|---|
| `docx` | docx-js generate → unpack → pack → validate → pandoc read → LibreOffice PDF → `pdftoppm` → `accept_changes.py` |
| `pptx` | pptxgenjs deck → `markitdown` read → `thumbnail.py` → unpack/pack/validate |
| `xlsx` | openpyxl workbook with a formula → `recalc.py` → value read back |
| `pdf` | PDF → images, form field extract/structure/fill, annotation fill, validation image, bounding-box check |
| `slack-gif-creator` | 12-frame eased GIF via `core.gif_builder` → `validate_gif` / `is_slack_ready` |
| `webapp-testing` | Playwright click + screenshot + console capture, `with_server.py` around a live server |
| `web-artifacts-builder` | `init-artifact.sh` scaffold → `bundle-artifact.sh` → single-file bundle rendered in Chromium with no page errors |
| `mcp-builder` | `create_connection` against a live stdio MCP server: `list_tools`, `call_tool` |
| `skill-creator` | all seven scripts via their documented `python -m scripts.<name>` form |
| `remembering-conversations` | `npm install` + full vitest suite (18/18) |
| `canvas-design` | all 54 bundled TTFs load |
| `gardening-skills-wiki`, `root-cause-tracing` | shell scripts run against this skills tree |
| `firecrawl*` | CLI installed and responding; live fetches need your API key |

## Changes made to the upstream skills

Fixes applied so the skills work in this flat, project-scoped layout:

- **Frontmatter names** — 31 skills had a title-cased `name:` (`Writing Plans`)
  that doesn't match the directory. Normalized to the directory slug so each
  skill is invocable as `/writing-plans`.
- **Trigger text** — those same skills kept their trigger in a `when_to_use:`
  field, which Claude Code doesn't read. Folded into `description:`, which is
  what drives auto-invocation.
- **Cross-references** — 86 links pointed at the upstream nested layout
  (`skills/testing/condition-based-waiting/`). Rewritten to resolve here;
  `firecrawl-cli` links now point at the `firecrawl` hub skill.
- **`pdf/scripts/convert_pdf_to_images.py`** — created the output directory it
  writes into; the documented invocation passes a directory that doesn't exist
  yet and crashed.
- **`web-artifacts-builder/scripts/bundle-artifact.sh`** — the scaffold's
  `index.html` links `/favicon.svg` from `public/`, which Parcel resolves from
  the project root and fails on. The favicon link is now dropped for the build
  and `index.html` restored afterwards.
- **`mcp-builder`** — `streamablehttp_client` was renamed in MCP SDK 2.0;
  added a fallback import and pinned `mcp<2.0.0`, which the scripts target.
- **`remembering-conversations`** — `getDbPath()` ignored the `TEST_DB_PATH`
  override its own tests set, so running the suite wrote into the real
  conversation index at `~/.config/superpowers/` and 2 tests failed with
  accumulated rows. Honoring the override fixes both.
