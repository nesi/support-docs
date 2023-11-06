---
created_at: '2020-03-13T03:23:18Z'
hidden: false
label_names: []
position: 13
title: MAKER
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001419576
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<h1 dir="auto">Local Customisations</h1>
<p dir="auto">Since the MAKER control file <em>maker_exe.ctl</em> is just an annoyance in an environment module based system we have patched MAKER to make that optional. If it is absent then the defaults will be used directly. </p>
<h1 dir="auto">Parallelism</h1>
<p>MAKER can be used with MPI, though due to a complicated interaction between Infiniband libraries and MAKER's use of forking it can't be used across multiple nodes. So we recommend running large MAKER jobs with up to 36 tasks on one node (ie: one full regular node), eg:</p>
<pre>#SBATCH --nodes=1<br>#SBATCH --ntasks-per-node=36<br>#SBATCH --mem-per-cpu=1500<br><br>module load MAKER/2.31.9-gimkl-2020a<br>srun maker -q</pre>
<h1>Resources</h1>
<p>MAKER creates many files in its output, sometimes hundreds of thousands.  There is a risk that you exhaust your quota of inodes, so:</p>
<ul>
<li>Don't run too many MAKER jobs simultaneously.</li>
<li>Delete unneeded output files promptly after MAKER finishes.  You can of course use <code>nn_archive_files</code> or <code>tar</code> to archive them first.</li>
</ul>
<p dir="auto"> </p>