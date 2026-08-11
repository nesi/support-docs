---
title: OpenFold3
tags:
- biology
- machine_learning
- gpu
description: Predicting protein structures from amino acid sequences with OpenFold3
---

[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Description


## Referencing


## Setting up OpenFold3

### Downloading the parameters files 

If you are using OpenFold3 for the first time on Mahuika, you will need to download the OpenFold3 model parameters to your directory. 

1. Load OpenFold3:

	```bash
	module load OpenFold3
	```

2. Run `setup_openfold` in the terminal:

	```bash
	setup_openfold
	```

	* You will need to write out in full the direct path to where you want to store OpenFold3 files.
	* `Please specify the OpenFold cache directory`: Best idea to change this to your project folder. Example: `/nesi/project/<PROJECT_ID>/<USERNAME>/openfold3`
	* `Please specify the directory for parameter download`: This should default to your cache directory. Example `/nesi/project/<PROJECT_ID>/<USERNAME>/openfold3`
	* `Select parameters to download`: Download whatever parameters you would like.
	* `Force re-download parameters even if they already exist?`: Set this to `yes`
	* `Run integration tests?`: `no`

	The setup should look something like this

	```bash
	user.name@login03:~$ setup_openfold
	[2026-08-11 17:54:31,291] [WARNING] [real_accelerator.py:199:get_accelerator] Setting accelerator to CPU. If you have GPU or other accelerator, we were unable to detect it.
	Setting up OpenFold3...
	Please specify the OpenFold cache directory (default: /home/user.name/.openfold3): /nesi/project/nesi12345/user.name/openfold3
	Please specify the directory for parameter download (default: /nesi/project/nesi12345/user.name/openfold3): 
	Select parameters to download:
	1) Download only the default checkpoint (openfold3-p2-155k)
	2) Download all parameters (openfold3-p2-145k, openfold3-p2-155k)
	3) Download a specific parameter by name
	Enter your choice (1/2/3, default: 1): 2
	Force re-download parameters even if they already exist? (yes/no, default: no) yes
	Run integration tests? (yes/no) no
	Parameters directory set to: /nesi/project/nesi12345/user.name/openfold3
	Starting parameter download...
	Downloading s3://openfold3-data/openfold3-parameters/of3-p2-145k.pt (2.13 GB) to /nesi/project/nesi12345/user.name/openfold3/of3-p2-145k.pt...
	of3-p2-145k.pt: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.29G/2.29G [00:19<00:00, 115MB/s]
	Download complete.
	Downloading s3://openfold3-data/openfold3-parameters/of3-p2-155k.pt (2.13 GB) to /nesi/project/nesi12345/user.name/openfold3/of3-p2-155k.pt...
	of3-p2-155k.pt: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.29G/2.29G [00:19<00:00, 116MB/s]
	Download complete.
	Download completed successfully.
	Starting Biotite CCD setup...
	Biotite CCD file at /opt/nesi/zen3/OpenFold3/0.4.4-foss-2026-CUDA-13.2.1/lib/python3.14/site-packages/biotite/structure/info/components.bcif is up-to-date with s3://openfold3-data/components.bcif, skipping.
	Skipping integration tests.
	Setup configuration saved to /nesi/project/nesi12345/user.name/openfold3/setup_config.json
	```

	!!! warning

		If you get an error message relating to Biotite CCD, get in touch with support.

3. Add the following line to your `.bashrc` and source it:

	```bash
	printf '\n# Path to your OpenFold3 Cache\nexport OPENFOLD_CACHE=/nesi/project/<PROJECT_ID>/<USERNAME>/openfold3\n' >> ~/.bashrc
	source ~/.bashrc
	```

	Check that your `OPENFOLD_CACHE` path is correct:

	```bash
	echo $OPENFOLD_CACHE
	```

	If this doesn't look right, you will need to change your `~/.bashrc` file by using `nano` or `vim`

4. Test that your setup was successful. In the terminal, copy the following json file from [openfold3](from https://github.com/aqlaboratory/openfold-3/blob/main/examples/example_inference_inputs/query_ubiquitin.json): 

	```bash
	cat > query_ubiquitin.json << 'EOF'
	{
	  "queries": {
	    "ubiquitin": {
	      "chains": [
	        {
	          "molecule_type": "protein",
	          "chain_ids": ["A"],
	          "sequence": "MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG"
	        }
	      ]
	    }
	  }
	}
	EOF
	```

	Then run the following in your terminal:

	```bash
	python - <<'EOF'
	import os, pathlib, zipfile

	import openfold3
	from openfold3.projects.of3_all_atom.config.inference_query_format import InferenceQuerySet
	print("[ok] openfold3 imports")

	import biotite.structure.info as info
	print(f"[ok] CCD: {len(info.all_residues())} components, "
	      f"ALA={info.residue('ALA').array_length()} atoms")

	cache = pathlib.Path(os.environ.get("OPENFOLD_CACHE", pathlib.Path.home() / ".openfold3"))
	ckpts = sorted(cache.glob("*.pt"))
	assert ckpts, f"no checkpoint in {cache}"
	for c in ckpts:
	    print(f"[ok] checkpoint {c.name}: {c.stat().st_size/1e9:.2f} GB, "
	          f"intact={zipfile.is_zipfile(c)}")

	InferenceQuerySet.from_json("query_ubiquitin.json")
	print("[ok] query JSON validates against this version's schema")
	EOF
	```

	If successful, you will get the following output:

	```bash
	[2026-08-11 18:03:24,289] [WARNING] [real_accelerator.py:199:get_accelerator] Setting accelerator to CPU. If you have GPU or other accelerator, we were unable to detect it.
	[ok] openfold3 imports
	[ok] CCD: 49282 components, ALA=13 atoms
	[ok] checkpoint of3-p2-145k.pt: 2.29 GB, intact=True
	[ok] checkpoint of3-p2-155k.pt: 2.29 GB, intact=True
	[ok] query JSON validates against this version's schema
	```

### Downloading the database files

1. `cd` into the path where you would like to store your OpenFold3 databases. Ideally, this should be in your project directory:

	```bash
	mkdir -p /nesi/project/<PROJECT_ID>/openfold3_databases
	cd /nesi/project/<PROJECT_ID>/openfold3_databases
	```

2. Load OpenFold3:

	```bash
	module load OpenFold3
	```

3. Download the desired databases from the list below:

	```bash
	aws s3 ls --no-sign-request --human-readable s3://openfold/alignment_databases/
	```

	For example, the following will download and uncompress your desired databases:

	```bash
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/rfam.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/pdb_seqres.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/rnacentral.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/nucleotide_collection.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/uniref90.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/uniprot.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/mgnify.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/uniref30.tar.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/cfdb.tar.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/bfd.tar.gz .
	```

	Be mindful of the amount of space you will need before you download the databases:

	| #  | Database | Format | Size | Type |
	|----|----------------------|------------|--------|--------------------|
	| 1  | pdb_seqres | .fasta.gz | 55 MB | protein |
	| 2  | rfam | .fasta.gz | 61 MB | RNA |
	| 3  | nucleotide_collection | .fasta.gz | 2.3 GB | RNA |
	| 4  | rnacentral | .fasta.gz | 4.2 GB | RNA |
	| 5  | uniref90 | .fasta.gz | 47 GB | protein |
	| 6  | uniprot | .fasta.gz | 61 GB | protein |
	| 7  | mgnify | .fasta.gz | 79 GB | protein |
	| 8  | uniref30 | .tar.gz | 141 GB | protein (HHblits) |
	| 9  | cfdb | .tar.gz | 290 GB | protein (HHblits) |
	| 10 | bfd | .tar.gz | 292 GB | protein (HHblits) |

	**Total download:** ~918 GB — budget ~3–4 TB of filesystem for the decompressed set.

