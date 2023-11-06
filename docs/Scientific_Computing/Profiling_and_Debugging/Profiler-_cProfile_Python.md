---
created_at: '2020-05-11T22:03:36Z'
hidden: true
label_names: []
position: 0
title: 'Profiler: cProfile (Python)'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001523256
zendesk_section_id: 360000278935
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>cProfile is the recommended profiler for most users. Documentation <a href="https://docs.python.org/2/library/profile.html#module-profile" target="_self">here</a>.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tip</h3>
<p><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000930396" target="_self">ARM MAP</a> can also be used to profile Python code.</p>
</blockquote>
<h1>Running cProfile</h1>
<p>Profiling your python code with cProfile is as simple as passing your script as an argument to the cProfile module. </p>
<p>It is probably a good idea to provide an output file using the -o flag if you don't want the profiling data sent to your stdout in string format. </p>
<pre><code>module load python<br>python -m cProfile -o myCode.prof myCode.py</code></pre>
<p>The output will be a binary file.</p>
<h1>Visualising</h1>
<p>There are several different packages that can be used to better visualise your profile data.</p>
<h2>gprof2dot</h2>
<p>One of the simplest way to visualise your data is with <a href="https://github.com/jrfonseca/gprof2dot" target="_self">gprof2dot</a> </p>
<pre><code>pip install gprof2dot --user</code></pre>
<pre><code>gprof2dot -f pstats myCode.prof | dot -Tpng -o myCode.png</code></pre>
<p>This will generate a .png file showing a breakdown of functions run by your code.</p>
<p>Either download the image, or view it on the cluster using display myCode.png (requires X11 setup)</p>
<h2>snakevis</h2>
<p><a href="https://jiffyclub.github.io/snakeviz/">https://jiffyclub.github.io/snakeviz/</a></p>
<p> </p>