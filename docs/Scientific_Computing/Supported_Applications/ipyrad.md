---
created_at: '2022-09-26T08:09:35Z'
hidden: false
label_names: []
position: 2
title: ipyrad
vote_count: 0
vote_sum: 0
zendesk_article_id: 5565081844623
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<h1><span>Description</span></h1>
<p><strong>ipyrad</strong><span>, an interactive assembly and analysis toolkit for restriction-site associated DNA (RAD-seq) and related data types. Please explore the documentation to find out more about the features of ipyrad.\</span></p>
<p><span>Home page is at https://ipyrad.readthedocs.io/en/latest/index.html</span></p>
<h2 dir="auto">Cite the Manuscript</h2>
<p dir="auto">Eaton DAR &amp; Overcast I. "ipyrad: Interactive assembly and analysis of RADseq datasets." Bioinformatics (2020).</p>
<h2 dir="auto">License</h2>
<p dir="auto">GPLv3</p>
<h2 dir="auto">Getting Started</h2>
<p>Following <strong>example</strong> uses  rad_example which can be downloaded as per instructions on  <a href="https://ipyrad.readthedocs.io/en/latest/tutorial_advanced_cli.html">https://ipyrad.readthedocs.io/en/latest/tutorial_advanced_cli.html</a> </p>
<pre>$ curl -LkO https://eaton-lab.org/data/ipsimdata.tar.gz
$ tar -xvzf ipsimdata.tar.gz</pre>
<p><span>Start by creating a new Assembly  <span></span><code>data1</code>  , and then we’ll edit the params file to tell it how to find the input data files for this data set.</span></p>
<pre><span>$ module purge<br>$ module load ipyrad/0.9.85-gimkl-2022a-Python-3.10.5<br>$ ipyrad -n data1<br><br>New file 'params-data1.txt' created in ........<br><br></span></pre>
<p><span><code>params-data1.txt</code> will be created on current working directory. Review and edit the paths in parameter file to match the destinations of input data, barcode paths,etc. </span></p>
<h2><span id="Job_Script_for_Using_Multiple_Cores_on_a_Single_Compute_Node" class="mw-headline">Slurm Script for Using Multiple CPUs a Single Compute Node</span></h2>
<pre>#!/bin/bash<br><br>#SBATCH --account       nesi12345<br>#SBATCH --job-name      ipyrad<br>#SBATCH --cpus-per-task 12<br>#SBATCH --time          00:05:00<br>#SBATCH --mem           10G<br>#SBATCH --output        ipyrad_output_%j.txt<br><br>## assembly name<br>assembly_name="data1"<br><br>## load environment and module<br>module purge<br>module load ipyrad/0.9.85-gimkl-2022a-Python-3.10.5<br><br>## create, prepare and change to a job specific dir<br>jobdir="ipyrad_${SLURM_JOB_ID}"<br>params="params-${assembly_name}.txt"<br><br>mkdir $jobdir<br>sed "s#$(pwd) #$(pwd)/$jobdir#" $params &gt; $jobdir/$params<br>cd $jobdir<br><br><br>## call ipyrad on your params file and perform 7 steps from the workflow<br>srun ipyrad -p $params -s 12 --force <br><br><br></pre>