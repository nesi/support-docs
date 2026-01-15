---
created_at: 2026-01-15
description: Information about databases on Mahuika
tags:
    - database
    - biology
---

Many research projects use reference or external databases.
This page describes databases that exist on Mahuika for use as well as recommendations for using some specific external databases.

## Maintained databases on Mahuika

Some databases are readable for all users on Mahuika.
These databases can be found at `/opt/nesi/db`.
Some environmental modules depend on these databases and connect to these directories automatically.

``` sh
ls -la /opt/nesi/db
```

```sh
-rw-rw-r--  1 nesi-apps-admin nesi-apps-admin  457 Jun 16  2025 2_dram_preparedatabases.slurm
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Dec  1  2024 alphafold_db
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Oct 29 19:14 blast
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Sep 10  2021 cartopy
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Jan 13  2020 centrifuge
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Jan 30  2023 CheckM2_DB
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Jul 21  2019 CheckM_DB
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 May  7  2020 checkv-db-v0.6
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Feb 20  2021 dammit_db
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Oct 17  2022 DAS_DB
drwxr-xr-x+ 1 nesi-apps-admin nesi-apps-admin    0 Nov 12 07:36 dfam_3.9
-rw-rw-r--  1 nesi-apps-admin nesi-apps-admin 2400 Apr 18  2022 down_pdb_mmcif.sh
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Sep 27  2022 DRAM_1.3.5
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Oct 17  2023 eggnog_db
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Jun 16  2024 FCS-GX
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Jul 19  2021 gtdbtk_202
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 May  9  2022 gtdbtk_207_v2
drwxr-xr-x  1 nesi-apps-admin nesi-apps-admin    0 Apr 27  2023 gtdbtk_214
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Apr 10  2024 gtdbtk_220
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Mar 13  2022 Humann
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Mar  5  2022 Kaiju
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Mar 31  2025 Kraken2
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Feb 26  2021 megaX
drwxr-xr-x  1 nesi-apps-admin nesi-apps-admin    0 Feb 21  2025 nesi-apps-admin
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Jan 27  2021 nullarbor_db
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Nov  7  2023 Pfam
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Mar  4  2022 PhyloPhlAn
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Jul 15  2019 prokka
drwxr-xr-x  1 nesi-apps-admin nesi-apps-admin    0 Aug 18  2023 ProteinDataBank
dr-xr-xr-x  1 nesi-apps-admin nesi-apps-admin    0 Jan 24  2020 RQCFilterData
drwxrwxr-x+ 1 nesi-apps-admin nesi-apps-admin    0 Feb  4  2021 sortmerna_db
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Sep  8 12:17 SqueezeMeta
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Mar 16  2020 StrVCTVRE
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Mar 29  2023 TEST
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Feb 26  2021 Trinotate
drwxr-xr-x  1 nesi-apps-admin nesi-apps-admin    0 Sep 22 08:43 Uniprot
-rw-------  1 nesi-apps-admin nesi-apps-admin  379 Jul 19  2021 UniRef30_2021_06.md5sums
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Jul  5  2021 VariantEffectPredictor
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Nov  2  2020 VIBRANT_v1.2.1_databases
drwxrwxr-x  1 nesi-apps-admin apps-team          0 Feb 10  2021 VirSorter
drwxrwxr-x  1 nesi-apps-admin nesi-apps-admin    0 Jul 27  2022 waafle
```

!!! note "Requesting new or updated databases"
    If there is a database you think may be useful to many Mahuika users, or if you would like an updated version of one of the maintained databases, please {% include "partials/support_request.html" %} with details about the source and version of the database of interest.

There are also some versioned databases which are accessible through environmental modules, specifically:

- AlphaFold2DB: `module avail AlphaFold2DB`
- AlphaFold3DB: `module avail AlphaFold3DB`
- BLASTDB: `module avail BLASTDB`

## Recommendations for obtaining data from selected external databases

### JGI Portals

The [Joint Genome Institute](https://jgi.doe.gov/) has many databases and data portals available.
To download/access files from JGI you will need to register for an account.
We recommend you utilize the [Global endpoint provided by JGI](https://genome.jgi.doe.gov/portal/help/download.jsf#/globus) to directly transfer files from the JGI servers to Mahuika.
For more information about using Globus on Mahuika see [the Globus docs section](../Data_Transfer/Globus/Overview.md).

### NCBI

We have two environmental modules to aid in finding and downloading data from NCBI:

- the [NCBI Datasets command-line tools](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/download-and-install/): `module avail datasets`
- the [EDirect command line interface](https://www.ncbi.nlm.nih.gov/books/NBK179288/) with the [Entrez search system](https://www.ncbi.nlm.nih.gov/books/NBK3837/): `module avail entrez-direct`
