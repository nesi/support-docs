---
created_at: '2023-07-05T23:50:46Z'
tags:
- account
description: How to read the monthly usage report sent to subscribers
---

As part of our Subscriber service agreements, we share
monthly usage reports. They provide a monthly view of chargeable usage
(as well as any Merit / non-chargeable usage) across all platform
services:

- Compute - CPUs

- Compute - GPUs

- Storage - Persistent (active project storage)

- Storage - Freezer (long-term storage)

We send these usage report emails via our Support portal so that
our team has better visibility internally of our monthly check-ins and
we can more easily loop in others to answer technical questions or
follow up on system-related requests.

The monthly emails also include any timely updates on other news or
training events that would be of interest to your research community.

## How to read your Subscriber Usage Report

A new tab is added to the report for each month, making it easy to view,
reference, and compare recent and past usage.

At the top of each tab is a summary of the contract, indicating the:

  - Term of agreement (contract start and end dates)
  - Maximum contracted value
  - Value of services utilised to date
  - Usage for each service is shown in the corresponding sections below

In cases where a service has differently priced resources (eg. Compute pricing varies across our CPU and GPU resources), we will also indicate additional information (eg. “Type of CPU” and “Type of GPU”) so you have a breakdown of what usage contributes to the total chargeable costs that month. See the Pricing section above for more information on our service pricing.

To showcase full value delivered through our services, our reports will also show usage that is not chargeable (eg. Merit usage). This is shown simply for information purposes and is not included or reflected on invoices.

Usage reports are generally ready to view by the middle of the following
month. So, for example, January usage will appear as a new tab by mid-
to late February.

### What are Compute Units?

Compute Units are used to allocate and schedule access to shared HPC infrastructure. They are designed to reflect the relative demand a job places on the platform and account for factors such as: 

- CPU type and performance
- GPU type and performance
- Memory requested
- Other hardware characteristics that affect platform capacity and scheduling 

The purpose of Compute Units is to encourage efficient use of shared resources and to ensure fair access to the platform. For example, requesting large amounts of memory or utilising higher-performance hardware has a greater impact on the platform and therefore consumes Compute Units at a different rate than standard CPU usage. 

### How are subscription charges calculated?

Compute Units and subscription charges do not have a fixed one-to-one relationship. Subscription charges are calculated separately from Compute Units. 

Under the subscription model, users are charged according to a simplified pricing schedule. This pricing does not reflect all of the factors incorporated into compute usage calculation. For example: 

- Newer or higher-performance CPUs are not charged at higher rates than older CPUs.
- Memory is not separately charged.
- Pricing is designed to provide a simple and predictable charging model for subscribers. 

### Why Compute Units and charges can differ 

Compute Units should not be interpreted as a direct representation of remaining contract value. The number of Compute Units consumed depends on the mix of resources used, while the amount charged depends on the subscription pricing schedule. 

This means that: 

- Two projects with the same dollar value of usage may consume different numbers of Compute Units.
- Two projects consuming the same number of Compute Units may incur different charges.
- A project may use only a small proportion of its allocated Compute Units while consuming a larger proportion of its subscription value.
- Conversely, a project may consume a large proportion of its Compute Units while using only part of its subscription value. 

### How Compute Unit allocations are determined

When a subscription allocation is created, the Compute Unit allocation is estimated using: 

- Historical resource usage patterns;
- The expected mix of resources to be used during the allocation period; and
- Any additional information provided about anticipated workloads.
- This estimate is intended to provide sufficient access to platform resources throughout the subscription period. 

Because future resource usage can never be predicted with complete accuracy, actual consumption patterns may differ from those assumed when the allocation was created. As projects evolve, the ratio of CPUs, GPUs, memory, and other resources used often changes. This can result in compute-unit consumption diverging from the original estimate, even where the total dollar value of usage remains similar. 

You can read more about our allocation process on our ['What is an allocation?' page](/Getting_Started/Allocations/What_is_an_allocation/).

### Monitoring subscription value

Monitoring usage against the dollar value of a subscription provides an additional safeguard to help identify when a project is approaching its contractual spending limit, regardless of the number of Compute Units remaining within the allocation. 

Where appropriate, users may be contacted when their subscription value is nearing exhaustion (i.e., 90%) so they can review their usage and discuss options for continuing their work.

If you have any questions about anything mentioned on this page, don’t
hesitate to [get in touch](mailto:info@nesi.org.nz).
