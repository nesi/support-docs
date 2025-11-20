---
created_at: 2025-11-20
description: Details on running fastStructure on the HPC
tags:
    - biology
    - software
---

## Using fastStructure executables

While the modules are python scripts, they must be run as executables, not python scripts, as in the following `sbatch`.

```sl
#!/bin/bash -e

#SBATCH --job-name        fastStructure
#SBATCH --account         nesi12345
#SBATCH --time            01:00:00
#SBATCH --mem             2G

module purge
module load fastStructure/1.0-gimkl-2020a-Python-2.7.18

structure.py -K 3 --input=<infile> --output=<outfile>
```

The `distruct.py` module may cause issues due to the module wanting to open a new window to view the plot. You may be able to work around this by telling `matplotlib` to write the plot to a file:

```bash
env MPLBACKEND='svg'
distruct.py --output myplot.svg
```

Thanks to our friends at Purdue for [their documentation about these issues](https://www.rcac.purdue.edu/software/faststructure).

## fastStructure `.str` format

fastStructure can take inputs in the form of a `.bed` file or an `.str` format
Despite using the same `.str` suffix, the format required for fastStructure differs from that required for Structure.
For fastStructure, no header row is required, but the first 6 columns of the file are ignored and there must be two lines per sample. Below is an example input (`input.str`) that will work with fastStructure:

```input.str
#	#	#	#	Smpl_ID	Pop_ID	Locus_1	Locus_2	Locus_3	Locus_4	Locus_5	Locus_6	Locus_7	Locus_8	Locus_9	Locus_10
#	#	#	#	Sample1	1	1	-9	0	1	0	1	1	1	1	0
#	#	#	#	Sample1	1	1	-9	1	0	1	0	0	0	0	1
#	#	#	#	Sample2	2	0	0	1	1	1	0	1	1	0	1
#	#	#	#	Sample2	2	1	0	1	0	1	1	0	1	0	1
```

To use this, use the `--format=str` flag and include the file **without** the file extension `--input=input` or fastStructure will append an extra `.str` to the filename.

Shout out to a [rather old blog post](https://flowersoftheocean.wordpress.com/2018/04/15/running-faststructure-and-associated-difficulties/) for solving this issue!

The `.str` files output by [ipyrad](../../Scientific_Computing/Supported_Applications/ipyrad.md) should work without issue. Otherwise you may want to convert `.vcf` files to `.bed` files using another tool and proceed with fastStructure using the `.bed` files.
