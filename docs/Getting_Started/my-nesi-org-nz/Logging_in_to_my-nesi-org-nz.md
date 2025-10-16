---
created_at: '2021-03-01T21:23:33Z'
tags: []
title: Logging in to my.nesi.org.nz
vote_count: 2
vote_sum: -2
zendesk_article_id: 360003584515
zendesk_section_id: 360001059296
---

## Login credentials

We allow students, academics, alumni and researchers to securely login
and create a [NeSI account
profile](../Accounts-Projects_and_Allocations/Creating_an_Account_Profile.md)
using the credentials granted by their home organisation via Tuakiri.

### Tuakiri - federated identity and access management

Most New Zealand universities and Crown Research Institutes are members
of the [Tuakiri authentication
federation](https://www.reannz.co.nz/products-and-services/tuakiri/join/),
but many other institutions, including private sector organisations and
most central and local government agencies, are not.

See also [Creating a NeSI Account
Profile](../Accounts-Projects_and_Allocations/Creating_an_Account_Profile.md)

### Support for users outside the Tuakiri federation

In case your organisation is not part of the Tuakiri federated identity
management service, a user can still [request a NeSI Account
profile.](https://my.nesi.org.nz/html/request_nesi_account) NeSI will
(if approved) provision a so-called "virtual home account" on Tuakiri.

See also [Account Requests for non-Tuakiri
Members](../../General/NeSI_Policies/Account_Requests_for_non_Tuakiri_Members.md)

## Troubleshooting login issues

Please use the [Tuakiri Attribute Validator](https://attributes.tuakiri.ac.nz/snapshots/latest) to
verify the details of your account. Contact your identity provider (e.g.
institution, university) in case there are details missing or wrong.

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
