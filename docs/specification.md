# Specification

## Formatting

### Headers

#### Header 4

```md
# Specification (H1)

## Formatting (H2)

### Headers (H3)

#### Sub Header (H4)
```

Headers should have a blank line before and after.

'H1' (`#`) is for the page title. Setting a title here will change it in the nav also.

See [Title](#title) for more info.

'H2' (`##`) Should be the top level nav for table of contents.

### Text Emphasis

**bold**: `**bold**`

_italic_: `_italic`

### Tab Containers

=== "Tab One"
    someting in the tab
=== "Tab two"
    something else

```md
=== "Tab One"
    someting in the tab
=== "Tab two"
    something else
```

### Admonations

=== "Note"
    !!! note
        This is a test admonation.

    ```md
    !!! note
        This is a test admonation.
    ```
=== "Abstract"
    !!! abstract
        This is a test admonation.

    ```md
    !!! abstract
        This is a test admonation.
    ```
=== "Tip"
    !!! tip
        This is a test admonation.

    ```md
    !!! tip
        This is a test admonation.
    ```
=== "Info"
    !!! info
        This is a test admonation.

    ```md
    !!! info
        This is a test admonation.
    ```
=== "Success"
    !!! success
        This is a test admonation.

    ```md
    !!! success
        This is a test admonation.
    ```
=== "Question"
    !!! question
        This is a test admonation.

    ```md
    !!! question
        This is a test admonation.
    ```
=== "Warning"
    !!! warning
        This is a test admonation.

    ```md
    !!! warning
        This is a test admonation.
    ```
=== "Failure"
    !!! failure
        This is a test admonation.

    ```md
    !!! failure
        This is a test admonation.
    ```
=== "Danger"
    !!! danger
        This is a test admonation.

    ```md
    !!! danger
        This is a test admonation.
    ```
=== "Bug"
    !!! bug
        This is a test admonation.

    ```md
    !!! bug
        This is a test admonation.
    ```
=== "Example"
    !!! example
        This is a test admonation.

    ```md
    !!! example
        This is a test admonation.
    ```
=== "Quote"
    !!! quote
        This is a test admonation.

    ```md
    !!! quote
        This is a test admonation.
    ```
_Note for future, once decided which of these we will use, remove the others. And give description of when to use._

### Code

Code blocks require a language lexxer in order to do syntax hilighting, e.g. `python` ,`slurm`, `cuda`, `json`, `md`.
[A full list of lexxers can be found in this list](https://pygments.org/languages/).

For plain code blocks, still good to use a class as descriptor (e.g. `txt`, `stdout`, `stderr`).
May want to add formatting to this later.

<pre><code><span>```stdout</span>
<span>some code</span>
<span>```</span>
</code></pre>

```stderr
some code 
```

#### Block

```py
import somepackage

formatting = True
if formatting:
    Print(formatting) # A comment
```

<pre><code><span>```py</span>
<span>import somepackage</span>
<span></span>
<span>formatting = True</span>
<span>if formatting:</span>
<span>  Print(formatting) # A comment</span>
<span>```</span>
</code></pre>

#### Inline

This is some `echo "Inline Code"`.

<pre><code><span>This is some `echo "Inline Code"`.</span></code></pre>

#### Keyboard

Keyboard keys can be added using the `<kbd>` tag.

Press <kbd>ctrl</kbd> + <kbd>c</kbd> to copy text from terminal.

```md
Press <kbd>ctrl</kbd> + <kbd>c</kbd> to copy text from terminal.
```

Note the additional spacing around the `+` else it will appear cramped.

### Images

```md
![This is an image]("assets/images/FENSAP_GUI1.png")
```

![This is an image]("assets/images/FENSAP_GUI1.png")

### Links

[External Link]("https://example.com")

```md
[External Link]("https://example.com")

```

[Internal Link]("General/Announcements")

```md
[Internal Link]("General/Announcements")

```

[Anchor Link](#links)

```md
[Anchor Link](#links)

```

### Tooltips

[Hover over me](https://example.com "I'm a link with a custom tooltip.")

```md
[Hover over me](https://example.com "I'm a link with a custom tooltip.")
```

Acroynym should be automatically tooltipped e.g. MPI.

```md
Acroynym should be automatically tooltipped e.g. MPI.
```

## Structure

Public facing articles are found in the `docs` folder. Any markdown files inside will be rendered, any directory will be subcategories.
Pages can be excluded from being shown in the nav by adding them to `mkdocs.yml: not_in_nav`, as in the case of `includes`.

By default, all categories are a group only (e.g. they have nothing rendered, only children),
However, if the folder contains an `index.md` file, it will be rendered instead.

### Article Name/Location

An articles location is determined by its location in the `docs` directory.
Article file can be nested up to two folders deep, and use the title name, in snake_case.

### Title

Article title is determined in order of preference,

- A title defined in the 'title' meta-data.
- A level 1 Markdown header on the first line of the document body.
- The filename of a document.

### Headers

Unless setting a title, the first 'real' header will be an H2.
It's fine to have text before the first header if it is relevent to the entire page.

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

Try to avoid only-child headers (e.g shares a parent with at least one other header)

### Meta

Article metadata is yaml format at the top of the page between two `---`

#### Mkdocs Parameters

- `template` : which [template](#templates) to use.
- `title`    : [title](#title).

#### Material Parameters

- `description` : used for site meta.
- `icon`        : page icon.
- `status`      : `new`, `deprecated`.

#### Custom Parameters

- `prereq`      : List of prerequisites. Formatted in markdown. Will be rendered inside a admonation.
- `postreq`     : List of what next. Formatted in markdown. Will be rendered inside a admonation.

#### Zendesk Imported

Not used for anything currently. Info imported from Zendesk Page.

- `created_at`:
- `hidden`:
- `label_names`: []
- `position`:
- `vote_count`:
- `vote_sum`:
- `zendesk_article_id`:
- `zendesk_section_id`:

## Templates

Template can be set in article meta.

- `main`                : Used for regular pages (default).
- `application`         : Used for 'application' pages, will include software details header (and be linked in supported apps page).
- `supportedApplication`: For supported applications page.
- `home`                : Homepage.

By default, the `main` theme will be used. template of a theme to render Markdown pages. You can use the template meta-data key to define a different template file for that specific page. The template file must be available on the path(s) defined in the theme's environment.

## Accessability standards

- [nz spec](https://www.digital.govt.nz/standards-and-guidance/nz-government-web-standards/web-accessibility-standard-1-1/)
- [WCAG spec](https://www.w3.org/TR/WCAG21/)

{{ macros_info() }}
