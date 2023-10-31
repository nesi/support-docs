# Header 1 
## Header 2 
### Header 3 
#### Header 4


```
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

### Block

```python
import somepackage

formatting = True
if formatting:
    Print(formatting) # A comment
```

```md
    ```py 
        import somepackage

        formatting = True
        if formatting:
            Print(formatting) # A comment
    ```
```

### Inline

`echo "Hello World"`

``echo "Hello World"``

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