---
created_at: '2026-09-28'
tags:
- account
description: Find your projects, project members, roles and resources in the REANNZ HPC Portal.
status: new
---

!!! warning "Beta testers only"
    Only users with a BSI email have access to [the new portal](https://hpc-portal.reannz.co.nz).  
    If you are not with BSI please continue using my.nesi.org,
    see [Logging In](../Getting_Started/my-nesi-org-nz/Logging_in_to_my-nesi-org-nz.md) for further instructions.

The [REANNZ HPC Portal](https://hpc-portal.reannz.co.nz) is where you see your projects,
who is in them, and the allocations (resources) they hold.
The portal is built on [Waldur](https://docs.waldur.com/latest/user-guide/).

## Log in

1. Go to [https://hpc-portal.reannz.co.nz](https://hpc-portal.reannz.co.nz).
2. Click **Sign in with REANNZ**.
    ![Sign in with REANNZ button](../assets/images/HPC_Portal_sign_in_with_reannz.png)
3. Choose your home institution and log in with your institutional credentials.
   This login goes through Tuakiri, the same as for my.nesi.org.nz.

If your institution is not part of the Tuakiri federation, see
[Account Requests for non-Tuakiri Members](../Policy/Account_Requests_for_non_Tuakiri_Members.md).
For other login problems, see
[Logging in to my.nesi.org.nz](../Getting_Started/my-nesi-org-nz/Logging_in_to_my-nesi-org-nz.md#troubleshooting-login-issues).

## Main navigation

The sidebar on the left holds the main sections:

- **Organizations** – the institutions you belong to.
- **Projects** – every project you are a member of.
- **Resources** – your allocations, grouped by type (for example **HPC** for Mahuika and **Storage** for Freezer).
- **REANNZ Marketplace** – the services on offer.

The breadcrumb at the top of each page shows where you are, for example
*Organizations / your institution / your project*.
Your name menu on the top right holds your profile and the option to log out.

## See your roles

After you log in, the portal opens your **User dashboard**.
The **Roles and permissions** table lists every role you hold:

| Column | Meaning |
| --- | --- |
| Scope type | Whether the role is on a project or an organization. |
| Scope name | The project or organization name. Click it to open it. |
| Organization | The institution that owns the project. |
| Role name | Your role, for example *Project manager* or *Project member*. |

## What each role can do

| Role | Who holds it | What they can do |
| --- | --- | --- |
| Project member | Researchers on a project | View the project and its resources, and request an end date change. |
| Project manager | The project owner or PI | Change resource limits and request an end date change. |
| Organization owner | Nominated staff at your institution | Approve orders and end date changes for their organization, and set end dates directly. See [HPC Portal Approvals](HPC_Portal_Approvals.md). |

## Guides

- [HPC Portal Projects](HPC_Portal_Projects.md) – find your projects, members and allocations.
- [HPC Portal Renewals](HPC_Portal_Renewals.md) – extend an end date or change limits.
- [HPC Portal Approvals](HPC_Portal_Approvals.md) – find and approve requests from your organization.
