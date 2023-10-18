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


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
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

<table style="font-weight: 400; height: 1258px;" width="633">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd" style="height: 51px;">
<td style="height: 51px; width: 196.789px"><p><strong>CLE
Components</strong></p></td>
<td style="height: 51px; width: 180.992px"><p><strong>Version
pre-upgrade</strong></p>
<p><strong>19.04</strong></p></td>
<td style="height: 51px; width: 221.219px"><p><strong>Version
post-upgrade</strong></p>
<p><strong>23.02</strong></p></td>
</tr>
<tr class="even" style="height: 22px;">
<td style="height: 22px; width: 196.789px"><p><strong>Cray Developer
Toolkit</strong></p></td>
<td style="height: 22px; width: 180.992px"><p>19.04</p></td>
<td style="height: 22px; width: 221.219px"><p>23.02</p></td>
</tr>
<tr class="odd" style="height: 44px;">
<td style="height: 44px; width: 196.789px"><p><strong>Cray Compiling
Environment</strong></p></td>
<td style="height: 44px; width: 180.992px"><p>CCE 8.7.10</p></td>
<td style="height: 44px; width: 221.219px"><p>CCE 15.0.1</p></td>
</tr>
<tr class="even" style="height: 110px;">
<td style="height: 110px; width: 196.789px"><p><strong>Cray Message
Passing Toolkit</strong></p></td>
<td style="height: 110px; width: 180.992px"><p>MPT 7.7.6</p>
<p>PMI 5.0.14</p>
<p>GA 5.3.0.10</p>
<p>Cray OpenSHMEMX 8.0.1</p></td>
<td style="height: 110px; width: 221.219px"><p>MPT 7.7.20</p>
<p>PMI 5.0.17</p>
<p>Cray OpenSHMEMX 9.1.2</p></td>
</tr>
<tr class="odd" style="height: 169px;">
<td style="height: 169px; width: 196.789px"><p><strong>Cray Debugging
Support Tools</strong></p></td>
<td style="height: 169px; width: 180.992px"><p>ATP 2.13</p>
<p>CCDB 3.0.4</p>
<p>CTI 2.15.5</p>
<p>Gdb4hpc 3.0.10</p>
<p>STAT 3.0.1.3</p>
<p>Valgrind4hpc 1.0.0</p></td>
<td style="height: 169px; width: 221.219px"><p>ATP 3.14.13</p>
<p>CCDB 4.12.13</p>
<p>CTI 2.17.2</p>
<p>Gdb4hpc 4.14.3</p>
<p>STAT 4.11.13</p>
<p>Valgrind4hpc 2.12.11</p></td>
</tr>
<tr class="even" style="height: 67px;">
<td style="height: 67px; width: 196.789px"><p><strong>Cray Performance
Measurement &amp; Analysis Tools –CPMAT (1)</strong></p></td>
<td style="height: 67px; width: 180.992px"><p>Perftools 7.0.6</p>
<p>PAPI 5.6.0.6</p></td>
<td style="height: 67px; width: 221.219px"><p>Perftools 23.02.0</p>
<p>PAPI 7.0.0.1</p></td>
</tr>
<tr class="odd" style="height: 221px;">
<td style="height: 221px; width: 196.789px"><p><strong>Cray Scientific
and Math Libraries -CSML</strong></p></td>
<td style="height: 221px; width: 180.992px"><p>LibSci 19.02.1</p>
<p>LibSci_ACC 18.12.1 (CLE 6)</p>
<p>PETSc 3.9.3.0</p>
<p>Trilinos 12.12.1.1</p>
<p>TPSL 18.06.1</p>
<p>FFTW 2.1.5.9</p>
<p>FFTW 3.3.8.2</p></td>
<td style="height: 221px; width: 221.219px"><p>Petsc 3.14.5.0</p>
<p>TPSL 20.03.2</p>
<p>Trilinos 12.18.1.1</p></td>
</tr>
<tr class="even" style="height: 191px;">
<td style="height: 191px; width: 196.789px"><p><strong>Cray Environment
Setup and Compiling support -CENV</strong></p></td>
<td
style="height: 191px; width: 180.992px"><p>craype-installer1.24.5</p>
<p>craypkg-gen1.3.7</p>
<p>craype 2.5.18</p>
<p>cray-modules 3.2.11.1</p>
<p>cray-mpich-compat1.0.0-8 (patch)</p>
<p>cdt-prgenv 6.0.5</p></td>
<td style="height: 191px; width: 221.219px"><p>craypkg-gen 1.3.26</p>
<p>craype 2.7.15</p></td>
</tr>
<tr class="odd" style="height: 302px;">
<td style="height: 302px; width: 196.789px"><p><strong>Third party
products</strong></p></td>
<td style="height: 302px; width: 180.992px"><p>HDF5 1.10.2.0</p>
<p>NetCDF 4.6.1.3</p>
<p>parallel-NetCDF 1.8.1.4</p>
<p>iobuf 2.0.8</p>
<p>java jdk 1.8.0_51 (CLE 6)</p>
<p>GCC 7.3.0</p>
<p>GCC 8.3.0</p>
<p>cray-python 2.7.15.3 &amp; 3.6.5.3 (CLE 6)</p>
<p>cray-R 3.4.2</p></td>
<td style="height: 302px; width: 221.219px"><p>HDF5 1.12.2.3</p>
<p>NetCDF 4.9.0.3</p>
<p>Parallel-NetCDF 1.12.3.3</p>
<p>iobuf 2.0.10</p>
<p>GCC 10.3.0</p>
<p>GCC 12.1.0</p>
<p>cray-python 3.9.13.2</p>
<p>cray-R 4.2.1.1</p></td>
</tr>
<tr class="even" style="height: 81px;">
<td style="height: 81px; width: 196.789px"><p><strong>Third Party
Licensed Products</strong></p></td>
<td style="height: 81px; width: 180.992px"><p>PGI 18.10 (CLE 6 only)</p>
<p>TotalView 2018.3.8</p>
<p>Forge 19.0.3.1</p></td>
<td style="height: 81px; width: 221.219px"><p>Forge 21.0.3</p>
<p>Totalview 2021.2.14</p></td>
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
