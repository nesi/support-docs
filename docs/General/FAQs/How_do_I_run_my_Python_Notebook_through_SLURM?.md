---
created_at: '2023-09-17T23:51:43Z'
hidden: false
label_names: []
position: 0
title: How do I run my Python Notebook through SLURM?
vote_count: 0
vote_sum: 0
zendesk_article_id: 7918332923023
zendesk_section_id: 360000039036
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>The first thing you will need to do is to convert your <code>.ipynb</code> (<strong>I</strong>nteractive <strong>PY</strong>thon <strong>N</strong>ote <strong>B</strong>ook) file into a regular <code>.py</code> python file. There are two ways to do this.</p>
<h3>nbconvert</h3>
<p><code>nbconvert</code> is a tool used to convert notebooks to other formats, it is accessible through the command line if you are logged in through Jupyter.</p>
<pre>jupyter nbconvert --to script my_notebook.ipynb </pre>
<p>will create a new python script called <code>my_notebook.py</code>.</p>
<h3>Export Notebook</h3>
<p>With your notebook open, select <em>File</em> -&gt; <em>Save and Export Notebook As...</em> -&gt; <em>Executable Script</em></p>
<p>This option might be less convenient as the exporter saves the python file to your local computer, meaning you will have to drag it back into the file explorer in Jupyter from your downloads folder.</p>
<p> </p>
<p>This script can then be run as a regular python script as described in our <a href="https://support.nesi.org.nz/hc/en-gb/articles/207782537" target="_self">Python</a> documentation.</p>