# Publishing the native GitHub Wikis

The project documentation source is already committed in each repository under `docs/wiki/`. GitHub's native Wiki is a separate Git repository, so the normal repository Contents API cannot publish those pages directly.

## One-time setup

1. Open each repository's **Settings → General → Features**.
2. Enable **Wikis**.
3. Open the Wiki tab and create the first page if GitHub prompts you to initialize it.
4. Install and authenticate the GitHub CLI: `gh auth login`.

## Publish the prepared pages

From a local clone of this profile repository, run:

```bash
bash scripts/publish-wikis.sh
```

The script copies `Home.md` and `Architecture.md` from each repository's `docs/wiki/` folder into its native `.wiki.git` repository and pushes the pages. It skips repositories where the Wiki is disabled or inaccessible.

Review the diff before publishing if you have made local edits to any Wiki page.
