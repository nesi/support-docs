---
title: Create a new page
---

**[CLICK TO VIEW THIS PAGE RENDERED IN MKDOCS](https://nesi.github.io/support-docs/NEWPAGE/)**{ .hidden }

!!! prerequisite "See also"
    - To learn how you can contribute, [see CONTRIBUTING](CONTRIBUTING.md).
    - For examples of markdown use, [see FORMAT](FORMAT.md).

This page details how to create a new article or category in the documentation.

## Article/Category Location

Public facing articles are found in the `docs` folder:

- Any directory will be a category.
- Any markdown file, i.e. a text file ending with the `.md` extension, inside will be rendered as an article.
- A directory containing a `index.md` file will be both an article and category.
(clicking on will take to the rendered markdown in `index.md`, any other markdown in the directory will be nested articles.)

![Documentation Structure](assets/images/doc_struct.png)

## Article/Category Naming

By default, the file name will be use as title of the article/category.

Try to keep your title short enough that it does not 'wrap' (become more than one line) in the nav,
this usually happens around 24-ish characters however this will vary depending on the letters being used.

!!! tip "File Name hygiene"
  Regular 'snake_case' naming conventions should be used for articles/categories.

  i.e. No non-alphanumeric characters (except `_` and `-`).
  
  When converting from filename, to title, spaces will replace `_` and the first letter of the first word will be capitalised (if it wasn't already).

  e.g. `My_Nice_and_Tidy_Filename.md` -> `My Nice and Tidy Filename`

In the case of an articles (including category-articles), this title can be overridden by setting one in the page [front-matter using the 'title' keyword](#article-metadata).
If you need to rename a regular category (one without an `index.md`), this can be done in the [`.pages.yml` file](#articlecategory-order).

## Article/Category Order

By default articles will be ordered alphabetically.

Order can be set manually with the use of a `.page.yml` file, this file determines the ordering of all of it's sibling articles and categories.

The `.page.yml` might looks like this:

```yml
---
nav: 
  - Introduction.md
  - Next_Steps.md
  - ... 
```

`...` will be replaced by all other pages, in the default order.

!!! warning
    If you do set page order manually, make sure you include the `...` else some pages will not be rendered.

When being used to order _non-article categories_ you may overwrite the name in `.page.yml`.

Don't use this method to set the names of articles or category-articles (use the `title` parameter in that pages meta).

```yml
nav:
- Getting_Started
- Māui-Mahuika (Differences) : Maui_Mahuika_Differences
- ZA̡͊͠͝LGΌ H̸̡̪̯ͨ͊̽̅̾̎Ȩ̬̩̾͛ͪ̈́̀́͘ ̶̧̨̱̹̭̯ͧ̾ͬC̷̙̲̝͖ͭ̏ͥͮ͟Oͮ͏̮̪̝͍M̲̖͊̒ͪͩͬ̚̚͜Ȇ̴̟̟͙̞ͩ͌͝S̨̥̫͎̭ͯ̿̔̀ͅ : Using_regex_to_parse_html
- ...

```

For full description of `.pages.yml` use, see the [awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin).

## Article Metadata

Article metadata (or 'front-matter') is `yaml` format at the top of the markdown file between two `---`.
This content is not rendered but will inform how the article will be shown.

Here is an example of metadata header:

```yml
---
created_at: '2021-08-25T02:05:42Z'
tags:
- profiling
title: VTune
description: VTune is a tool that allows you to quickly identify where most of the execution time of a program is spent.
vote_count: 1
vote_sum: -1
zendesk_article_id: 4405523725583
zendesk_section_id: 360000278935
---
```

The following sections detail the most usual entries.

### Mkdocs Parameters

- `title`  : article title

### Material Theme Parameters

- `description` : This will appear when Googling, or using the internal search. : `string`
- `icon`        : Page icon.                                                    : `path`
- `status`      : Will display a symbol on nav                                  : only `new` or `deprecated` are supported
- `hide`        : Used to turn off features (e.g. table of content)             : `tags` `toc` `nav`

### Zendesk Imported

The following fields were imported from Zendesk Page:

- `created_at`
- `vote_count`
- `vote_sum`
- `zendesk_article_id`
- `zendesk_section_id`

They are not used for anything currently, although comparing vote count, and vote sum is useful for gauging the popularity of a page migration.

## Accessibility Standards

- [nz spec](https://www.digital.govt.nz/standards-and-guidance/nz-government-web-standards/web-accessibility-standard-1-1/)
- [WCAG spec](https://www.w3.org/TR/WCAG21/)
