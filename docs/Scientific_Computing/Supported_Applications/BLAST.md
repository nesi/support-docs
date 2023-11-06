---
created_at: '2015-08-27T04:44:00Z'
hidden: false
label_names:
- mahuika
- biology
position: 26
title: BLAST
vote_count: 1
vote_sum: -1
zendesk_article_id: 208619807
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
<p> </p>
<h1 id="h_01HC1J2A6QTFF6AY7Q54W6AFSJ">BLAST Databases</h1>
<p>We download the standard NCBI databases quarterly, and create a corresponding environment module named like <code>BLASTDB/&lt;yyyy-mm&gt;</code> which sets the BLASTDB environment variable accordingly. If you want to use one of these databases then you should find out what our most recent version is (<code>module avail BLASTDB</code>) and then load it in your batch script.</p>
<pre>module load BLASTDB<br>ls $BLASTDB</pre>
<p>Because we only keep a few recent versions of the databases, you may be required from time to time to change the BLASTDB module version if you use old job submission scripts as templates for new ones.</p>
<h1 id="example-scripts">Example scripts</h1>
<p>When given a large amount of query sequence to get through the BLAST search programs will take batches of it, running through the database with each batch and then starting over with the next batch.  This can cause the database to be repeatedly read from disk and so limit the speed of your search, and using multiple threads only makes it worse. So there are two reasonable ways to run BLAST programs on our system: single threaded for small jobs, or multithreaded with a local copy of the database for large jobs.  If in doubt try the simpler single-thread approach first and see if it takes too long.</p>
<h2 id="h_01HC1J2A6Q5K7PZF9S9ANV7WRG">Single Thread</h2>
<p>For jobs which need less than 24 CPU-hours, eg: those that use small databases (&lt; 10 GB) or small amounts of query sequence (&lt; 1 GB), or fast BLAST programs such as <em>blastn</em> with its default (megablast) settings.  </p>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      BLAST
#SBATCH --time          00:30:00  # ~10 CPU minutes / MB blastn query vs nt
#SBATCH --mem           30G<br>#SBATCH --cpus-per-task 2

module load BLAST/2.13.0-GCC-11.3.0
module load BLASTDB/2023-01

# This script takes one argument, the FASTA file of query sequences.
QUERIES=$1
FORMAT="6 qseqid qstart qend qseq sseqid sgi sacc sstart send staxids sscinames stitle length evalue bitscore"
BLASTOPTS="-evalue 0.05 -max_target_seqs 10"
BLASTAPP=blastn
DB=nt
#BLASTAPP=blastx
#DB=nr

$BLASTAPP $BLASTOPTS -db $DB -query $QUERIES -outfmt "$FORMAT" \
    -out $QUERIES.$DB.$BLASTAPP -num_threads $SLURM_CPUS_PER_TASK
</code></pre>
<h2 id="h_01HC1J2A6QA3D40BVABPFE25C2">Multiple threads and local database copy</h2>
<p>For jobs which need more than 24 CPU-hours, eg: those that use large databases (&gt; 10 GB) or large amounts of query sequence (&gt; 1 GB), or slow BLAST searches such as classic <em>blastn</em> (<code class="bash">blastn -task blastn</code>).</p>
<p>This script copies the BLAST database into the per-job temporary directory $TMPDIR before starting the search. Since compute nodes do not have local disks, this database copy is in memory, and so must be allowed for in the memory requested by the job.  As of mid 2023 that is 283 GB for the <em>nt</em> database, 157 GB for <em>refseq_protein. </em><span></span></p>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      BLAST
#SBATCH --time          02:30:00
#SBATCH --mem           120G  # 30 GB plus the database
#SBATCH --ntasks        1
#SBATCH --cpus-per-task 36    # half a node

module load BLAST/2.13.0-GCC-11.3.0
module load BLASTDB/2023-01

# This script takes one argument, the FASTA file of query sequences.
QUERIES=$1
FORMAT="6 qseqid qstart qend qseq sseqid sgi sacc sstart send staxids sscinames stitle length evalue bitscore"
BLASTOPTS="-task blastn"
BLASTAPP=blastn
DB=nt
#BLASTAPP=blastx
#DB=nr

# Keep the database in RAM
cp $BLASTDB/{$DB,taxdb}.* $TMPDIR/ 
export BLASTDB=$TMPDIR

$BLASTAPP $BLASTOPTS -db $DB -query $QUERIES -outfmt "$FORMAT" \
    -out $QUERIES.$DB.$BLASTAPP -num_threads $SLURM_CPUS_PER_TASK
</code></pre>
<p> </p>