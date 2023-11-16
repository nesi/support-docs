---
created_at: '2021-04-30T03:29:54Z'
hidden: false
position: 0
tags: []
title: Tuakiri Attribute Validator
vote_count: 0
vote_sum: 0
zendesk_article_id: 360004218816
zendesk_section_id: 360001059296
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

### Tuakiri Attribute Validator

This Tuakiri service is a health check for your managed identity. It
checks the attributes provided about you from your identity provider,
seeing whether they are provided in a format that is suitable for
consumption by Tuakiri connected services. It will report any problems
that it finds with your identity record, so that you can talk with the
IT department at your identity provider (normally your employer or
university) and have the problems fixed.

Generally speaking, errors in your Tuakiri Core Attributes, such as
empty values, will probably cause problems for you when you try to log
in to a service using Tuakiri; while errors in your Tuakiri Optional
Attributes are mostly harmless, and not worth bothering your IT
department about unless you need a particular Optional Attribute to be
correctly set for a specific purpose.

To access the Tuakiri Attribute Validator, browse to this page:
[https://attributes.tuakiri.ac.nz/snapshots/latest﻿](https://attributes.tuakiri.ac.nz/snapshots/latest)

The primary identifier NeSI consumes is the
attribute **auEduPersonSharedToken**. This is a so-called, "Tuakiri Core
Attribute," expected to exist for every account.

If your institution has issued you an empty or invalid
auEduPersonSharedToken (rare), or if there is a difference between the
value of your auEduPersonSharedToken as proffered by your institution's
identity provision service and its value as recorded in the NeSI
database (more common), you will not be able to log in to My NeSI. If
you cannot log in, please raise a support ticket with your institutions
IT support. 

For troubleshooting the support team may ask you for a PDF of your
Tuakiri attributes. Tuakiri does not include your password in the
attribute printout and there is no security risk involved in providing a
copy of that PDF.
