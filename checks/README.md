# Checks

This directory contains QA tests for the documentation.

Tests should be made as Python scripts to allow flexibility of use. Currently these checks are run two ways:

- [GitHub Actions](https://docs.github.com/en/actions) as defined in [workflows](../.github/workflows/),
- [VSCode Problem Matchers](https://code.visualstudio.com/docs/editor/tasks#_processing-task-output-with-problem-matchers) as defined in [tasks.json](../.vscode/tasks.json).

## Spellcheck

*This linter is defined in [run_pyspelling.py](run_pyspelling.py) script.*

Spellcheck pipeline settings can be modified in [.spellcheck.yml](../.spellcheck.yml).

List of custom words can be found in [dictionary.txt](../docs/assets/glossary/dictionary.txt),
however you **should not edit this manually**, see [adding-words-to-dictionary](../docs/CONTRIBUTING.md#adding-words-to-dictionary).

### Limitations

Spellchecker does not provide output lineumber / column.
In order to get this a regex match is done on the markdown.
This means that you might occassionally see a word highlighted inside a context where it should be ignored (e.g. code block),
the typo is probably occuring elsewhere in the text in a valid context, fix it here and the first error will resolve.

## Prose Lint

*This linter is defined in [run_proselint.py](run_proselint.py) script.*

Checks text follows best practice for English language.

Individual rules can be disabled/enabled in [.proselint.json](../.proselint.json).

## Markdown Lint

Checks markdown for complience against general [best practice rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md).

Individual rules can be disabled/enabled in [.markdownlint.json](../.markdownlint.json)

## Meta Checks

*This linter is defined in [run_meta_check.py](run_meta_check.py) script.*

Catch-all for custom checks.
Currently defined checks are:

- title_redundant,
- title_length,
- meta_missing_description,
- meta_unexpected_key,
- minimum_tags,
- walk_toc.

## Test Build

Does a 'strict' build of the site, capturing any errors emmited by mkdocs.
