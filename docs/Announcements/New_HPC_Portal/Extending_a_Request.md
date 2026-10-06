---
title: Extending a Request - Renew an Allocation
created_at: '2026-09-29'
tags:
- account
description: How to extend the end date or change the limits of a Mahuika or Freezer allocation in the REANNZ HPC Portal.
status: new
---

{% include 'partials/status-only-pro.md' %}

Allocations on Mahuika and Freezer have an end date.
To keep using an allocation past that date, ask for a new end date in the
[REANNZ HPC Portal](https://hpc-portal.reannz.co.nz).
To make an allocation bigger or smaller, change its limits.

These are two separate requests, approved by different people.
To renew *and* grow an allocation, make both.

!!! note "Renew your existing project"
    To renew a project, use the steps on this page.
    Do not ask for a new project through a group invitation link.
    That creates a new project with a new project code.

## Before you start

- You need a role on the project. See [your roles in the HPC Portal](HPC_Portal_Overview.md#see-your-roles).
- Make your request **before** the current end date.
  The portal does not accept an end date in the past,
  and an allocation may be removed once its end date has passed.
- Request well ahead. Do not wait for a reminder.

## Extend the end date

Project managers and project members can ask for a new end date.
An organisation owner at your institution approves it.

1. Log in to [https://hpc-portal.reannz.co.nz](https://hpc-portal.reannz.co.nz) with **Sign in with REANNZ**.
   See [logging in to the HPC Portal](HPC_Portal_Overview.md#log-in).
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

## After you send a request

- An organisation owner at your institution reviews the request and approves or rejects it.
- When approved, the new end date applies at once. There is no further step.
- When rejected, the end date does not change.
- Check the **End date change requests** tab on the resource to see the outcome.

If you are an organisation owner, see [Approving requests](Approving_Requests.md).

If you see **Set termination date** instead of **Request end date change**,
you are an organisation owner and can set the date directly.

If you do not know who approves requests at your institution,
or the request is waiting too long,
{% include "partials/support_request.html" %}.

## Change allocation limits

Project managers can change limits, such as compute or storage.
Project members cannot; ask your project manager.

1. Open the resource as above.
2. Click **Actions**, then **Change limits**.
3. The **Change resource limits** dialog shows each component with its **Usage** and **Current limit**.
   Enter the **New limit** for each component you want to change.
4. Click **Request for a change**.

The change goes to your organisation for approval, then to REANNZ.
The new limits apply once both approve.

## Allocation size limits

Allocations are subject to the size and duration limits in force at the time,
and to approval by your institution.
See [Project Extensions and New Allocations on Existing Projects](../../Getting_Started/Allocations/Allocations_and_Extensions.md)
for more details.

The HPC Portal is built on Waldur. Its user guide covers
[resource end date changes](https://docs.waldur.com/latest/user-guide/customer-organization/resource-end-date-changes)
in more depth. Some screens in that guide may differ from the REANNZ HPC Portal.
