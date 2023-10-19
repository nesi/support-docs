---
created_at: '2023-03-06T19:04:56Z'
hidden: false
label_names: []
position: 0
title: BRAKER
vote_count: 0
vote_sum: 0
zendesk_article_id: 6529511928207
zendesk_section_id: 360000040076
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h1><span>Description</span></h1>
<p dir="auto">The rapidly growing number of sequenced genomes requires fully automated methods for accurate gene structure annotation. With this goal in mind, we have developed BRAKER1<sup><a href="https://github.com/Gaius-Augustus/BRAKER#f1">R1</a></sup><sup><a href="https://github.com/Gaius-Augustus/BRAKER#f0">R0</a></sup>, a combination of GeneMark-ET<span> </span><sup><a href="https://github.com/Gaius-Augustus/BRAKER#f2">R2</a></sup><span> </span>and AUGUSTUS<span> </span><sup><a href="https://github.com/Gaius-Augustus/BRAKER#f3">R3,<span> </span></a></sup><sup><a href="https://github.com/Gaius-Augustus/BRAKER#f4">R4</a></sup>, that uses genomic and RNA-Seq data to automatically generate full gene structure annotations in novel genome.</p>
<p dir="auto">However, the quality of RNA-Seq data that is available for annotating a novel genome is variable, and in some cases, RNA-Seq data is not available, at all.</p>
<p dir="auto">BRAKER2 is an extension of BRAKER1 which allows for<span> </span><strong>fully automated training</strong><span> </span>of the gene prediction tools GeneMark-EX<span> </span><sup><a href="https://github.com/Gaius-Augustus/BRAKER#f14">R14,<span> </span></a></sup><sup><a href="https://github.com/Gaius-Augustus/BRAKER#f15">R15,<span> </span></a><a href="https://github.com/Gaius-Augustus/BRAKER#f17">R17,<span> </span></a></sup><sup><a href="https://github.com/Gaius-Augustus/BRAKER#g1">F1</a></sup><span> </span>and AUGUSTUS from RNA-Seq and/or protein homology information, and that integrates the extrinsic evidence from RNA-Seq and protein homology information into the<span> </span><strong>prediction</strong>.</p>
<p dir="auto">In contrast to other available methods that rely on protein homology information, BRAKER2 reaches high gene prediction accuracy even in the absence of the annotation of very closely related species and in the absence of RNA-Seq data.</p>
<p dir="auto">BRAKER3 is the latest pipeline in the BRAKER suite. It enables the usage of RNA-seq<span> </span><strong>and</strong><span> </span>protein data in a fully automated pipeline to train and predict highly reliable genes with GeneMark-ETP and AUGUSTUS. The result of the pipeline is the combined gene set of both gene prediction tools, which only contains genes with very high support from extrinsic evidence.</p>
<p dir="auto"> </p>
<p dir="auto">Home page : <a href="https://github.com/Gaius-Augustus/BRAKER">https://github.com/Gaius-Augustus/BRAKER</a></p>
<h1>License and Disclaimer</h1>
<p><span>All source code, i.e. </span><code>scripts/*.pl</code><span> or </span><code>scripts/*.py</code><span> are under the Artistic License (see </span><a href="http://www.opensource.org/licenses/artistic-license.php" rel="nofollow">http://www.opensource.org/licenses/artistic-license.php</a><span>).</span></p>
<h1>Prerequisites</h1>
<h3> </h3>
<blockquote class="blockquote-prereq">
<h3>Obtain GeneMark-ES/ET Academic License </h3>
<p>GeneMark-ES/ET which is one of the dependencies for BRAKER requires an individual academic license  (this is free). This can be obtained as below</p>
<ul>
<li>Download URL <a href="http://topaz.gatech.edu/genemark/license_download.cgi">http://topaz.gatech.edu/genemark/license_download.cgi</a>
</li>
</ul>
<p> </p>
<p> </p>
<ul>
<li class="wysiwyg-text-align-center"><img src="https://support.nesi.org.nz/hc/article_attachments/6529551751823" alt="genemark_es_license.png" width="476" height="464"></li>
<li>Downloaded filename will be in the format of<strong> gm_key_64.gz. </strong>
</li>
<li>Decompress this file with <code>gunzip gm_key_64.gz</code>  and move it to home directory as  a <strong>hidden</strong> file under the filename <code>.gm_key</code>  .i.e. <code>~/.gm_key</code>
</li>
</ul>
<h3>Copy AUGUSTUS config to a path with read/write permissions</h3>
<p>Make a copy of AUGUSTUS config from <strong><em>/opt/nesi/CS400_centos7_bdw/AUGUSTUS/3.4.0-gimkl-2022a/config</em> </strong> to path with read/write permissions .i.e. project, nobackup,home </p>
</blockquote>
<h2>Example Slurm scripts</h2>
<p>Following example uses the .fa files provided BRAKER developers on <a href="https://github.com/Gaius-Augustus/BRAKER/tree/master/example">https://github.com/Gaius-Augustus/BRAKER/tree/master/example</a></p>
<pre>#!/bin/bash -e<br><br>#SBATCH --account nesi12345<br>#SBATCH --job-name braker-test<br>#SBATCH --cpus-per-task 4<br>#SBATCH --mem 1G<br>#SBATCH --time 02:00:00<br>#SBATCH --output slurmlogs/%x.%j.out<br>#SBATCH --error slurmlogs/%x.%j.err<br><br><br>module purge<br>module load BRAKER/3.0.2-gimkl-2022a-Perl-5.34.1<br><br>#export the path to augustus config copied above - prerequisites<br>export AUGUSTUS_CONFIG_PATH=/path/to/augustus/config<br><br>srun braker.pl --threads=${SLURM_CPUS_PER_TASK} --genome=genome.fa --prot_seq=proteins.fa</pre>
<p>This will generate the output directory named <strong>braker</strong> in the current working directory with content similar to below </p>
<pre>augustus.hints.aa              braker.gtf   genemark_evidence.gff  prothint.gff<br>augustus.hints.codingseq       braker.log   genemark_hintsfile.gff seed_proteins.faa<br>augustus.hints.gtf             cmd.log      genome_header.map      species/<br>augustus.hints_iter1.aa        errors/      hintsfile.gff          uniqueSeeds.gtf<br>augustus.hints_iter1.codingseq evidence.gff hintsfile_iter1.gff    what-to-cite.txt<br>augustus.hints_iter1.gff       GeneMark-EP/ prevHints.gff <br>augustus.hints_iter1.gtf       GeneMark-ES/ proteins.fa </pre>