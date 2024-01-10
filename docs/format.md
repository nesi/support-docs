**[CLICK HERE TO VIEW THIS PAGE RENDERED IN MKDOCS](https://nesi.github.io/support-docs-concept/format/)**{ .hidden }

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

### Admonitions

!!! warning
    A warning.

```md
!!! warning
    A warning.
```

#### Admonition Titles

!!! info "Optional title"
    Admonition with optional title.

```md
!!! info "Optional title"
    Admonition with optional title.
```

Adding titles helps users find key information, however if you can't be bothered thinking of a good title,
refrain from using something unnecessary or non descriptive (e.g. `!!! info "More Information"`), better to leave titleless.

Don't use a title if another Admonition already exists for that purpose (e.g. `!!! info "Watch out!"`).

#### Collapsable Admonitions

Any Admonition can be made collapsable by replacing the `!!!` with `???` (closed), or `???+` (open)

Consider making a Admonition collapsable-open (`???+`) if it is particularly long.
An Admonition **shouldn't be made collapsable-closed** (`???`) unless it has been given an **optional title explaining it's contents**.

#### Admonition Flavours

There are various flavors.

!!! prerequisite
    - [link to page a user should read in order to follow](format.md)
    - some thing other requirement user must have to follow this page
    - usually you will want this to be a list format.
    - Should be right at the top of the page.

!!! tip
    For tangential actionable advice.  
    *`x` other command may be useful here.*

!!! info
    Use this to provide (optional) additional context or make an in depth explaination.
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

??? warning "Extra Admonitions you probably won't need"
    !!! note
        Use `info` instead of this.

    !!! question
        Havn't seen a reason to use this yet.
    
    !!! failure
        Havn't seen a reason to use this yet.
    
    !!! example
        Havn't seen a reason to use this yet.
    
    !!! quote
        Havn't seen a reason to use this yet.
    
    !!! pied-piper
        don't use this (unless Dini).
    
    !!! desktop-download-24
        don't use this (unless Dini).
    
    !!! magnifying-glass
        don't use this (unless Dini).
    
    !!! microscope
        don't use this (unless Dini).
    
    !!! vial-virus
        don't use this (unless Dini).
    
    !!! database
        don't use this (unless Dini).
    
    !!! folder-open
        don't use this (unless Dini).
    
    !!! backward
        don't use this (unless Dini).
    
    !!! jupyter
        don't use this (unless Dini).
    
    !!! terminal
        don't use this (unless Dini).
    
    !!! r-project
        don't use this (unless Dini).
    
    !!! calendar-days
        don't use this (unless Dini).
    
    !!! bell
        don't use this (unless Dini).
    
    !!! comment-dots
        don't use this (unless Dini).
    
    !!! check-to-slot
        don't use this (unless Dini).
    
    !!! square-xmark
        don't use this (unless Dini).
    
    !!! rectangle-list
        don't use this (unless Dini).
    
    !!! screwdriver-wrench
        don't use this (unless Dini).
    
    !!! linux
        don't use this (unless Dini).
    
    !!! code-compare
        don't use this (unless Dini).
    
    !!! heading
        don't use this (unless Dini).
    
    !!! space-awesome
        don't use this (unless Dini).
    
    !!! stethoscope
        don't use this (unless Dini).
    
    !!! key
        don't use this (unless Dini).
    
    !!! users-line
        don't use this (unless Dini).
    
    !!! file-code
        don't use this (unless Dini).
    
    !!! hand-holding-dollar
        don't use this (unless Dini).
    
    !!! circle-question
        don't use this (unless Dini).
    
    !!! microphone
        don't use this (unless Dini).
    
    !!! tower-observation
        don't use this (unless Dini).
    
    !!! circle-info
        don't use this (unless Dini).
    
    !!! icon--python
        don't use this (unless Dini).
    
    !!! quote-right
        don't use this (unless Dini).
    
    !!! image
        don't use this (unless Dini).
    
    !!! table
        don't use this (unless Dini).
    
    !!! glass-chart
        don't use this (unless Dini).
    
    !!! file-export
        don't use this (unless Dini).

### Code

#### Block

Code blocks require a language lexxer in order to do syntax hilighting, e.g. `python` ,`slurm`, `cuda`, `json`, `markdown`, `bash`
(most of these have short codes too, `py`,`sl`,`cd`,`md`,`sh`).
[A full list of lexxers can be found in this list](https://pygments.org/languages/).

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

#### Inline

This is some `echo "Inline Code"`.

<pre><code><span>This is some `echo "Inline Code"`.</span></code></pre>

Inline code does not have syntax highlighting.
Code should be used for any text that you want the user to copy exactly.

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
  multi-line
- item
- nested
  - items
    - nesteder
```

#### Ordered List

1. item1
2. a
   multi-line
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

Tables can be constructed using `|` to seperate columns, and `--` to designate headers.

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
