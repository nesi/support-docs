---
created_at: 2025-02-20
title: High Performance Computing
hide: 
  - toc
---

Technical Documentation for NeSI's High Performance Computing Cluster, Mahuika.

## Quickstart

<div class="grid cards" markdown>

-   ![](../assets/icons/material/account-details.svg){ .index-icon } __NeSI Accounts__

    ---

    How to get started with NeSI accounts and projects.

    - [Creating a NeSI Account](../Access/Accounts-Projects_and_Allocations/Creating_a_NeSI_Account_Profile.md)
    - [Applying For a New NeSI Project](../Access/Accounts-Projects_and_Allocations/Applying_for_a_new_NeSI_project.md)
    - [Applying to Join a NeSI Project](../Access/Accounts-Projects_and_Allocations/Applying_to_join_an_existing_NeSI_project.md)

-   ![](../assets/icons/material/compass.svg){ .index-icon } __Cluster Access__

    ---

    Recommended clients for Linux, Mac, and Windows users.

-   ![](../assets/icons/material/cog-transfer-outline.svg){ .index-icon } __SSH Config__

    ---

    How to Set Up your SSH config file.

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
