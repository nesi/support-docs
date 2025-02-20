---
hidden: false
label_names:
- identity
- create
- manage
position: 1
title: Create and Manage identity
vote_count: 1
vote_sum: 1
---

`Application Credentials` help you to avoid the practice of embedding user account credentials in configuration files. Instead, the user creates an Application Credential that receives delegated access to a single project and has its own distinct secret. The user can also limit the delegated privileges to a single role in that project. This allows you to adopt the principle of least privilege, where the authenticated service only gains access to the one project and role that it needs to function, rather than all of them.

This approach allows you to consume an API with revealing your user credentials, and lets applications authenticate to Keystone without requiring embedded user credentials.

Within FlexiHPC you are able to mange `Application Credentials` from the dashboard and/or the CLI.

- [Creating and Managing Application Credentials from the dashboard](creating-and-managing-application-credentials-with-the-dashboard.md)

- [Creating and Managing Application Credentials via CLI](creating-and-managing-application-credentials-via-cli.md)

!!! note
    The Application Credential is dependent on the user account that created it, so it will terminate if that account is ever deleted, or loses access to the relevant role.