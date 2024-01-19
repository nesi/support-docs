**[CLICK HERE TO VIEW THIS PAGE RENDERED IN MKDOCS](https://nesi.github.io/support-docs-concept/format/)**{ .hidden }

!!! prerequisite "See also"
    - To learn how you can contribute, [see CONTRIBUTING](CONTRIBUTING.md).
    - For examples of markdown use, [see FORMAT](FORMAT.md).

## Structure

Public facing articles are found in the `docs` folder. Any markdown files inside will be rendered, any directory will be subcategories.
Pages can be excluded from being shown in the nav by adding them to `mkdocs.yml: not_in_nav`, as in the case of `includes`.

By default, all categories are a group only (e.g. they have nothing rendered, only children),
However, if the folder contains an `index.md` file, it will be rendered instead.

### Article Name/Location

An articles location is determined by its location in the `docs` directory.
Article file can be nested up to two folders deep, and use the title name, in snake_case.

### Article Order

By default articles will be ordered alphabetically.
Article order can be m set using the `weight` property in the articles front matter, or by using the `nav` property of `mkdocs.yml`.
Lower weight values will be first in the nav.

As `weight` was inherited from Zendesk, all articles have a weight value post migration.
If ordering is not required remove the `weight` property from the front matter to allow default alphabetical ordering.

### Title

Headers should have a blank line before and after.

#### Succession

Article title has the following succession,

- A title defined in the 'title' meta-data.
- A level 1 Markdown header on the first line of the document body.
- The filename of a document.

Our preference is the opposite (filename > H1 > meta).

#### Filename Rendering

When converting a filename for the nav/title the `.md` will be dropped and 'snake_case' and 'kebab-case' will both be rendered with spaces, e.g. 'Snake case' and 'Kebab case' respectively.

The first letter of the filename will be capitalised, but not any subsequent words.

(Note: Choose only one for naming convention)

### Sub Headers

Unless setting a title, the first 'real' header will be an H2.
It's fine to have text before the first header if it is relevant to the entire page.

No skipping levels, e.g.

```md
H2
H3
H4
```

never

```md
H2
H4
```

Try to avoid only child headers (e.g shares a parent with at least one other header).

## Meta

Article metadata (or 'front-matter') is yaml format at the top of the page between two `---`.
Content is not rendered.

### Mkdocs Parameters

- `title`    : [title](#title).
- `weight`   : Used to set page order. Lower comes first. Migrated from Zendesk `position`.
               See [page order](#article-order)

### Material Parameters

- `description` : Used for site meta.           : `string`
- `icon`        : Page icon.                    : `path`
- `status`      : Will display a symbol on nav  : only `new` or `deprecated` are supported
- `hide`        : Used to turn off features (e.g. table of content)    : `tags`

### Zendesk Imported

Info imported from Zendesk Page:

- `created_at`
- `hidden`
- `vote_count`
- `vote_sum`
- `zendesk_article_id`
- `zendesk_section_id`

Not used for anything currently.


### Accessability standards

- [nz spec](https://www.digital.govt.nz/standards-and-guidance/nz-government-web-standards/web-accessibility-standard-1-1/)
- [WCAG spec](https://www.w3.org/TR/WCAG21/)
