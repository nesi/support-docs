---
created_at: '2026-09-28'
tags:
- account
description: Find your projects, project members, roles and resources in the REANNZ HPC Portal.
status: new
---

The [REANNZ HPC Portal](https://hpc-portal.reannz.co.nz) is where you see your projects,
who is in them, and the allocations (resources) they hold.
The portal is built on [Waldur](https://docs.waldur.com/latest/user-guide/).

## Log in

1. Go to [https://hpc-portal.reannz.co.nz](https://hpc-portal.reannz.co.nz).
2. Click **Sign in with REANNZ**.
    ![Sign in with REANNZ button](../../assets/images/HPC_Portal_sign_in_with_reannz.png)
3. Choose your home institution and log in with your institutional credentials.
   This login goes through Tuakiri, the same as for my.nesi.org.nz.

If your institution is not part of the Tuakiri federation, see
[Account Requests for non-Tuakiri Members](../../Policy/Account_Requests_for_non_Tuakiri_Members.md).
For other login problems, see
[Logging in to my.nesi.org.nz](../my-nesi-org-nz/Logging_in_to_my-nesi-org-nz.md#troubleshooting-login-issues).

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
| Organization owner | Nominated staff at your institution | Approve requests from projects in their organization and set end dates directly. |

## See your projects

1. Click **Projects** in the sidebar.
2. Each card shows the project name, its **Organization**, its **Resources** and its **End date**.
3. Click **Details** to open the project.

A project page has four tabs:

- **Project dashboard** – description, team summary and usage views.
- **Resources** – the allocations the project holds.
- **Team** – the project members.
- **Audit logs** – a record of changes to the project.

## See project members

1. Open the project and click the **Team** tab.
2. The **Active** list shows each **Member**, their **Email**, their **Role in project** and any **Role expiration**.
3. The **Invitations** list shows people invited who have not yet joined.

## See resources

1. Open the project and click the **Resources** tab, or pick a group under **Resources** in the sidebar.
2. Click a resource to open it.

The resource page shows:

- the offering, for example **Mahuika** or **Freezer**;
- the **Termination date**, when the allocation ends;
- current usage against each limit, for example compute, project storage and scratch storage;
- a **Usage history** chart.

The **Actions** button on the resource page lists what you can do with it.
The options depend on your role.
To extend or grow an allocation, see
[Renewing an Allocation](Renewing_an_Allocation.md).

## Extending a Request

Allocations on Mahuika and Freezer have an end date.
To keep using an allocation past that date, ask for a new end date in the
[REANNZ HPC Portal](https://hpc-portal.reannz.co.nz).
To make an allocation bigger or smaller, change its limits.

These are two separate requests, approved by different people.
To renew *and* grow an allocation, make both.

!!! note "Renew in the portal, not through an allocation call"
    To renew an existing project, use the steps on this page.
    Do not apply to an allocation call again.
    A call application creates a new project with a new project code.

### Before you start

- You need a role on the project. See [Navigating the HPC Portal](Navigating_the_HPC_Portal.md#see-your-roles).
- Make your request **before** the current end date.
  The portal does not accept an end date in the past,
  and an allocation may be removed once its end date has passed.
- Request well ahead. Do not wait for a reminder.

### Extend the end date

Project managers and project members can ask for a new end date.
An organization owner at your institution approves it.

1. Log in to [https://hpc-portal.reannz.co.nz](https://hpc-portal.reannz.co.nz) with **Sign in with REANNZ**.
   See [Log in](Navigating_the_HPC_Portal.md#log-in).
2. Open the resource: go to **Projects**, open your project, click the **Resources** tab and select the allocation.
3. Click **Actions**, then **Request end date change**.
4. In **Requested end date**, pick the new end date.
5. In **Comment**, explain why you need the extension.
   Whoever reviews it sees only the date and your comment, so include:
    - what the allocation is used for;
    - your recent usage, for example compute used against the limit;
    - what you expect to need over the new period.
6. Click **Send for Approval**.

The request appears on the resource's **End date change requests** tab.
The **Pending** list shows open requests and **All** shows past ones.

### After you send a request

- An organization owner at your institution reviews the request and approves or rejects it.
- When approved, the new end date applies at once. There is no further step.
- When rejected, the end date does not change.
- Check the **End date change requests** tab on the resource to see the outcome.

If you see **Set termination date** instead of **Request end date change**,
you are an organization owner and can set the date directly.

If you do not know who approves requests at your institution,
or the request is waiting too long,
{% include "partials/support_request.html" %}.

### Change allocation limits

Project managers can change limits, such as compute or storage.
Project members cannot; ask your project manager.

1. Open the resource as above.
2. Click **Actions**, then **Change limits**.
3. The **Change resource limits** dialog shows each component with its **Usage** and **Current limit**.
   Enter the **New limit** for each component you want to change.
4. Click **Request for a change**.

The change goes to your organization for approval, then to REANNZ.
The new limits apply once both approve.

### Approve a request

This section is for organization owners, who receive requests from projects in their organization.

1. Open the resource and click the **End date change requests** tab.
2. Under **Pending**, find the request.
   Read the **Requested end date**, **Current end date** and **Comment**.
3. Click the **⋮** menu on the row, then **Approve** or **Reject**.
4. Confirm.

To check usage before you decide, use the **Usage history** chart on the resource page
or **Actions** → **Show usage**.

### Allocation size limits

Allocations are subject to the size and duration limits in force at the time,
and to approval by your institution.
See [Project Extensions and New Allocations on Existing Projects](../Allocations/Allocations_and_Extensions.md)
for more details.


The HPC Portal is built on Waldur. Its user guide covers these features in more depth:

- [Resource end date changes](https://docs.waldur.com/latest/user-guide/customer-organization/resource-end-date-changes)
- [Resource limit change requests](https://docs.waldur.com/latest/user-guide/customer-organization/resource-limit-change-requests)

Some screens in that guide may differ from the REANNZ HPC Portal.
