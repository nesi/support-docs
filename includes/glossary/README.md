## How to use.

The `dictionary.yaml` informs three different things.

### Spellcheck
 - All words listed will be included in spellcheck unless `spellcheck: false`.
- [NOT IMPLIMENTED] Will be case sensitive unless `checkcase: false` 

### [NOT IMPLIMENTED] Glossary
- All word will be included along with any aliases unless `glossary: false` or `long:` is empty.

### [NOT IMPLIMENTED] Snippets
- All words will be included for snippets unless `snippets: false` or `long:` is empty.
- For a page to impliment snippets it must include 
```
--8<-- "includes/glossary/.dictionary.md"
```
at the page footer. (consider adding to page material).


example entry.
```
- minimal:
- full: &full
  long: The long form of this word. # What to say in glossary, or hover. Default ''
  checkcase: false # Whether to care about case.Default 'true'
  glossary: false  # Include in glossary or not. Default 'true'
  spellcheck: false  # Include in spellcheck or not. Default 'true'
  snippet: false  # Enable snippet or not. Default 'true'
- alias: *full # This is an alias of example.
```

## Implimentation


Running `./glossary.py` should create the following outputs.
### `.snippets.md` 
Used for the generation of snippets. Uses the following format

```
*[tfe]: The Full Explanation 
*[smth-e]: Something Else
*[smthe]: Something Else
```

### `.dictionary.txt` 
Used by mkdocs spellcheck. Uses the following format.
```
tfe
smth-e
smthe
```

### `Glossary.md`
Nicely formatted markdown page for human reading.
Format

```
#### - tfe : 
The Full Explanation.
#### - smth-e, smthe : 
Something Else
```
