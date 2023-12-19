---
created_at: '2023-07-13T01:04:38Z'
hidden: false
position: 0
tags: []
title: snpEff
vote_count: 0
vote_sum: 0
zendesk_article_id: 7403361932431
zendesk_section_id: 360000040076
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)
snpEff is a genetic variant annotation, and functional effect prediction
tool.

## Configuration File

snpEff requires a one-off configuration of the `.config` file. The
following instructions are a one-off set up of the configuration file
required for snpEff.

1. Load the latest version of the `snpEff` module.

2. Make a copy of the snpEff config file, replacing
   &lt;project\_id&gt;, with your project ID.

    ``` sl
    cp $EBROOTSNPEFF/snpEff.config /nesi/project/<project_id>/my_snpEff.config
    ```

3. Open the`my_snpEff.config` file, and edit **line 17** from the top
   to point to a preferred path within your project directory or home
   directory, e.g., edit line 17 `data.dir = ./data/` to something
   like:`data.dir =/nesi/project/<project_id>`  
   Please note that you must have read and write permissions to this
   directory.

4. Run `snpEff.jar` using the `-c` flag to point to your new config
   file, e.g., `-c path/to/snpEff/my_snpEff.config` For example:

    ``` sl
    java -jar $EBROOTSNPEFF/snpEff.jar -c /nesi/project/<project_id>/my_snpEff.config
    ```

## Example Script

You will need to set up your configuration file before you run snpEff.

``` sl
#!/bin/bash -e

#SBATCH --account        nesi12345
#SBATCH --job-name       my_snp_EFF_job
#SBATCH --time           20:00
#SBATCH --memory         4G
#SBATCH --output         %x_%j.out   # Name output file according to job name with Job ID

# purge all other modules that have already been loaded
module purge

# load specific snpEff version
module load snpEff/5.0-Java-11.0.4

# bring up help menu
java -jar $EBROOTSNPEFF/snpEff.jar -h

# run snpEff
java -jar $EBROOTSNPEFF/snpEff.jar -c /nesi/project/<project_id>/my_snpEff.config <other flags>
```
