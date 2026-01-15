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

Name | Path |
|--|--|
alphafold_db |`/opt/nesi/db/alphafold_db`
blast |`/opt/nesi/db/blast`
cartopy |`/opt/nesi/db/cartopy`
centrifuge |`/opt/nesi/db/centrifuge`
CheckM2_DB |`/opt/nesi/db/CheckM2_DB`
CheckM_DB |`/opt/nesi/db/CheckM_DB`
checkv-db-v0.6 |`/opt/nesi/db/checkv-db-v0.6`
dammit_db |`/opt/nesi/db/dammit_db`
DAS_DB |`/opt/nesi/db/DAS_DB`
db/ |`/opt/nesi/db/db/`
dfam_3.9 |`/opt/nesi/db/dfam_3.9`
DRAM_1.3.5 |`/opt/nesi/db/DRAM_1.3.5`
eggnog_db |`/opt/nesi/db/eggnog_db`
FCS-GX |`/opt/nesi/db/FCS-GX`
gtdbtk_202 |`/opt/nesi/db/gtdbtk_202`
gtdbtk_207_v2 |`/opt/nesi/db/gtdbtk_207_v2`
gtdbtk_214 |`/opt/nesi/db/gtdbtk_214`
gtdbtk_220 |`/opt/nesi/db/gtdbtk_220`
Humann |`/opt/nesi/db/Humann`
Kaiju |`/opt/nesi/db/Kaiju`
Kraken2 |`/opt/nesi/db/Kraken2`
megaX |`/opt/nesi/db/megaX`
nesi-apps-admin |`/opt/nesi/db/nesi-apps-admin`
nullarbor_db |`/opt/nesi/db/nullarbor_db`
Pfam |`/opt/nesi/db/Pfam`
PhyloPhlAn |`/opt/nesi/db/PhyloPhlAn`
prokka |`/opt/nesi/db/prokka`
ProteinDataBank |`/opt/nesi/db/ProteinDataBank`
RQCFilterData |`/opt/nesi/db/RQCFilterData`
sortmerna_db |`/opt/nesi/db/sortmerna_db`
SqueezeMeta |`/opt/nesi/db/SqueezeMeta`
StrVCTVRE |`/opt/nesi/db/StrVCTVRE`
TEST |`/opt/nesi/db/TEST`
Trinotate |`/opt/nesi/db/Trinotate`
Uniprot |`/opt/nesi/db/Uniprot`
VariantEffectPredictor |`/opt/nesi/db/VariantEffectPredictor`
VIBRANT_v1.2.1_databases |`/opt/nesi/db/VIBRANT_v1.2.1_databases`
VirSorter |`/opt/nesi/db/VirSorter`
waafle |`/opt/nesi/db/waafle`

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
We recommend you utilize the [Globus endpoint provided by JGI](https://genome.jgi.doe.gov/portal/help/download.jsf#/globus) to directly transfer files from the JGI servers to Mahuika.
For more information about using Globus on Mahuika see [the Globus docs section](../Data_Transfer/Globus/Overview.md).

### NCBI

We have two environmental modules to aid in finding and downloading data from NCBI:

- the [NCBI Datasets command-line tools](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/command-line-tools/download-and-install/): `module avail datasets`
- the [EDirect command line interface](https://www.ncbi.nlm.nih.gov/books/NBK179288/) with the [Entrez search system](https://www.ncbi.nlm.nih.gov/books/NBK3837/): `module avail entrez-direct`
