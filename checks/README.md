# Checks

## Spellcheck

### Limitiations

Spellchecker does not provide output lineumber / column.
In order to get this a regex match is done on the markdown.
This means that you might occassionally see a word highlighted inside a context where it should be ignored (e.g. code block),
the typo is probably occuring elsewhere in the text in a valid context, fix it here and the first error will resolve.
