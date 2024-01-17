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

- `template` : which [template](#templates) to use.
- `title`    : [title](#title).
- `weight`   : Used to set page order. Lower comes first. Migrated from Zendesk `position`.
               See [page order](#article-order)

### Material Parameters

- `description` : used for site meta.           : `string`
- `icon`        : page icon.                    : `path`
- `status`      : Will dsiplay a symbol on nav  : `new`, `deprecated`.
- `hide`        : Used to turn off features.    : `tags`

### Custom Parameters

- `prereq`      : List of prerequisites. Formatted in markdown. Will be rendered inside a admonation.
- `postreq`     : List of what next. Formatted in markdown. Will be rendered inside a admonation.
- `suggested`   : Page similar pages to link to. (Not implimented).

### Zendesk Imported

Not used for anything currently. Info imported from Zendesk Page.

- `created_at`:
- `hidden`:
- `label_names`: []
- `vote_count`:
- `vote_sum`:
- `zendesk_article_id`:
- `zendesk_section_id`:

## Templates

Template can be set in article meta.

- `main.html`                : Used for regular pages (default).
- ~~`application.html`         : Used for 'application' pages, will include software details header (and be linked in supported apps page).~~
- `supportedApplication.html`: For supported applications page.
- `home.html`                : Homepage.

By default, the `main` theme will be used. template of a theme to render Markdown pages. You can use the template meta-data key to define a different template file for that specific page. The template file must be available on the path(s) defined in the theme's environment.

## Macros

Macros allow use of Jinja filter syntax _inside the mardown files_ allowing for much more flexible templating.
More details can be found on the [mkdocs-macros-plugin page](https://mkdocs-macros-plugin.readthedocs.io/)

### Filters

`module load ANSYS/{{ applications.ANSYS.machines.mahuika.versions | last }}`

```md
{% raw %}
`module load ANSYS/{{ applications.ANSYS.machines.mahuika.versions | last }}`
{% endraw %}
```

??? "Fancy Example"
    Our Python modules come prebuilt with the following packages:
    {% set pyexts=applications.Python.extensions.split(', ') %}
    <table>
    <tr><th>Package</th></tr>
    {% for pyext in pyexts %}
    <tr><td>{{ pyext }}</td></tr>
    {% endfor %}
    </table>

    ```md
    {% raw %}
    Our Python modules come prebuilt with the following packages: 
    {% set pyexts=applications.Python.extensions.split(', ') %}
    <table>
    <tr><th>Package</th></tr>
    {% for pyext in pyexts %}
    <tr><td>{{ pyext }}</td></tr>
    {% endfor %}
    {% endraw %}
    </table>
    ```

### Includes

The macro plugin also allows the use of 'includes',

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
| ```{% raw %}{% include "partials/app/app_version.html" %}{% endraw %}``` | List of versions and a 'module load' codeblock. | When dynamic version info is required |

## Style Guide

### Code blocks

Don't include prompt or

### Links

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

## Accessability standards

- [nz spec](https://www.digital.govt.nz/standards-and-guidance/nz-government-web-standards/web-accessibility-standard-1-1/)
- [WCAG spec](https://www.w3.org/TR/WCAG21/)

## mkdocs.yml

When setting a parameter in the YAML, you can use the following syntax.

```yaml
some-param : !ENV [TEST_ENV, false]
```

This will use the value of the env variable `TEST_ENV`, or if unset, false.
