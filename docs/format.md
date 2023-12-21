# Title (H1)

```md
# Title (H1)
```

## H2

```md
## H2
```

### H3

```md
### H3
```

#### H4

```md
#### H4
```

Headers should have a blank line before and after.

'H1' (`#`) is for the page title. Setting a title here will change it in the nav also.

!!! warning
    Put 2 spaces at the end of a line to force a line break. 
    If you simply hit enter and don't use 2 spaces it will be considered one line.

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

!!! warning
    A warning.

```md
!!! warning
    A warning.
```

!!! info "Optional title"
    Admonation with optional title.

```md
!!! info "Optional title"
    Admonation with optional title.
```

Any admonation can be made collapsable by replacing the `!!!` with `???` (closed), or `???+` (open)

_Note for future, once decided which of these we will use, remove the others. And give description of when to use._

There are lots of different flavors.

---

!!! note
    This is a test admonation.

!!! tip
    This is a test admonation.

!!! info
    This is a test admonation.

!!! question
    This is a test admonation.

!!! warning
    This is a test admonation.

!!! failure
    This is a test admonation.

!!! danger
    This is a test admonation.

!!! bug
    This is a test admonation.

!!! example
    This is a test admonation.

!!! quote
    This is a test admonation.

!!! prerequisite
    This is a test admonation.

!!! pied-piper
    this is a test admonation.

!!! desktop-download-24
    this is a test admonation.

!!! magnifying-glass
    this is a test admonation.

!!! microscope
    this is a test admonation.

!!! vial-virus
    this is a test admonation.

!!! database
    this is a test admonation.

!!! folder-open
    this is a test admonation.

!!! backward
    this is a test admonation.

!!! jupyter
    this is a test admonation.

!!! terminal
    this is a test admonation.

!!! r-project
    this is a test admonation.

!!! calendar-days
    this is a test admonation.

!!! bell
    this is a test admonation.

!!! comment-dots
    this is a test admonation.

!!! check-to-slot
    this is a test admonation.

!!! square-xmark
    this is a test admonation.

!!! rectangle-list
    this is a test admonation.

!!! screwdriver-wrench
    this is a test admonation.

!!! linux
    this is a test admonation.

!!! code-compare
    this is a test admonation.

!!! heading
    this is a test admonation.

!!! space-awesome
    this is a test admonation.

!!! stethoscope
    this is a test admonation.

!!! key
    this is a test admonation.

!!! users-line
    this is a test admonation.

!!! file-code
    this is a test admonation.

!!! hand-holding-dollar
    this is a test admonation.

!!! circle-question
    this is a test admonation.

!!! microphone
    this is a test admonation.

!!! tower-observation
    this is a test admonation.

!!! circle-info
    this is a test admonation.

!!! icon--python
    this is a test admonation.

!!! quote-right
    this is a test admonation.

!!! image
    this is a test admonation.

!!! table
    this is a test admonation.

!!! glass-chart
    this is a test admonation.

!!! file-export
    this is a test admonation.

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

Press `<kbd>`ctrl`</kbd>` + `<kbd>`c`</kbd>` to copy text from terminal.

```md
Press <kbd>ctrl</kbd> + <kbd>c</kbd> to copy text from terminal.
```

Note the additional spacing around the `+` else it will appear cramped.

### Images

```md
![This is an image](./assets/images/ANSYS_0.png)
```

![This is an image](./assets/images/ANSYS_0.png)

### Links

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

snake-case anchors are automatically generated for all headers.

For example a header `## This is my Header` can be linked to with the anchor `[Anchor Link](#this-is-my-header)`

### Tooltips

[Hover over me](https://example.com "I'm a link with a custom tooltip.")

```md
[Hover over me](https://example.com "I'm a link with a custom tooltip.")
```

Acroynym should be automatically tooltipped e.g. MPI.

```md
Acroynym should be automatically tooltipped e.g. MPI.
```

### Lists

#### Unordered List

- item1
- item2
- a
- item

```md
- item1
- item2
- a
  multiline
- item
- nested
  - items
    - nesteder
```

#### Ordered List

1. item1
2. a
   multiline
   item
   with multiple
   lines
3. nested
   1. nested item 1
   2. nested item 2
      1. even nesteder

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
        1. even nesteder
```

*Note, nested list items use numbers, but will be rendered as whatever the indent is.*

### Tables

[Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables), is a handy tool for complex tables/

Tables can be constructed using `|` to seperate colums, and `--` to designate headers.

Number of dashes has no effect, things dont have to be lined up when in markdown, just looks nice.
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
