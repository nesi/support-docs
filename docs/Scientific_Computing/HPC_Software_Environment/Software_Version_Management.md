---
created_at: '2019-07-04T20:48:57Z'
hidden: false
position: 10
tags:
- software
- versions
title: Software Version Management
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001045096
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

Much of the software installed on the NeSI cluster have multiple
versions available as shown
[here](https://support.nesi.org.nz/hc/en-gb/sections/360000040076-Supported-Applications)
or by using the `module avail` or `module spider` commands.

If only the application name is given a default version will be chosen,
generally the most recent one. However it is good practice to load
modules using the specific version so you can ensure consistent
execution of your job even after the default version has been changed.

If you need a specific version of software, feel free to ask support and
we may install it.

## Example

``` sl
module load ANSYS
```

Will load the default version of ANSYS, in this case ANSYS/19.2, however
this may change.

``` sl
module load ANSYS/18.1
```

Will always load that version specifically.
