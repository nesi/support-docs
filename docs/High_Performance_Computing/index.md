---
created_at: 2025-02-20
title: High Performance Computing
hide: 
  - toc
---

Technical Documentation for NeSI's High Performance Computing Cluster, Mahuika.

## Quickstart

<div class="grid cards" markdown>

-   ![](../assets/icons/material/account-details.svg) __Mahuika Cluster__

    ---
    Learn about our High Performance Computer _Mahuika_, and how to access.

    - [How to Get Access](Mahuika_Cluster/index.md)


-   ![](../assets/icons/material/compass.svg) __Data Management__

    ---

    Learn about the [NeSI filesystem](Data_Management/File_Systems_and_Quotas/index.md), and how to [transfer files](Data_Management/Moving_files_to_and_from_the_cluster.md).

-   ![](../assets/icons/material/cog-transfer-outline.svg) __Software__

    ---

    How to [load software](Software/index.md)

    Browse [installed software](Software/Software_Catalouge/index.md)
    
    How to [build software on Mahuika](Software/Building_Software/index.md).

-   ![](../assets/icons/material/cog-transfer-outline.svg) __Batch Computing__

    ---

    Learn about our scheduler [Slurm](), and how to make the most of your allocation.

</div>

## Popular

<div class="grid cards" markdown>

-   [__NeSI Accounts__](../Access/Accounts-Projects_and_Allocations/Applying_to_join_an_existing_NeSI_project.md)

    some description

-   [__NeSI Accounts__](../Access/Accounts-Projects_and_Allocations/Applying_to_join_an_existing_NeSI_project.md)
    
    some description


-   [__NeSI Accounts__](../Access/Accounts-Projects_and_Allocations/Applying_to_join_an_existing_NeSI_project.md)
    
    some description

</div>

## Announcements 

{% for file in files %}
{% if file.is_documentation_page() and file.src_uri.split("/")[0] == "Announcements" %}

[{{file.name}}]({{file.src_uri}})

{% endif %}

{% endfor %}
