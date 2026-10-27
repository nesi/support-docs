---
created_at: '2026-10-01'
tags:
- account
description: How organisation owners find and approve orders and end date changes in the REANNZ HPC Portal.
status: new
---

{% include 'partials/status-only-pro.md' %}

As an organisation owner, you approve what projects in your organisation ask for.
A request waits until you act on it.

## Find pending requests

The portal has no single list of approvals.
Each type of request waits in its own place.

| Request | Raised by | Email to you | Where to act |
| --- | --- | --- | --- |
| New resource | A project manager | Yes. The subject names the order. | Your organisation's **Resources** → **Orders**. See [Approve an order](#approve-an-order). |
| Limit change | A project manager | Yes, as for a new resource. A limit change is an order. | As for a new resource. |
| New project | A researcher, through a link that needs approval | Yes. | Your organisation's **Team** → **Group invitations**. See [Approve a project request](Requesting_a_New_Project.md#approve-a-project-request). |
| End date change | A project manager or member | Sometimes a short notice. Do not rely on it. | The resource's **End date change requests** tab. See [Approve end dates](#approve-end-dates). |

Most portal emails do not repeat the request details.
Log in to the portal to review them.

End date change requests have no organisation-wide list.
Open your organisation's **Resources** and check the allocations with the nearest **Termination date**.

## New projects

Researchers create a new project through your organisation's group invitation link.
You share the link with them.
See [Share the link](Requesting_a_New_Project.md#share-the-link).

What happens next depends on the link:

- **Approved automatically.** The portal creates the project at once.
  You do not approve this step, and the portal does not email you.
- **Needs approval.** The request waits for you.
  See [Approve a project request](Requesting_a_New_Project.md#approve-a-project-request).

Either way, the requester becomes the project manager.
To see who has used a link:

1. Open your organisation and click **Team**.
2. Click the **Group invitations** tab.
3. Expand the invitation to see its requests.

The new project has no allocation yet.
Its project manager orders one from the **REANNZ Marketplace**,
and that order comes to you. See [Approve an order](#approve-an-order).

## Approve an order

Orders cover new resources and limit changes.
A project manager raises a limit change with **Actions** → **Change limits** on the resource.

1. Open your organisation, then click **Resources** → **Orders**.
2. Click the order to open it.
   You cannot approve from the **⋮** menu in the list.
3. Check the project, the offering and the requested limits.
4. Click **Actions**, then **Approve** or **Decline**, and confirm.

You can also approve from **Actions** on the resource page.

After you approve, REANNZ reviews the order and makes recommendations if need be.
The change applies once that review is complete.
Orders you place yourself skip your approval step.

## Approve end dates

1. Open the resource and click the **End date change requests** tab.
2. Under **Pending**, find the request.
   Read the **Requested end date**, **Current end date** and **Comment**.
3. Click the **⋮** menu on the row, then **Approve** or **Reject**.
4. Confirm.

The new end date applies at once.
It does not change the allocation's limits.

To check usage before you decide, use the **Usage history** chart on the resource page
or **Actions** → **Show usage**.

To change an end date yourself, click **Actions** → **Set termination date** on the resource.

## Further reading

For how projects raise these requests, see [Extending a request](Extending_a_Request.md).

The HPC Portal is built on Waldur. Its user guide covers
[resource end date changes](https://docs.waldur.com/latest/user-guide/customer-organization/resource-end-date-changes)
in more depth. Some screens in that guide may differ from the REANNZ HPC Portal.
