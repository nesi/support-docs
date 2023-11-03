# Header 1 
## Header 2 
### Header 3 
#### Header 4

```md
# Header 1 
## Header 2
### Header 3
#### Header 4
```

## Text Emphasis

**bold**: `**bold**`
_italic_: `_italic`

## Tab Containers

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

## Admonations

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

## Code

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

### Block

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

### Inline

`echo "Hello World"`

<pre><code><span>`echo "Hello World"`</span></code></pre>

### Keyboard

Keyboard keys can be added using the `<kbd>` tag.

Press <kbd>ctrl</kbd>+<kbd>c</kbd> to copy text from terminal.

```md
Press <kbd>ctrl</kbd> + <kbd>c</kbd> to copy text from terminal.
```

Note the additional spacing around the `+` else it will appear cramped.

## Images

```md
![This is an image]("assets/images/FENSAP_GUI1.png")
```

![This is an image]("assets/images/FENSAP_GUI1.png")

## Links

[External Link]("https://example.com")

```md
[External Link]("https://example.com")

```

[Internal Link]("General/Announcements")

```md
[Internal Link]("General/Announcements")

```

## Tooltips

[Hover over me](https://example.com "I'm a link with a custom tooltip.")

```md
[Hover over me](https://example.com "I'm a link with a custom tooltip.")
```

Acroynym should be automatically tooltipped e.g. MPI.

```md
Acroynym should be automatically tooltipped e.g. MPI.
```

## Accessability standards

- [nz spec](https://www.digital.govt.nz/standards-and-guidance/nz-government-web-standards/web-accessibility-standard-1-1/)
- [WCAG spec](https://www.w3.org/TR/WCAG21/)



{{ macros_info() }}