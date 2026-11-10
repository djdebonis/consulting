# David J. DeBonis — personal website

Hugo 0.165.0 with the `hugo-profile` Git submodule. Project-level layouts supply the editorial presentation; Bootstrap navigation and the theme's appearance switch remain in use. No Node installation is required.

## Build and preview

```sh
git submodule update --init --recursive
hugo --minify --cleanDestinationDir --printPathWarnings --panicOnWarning
python3 scripts/validate_site.py public
hugo server --bind 127.0.0.1 --disableFastRender
```

Netlify uses the pinned version and build command in `netlify.toml`. Building locally does not deploy. `public/` is tracked in this repository and should be regenerated alongside source changes. Do not hand-edit generated files.

## Editing

- `content/`: About, Experience introduction, Selected Work, Writing, Contact, and Photography.
- `config.yaml`: identity, navigation, employment history, and education. Keep dates and titles evidence-based.
- `layouts/`: project overrides; leave the theme submodule untouched.
- `static/css/editorial.css`: responsive light/dark styling.
- `static/js/search.js`: keyboard-accessible client-side search, rendering text through DOM APIs.
- `scripts/validate_site.py`: generated HTML, resource/link/anchor, metadata, schema, sitemap, RSS/XML, and search checks.
- `docs/website-audit.md`: audit decisions, sources, factual questions, and validation limitations.

Keep existing public paths when editing. If a URL must change, add a permanent redirect. Portfolio descriptions should distinguish delivered work from measured outcomes; only add outcome metrics with supporting evidence.
