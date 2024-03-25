# Checks

This directory contains QA tests for the documentation.

Tests should be made as Python scripts to allow flexibility of use. Currently these checks are run two ways.

    - [GitHub Actions](https://docs.github.com/en/actions) as defined in [workflows](../.github/workflows/) (should also with with GitLab CI, may require tweaking).
    - [VSCode Problem Matchers](https://code.visualstudio.com/docs/editor/tasks#_processing-task-output-with-problem-matchers) as defined in [tasks.json](../.vscode/tasks.json).

## Spellcheck

Spellcheck pipeline settings can be modified in [.spellcheck.yml](../.spellcheck.yml).

List of custom words can be found in [dictionary.txt](../docs/assets/glossary/dictionary.txt),
however you **should not edit this manually**, see [adding-words-to-dictionary](../docs/CONTRIBUTING.md#adding-words-to-dictionary).

### Limitiations

Spellchecker does not provide output lineumber / column.
In order to get this a regex match is done on the markdown.
This means that you might occassionally see a word highlighted inside a context where it should be ignored (e.g. code block),
the typo is probably occuring elsewhere in the text in a valid context, fix it here and the first error will resolve.

## Prose Lint

Checks text follows best practice for English language.

Individual rules can be disabled/enabled in [.proselint.json](../.proselint.json).

## Markdown Lint

Checks markdown for complience against general [best practice rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md).

Individual rules can be disabled/enabled in [.markdownlint.json](../.markdownlint.json)

## Meta Checks

Catch-all for custom checks.

### title_redundant

### title_length

### meta_missing_description

### meta_unexpected_key

### minimum_tags

### walk_toc

## Test Build

Does a 'strict' build of the site, capturing any errors emmited by mkdocs.
