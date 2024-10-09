---
created_at: '2023-09-17T23:51:43Z'
tags: []
title: How do I run my Python Notebook through SLURM?
vote_count: 1
vote_sum: -1
zendesk_article_id: 7918332923023
zendesk_section_id: 360000039036
---

The first thing you will need to do is to convert your `.ipynb`
(**I**nteractive **PY**thon **N**ote **B**ook) file into a regular `.py`
python file. There are two ways to do this.

## nbconvert

`nbconvert` is a tool used to convert notebooks to other formats, it is
accessible through the command line if you are logged in through
Jupyter.

```sh
jupyter nbconvert --to script my_notebook.ipynb 
```

will create a new python script called `my_notebook.py`.

### Export Notebook

With your notebook open, select *File* -> *Save and Export Notebook
As...* -> *Executable Script*

This option might be less convenient as the exporter saves the python
file to your local computer, meaning you will have to drag it back into
the file explorer in Jupyter from your downloads folder.

This script can then be run as a regular python script as described in
our
[Python](../../Scientific_Computing/Supported_Applications/Python.md)
documentation.
