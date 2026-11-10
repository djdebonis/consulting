# Editorial voice review

Reviewed November 8, 2026. Source edits only; no deployment, push, or submission to an external AI detector.

## Voice evidence

This pass compared the new site copy with the repository's previous homepage introduction, About page, experience descriptions, education notes, and circadian-rhythm introduction (`git show HEAD:...`). It also read David's [Seeking Synthesis founder note](https://seekingsynthesis.com/) and [Antilo profile](https://antilodesign.com/team/).

The recurring qualities were first-person curiosity, an interest in language and human experience, direct explanations of research, and a willingness to acknowledge what evidence cannot establish. The historical homepage and founder note provide stronger guidance for the personal site's voice than the consulting site's promotional language. These are reference samples associated with David, not independently authenticated samples of unaided authorship.

Editorial approach: use plain descriptions of actual work, retain the researcher's care with claims, and let personal interests appear without adding anecdotes or invented results. Keep the About page as a formal third-person biography; use first person in the portfolio, writing pages, and contact copy. Preserve exact professional titles, dates, links, and existing project anchors.

## Page coverage

All 15 non-redirect HTML pages were accounted for through their source content and shared templates. The existing rendered utility/taxonomy pages were also read directly. No hidden content file remains in the content directory.

| Page | Review and action |
| --- | --- |
| `/` | Rewrote abstract introductory copy and repetitive section slogans; named the actual work and employers. Replaced the portrait's branding caption with a description. Kept the user’s core hero statement, positioning line, section structure, and anchors. |
| `/about-david-debonis/` | Kept third-person biography; replaced broad claims with roles and projects. Simplified headings and independent-interests copy. Updated description. |
| `/experience/` | Added a direct first-person introduction; clarified consulting and writing-center descriptions. Reviewed every role, research presentation, tool, degree, and date. Kept factual records intact. |
| `/work/` | Rewrote project accounts in first person with concrete responsibilities. Preserved qualifications around the housing research and the limited contribution to Cafelytics. Kept headings and link targets. |
| `/blogs/` | Explained where to find the writing instead of using a generic statement about communication. Removed repeated organizational disclaimers. |
| `/blogs/circadian_rhythm_article/` | Made the archive introduction and date note personal and direct. Preserved the caveat that the linked version may differ. |
| `/contact/` | Replaced formal third-person inquiry language with direct first-person invitations; preserved contact destinations. |
| `/gallery/` | Simplified introduction. Reviewed all six captions/alt descriptions and retained their factual language. |
| `/404.html` | Reviewed; existing short navigation guidance already reads naturally. No edit needed. |
| `/categories/` | Reviewed empty taxonomy page and inherited labels; no promotional prose to rewrite. |
| `/tags/` | Reviewed taxonomy labels; retained them. |
| `/tags/article/` | Reviewed inherited archive title and description; retained accurate labels. |
| `/tags/blog-post/` | Reviewed inherited archive title and description; retained accurate labels. |
| `/tags/science-communication/` | Reviewed inherited archive title and description; retained accurate labels. |
| `/tags/writing/` | Reviewed inherited archive title and description; retained accurate labels. |

Shared surfaces reviewed: navigation, footer, search input labels, accessibility labels, metadata descriptions, social descriptions, structured-data descriptions, search-index text sources, list entries, gallery captions, and the experience template. The site's default description now identifies David and what the site contains directly. Existing factual page descriptions and utility labels were retained where no rewrite was needed. JavaScript, CSS, link destinations, and generated output were not edited in this pass.

## Representative changes

- “I connect research, storytelling, and digital strategy…” became a first-person introduction tied to marketing, writing, language, and how readers understand information.
- “A wider field of curiosity” became “Outside my day-to-day work.”
- “Connecting a brand’s next chapter” became “Colorado Sauce Company’s brand transition.”
- “These examples show the subjects, responsibilities, and published outputs behind the experience” became a short explanation of what the portfolio links contain.
- “Have something worth communicating?” became “Let’s talk.”

The goal was not to remove all polished phrasing, lists, or professional terminology. It was to remove repetition and claims that could describe almost anyone, while keeping the design and professional purpose the user liked.

## Verification and limits

The coordinating agent reviewed the edits, retained the original hero line from the user’s brief, and removed two wording changes that implied unsupported frequency or a more specific training audience.

Validation completed after the copyedit:

- `hugo --minify --cleanDestinationDir --printPathWarnings --panicOnWarning`: passed without warnings.
- `python3 scripts/validate_site.py public`: passed for all 15 non-redirect HTML pages, including internal links/anchors, resources, metadata, schema, XML, and search output.
- `git diff --check -- . ':!.gitignore'`: passed; pre-existing user changes to `.gitignore` were preserved.
- Generated `public/` was refreshed. No CSS, JavaScript, or layout structure changed.
- A fresh browser preview was blocked by the browser URL policy, so no new visual verification is claimed for this copyedit. The existing homepage screenshot records the earlier version.

Voice matching remains an editorial judgment, based on the available samples. This is not a claim that David personally wrote every revised sentence. No AI-checker result is claimed or guaranteed, and no detector-gaming techniques were used. The factual questions already recorded in `website-audit.md` remain open; this copyedit does not verify degree dates, role overlaps, or credential status.

## Follow-up review — November 9, 2026

The earlier review missed an editorial artifact: “I’ve kept the original date…” described site maintenance in the author's voice. Removed that sentence and its speculative republishing caveat. The article's original date remains in front matter without an explanation in the public copy.

Reviewed all content pages, homepage/experience templates, shared copy, and metadata again for process narration and generic phrasing. Also removed explanations such as “Each links to…” and “The roles and research projects below…”, replaced the article's archive-management meta description with its subject, and made the Writing introduction and scientific article summaries more specific. Simplified vague statements about the publication's purpose. Retained the research-specific limitation on causal inference, which is substantive rather than editorial housekeeping. No credentials, dates of employment, project outcomes, or link destinations changed.

Rebuilt tracked output. Warning-free Hugo build, all 15 HTML-page validation checks, and whitespace checks passed. This follow-up supersedes the earlier report's decision to retain the archive caveat. No deployment or detector submission performed.
