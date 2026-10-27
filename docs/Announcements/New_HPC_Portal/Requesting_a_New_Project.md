---
created_at: '2026-10-27'
tags:
- account
description: How researchers get a new project in the REANNZ HPC Portal through a group invitation link, an organisation owner, or a call for proposals.
status: new
---

{% include 'partials/status-only-pro.md' %}

There are three ways to get a new project:

| Route | Use it when |
| --- | --- |
| [Group invitation link](#use-a-group-invitation-link) | Your organisation has a link. |
| [Ask an organisation owner](#ask-an-organisation-owner) | Your organisation has no link, or you prefer to ask. |
| [Apply to a call](#apply-to-a-call) | Your organisation runs a call for proposals. |

Whichever route you use, you become the project's project manager.
An organisation owner approves the allocation for it.
REANNZ then reviews the allocation and makes recommendations if need be.

Organisation owners, see [For organisation owners](#for-organisation-owners).

!!! note "Renew your existing project"
    Do not use these routes to renew a project.
    They create a new project with a new project code.
    To renew, see [Extending a request](Extending_a_Request.md).

## Use a group invitation link

REANNZ sets up a link for each organisation that uses one.
A link works in one of two ways:

| Link type | What happens when you use it |
| --- | --- |
| Approved automatically | The portal creates the project at once. |
| Needs approval | Your request waits for an organisation owner. The project is created when they approve it. |

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

## Ask an organisation owner

One of your institution's organisation owners can create the project for you.
Send them:

- a name for the project;
- a short description of the research;
- the email address you use to log in to the portal.

The owner creates the project and adds you as its project manager.
If you have not used the portal before, you get an email invitation.
Open the link in it and log in with **Sign in with Tuakiri** to accept.

The project then appears under **Projects**.
Go on to [order an allocation](#order-an-allocation).

## Apply to a call

Some organisations run a call for proposals.
A call has rounds, each with a deadline.
You apply with a proposal that describes the project and the resources it needs.

1. In the sidebar, click **Calls**, then **Calls for proposals**.
2. Find the call and click **Apply to call**.
3. In the **Create proposal** dialog, enter a **Name** for your project and click **Create**.
4. Work through the proposal steps:
   **Project details**, **Resource requests** and **Project team**.
   Some calls also have a **Compliance checklist**.
5. Click **Submit**, then confirm.
   To finish later, click **Save as draft**.

Track your proposal under **Calls** → **My proposals**.
Its state moves from **Submitted** to **In review**, then to **Accepted** or **Rejected**.

When a proposal is accepted, the portal creates the project.
It also orders the resources you asked for, so you do not order them yourself.
REANNZ reviews those orders and makes recommendations if need be.

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

The order goes to an organisation owner at your institution for approval.
REANNZ then reviews it and makes recommendations if need be.
The allocation is created once that review is complete.

## For organisation owners

As an organisation owner, you share your organisation's link,
approve project requests that come through it,
and create projects for researchers who ask you.
You also approve the allocation order for each new project.
See [Approve an order](Approving_Requests.md#approve-an-order).

### Share the link

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

### Approve a project request

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

### Create a project

1. Open your organisation and click the **Projects** tab.
2. Click **Add**.
3. In the **Create project** dialog, enter the **Project name** and **Project description**.
   Use a name that no other project in your organisation has.
4. Choose an **OECD FoS code** if you know it.
5. Click **Create**.
   The portal shows **Project has been created.** and opens the project.

Then add the researcher as project manager:

1. On the project, click the **Team** tab.
2. Click **Add**, then **Invite by mail**.
3. Enter the researcher's **Email** and choose **Project manager** as the **Role**.
4. Click **Continue**, then **Send invitation**.

The researcher gets an email with a link to accept.
If the researcher already belongs to a project in your organisation,
you can click **Add** → **Member** instead, find them under **User**,
choose the role and click **Add role**.

The project gets its project code automatically, as for a link.
The researcher then orders the allocation, and the order comes to you.
