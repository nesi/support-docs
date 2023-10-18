---
created_at: '2016-03-22T01:33:34Z'
hidden: true
label_names:
- mahuika
- tier1
- biology
position: 22
title: ABySS
vote_count: 0
vote_sum: 0
zendesk_article_id: 217751818
zendesk_section_id: 360000040076
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

<div class="toc">
<ul>
<li><a href="#description">Description</a></li>
<li>
<a href="#available-modules">Available modules</a><ul>
<li><a href="#packages-with-modules">Packages with modules</a></li>
</ul>
</li>
<li><a href="#licensing-requirements">Licensing requirements</a></li>
<li>
<a href="#example-scripts">Example scripts</a><ul>
<li><a href="#example-script-for-the-pan-cluster">Example script for the Pan cluster</a></li>
</ul>
</li>
</ul>
</div>
<h1 id="description">Description</h1>
<p>ABySS ("<strong>A</strong>ssembly <strong>By</strong> <strong>S</strong>hort <strong>S</strong>equences") is a <em>de novo</em>, parallel,
paired-end sequence assembler.</p>
<p>The ABySS home page is at <a href="http://www.bcgsc.ca/platform/bioinfo/software/abyss">http://www.bcgsc.ca/platform/bioinfo/software/abyss</a>.</p>
<h1 id="available-modules">Available modules</h1>
<h2 id="packages-with-modules">Packages with modules</h2>
<table>
  <tr>
    <th>Module</th>
    <th>NeSI Cluster</th>
  </tr>
  <tr>
    <td>ABySS/2.0.2-gimkl-2017a</td>
    <td>pan</td>
  </tr>
  <tr>
    <td>ABySS/2.0.1-foss-2015a</td>
    <td>pan</td>
  </tr>
</table>

<h1 id="licensing-requirements">Licensing requirements</h1>
<p>ABySS is made available at no cost for non-commercial use under the terms of
<a href="http://www.gnu.org/licenses/gpl-3.0.html">version 3 of the GNU General Public Licence</a> or,
at the option of the user, any later version of the same licence. Researchers
intending to use ABySS for commercial purposes should contact <a href="mailto:prebstein@bccancer.bc.ca">Patrick Rebstein</a>.
For more details, including the full text of the licence, please consult the
<code>LICENSE</code> file located in the <code>share/doc/abyss</code> subdirectory of the ABySS
installation directory.</p>
<h1 id="example-scripts">Example scripts</h1>
<h2 id="example-script-for-the-pan-cluster">Example script for the Pan cluster</h2>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name        ABySS_job
#SBATCH --account         nesi99999
#SBATCH --time            01:00:00
#SBATCH --mem-per-cpu     4G
#SBATCH --nodes           1 
#SBATCH --ntasks-per-node 12
#SBATCH --output          ABySS_job.%j.out # Include the job ID in the names
#SBATCH --error           ABySS_job.%j.err # of the output and error files

module load ABySS/2.0.1-foss-2015a

# This example specifies --ntasks-per-node and --nodes rather than the usual 
# --ntasks because, when given multiple CPUs, ABySS runs both MPI and non-MPI 
# parallel sub-programs.  It does its own MPI launching and so should not be 
# started via srun.
# See https://github.com/bcgsc/abyss#parallel-processing for details.

abyss-pe name=ecoli k=64 in='reads1.fa reads2.fa'
</code></pre>