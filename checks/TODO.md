# TODO

Suggestions for possible linting checks.
These could be be migration filters, post build checks, specifications or all.

- [] Extra long articles
- [] Unbalanced structure. e.g.
  - [X] Excessivly long titles.
  - [X] More than two children, less than 10 (`meta.siblings`, currently 4 to 8).
  - [] Load balancing (check with usage statistics).
- [] Long unbroken paragraphs.
- [] Unbalanced headings e.g.
  - [X] H1,H2,H3 must be less than x characters.
  - [X] No floating headers (e.g. no H2 without H1).
  - [] More than 1 child, less than 5.
- [] Blockquotes in weird places.
- [] Use of wrong tense
- [] Lines too long (< 90)
- [X] Glossary
  - [X] Use dictionary from spellcheck (both come from [nesi-wordlist](https://github.com/nesi/nesi-wordlist))
- [X] Impliment accesability standards and automatic checking (`run_a11y_check.sh`, `run_aria_check.py`).
  - [nz spec](https://www.digital.govt.nz/standards-and-guidance/nz-government-web-standards/web-accessibility-standard-1-1/)
  - [WCAG spec](https://www.w3.org/TR/WCAG21/)
- [] Automate checking all SLURM codeblocks run on the cluster.
- [] Automated tests for the checks: run each check on `fail_checks.md` and compare with the expected annotations.
