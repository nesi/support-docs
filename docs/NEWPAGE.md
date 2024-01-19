---
title: 'Create a new page'
---

!!! prerequisite "See also"
    - To learn how you can contribute, [see CONTRIBUTING](CONTRIBUTING.md).
    - For examples of markdown use, [see FORMAT](FORMAT.md).

This page details how to create a new article in the documentation.

## Article Location

Public facing articles are found in the `docs` folder:

- Any directory will be subcategories.
- Any markdown file, i.e. a text file ending with the .md extension, inside will be rendered.

Pages can be excluded from being shown in the nav by adding them to `mkdocs.yml: not_in_nav`, as in the case of `includes`.

By default, all categories are a group only (e.g. they have nothing rendered, only children).
However, if the folder contains an `index.md` file, it will be rendered instead.

## Article Filename

By default, the markdown file name will be use as title of the article.
Title can also be specified in the page metadata, which is the recommended way, see the [section below](#article-metadata) for more information.

When converting the filename for the nav/title the `.md` will be dropped and 'snake_case' and 'kebab-case' will both be rendered with spaces, e.g. 'Snake case' and 'Kebab case' respectively.

The first letter of the filename will be capitalised, but not any subsequent words.

## Article Order

By default articles will be ordered alphabetically.
Article order can be m set using the `weight` property in the articles front matter, or by using the `nav` property of `mkdocs.yml`.
Lower weight values will be first in the nav.

As `weight` was inherited from Zendesk, all articles have a weight value post migration.
If ordering is not required remove the `weight` property from the front matter to allow default alphabetical ordering.

## Article Metadata

Article metadata (or 'front-matter') is yaml format at the top of the markdown file between two `---`.
This content is not rendered but will inform how the article will be rendered.

Here is an example of metadata header:

```md
---
created_at: '2021-08-25T02:05:42Z'
hidden: false
tags: []
title: 'Profiler: VTune'
vote_count: 1
vote_sum: -1
zendesk_article_id: 4405523725583
zendesk_section_id: 360000278935
---
```

The following sections detail the most usual entries.

### Mkdocs Parameters

- `title`  : article title
- `weight` : Used to set page order. Lower comes first. Migrated from Zendesk `position`. See [page order](#article-order)

### Material Theme Parameters

- `description` : Used for site meta.           : `string`
- `icon`        : Page icon.                    : `path`
- `status`      : Will display a symbol on nav  : only `new` or `deprecated` are supported
- `hide`        : Used to turn off features (e.g. table of content)    : `tags`

### Zendesk Imported

The following fieds were imported from Zendesk Page:

- `created_at`
- `hidden`
- `vote_count`
- `vote_sum`
- `zendesk_article_id`
- `zendesk_section_id`

They are not used for anything currently.

## Accessability standards

- [nz spec](https://www.digital.govt.nz/standards-and-guidance/nz-government-web-standards/web-accessibility-standard-1-1/)
- [WCAG spec](https://www.w3.org/TR/WCAG21/)
