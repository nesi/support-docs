# Writing Articles

## Templates

Template can be set in article meta.

- `main`                : Used for regular pages (default).
- `application`         : Used for 'application' pages, will include software details header (and be linked in supported apps page).
- `supportedApplication`: For supported applications page.
- `home`                : Homepage.

By default, the `main` theme will be used. template of a theme to render Markdown pages. You can use the template meta-data key to define a different template file for that specific page. The template file must be available on the path(s) defined in the theme's environment.

## Structure

By default, all categories are a group only (e.g. they have nothing rendered, only children),
However, if the folder contains an `index.md` file, it will be rendered instead.

## Article Name/Location

An articles location is determined by its location in the `docs` directory.
Article file can be nested up to two folders deep, and use the title name, in snake_case.

### Title

Article title is determined in order of preference,

- A title defined in the 'title' meta-data.
- A level 1 Markdown header on the first line of the document body.
- The filename of a document.

## Meta

Article metadata is yaml format at the top of the page between two `---`

### Mkdocs Parameters

- `template` : which template to use.
- `title`    : title, see above.

### Material Parameters

- `description` : used for site meta.
- `icon`        : page icon.
- `status`      : `new`, `deprecated`.

### Custom Parameters

- `prereq`      : List of prerequisites. Formatted in markdown. Will be rendered inside a admonation.
- `postreq`     : List of what next. Formatted in markdown. Will be rendered inside a admonation.

### Zendesk Imported

Not used for anything currently. Info imported from Zendesk Page.

- `created_at`:
- `hidden`:
- `label_names`: []
- `position`:
- `vote_count`:
- `vote_sum`:
- `zendesk_article_id`:
- `zendesk_section_id`:


## Formatting

Most details about the extra markdown features can be found here.
Will copy the specifics that apply to this site when I get time.

https://squidfunk.github.io/mkdocs-material/reference/

## Code Formatting

### Blocks

    import tensorflow as tf
    import numpy as numpy

Preferably

```py
import tensorflow as tf
import numpy as np 
```

Preferablyer

```py title="myScript.py"
import tensorflow as tf
import numpy as np 
```

All available lexers
https://pygments.org/docs/lexers/

### Inline

The command `ls -latr`

Or preferably

This codeblock '#!bash echo "is inline"

### Snippet from another file.

```md
--8<-- "../../includes/images/glossary/.dictionary.md"
```
