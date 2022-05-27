


For full list of pandoc plugins.

```
pandoc --list-extensions=markdown
```

## Version Control.


MAKE SURE ALL PANDOC FILTERS ARE EXECUTABLE

Changes made to markdown versions of code need to be compatible with later versions of converted docs.

* After running `convert_docs.py`. 

* Move into import worktree. Or `cd from_zendesk/import_worktree/`

* `git add --all`

* `git commit -m "Import run $(date)\n$(git status -s)"`

* `cd ../../`