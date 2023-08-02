---
created_at: '2023-03-09T02:46:57Z'
hidden: false
label_names:
- announcement
position: 0
status: new
title: "M\u0101ui upgrade is complete"
vote_count: 1
vote_sum: 1
zendesk_article_id: 6546340907919
zendesk_section_id: 200732737
---

The recent upgrade of the Māui is now complete. The operating system,
libraries, and software stack have been upgraded and rebuilt, improving
performance and stability and enabling new capabilities.

If you encounter any issues, have any questions about the upgrade, need
help with getting your software working on the upgraded system, or have
a suggestion for our documentation, please contact us via email at
[support@nesi.org.nz](mailto:support@nesi.org.nz). We are committed to
providing you with the best computing resources possible and will do our
best to assist you.

## Why

This upgrade brings Māui's operating environment up to the latest
supported release available for Cray's XC50 supercomputing platforms,
with performance, reliability, and security benefits. This includes more
up-to-date tooling and libraries with associated features and
performance benefits. This work also enables further upgrades to NeSI's
shared HPC storage system.

## Impact

Please be aware that this is a major upgrade to Māui’s operating
environment which may impact the compatibility of software compiled with
the current toolchains and libraries, as such users should expect to
need to test existing applications post-upgrade and in some cases
(especially where the application is leveraging software modules on
Māui) rebuilding will be required. Users of applications maintained as
software modules in the NeSI software stack can expect NeSI to provide
rebuilt and/or updated versions of these applications (though this will
be an ongoing effort post-upgrade).

The following information will help your transition from the pre-upgrade
Māui environment to the post-upgrade one: 

-   The three main toolchains (CrayCCE, CrayGNU and CrayIntel) have all
    been updated to release 23.02 (CrayCCE and CrayGNU) and 23.02-19
    (CrayIntel). **The previously installed versions are no longer
    available**.
-   Consequently, nearly all of the previously provided **environment
    modules have been replaced by new versions**. You can use the
    *module avail* command to see what versions of those software
    packages are now available. If your batch scripts load exact module
    versions, they will need updating.
-   The few jobs in the Slurm queue at the start of the upgrade process
    have been placed in a “user hold” state. You have the choice of
    cancelling them with *scancel &lt;jobid&gt;* or releasing them with
    *scontrol release &lt;jobid&gt;*.
-   Be aware that if you have jobs submitted that rely on any software
    built before the upgrade, there is a good chance that this software
    will not run. **We recommend rebuilding any binaries you maintain**
    before running jobs that utilise those binaries.
-   Note that Māui login does not require adding a second factor to the
    password when authenticating on the Māui login node after the first
    successful login attempt. That is, if you have successfully logged
    in using &lt;first factor&gt;&lt;second factor&gt; format, no second
    factor part will be required later on.

We have also updated our support documentation for Māui to reflect the
changes, so please review it before starting any new projects. 

## Software Changes

Software built on Māui may not work without recompilation after the
upgrade. See the tables below for more detail regarding version changes.
If you have any particular concerns about the impact on your work,
please contact [NeSI
Support](https://support.nesi.org.nz/hc/en-gb/requests/new).

The table below outlines the known and expected Cray component changes:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

[S-2529: XC Series Cray Programming Environment User's
Guide](https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=a00113984en_us)

[S-2559: XC Series Software Installation and Configuration Guide (CLE
7.0.UP04 Rev
E)](https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=sd00002132en_us)

Reference:

[HPE Cray Programming Environment 21.09 for Cray XC (x86)
Systems](https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=a00118188en_us)

[Cray XC (x86) Programming Environments
19.04](https://support.hpe.com/hpesc/public/docDisplay?docId=a00114073en_us&docLocale=en_US)

[Applications supported by NeSI
team](https://support.nesi.org.nz/hc/en-gb/sections/360000040076)
