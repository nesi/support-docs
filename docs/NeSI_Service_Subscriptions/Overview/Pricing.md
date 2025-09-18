---
created_at: '2023-07-05T23:56:56Z'
tags: []
title: Pricing
vote_count: 0
vote_sum: 0
zendesk_article_id: 7349177261455
zendesk_section_id: 7348891753487
---


!!! note "REANNZ Integration"
    On 01 July 2025, New Zealand eScience Infrastructure (NeSI) was integrated into the Crown company, Research and Education Advanced Network New Zealand (REANNZ) Ltd. NeSI’s services and technologies are now hosted by REANNZ as a national [eResearch Infrastructure Platform](https://www.mbie.govt.nz/science-and-technology/science-and-innovation/funding-information-and-opportunities/investment-funds/strategic-science-investment-fund/funded-infrastructure/eresearch-infrastructure-platform). Some of our tools (eg. my.nesi.org.nz) and emails (eg. support@nesi.org.nz) will retain a ‘NeSI’ brand as we transition our services and develop a longer-term strategy for this integrated platform.

    All NeSI services and support – including these Support Documentation pages and team monitoring the support@nesi.org.nz email – are continuing as you’ve known them. Also, the principles of our policies (Access, Acceptable Use, Security & Privacy, etc.) are carrying over and remain in effect. We'll be in touch if anything changes. If you have any questions about the NeSI-REANNZ integration, {% include "partials/support_request.html" %}


We have two categories of pricing for Subscription services:

- Public sector & not-for-profit
- Commercial

Prices are reviewed annually and subject to change.

## HPC Platform

The following pricing table covers our core HPC Platform service offerings.

*(Last updated June 2025. Prices subject to change.)*

| Service      | Public sector & not-for-profit | Commercial     |
| :---        |    :---   |          :--- |
| ***Research Software Expertise***      |        |    |
| Computational science and data science Consultancy (per hour)   | $160.00        | $320.00      |
| ***High Performance Computing (HPC) and Data Analytics***   |         |       |
| Mahuika Milan HPC core hours (per CPU core hour)   | $0.08        | $0.09      |
| Mahuika Genoa HPC core hours (per CPU core hour)   | $0.08        | $0.09      |
| P100 Graphical Processing Unit (GPU) hours (per GPU hour)   | $0.35        | $0.40      |
| A100 Graphical Processing Unit (GPU) hours (per GPU hour)   | $0.90        | $1.00      |
| H100 Graphical Processing Unit (GPU) hours (per GPU hour)   | $0.90        | $1.00      |
| L4 Graphical Processing Unit (GPU) hours (per GPU hour)   | $0.90        | $1.00      |
| ***Research Data Management***      |        |    |
| Freezer long-term storage (per Terabyte per year)   | $30.00        | $37.50      |
| Persistent storage (>2 TB) (per Terabyte per year)   | $150.00        | $187.50      |
| National Data Transfer Platform membership & managed endpoint (per year)   | $4,000.00        | $P.O.A      |


## Research Developer Cloud

Billable services in the Research Developer Cloud include Virtual Machines (VMs), General Purpose Graphical Processing Units (GPUs), and Storage.

Pricing listed is for Public section & not-for-profit organisations. To discuss commercial pricing, [please get in touch](mailto:support@nesi.org.nz).


*(Last updated September 2024. Prices are subject to change.)*

### Virtual Machines (VMs)

- The flavours available by default are the balanced VMs with 1 CPU to 2GB RAM ratio.
- They are named balanced1.1cpu2ram and increment up to balanced1.32cpu64ram.
- The price scales linearly with the number of cores in the VMs.

| Flavours      | Price per hour ($) | Price per month ($ in approximation)     |
| :---        |    :---   |          :--- |
| balanced1.1cpu2ram   | 0.039        | 28.50      |
| balanced1.2cpu4ram   | 0.078        | 56.99      |
| balanced1.4cpu8ram   | 0.156        | 113.98      |
| balanced1.8cpu16ram   | 0.312        | 227.96      |
| balanced1.16cpu32ram   | 0.625        | 455.92      |
| balanced1.32cpu64ram   | 1.249        | 911.85      |

### High Memory & Development VMs

The Research Developer Cloud also offers high memory flavours (memory1) and flavours designed for quick development and test purposes (devtest1): 

- high memory flavours having 1 to 4 ratio of CPU per GB of RAM
- development focused flavours with 1 to 1 ratio

[Please contact us](mailto:support@nesi.org.nz) if you would like to access these specialised compute flavours.

| Flavours      | Price per hour ($) | Price per month ($ in approximation)     |
| :---        |    :---   |          :--- |
| memory1.1cpu4ram   | 0.062        | 45.59      |
| memory1.2cpu8ram   | 0.125        | 91.18      |
| memory1.4cpu16ram   | 0.250        | 182.37      |
| memory1.8cpu32ram   | 0.500        | 364.74      |
| memory1.16cpu64ram   | 0.999        | 729.48      |
| memory1.32cpu128ram   | 1.999        | 1,458.96      |
| devtest1.1cpu1ram   | 0.028        | 20.35      |
| devtest1.2cpu2ram   | 0.056        | 40.71      |
| devtest1.4cpu4ram   | 0.112        | 81.42      |

## General Purpose GPUs
General Purpose GPUs are currently accessible as a whole node or half a node of A40 GPUs. The GPU flavour won’t be visible by default on your project. We will be working on making vGPU access available in smaller portions instead of the whole node. [Please contact us](mailto:support@nesi.org.nz) if you would like to access them.

| Flavours      | Price per hour ($) | Price per month ($ in approximation)     |
| :---        |    :---   |          :--- |
| gpu1.44cpu240ram.a40.1g.48gb   | 3.672        | 2,680.43      |
| gpu1.88cpu480ram.a40x2.1g.48gb   | 7.344        | 5,360.85      |

## Storage

| Flavours      | Price per hour ($) per GB | Price per month ($ in approximation) per GB     |
| :---        |    :---   |          :--- |
| Flash   | 0.0005        | 0.37      |
| Spinning disk   | 0.0002        | 0.12      |






