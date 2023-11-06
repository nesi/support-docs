---
created_at: '2023-02-21T21:21:50Z'
hidden: true
label_names: []
position: 1
title: GATK
vote_count: 0
vote_sum: 0
zendesk_article_id: 6443618773519
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>The Genome Analysis Toolkit (GATK), developed at the <a href="http://www.broadinstitute.org/">Broad Institute</a>, provides a wide variety of tools focusing primarily on variant discovery and genotyping. It is regarded as the industry standard for identifying SNPS and indels in germline DNA and RNAseq data.</p>
<p>General documentation for running GATK can be found at their website <a href="https://gatk.broadinstitute.org/hc/en-us" target="_self">here.</a></p>
<p> </p>
<h1>Running GATK</h1>
<p>GATK uses <span>requires the Java Runtime Environment. The appropriate version of Java is already included as part of the GATK module, you will not need to load a Java module separately.</span></p>
<p> </p>
<p><span class="wysiwyg-underline"><strong>Note</strong></span>  :</p>
<ul>
<li>
<code>--time</code> and <code>--mem</code> defined in the following example are just place holders.</li>
<li>Please load the GATK version of your choice</li>
</ul>
<pre><code>#!/bin/bash -e<br>#SBATCH --job-name=MarkDuplicates<br>#SBATCH --output=%x_%j.out     # log file<br>#SBATCH --error=%x_%j.err      # error log file<br>#SBATCH --account=nesi12345    # your NeSI project code<br>#SBATCH --time=2:00:00         # maximum run time hh:mm:ss<br>#SBATCH --mem=30G              # maximum memory available to GATK<br><br># create temporary directory for Java so it does not fill up /tmp<br>TMPDIR=/nesi/nobackup/&lt;project_ID&gt;/GATK_tmp/<br>mkdir -p ${TMPDIR}<br><br># remove other modules that may be loaded<br># load specific GATK version<br>module purge<br>module load</code> GATK/4.3.0.0-gimkl-2022a<br><br># tell Java to use ${TMPDIR} as the temporary directory<br><code>export _JAVA_OPTIONS=-Djava.io.tmpdir=${TMPDIR} </code><br><br># run GATK command<br><code>gatk </code>MarkDuplicates I=input.bam O=marked_duplicates.bam M=marked_dup_metrics.txt</pre>
<p> </p>
<h2>GATK-Picard</h2>
<p><span class="ILfuVd" lang="en"><span class="hgKElc">GATK versions 4.0 or higher all contains a copy of the Picard toolkit, you will not need to separately load the Picard module. To run GATK-picard commands, use:<br></span></span></p>
<pre><span class="ILfuVd" lang="en"><span class="hgKElc">gatk &lt;picard function&gt; &lt;options&gt;</span></span></pre>
<p>This is different what what is currently written on the GATK documentation, you do not need to call "java -jar picard.jar &lt;Picard-function&gt;". Simply replace the Java parts with "gatk" and the function of interest.</p>
<p>Please also note that there are some inconsistencies between Picard and GATK flag naming conventions, so it is best to double check them.</p>
<p> </p>
<h1>Common Issues</h1>
<h2 id="Out-of-Memory-or-Insufficient-space-for-shared-memory-file" data-renderer-start-pos="101">Out of Memory or Insufficient Space for Shared Memory File<span class="heading-anchor-wrapper" role="presentation"></span>
</h2>
<p>This is related to temporary files being created by Java in <code>/tmp</code>, and then running out of space. If you see the error message <code>IOException: No space left on device</code>, this is not necessarily referring to your nobackup or projects directory, but is likely to be Java applications pointing to the small temporary filesystem available in a compute node.</p>
<p>To work around this, create another directory to use for temporrary files.</p>
<pre><code># create a new temporary directory<br>TMPDIR="/nesi/nobackup/&lt;project_directory&gt;/GATK_tmp/"<br>mkdir -p ${TMPDIR}<br><br># put this line in AFTER you load GATK but BEFORE running GATK<br>export _JAVA_OPTIONS=-Djava.io.tmpdir=${TMPDIR} </code></pre>
<p> </p>
<h2>File is not a supported reference file type</h2>
<p>The error message "File is not a supported reference file type" comes in one of the log files. It appears that sometimes GATK requires the file extension of "fasta" or "fa", for fasta files. Please make sure your file extensions correctly reflect the file type.</p>
<p> </p>
<p> </p>
<p> </p>