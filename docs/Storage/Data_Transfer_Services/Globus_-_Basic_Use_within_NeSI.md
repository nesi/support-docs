---
created_at: '2018-05-28T22:41:27Z'
hidden: true
label_names:
- globus
- dtn
position: 12
title: Globus - Basic Use within NeSI
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000216695
zendesk_section_id: 360000040596
---

Note: after the system upgrade of July 2018, some of the Globus
endpoints or data-transfer nodes (DTN) which are named in this
documentation will no longer be in service. Please check back for
updated information once the new filesystems are in use.

## Preliminaries:

### 1)  register with Globus for an ID

To use Globus from within NeSI, you need a globus ID. If you do not have
one, sign up at [https://www.globusid.org](https://www.globusid.org/) ,
following the instructions at [Register for a Globus
ID](#Globus-BasicUse-Registration).

### 2) Identify NeSI Data Transfer Nodes

The NeSI cluster machines have been configured to act as Globus Data
Transfer Nodes (or endpoints). Associate your cluster filesystem with
the following Globus DTN names:

<table class="table table-striped table-bordered">
<colgroup>
<col style="width: 284.0px;">
<col style="width: 537.0px;">
</colgroup>
<thead>
<tr class="tablesorter-headerRow">
<th class="tablesorter-header sortableHeader tablesorter-headerUnSorted" style="user-select: none;" tabindex="0" scope="col" data-column="0">
Globus DTN

</th>
<th style="user-select: none;" tabindex="0" scope="col" data-column="1">
NeSI Filesystem

</th>
</tr>
</thead>
<tbody>
<tr>
<td>
nesi\#pan\_auckland

</td>
<td>
Pan cluster fileystem

</td>
</tr>
<tr>
<td>
nesi\#otago-dtn01

</td>
<td>
High Capacity Research Storage Cluster, U of Otago

</td>
</tr>
<tr>
<td>
nesi\#otago-dtn02

</td>
<td>
High Capacity Research Storage Cluster, U of Otago

</td>
</tr>
<tr>
<td>
nesi\#otago-dtn03

</td>
<td>
High Capacity Research Storage Cluster, U of Otago

</td>
</tr>
<tr>
<td>
nesi\#otago-dtn04

</td>
<td>
Otago AWS Endpoint

</td>
</tr>
<tr>
<td>
nesi\#otago-dtn-chc01

</td>
<td>
High Capacity Research Storage Cluster, Christchurch Campus

</td>
</tr>
<tr>
<td>
nesi\#otago-dtn-wlg01

</td>
<td>
High Capacity Research Storage Cluster, Wellington Campus

</td>
</tr>
<!--tr role="row">
<td> nesi#fitzroy_niwa</td>
<td> Data Transfer Node at NIWA serving the Fitzroy cluster</td>
</tr-->

<tr>
<td>
Plant and Food Research iRODS instance

</td>
<td>
Plant and Food Research iRODS instance

</td>
</tr>
</tbody>
</table>
</div>
###  

### 3) Be aware of Globus paths (see [Globus-Paths-Permissions-Storage-Allocation](https://support.nesi.org.nz/hc/en-gb/articles/360000216815-Globus-Paths-Permissions-Storage-Allocation)  if necessary).

4)  Note:  If you are accessing data on the Otago HCS, use the endpoint
nesi\#otago-dtn01  but in order to access this filesystem, you will need
to [register for access to
nesi\#otago-dtn01](https://www.otago.ac.nz/its/forms/otago604826.html)

##  

## Transfer Data between cluster nodes

1.  Sign in to [https://www.globus.org](https://www.globusid.org/) with
    your id. You will be taken to the transfer page
    <https://www.globus.org/app/transfer>
2.  Select the endpoints you wish to move files between (start typing
    <mark> "nesi\#"</mark> to see the list of NeSI DTNs to select
    from).  Authenticate via Tuakiri.    

3.  *Globus defaults to your home directory (maximum storage 2GB)* .
    Navigate your path to an appropriate directory (see [Globus Paths,
    Permissions, Storage
    Allocation](https://support.nesi.org.nz/hc/en-gb/articles/360000216815)
    ).
4.  Transfer the files.
5.  Check your email for confirmation the job has succeeded.

NOTE: Until mid-2018, your cluster may be on an older filesystem: check
with <support@nesi.org.nz> about when to move more than 0.5TB of data if
using Pan.

##  

## Transfer Data between your personal computer and cluster nodes

Install a [personal globus
DTN](https://nznesi.atlassian.net/wiki/spaces/nesiproj/pages/104955907/Personal+Globus+Endpoint)
on your personal computer (instructions at [Personal Globus
Endpoint](https://nznesi.atlassian.net/wiki/spaces/nesiproj/pages/104955907/Personal+Globus+Endpoint)
), and use globus to transfer files to/from there.

At Otago and Auckland Universities, you cannot currently transfer files
between your [personal globus
endpoint](https://nznesi.atlassian.net/wiki/spaces/nesiproj/pages/104955907/Personal+Globus+Endpoint)
and the local NeSI cluster endpoint from within the University (behind
firewall).
