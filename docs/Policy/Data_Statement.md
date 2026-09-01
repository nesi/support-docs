---
created_at: '2026-08-18T00:20:08Z'
tags:
- data
- data management
- data retention
description: Statement about the data on REANNZ platform
---

## Purpose

This Data Retention statement sets out how long user information is retained on the storage systems of the HPC Platform of Research and Education Advanced Network New Zealand (REANNZ), the circumstances in which it is removed, and the responsibilities that attach to holding data on the platform. It exists so that project owners can plan their research data lifecycle.

The retention periods that apply to each filesystem are published in [Filesystems and Quotas](../Storage/Filesystems_and_Quotas.md). 
This page lists the principles behind them.

## Scope

This statement applies to all users with any data on REANNZ HPC systems. This aims to assist users to make full use of the available data storage infrastructures and to understand their responsibilities.
All Users who are using the REANNZ Data storage must be aware of the content of this statement when using the REANNZ facilities.

## Principles

- All users are required to provide and, update as needed, their names, telephone number, email address and check that they belong to the correct organisation(s). Please contact [REANNZ]({% include "partials/support_request.html" %}) if it is not the case.
- The project owners, when leaving their organisation, must update the project records with subsequent owners in case of data being still present in REANNZ systems.
- It is the responsibility of the project owners to acknowledge all communications from the REANNZ staff.
- Project owners are given notice before data is deleted under REANNZ cleaning process with the contact information provided by the active project owners (and other active members).
    - for the scratch filesystem, an email is sent prior to the deletion cycle. Please contact [REANNZ]({% include "partials/support_request.html" %}) if you need to keep the data longer.
    - for the project and home filesystems as well as the freezer data, emails are sent on three occasions at least one month before the deletion is triggered. Please contact [REANNZ]({% include "partials/support_request.html" %}) if the project is going to be reopen or if the user is still going to use the REANNZ services.
- Data (in read-only mode) is retained for a defined period after a project or account ends, so that research outputs can be recovered or migrated in an orderly way.
- Responsibility for ensuring that irreplaceable data exists in more than one place rests with the project owners.
- In case of loss of ownership where project owners have left their organisation, REANNZ staff will contact the institution contacts to determine what to do with the data. 
- Each institution using REANNZ HPC Systems is expected to have its own guidance and procedures supporting effective data curation, and Users are expected to be aware of the data retention obligations that apply within their own institution. Nothing in this policy displaces those obligations, or the limits of liability set out in the [Acceptable Use Policy](Acceptable_Use_Policy.md).
- REANNZ will inform the users of any other events related to the data infrastructure (e.g. outages, failure, migration) from the REANNZ status page or by email.

## Roles and Responsibilities

### All User Responsibilities

- Store data on the filesystem appropriate to its purpose and to how long it needs to be kept.
- Act on notifications of pending deletion, and not circumvent automated cleaning processes.
- Maintain their own copies of any data they cannot afford to lose.
- Remove data that is no longer required.

### Project Owners Responsibilities

Ownership of a project carries accountability for the data held within it.

- Knowing what data the project holds, where it is stored, and which retention period applies to it.
- Ensuring that data of long-term value is held somewhere with a retention period that matches that value.
- Ensuring the project has a copy of irreplaceable data outside REANNZ HPC Systems.
- Be aware of any communication about data deletion.
- Planning for the end of the project, and migrating or deleting data before the applicable retention period expires.
- Ensuring the project's data handling is consistent with their own institutions' policies.
- Maintaining an accurate list of project members, and revoking access when a member no longer has a legitimate need for it.
- Notifying REANNZ before they cease to be able to act as Project Owner, so that accountability for the project's data can be transferred to a named successor.


### REANNZ Responsibilities

- Publishing retention periods and giving notice of any change to them.
- Providing notice before data is deleted wherever practicable.


!!! info "NeSI-REANNZ Integration"
    On 01 July 2025, New Zealand eScience Infrastructure (NeSI) was integrated into Research and Education Advanced Network New Zealand (REANNZ) Ltd. At that time, all aspects of NeSI delivery, including this policy, became the responsibility of REANNZ. Currently, some of our online spaces (e.g. `docs.nesi.org.nz`, `my.nesi.org.nz`, etc.) and email addresses (e.g. `support@nesi.org.nz`) have retained a ‘NeSI’ brand as we transition our services and develop a longer-term strategy for this integrated platform.
