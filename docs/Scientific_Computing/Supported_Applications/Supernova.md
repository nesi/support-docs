---
created_at: '2019-01-27T23:11:01Z'
tags:
- mahuika
- biology
title: Supernova
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000718515
zendesk_section_id: 360000040076
---

{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}

## Description

Supernova is a software package for *de novo* assembly from Chromium
Linked-Reads that are made from a single whole-genome library from an
individual DNA source. Supernova creates diploid assemblies, thus
separately representing maternal and paternal chromosomes over long
distances.

The Supernova software package includes two processing pipelines and one
for post-processing:

- `supernova mkfastq` wraps Illumina's bcl2fastq to correctly
    demultiplex Chromium-prepared sequencing samples and to convert
    barcode and read data to FASTQ files.
- `supernova run` takes FASTQ files containing barcoded reads from
    `supernova mkfastq` and builds a graph-based assembly. The approach
    is to first build an assembly using read kmers (K = 48), then
    resolve this assembly using read pairs (to K = 200), then use
    barcodes to effectively resolve this assembly to K ≈ 100,000. The
    final step pulls apart homologous chromosomes into phase blocks,
    which are often several megabases in length.
-   `supernova mkoutput` takes Supernova's graph-based assemblies
    and produces several styles of FASTA suitable for downstream
    processing and analysis.

Download latest release from 10xGenomics.

<https://support.10xgenomics.com/de-novo-assembly/software/downloads/latest>

## Availability

`Supernova/2.1.1` is installed as a module and can be loaded via
`module load Supernova`

## License

The developer grants a Limited License to all users. If you intend to
use Supernova on NeSI operated infrastructure please read the developers
own licensing agreement.

<https://support.10xgenomics.com/de-novo-assembly/software/downloads/latest>

## Example script``

``` sl
#SBATCH -J mySupernovajob
#SBATCH --partition=hugemem
#SBATCH --ntasks=1
#SBATCH --mem=460G
#SBATCH --cpus-per-task=16
#SBATCH --time=168:00:00
#SBATCH --hint=nomultithread

module load Supernova/2.1.1

supernova run --id=.....................
```

## Getting Supernova to run successfully

We suggest users initially read the developers notes, at
<https://support.10xgenomics.com/de-novo-assembly/guidance/doc/achieving-success-with-de-novo-assembly>

Further to that we also suggest,

- check --maxreads, to be passed to supernova, is correctly set.
    Recommended
    reading..[https://bioinformatics.uconn.edu/genome-size-estimation-tutorial/](https://bioinformatics.uconn.edu/genome-size-estimation-tutorial/#)<http://qb.cshl.edu/genomescope/>
- When passing `--localmem` to supernova, ensure this number is less
    than the total memory passed to Slurm.
- Pass `${SLURM_CPUS_PER_TASK}` to supernova with the `--localcores`
    argument.

## Tracking job progress via browser

Find the beginning of the `_log ` file, located in the directory where
the call to supernova was run, or the path specified in the Slurm batch
file via `--output`.

``` bash
    head -n 30 <job_name>.out

supernova run (2.1.1)

Copyright (c) 2018 10x Genomics, Inc. All rights reserved.
-------------------------------------------------------------------------------

Martian Runtime - '2.1.1-v2.3.3'
Serving UI at http://wbh001:37982?auth=Bx2ccMZmJxaIfRNBOZ_XO_mQd1njNGL3rZry_eNI1yU

Running preflight checks (please wait)...
```

 Find the line..

``` bash
Serving UI at http://wbh001:37982?auth=Bx2ccMZmJxaIfRNBOZ_XO_mQd1njNGL3rZry_eNI1yU 
```

The link assumes the form..

**http:// &lt;node&gt;: &lt;port&gt;?&lt;auth&gt;**

- &lt;node&gt; Taken from above code snippet is wbh001
- &lt;port&gt; Taken from above code snippet is 37982
- &lt;auth&gt; Taken from above code snippet is
    Bx2ccMZmJxaIfRNBOZ\_XO\_mQd1njNGL3rZry\_eNI1yU 

In a new local terminal window open an ssh tunnel to the node. This
takes the following general form

`ssh -L <d>:<node>:<port> -N <server>`

- &lt;d&gt; An integer
- &lt;server&gt; see: [Standard Terminal Setup](../../Scientific_Computing/Terminal_Setup/Standard_Terminal_Setup.md)

When details are added to the general form from the specifics in the
snippet above, the following could be run..

``` bash
ssh -L 9999:wbh001:39782 -N mahuika
```

Next, open your preferred web browser and construct the following link..

``` bash
http://localhost:<d>?<auth>
```

take &lt;d&gt; and &lt;auth&gt; from the code snippet above..

``` bash
http://localhost:9999/?auth=Bx2ccMZmJxaIfRNBOZ_XO_mQd1njNGL3rZry_eNI1yU
```

![Screen\_Shot\_2019-01-28\_at\_2.17.29\_PM.png](../../assets/images/Supernova.png)

## Things to watch out for

- Supernova will create checkpoints after completing stages in the
    pipeline. In order to run from a previously created checkpoint you
    will first need to delete the \_lock file located in the main output
    directory (the directory named by `ID=${SLURM_JOB_NAME}` where the
    `_log ` file is also located) and passed to supernova in the
    `--id=${ID}` argument in the sample Slurm script above. Avoid
    changing any other settings in both the call to Slurm and
    supernova.``````
