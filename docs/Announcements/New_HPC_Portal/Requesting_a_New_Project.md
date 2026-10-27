---
created_at: '2026-10-27'
tags:
- account
description: How organisation owners share a group invitation link, and how researchers use the link to create a new project in the REANNZ HPC Portal.
status: new
---

{% include 'partials/status-only-pro.md' %}

A new project starts from a group invitation link.
REANNZ sets up the link for each organisation that uses one.
Your organisation owner shares it with researchers at your institution.

The link creates the project at once, with you as its project manager.
The project starts with no allocation.
You then order one, and that order is what gets approved.
Organisation owners, see [Share the link](#share-the-link).

!!! note "Renew your existing project"
    Do not use the link to renew a project.
    It creates a new project with a new project code.
    To renew, see [Extending a request](Extending_a_Request.md).

## Create a project

1. Ask an organisation owner at your institution for the group invitation link.
2. Open the link.
   If you are not logged in, the portal asks you to log in with **Sign in with Tuakiri**,
   then returns you to the link.
3. The **Request permission** dialog names your organisation and the role you will get.
   Click **Submit**.
4. The **Project details** dialog opens.
   In **Project name**, replace the pre-filled name with a unique name for your project.
5. In **Project description**, describe the research.
6. Click **Submit request**.

The portal shows **Project created in** your organisation and opens the new project.
You are its project manager.

!!! warning "Always change the project name"
    Give each new project a unique name.
    If the portal says **You have joined an existing project**,
    do not order anything for it.
    {% include "partials/support_request.html" %}.

## Order an allocation

Your project needs a project code before you order.
The code is assigned automatically, usually within an hour of creating the project.

1. Open your project and go to the **REANNZ Marketplace**.
2. Choose the offering, for example **Mahuika**.
3. Next to the resource name, click **Suggest name**.
   The suggested name should start with your project code, for example `bsi0NNNN-1`.
   If it starts with your project name instead, the code is not ready yet.
   Leave the order form and try again later.
4. Enter the limits you need and submit the order.

The order goes to an organisation owner at your institution, then to REANNZ.
The allocation is created once both approve.

## Share the link

REANNZ creates the link for your organisation.
To find it:

1. Open your organisation and click **Team**.
2. Click the **Group invitations** tab.
3. Expand the invitation.
4. Copy the **Invitation link** with the copy icon next to it.

Send the link to researchers at your institution.
Anyone who logs in with the link can create a project in your organisation,
so do not share it outside your institution.

The portal does not email you when someone uses the link.
To see who has used it, expand the invitation and read the **User permission requests** list.
The **Requested project** column shows each project name.

You cannot change or cancel the link yourself.
If your organisation has no link, or you want it changed or cancelled,
{% include "partials/support_request.html" %}.

You approve the allocation order, not the project.
See [Approve an order](Approving_Requests.md#approve-an-order).
