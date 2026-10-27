---
created_at: '2026-10-27'
tags:
- account
description: How organisation owners share and approve group invitation links, and how researchers use a link to create a new project in the REANNZ HPC Portal.
status: new
---

{% include 'partials/status-only-pro.md' %}

A new project starts from a group invitation link.
REANNZ sets up the link for each organisation that uses one.
Your organisation owner shares it with researchers at your institution.

A link works in one of two ways:

| Link type | What happens when you use it |
| --- | --- |
| Approved automatically | The portal creates the project at once. |
| Needs approval | Your request waits for an organisation owner. The project is created when they approve it. |

Either way, you become the project's project manager.
The project starts with no allocation.
You then order one, and an organisation owner and REANNZ approve that order.

Organisation owners, see [Share the link](#share-the-link)
and [Approve a project request](#approve-a-project-request).

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
   If the link needs approval, the owner reads this to decide.
6. Click **Submit request**.

The message that follows tells you which type of link you used.

**Approved automatically.**
The portal shows **Project created in** your organisation and opens the new project.
Go on to [order an allocation](#order-an-allocation).

**Needs approval.**
The portal shows **Request submitted** and opens your permission requests.
The **Status** column shows where your request is.
You get an email when an owner approves or declines it.
Once approved, the project appears under **Projects**.

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
   **Auto approve** shows whether the link needs your approval.
4. Copy the **Invitation link** with the copy icon next to it.

Send the link to researchers at your institution.
Do not share it outside your institution.
With a link that is approved automatically,
anyone who logs in with it can create a project in your organisation.

You cannot change or cancel the link yourself.
If your organisation has no link, or you want it changed or cancelled,
{% include "partials/support_request.html" %}.

## Approve a project request

Requests through a link that needs approval wait for you.
The portal emails your organisation's owners when a request arrives.

1. Open your organisation and click **Team**.
2. Click the **Group invitations** tab and expand the invitation.
3. Under **User permission requests**, find the request.
   **Requested project** shows the project name.
4. Click **Review** on the row.
   Read the request, enter a **Reason** if you wish, then click **Approve** or **Decline**.

Decline a request whose **Requested project** matches a project that already exists
in your organisation.
Approving it adds the requester to that project as project manager,
instead of creating a new one.

When you approve, the portal creates the project and emails the requester.

With a link that is approved automatically, there is nothing to approve.
The portal does not email you, so check **User permission requests** to see who has used it.

Either way, the allocation order comes to you next.
See [Approve an order](Approving_Requests.md#approve-an-order).
