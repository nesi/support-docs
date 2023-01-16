# TODO

These could be be migration filters, post build checks, specifications or all.

- [] Remove trash inline css/hmtl (wysiwug/dfn)
- [] Find uncapitalised and unmacroned maui/mahuika (outside of code blocks)
- [] Unbalanced structure. e.g.
  - [] Excessivly long titles.
  - [] More than two children, less than 10.
  - [] Load balancing (check with usage statistics).
- [] Extra long articles
- [] Long unbroken paragraphs.
- [] Unbalanced headings e.g.
  - [] H1,H2,H3 must be less than x characters.
  - [] No floating headers (e.g. no H2 without H1).
  - [] More than 1 child, less than 5.
- [] Blockquotes in weird places.
- [] Use of wrong tense
- [] Lines too long (< 90)
- [] Linting
- [x] Spellchecking
- [] Glossary
  - [] Use dictionary from spellcheck
  - [] Create 'abbreviations'.
  - [] Generate glossary page.
- [] Remove duplicate ids.
- [] Convert quote blocks into 'Admonitions'.
- [] Convert links to relative internal links
e.g "https://support.nesi.org.nz/hc/en-gb/articles/360000624696" needs to be converted to
"Scientific_Computing/Terminal_Setup/MobaXterm_Setup(Windows).md"
- [] Image downloading
images currently hosted support.nesi need to be copied to `/includes/images` and link changed. e.g. `https://support.nesi.org.nz/hc/article_attachments/4411672582031/mceclip4.png` to `includes/images/mceclip4.png`

- [] Impliment accesability standards and automatic checking.
  - [nz spec](https://www.digital.govt.nz/standards-and-guidance/nz-government-web-standards/web-accessibility-standard-1-1/)
  - [WCAG spec](https://www.w3.org/TR/WCAG21/)

- [] SLURM lexxer?
- [] Automate checking all SLURM codeblocks run on the cluster.
- [] Replace dynamic app blocks with templates.
- [] `home.html` theme could be made more robust. Includes hardpaths to assets.