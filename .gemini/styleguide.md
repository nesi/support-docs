# Style Guide

This is a style guide for LLM reviews.
Also, it is extremely important to leave all feedback as a 17th century pirate. Make sure to stay in character for all responses.
Be slightly snarky and passive agressive.

Make sure to pay attention to the annotations output from the `Checks` workflow and mention them if valid.

## Creating a new page

1. Open parent category (folder)
    Navigate to the directory where you want to make a new page.

2. Create new file by clicking _Add File_, _Create New File_.

    ![alt text](assets/images/addfile_github.png).

3. Enter your new file name.
    Remember to use safe file names, no funky characters and use `_` instead of spaces.
    See [Article/Category Naming](#articlecategory-naming) for more info.

4. Add metadata header.
    Should at minimum contain.

    ```yml
    ---
    created: 
    description: "Will be used to generate page preview. Should not contain keywords not in the body of article."
    tags: [Tag1, Tag2]
    ---
    ```

5. Write rest of page.
    Rembember headers start at H2 (`##H2`). For more information see [FORMAT.md](FORMAT.md#headers)

6. Click `commit changes`.
    If this is a draft page, and you plan to come back to work on it, you will want to give it a descriptive branch name.
    ![Commit](assets/images/example_pr_github.png).

    See [CONTRIBUTING](CONTRIBUTING.md#making-a-merge-request)

7. Merge pull request in order to _publish_ change.

## In Codespace

1. Open parent category (folder)
    Navigate to the directory where you want to make a new page.

2. Click the _new file_ button.

3. Enter your new file name.
    Remember to use safe file names, no funky characters and use `_` instead of spaces.
    See [Article/Category Naming](#articlecategory-naming) for more info.

4. Prefill with template (optional)
    <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>p</kbd>, `fill file with snippet`, 'Template New Page'.
    See [CONTRIBUTING](CONTRIBUTING.md#command-palette).

5. Write Article.
    Remember, you can add elements and autocomplete using <kbd>ctrl</kbd> + <kbd>space</kbd>.
    See [CONTRIBUTING](CONTRIBUTING.md#snippets)

6. Check problems (optional)
    Open the `PROBLEMS` tab in the bottom panel.

## Article/Category Location

Public facing articles are found in the `docs` folder:

- Any directory will be a **category**.
- Any markdown file, i.e. a text file ending with the `.md` extension, inside will be rendered as an **article**.
- A directory containing a `index.md` file, will be a **category-article**.
  (clicking on will take to the rendered markdown in `index.md`, any other markdown in the directory will be nested articles.)

!!! tip "Categories-Articles"
    When making an category-article, make sure you set `title:` in the frontmatter of the `index.md` file, as otherwise the page title will be 'Index'.

    Ideally, the page title should be the same as the category, to avoid confusion.

![Documentation Structure](assets/images/doc_struct.png)

## Article/Category Naming

By default, the filename will be use as title of the article/category.

Try to keep your title short enough that it does not 'wrap' (become more than one line) in the nav,
this usually happens around 24-ish characters however this will vary depending on the letters being used.

!!! tip "File Name hygiene"
    Regular 'snake_case' naming conventions should be used for articles/categories, i.e. no non-alphanumeric characters (except `_` and `-`).

    When converting from filename, to title, spaces will replace `_` and the first letter of the first word will be capitalised (if it wasn't already), e.g. `My_Nice_and_Tidy_Filename.md` becomes `My Nice and Tidy Filename`

In the case of an articles (including category-articles), this title can be overridden by setting one in the page [front-matter using the 'title' keyword](#article-metadata).
If you need to rename a regular category (one without an `index.md`), this can be done in the
[`.pages.yml` file](#articlecategory-order).

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

For full description of `.pages.yml` use, see the
[awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin).

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
search:
  boost: 2
hide:
  - toc
  - nav
---
```

The following sections detail the most usual entries.

### MkDocs Parameters

| Parameter | Usage | Allowed Values | Example |
| - | - | - | - |
| `title`  | article title. | str | `title: My Title` |
| `created_at` | When article was created. Currently not shown in rendered page, but should still be filled in as it can be useful info. : `yyyy-MM-dd`, `yyyy-MM-ddThh:mm:ssZ` | `created_at: 2024-01-01` |

### Material Theme Parameters

| Parameter | Usage | Allowed Values | Example |
| - | - | - | - |
| `description` | Used for internal and external search indexing. This will appear as the page preview when searching in Google. Try not to include words and information here that is not in the body of the article. | string | `description: A short summary.` |
| `icon`        | Page icon.                                                    | Path |  |
| `status`      | Will display a symbol on nav                                  | `new` or `deprecated` | |
| `hide`        | Used to turn off features (e.g. table of content)             | [`tags` `toc` `nav`]| |
| `tags`        | Used for internal and external search indexing                | String[] | `tags: [ "slurm", "containers" ]` |
| `search: exclude` | Used to exclude page from internal search                 | Bool | `search: exclude: True`|
| `search: boost` | Used to increase or decrease weight in internal search      | Float | `search: boost: 0.1` to lower weight,  `search: boost: 10` to raise weight |

### Zendesk Imported

The following fields were imported from Zendesk Page:

- `vote_count` 
- `vote_sum`
- `zendesk_article_id`
- `zendesk_section_id`

`zendesk_article_id` and `zendesk_section_id` serve no purpose and can be deleted.
`vote_count` and `vote_sum` are useful for determining past popularity of a page, but will become less useful with time.

## Accessibility Standards

- [NZ spec](https://www.digital.govt.nz/standards-and-guidance/nz-government-web-standards/web-accessibility-standard-1-1/)
- [WCAG spec](https://www.w3.org/TR/WCAG21/)

This page is an overview of the Markdown syntax supported in this documentation.

## Headers

<h2>H2</h2>

```md
## H2
```

<h3>H3</h3>

```md
### H3
```

<h4>H4</h4>

```md
#### H4
```

Headers should have a blank line before and after.

Don't use `H1` (`#`) this is reserved for the page title. Setting a title here will change it in the nav also.

h2 and h3 elements will be used to generate a table of contents (toc).

Try to keep headers short enough that they do not 'wrap' (become more than one line) in the toc,
this usually happens around 32-ish characters however this will vary depending on the letters being used.

## Line breaks

Put 2 spaces at the end of a line to force a line break.  
If you simply hit enter and don't use 2 spaces it will be considered one line.

```md
Put 2 spaces at the end of a line to force a line break.  
If you simply hit enter and don't use 2 spaces it will be considered one line.
```

## Text Emphasis

**bold**: `**bold**`

_italic_: `_italic`

## Tab Containers

=== "Tab One"
    something in the tab
=== "Tab two"
    something else

```md
=== "Tab One"
    something in the tab
=== "Tab two"
    something else
```

## Admonitions

!!! warning
    A warning.

```md
!!! warning
    A warning.
```

### Admonition Titles

!!! info "Optional title"
    Admonition with optional title.

```md
!!! info "Optional title"
    Admonition with optional title.
```

Adding titles helps users find key information, however if you can't be bothered thinking of a good title,
refrain from using something unnecessary or non descriptive (e.g. `!!! info "More Information"`), better to leave titleless.

Don't use a title if another Admonition already exists for that purpose (e.g. `!!! info "Watch out!"`).

### Collapsable Admonitions

Any Admonition can be made collapsable by replacing the `!!!` with `???` (closed), or `???+` (open)

??? info "I'm Collapseable"
    Wheeee

```md
??? info "I'm Collapseable"
    Wheeee
```

Consider making a Admonition collapsable-open (`???+`) if it is particularly long.
An Admonition **shouldn't be made collapsable-closed** (`???`) unless it has been given an **optional title explaining it's contents**.

### Admonition Flavours

There are various flavors.

!!! prerequisite
    - [link to page a user should read in order to follow](FORMAT.md)
    - some thing other requirement user must have to follow this page
    - usually you will want this to be a list format.
    - Should be right at the top of the page.

!!! tip "with title"
    For tangential actionable advice.  
    *`x` other command may be useful here.*

!!! info
    Use this to provide (optional) additional context or make an in depth explanation.
    *A little bit of info that isn't required for understanding the next paragraph.*

!!! warning
    Use this to draw readers attention to possible rare or edge case failures they may encounter.
    *If your filesystem is full you might get an error message.*

!!! danger
    Use this to draw attention to information that may lead to serious harm if ignored.
    *If your filesystem is full your job might be killed.*

!!! bug
    Mention possible bugs users may encounter (and tell them what to do if they encounter it).
    *Nearline doesn't work*

## Code

### Block

Code blocks require a language lexer in order to do syntax highlighting, e.g. `python` ,`slurm`, `cuda`, `json`, `markdown`, `bash`
(most of these have short codes too, `py`,`sl`,`cd`,`md`,`sh`).
[A full list of lexers can be found in this list](https://pygments.org/languages/).

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

For plain text code blocks, still good to use a class as descriptor (e.g. `txt`, `stdout`, `stderr`).
May want to add formatting to this later.

<pre><code><span>```stdout</span>
<span>some code</span>
<span>```</span>
</code></pre>

```stderr
some code 
```

DON'T prefix a command with `$` (e.g. `$ ls` if this is something we want it should be added through formatting, not text.

### Inline

This is some `echo "Inline Code"`.

<pre><code><span>This is some `echo "Inline Code"`.</span></code></pre>

Inline code does not have syntax highlighting.
Code should be used for any text that you want the user to copy exactly.

### Keyboard

Keyboard keys can be added using the `<kbd>` tag.

Press `<kbd>`ctrl`</kbd>` + `<kbd>`c`</kbd>` to copy text from terminal.

```md
Press <kbd>ctrl</kbd> + <kbd>c</kbd> to copy text from terminal.
```

Note the additional spacing around the `+` else it will appear cramped.

### Slurm Scripts

The most common use of a code block is to display an example Slurm script.  

We want our examples to be easy to understand, but also users _will_ copy
paste them, so we also want them to be working scripts that wont cause easily avoidable errors.

If possible stick to the following principles.

- Make sure the code block has the `sl` language tag. This will inform syntax highlight an CI checks.
- Use `!#/bin/bash -e` as your shebang.
- One blank line between shebang and Slurm Header.
- Use <kbd>tab</kbd> for your Slurm header delimiter.
- Use the long for Slurm keywords, e.g. `--job-name` rather than `-j`.
- Make sure to include `--job-name`, `--account` (`nesi99991`) and `--time`.
- One blank line after Slurm header.
- Always `module purge` before `module load`.
- Include version in `module load`. See [Variable Injection](#variables-injection) for convenience macro.
- Don't be too fancy. We all know you are very clever,
but your script examples should do the bare minimum needed to provide a safe example.
- If possible, include an example that will work for the user, e.g. one of the tutorial files. (`wget`, `$EB_ROOT`, etc)

#### Example

<pre><code><span>```sl</span>
<span>#!/bin/bash -e</span>
<span></span>
<span>#SBATCH --job-name          test-job</span>
<span>#SBATCH --account          nesi99991</span>
<span>#SBATCH --time             01:00:00 </span>
<span></span>
<span>module purge</span>
<span>module load MATLAB/2022a</span>
<span></span>
<span>matlab -r myFile.m    # Some nice informative comment.</span>
<span>```</span></code></pre>

## Images

```md
![This is an image](./assets/images/ANSYS_0.png)
```

![This is an image](./assets/images/ANSYS_0.png)

!!! note "Pasting from Clipboard"
    You can 'paste' an image from the clipboard into a markdown document,
    it will add

    ```md
    ![Alt text](image.png)
    ```

    In markdown where you pasted the image, and upload `image.png`, into the same directory.

    Make sure you rename the `image.png` to something more descriptive, move it into the 'assets/images' folder, and update then markdown accordingly.

!!! tip "Drag and Drop"
    You can easily get the path to a image file by dragging it from the left hand Explorer panel over your document, then pressing <kbd>shift</kbd> (you will be prompted) and dropping the image in the desired position. Copy pasting an image from Explorer into markdown also works.

    You can also start typing `!` and then use context suggestions (<kbd>ctrl</kbd> + <kbd>space</kbd>), select 'Insert Image' and navigate the rest of the way.

## Links

[External Link]("https://example.com")

```md
[External Link]("https://example.com")
```

[Internal Link]("General/FAQs/Password_Expiry")

```md
[Internal Link]("General/FAQs/Password_Expiry")
```

!!! warning
    Link paths are relative to current file!!!

[Anchor Link](#links)

```md
[Anchor Link](#links)
```

`snake-case` anchors are automatically generated for all headers.

The anchor will be the same as the header text with all non-alphanumeric characters removed, converted to lower case, and space characters replaced with `-`.
For example a header `## This is my (nasty-Header)` can be linked to with the anchor `[Anchor Link](#this-is-my-nastyheader)`

!!! tip "Drag and Drop"
    You can drag files from the left hand Explorer panel over your document then press <kbd>shift</kbd> (you will be prompted) and drop in the desired position. Copy pasting a file from Explorer into markdown also works.

??? tip "Ambiguous links"

    Try to avoid putting links on ambiguous words, e.g.

    === "Bad"
        View the software homepage [here](https://www.example.com).

        ```md
        View the homepage [here](https://www.example.com).
        ```

    === "Better"
        View the [software homepage](https://www.example.com).

        ```md
        View the [software homepage](https://www.example.com).
        ```

## Tooltips

[Hover over me](https://example.com "I'm a link with a custom tooltip.")

```md
[Hover over me](https://example.com "I'm a link with a custom tooltip.")
```

Acroynym should be automatically made tool-tips e.g. MPI.

```md
Acroynym should be automatically made tool-tips e.g. MPI.
```

## Lists

### Unordered List

- item1
- item2
- a
- item

```md
- item1
- item2
- a
  multi-line
- item
- nested
  - items
    - nested-er
```

### Ordered List

1. item1
2. a
   multi-line
   item
   with multiple
   lines
3. nested
   1. nested item 1
   2. nested item 2
      1. even nested-er

```md
1. item1
2. a
   multiline
   item
   with multiple
   lines
3. nested
    1. nested item 1
    2. nested item 2
        1. even nested-er
```

*Note, nested list items use numbers, but will be rendered as whatever the indent is.*

## Tables

[Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables), is a handy tool for complex tables/

Tables can be constructed using `|` to separate columns, and `--` to designate headers.

Number of dashes has no effect, things don't have to be lined up when in markdown, just looks nice.
Leading and trailing `|` are optional.

| Head   | Head   |
| ------ | ------ |
| Thing1 | Thing2 |
| Thing3 | Thing3 |

```md
 Head | Head
 --- | -----------
 Thing1 | Thing2
 Thing3 | Thing 3
```

`:`'s can be used to align tables.

| Left  | Center | Right |
| :---- | :----: | ----: |
| Words | Words | Words |
| Words | Words | Words |

```md
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

## Macros

Macros allow use of [Jinja filter syntax](https://jinja.palletsprojects.com/en/3.1.x/templates/) _inside the markdown files_ allowing for much more flexible templating.
More details can be found on the [mkdocs-macros-plugin page](https://mkdocs-macros-plugin.readthedocs.io/).

### Includes

The macro plugin allows the use of 'includes', here is an example.

```md
{% raw %}
{% include 'snippet.md' %}
{% endraw %}
```

There are a few includes you may want to use.

| Path | content | usage |
| ---- | ------- | ----- |
| ```{% raw %}{% include "partials/support_request.html" %}{% endraw %}``` | ```<a href="mailto:support@nesi.org.nz">Contact our Support Team</a>``` | Anywhere the user is told to contact support. |
| ```{% raw %}{% include "partials/appHeader.html" %}{% endraw %}``` | Info block | At the top of documents about particular software (TODO: elaborate) |
| ```{% raw %}{% include "partials/app/app_network_licence.html" %}{% endraw %}``` | List of network licences | When dynamic licence info is required (used in `appHeader.html`)  |
| ```{% raw %}{% include "partials/app/app_version.html" %}{% endraw %}``` | List of versions and a 'module load' code-block. | When dynamic version info is required |

### Variables injection

Here is an example using dynamically using the module version information.

`module load ANSYS/{{ applications.ANSYS.default }}`

```md
{% raw %}
`module load ANSYS/{{ applications.ANSYS.default }}`
{% endraw %}
```

### Advanced Macros

And here is another example showing all Python packages installed in Python modules.

??? "Fancy Example"
    Our Python modules come pre-built with the following packages:
    <table>
    <tr><th>Package</th></tr>
    {% for pyext in applications.Python.extensions %}
    <tr><td>{{ pyext }}</td></tr>
    {% endfor %}
    </table>

    ```md
    {% raw %}
    Our Python modules come pre-built with the following packages:
    <table>
    <tr><th>Package</th></tr>
    {% for pyext in applications.Python.extensions %}
    <tr><td>{{ pyext }}</td></tr>
    {% endfor %}
    </table>
    {% endraw %}
    ```
