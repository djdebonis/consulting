# Website audit and implementation

Audit date: November 8, 2026. No deployment, push, external-site edit, or outbound message performed.

## Findings and implementation plan

Inspection covered tracked content (including the hidden theme sample), configurations, archetypes, local layouts, theme templates/assets, build setup, generated output, and Git state. The pre-existing `.gitignore` change was left intact. No AGENTS.md was present.

The repository uses Hugo Profile as a Git submodule, one YAML configuration, and Netlify pinned to Hugo 0.165.0, matching the locally installed extended build. No active analytics ID was configured; Hugo's analytics integration remains available.

The plan derived from that inspection was to establish consistent positioning, separate detailed professional content from the homepage, substantiate selected work with public sources, centralize metadata/schema, improve the existing responsive presentation, fix search and accessibility defects, and validate generated output without deploying.

## Architecture

| Page | Route | Purpose |
| --- | --- | --- |
| Home | `/` | Positioning, expertise, background, selected work, and contact path |
| About | `/about-david-debonis/` | Formal biography, interdisciplinary background, independent interests |
| Experience & Education | `/experience/` | Repository-supported roles, titles, dates, qualifications, and tools |
| Selected Work | `/work/` | Scientific publications, consulting examples, e-commerce, research, writing |
| Writing & Publications | `/blogs/` | CU Anschutz, Seeking Synthesis, and retained archive entry |
| Contact | `/contact/` | Professional networking and consulting routes |
| Photography | `/gallery/` | Existing personal photography, linked from About and the footer |

Original content routes, article path, taxonomy paths, and homepage section anchors remain available. Removed duplicate `content/blogs.md` and the hidden theme sample `content/blogs/.md`. Former standalone page feeds redirect to home or writing feeds through Netlify. The generated, obsolete `/tags/page/2/` pagination artifact is removed; it was not a content page.

## Editorial and positioning decisions

- Standardized the preferred name to **David J. DeBonis** and the positioning to **Marketing Strategist | Science Communicator | Writer**.
- Used first person for the homepage introduction and third person for the formal biography. Retained teaching, writing-center, linguistic research, and photography material.
- Presented science communication as a specialization alongside marketing and operational experience, rather than implying a narrow academic identity or an agency homepage.
- Added documented work for Colorado Sauce Company and TGB Flooring. No conversion, revenue, ranking, or campaign-performance claims were invented.
- Kept Antilo Design, Seeking Synthesis, and CU Anschutz publications distinct. Did not claim the ventures were the same organization.
- Corrected “M.S. Marketing and Communications” to “M.S. in Marketing,” consistent with the existing detailed degree description, the user's supplied background, and CU Denver's program page.
- Preserved employment titles/dates and degree completion dates from the repository rather than guessing corrections. Consulting dates are omitted because none were documented.
- Replaced the old health-writing destination with the corresponding article linked from Seeking Synthesis. Kept the archive entry's original date and explained that the external publication may have changed.
- Removed the misleading linguistics-chart thumbnail from the biomedical communication project. Retained the original portrait, logo, photography, research links, and source image assets.
- Omitted the personal Gmail address from the rendered site in favor of professional profile/venture links, consistent with the instruction not to expose private contact information.
- Removed unsupported current certification emphasis from the biography; health and wellness interests remain. Certification status is an open question below.

## SEO, performance, accessibility, and behavior

- One title, description, canonical, and set of social sharing metadata per page; default portrait social image and per-page archive image.
- Person and WebSite JSON-LD; ProfilePage only on Home/About; ContactPage and CollectionPage where appropriate; ordinary WebPage for a short archive link rather than falsely describing it as a full research article.
- `sameAs` contains verified identity pages: GitHub, the CU Anschutz author archive, and Antilo's personal profile. It excludes publication/business homepages and LinkedIn, whose live identity could not be independently fetched.
- Sitemap includes indexable content and accurate editorial modification dates; taxonomy pages are noindex and excluded. Robots advertises the canonical sitemap. Removed meaningless per-page RSS outputs; retained home, writing, and taxonomy feeds.
- Updated deprecated Hugo `languageCode` configuration to `locale`; retained version pin. Netlify now uses clean, minified builds to prevent obsolete files surviving publication.
- Editorial serif headings, restrained green/cream colors, responsive grids, readable article widths, light/dark styling, image dimensions, lazy gallery loading, and print styles for the experience page.
- Local system fonts replace external font downloads. The pages no longer load the large Font Awesome script or unused section styles.
- One H1, language declaration, main landmark, skip link, visible keyboard focus, labeled controls, active navigation state, reduced-motion support, and unique search input IDs.
- Search uses DOM text nodes rather than interpolating queries into HTML; includes error handling, stale-request protection, Escape dismissal, and Ctrl/Cmd+K support.

## Sources and verification

Public pages accessed during the audit:

- [CU Denver M.S. Marketing](https://business.ucdenver.edu/ms/marketing): program name, not evidence of individual graduation.
- [CU Anschutz author archive](https://news.cuanschutz.edu/dbmi/author/david-debonis): authorship and published work.
- [AI uncertainty article](https://news.cuanschutz.edu/dbmi/can-ai-say-i-dont-know-healthcare) and [Cytomining article](https://news.cuanschutz.edu/dbmi/cytomining-open-source-image-based-profiling): selected science writing.
- [Antilo founder profile](https://antilodesign.com/team/): founder/lead consultant role and individual connection to the case studies.
- [Colorado Sauce Company case study](https://antilodesign.com/work/colorado-sauce-company/) and [TGB Flooring case study](https://antilodesign.com/work/tgb-flooring/): deliverables and project context. The 117-listing figure is a sample size, not an outcome metric.
- [Seeking Synthesis](https://seekingsynthesis.com/): publication identity, founder, and current circadian article link.
- [GitHub profile](https://github.com/djdebonis): identity, backlink to this site, and visible Cafelytics project listing.

Automated retrieval could not verify LinkedIn, the two ForagerOne research presentation pages, the individual Cafelytics repository, or the current circadian article body. Their links are supported by repository content or verified parent pages; retrieval failure is not treated as proof of a broken link. Recheck these manually before deployment.

## Validation

Desktop visual record: [homepage-preview.jpg](homepage-preview.jpg).

- `hugo --minify --cleanDestinationDir --printPathWarnings --panicOnWarning`: passed on Hugo 0.165.0, no warnings; 26 Hugo page outputs, 7 aliases.
- `python3 scripts/validate_site.py public`: passed on 15 non-redirect HTML documents. Checks internal destinations/fragments, resources, metadata uniqueness, JSON-LD parsing/classification, language, main landmark, H1, alt attributes, button labels, unique IDs, XML parsing, search index, robots and sitemap exclusions.
- `git diff --check -- . ':!.gitignore'`: passed. The excluded file already had a user-authored trailing blank line before this work.
- Browser preview: initial numeric-loopback request timed out; `localhost` worked. Inspected the homepage at desktop size in dark and light appearances and at 390px width; verified no horizontal overflow at 390px.
- Verified mobile navigation expansion, desktop/mobile search results, Escape dismissal, safe literal rendering of an HTML-like query, and navigation to Experience. No browser errors were reported during those interactions.
- No standalone Node binary was on PATH; browser execution supplied the search behavior check. No Lighthouse score, automated WCAG conformance, exhaustive assistive-technology test, or measured Core Web Vitals claim is made.
- Generated `public/` was refreshed, matching the repository's existing tracked-output convention. Theme submodule and pre-existing `.gitignore` edits were left intact.

## Factual questions and follow-up

1. Confirm M.S. completion in May 2026, B.A. completion in 2023, and the exact specialization wording. These are repository assertions, not independently verified academic records.
2. Confirm the teaching role's June 2024–May 2026 dates, overlapping with the August 2025 CU Anschutz start. The overlap was preserved, not silently “corrected.”
3. Confirm whether the intermittent Research Assistant role is still current, and whether all employer titles remain exact.
4. Supply consulting start dates and clarify the historical relationship between Terra Firma Consulting and Antilo Design. Only the verified current Antilo identity is presented publicly.
5. Confirm current NASM credential status before restoring certification claims. No private credential records were accessed.
6. Confirm the preferred professional contact route and LinkedIn URL. The repository's LinkedIn link remains visible but is excluded from `sameAs` pending independent confirmation.
7. Add approved portfolio visuals and measured outcomes only when available and documented. Existing case studies currently support deliverable descriptions, not commercial-impact metrics.
8. Before any future authorized deployment, manually recheck unavailable external links and perform broader device/accessibility QA. After deployment, use Search Console for sitemap submission/indexing checks and field performance monitoring.
