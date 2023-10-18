---
created_at: '2016-05-05T04:11:49Z'
hidden: true
label_names:
- mahuika
- tier1
- biology
position: 23
title: ALLPATHS-LG
vote_count: 0
vote_sum: 0
zendesk_article_id: 218740578
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
<p>ALLPATHS-LG is a short read genome assembler from the Computational Research and
Development group at the Broad Institute.</p>
<p>The ALLPATHS-LG home page is at <a href="http://www.broadinstitute.org/software/allpaths-lg/blog/">http://www.broadinstitute.org/software/allpaths-lg/blog/</a>.</p>
<h1 id="available-modules">Available modules</h1>
<h2 id="packages-with-modules">Packages with modules</h2>
<table>
  <tr>
    <th>Module</th>
    <th>NeSI Cluster</th>
  </tr>
  <tr>
    <td>ALLPATHS-LG/50041-goolf-1.5.14</td>
    <td>pan</td>
  </tr>
</table>

<h1 id="licensing-requirements">Licensing requirements</h1>
<p>ALLPATHS-LG is made available at no cost subject to a permissive open-source
licence, the full text of which is available at <a href="ftp://ftp.broadinstitute.org/pub/crd/ALLPATHS/Release-LG/LICENSE">ftp://ftp.broadinstitute.org/pub/crd/ALLPATHS/Release-LG/LICENSE</a>.</p>
<h1 id="example-scripts">Example scripts</h1>
<h2 id="example-script-for-the-pan-cluster">Example script for the Pan cluster</h2>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      ALLPATHS-LG_job
#SBATCH --account       nesi99999
#SBATCH --time          01:00:00
#SBATCH --mem-per-cpu   4G
#SBATCH --output        ALLPATHS-LG_job.%j.out # Include the job ID in the names
#SBATCH --error         ALLPATHS-LG_job.%j.err # of the output and error files

module load ALLPATHS-LG/50041-goolf-1.5.14

# Arguments are from the basic example in the ALLPATHS-LG documentation; please
# modify them as necessary
srun RunAllPathsLG PRE=/assemblies DATA=datadir RUN=rundir SUBDIR=attempt1
</code></pre>