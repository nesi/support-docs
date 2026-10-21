---
created_at: '2021-03-01T21:23:33Z'
tags:
- access
- account
title: Logging in to my.nesi.org.nz
description: Logging in to my.nesi.org.nz through Tuakiri and fixing common login problems
---

{% include 'partials/status-no-pro.md' %}

## Login credentials

We allow students, academics, alumni and researchers to securely login
and create a [REANNZ HPC account
profile](../Creating_an_Account.md)
using the credentials granted by their home organisation via Tuakiri.

Most New Zealand universities and Public Research Organisations are members
of the [Tuakiri authentication
federation](https://www.reannz.co.nz/products-and-services/tuakiri/join/),
but many other institutions, including private sector organisations and
most central and local government agencies, are not.

If your organisation is not part of the Tuakiri federated identity
management service, you can still [request a REANNZ HPC Account
profile](https://my.nesi.org.nz/html/request_nesi_account). REANNZ will
(if approved) provision a so-called "virtual home account" on Tuakiri.
See [Account Requests for non-Tuakiri
Members](../../Policy/Account_Requests_for_non_Tuakiri_Members.md)
for details.

## Troubleshooting login issues

Please use the [Tuakiri Attribute Validator](Tuakiri_Attribute_Validator.md) to
verify the details of your account. Contact your identity provider (e.g.
institution, university) in case there are details missing or wrong.

The primary identifier REANNZ HPC consumes is the
attribute `auEduPersonSharedToken`. This is a so-called, "Tuakiri Core
Attribute," expected to exist for every account.

If your institution has issued you an empty or invalid
`auEduPersonSharedToken` (rare), or if there is a difference between the
value of your `auEduPersonSharedToken` as proffered by your institution's
identity provision service and its value as recorded in the REANNZ HPC
database (more common), you will not be able to log in to my.nesi.org.nz. If
you cannot log in, please raise a support ticket with your institution's
IT support.

For troubleshooting the support team may ask you for a PDF of your
Tuakiri attributes. Tuakiri does not include your password in the
attribute printout and there is no security risk involved in providing a
copy of that PDF.
