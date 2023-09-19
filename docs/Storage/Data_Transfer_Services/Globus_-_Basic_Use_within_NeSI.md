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


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>Note: after the system upgrade of July 2018, some of the Globus endpoints or data-transfer nodes (DTN) which are named in this documentation will no longer be in service. Please check back for updated information once the new filesystems are in use.</p>
<h2 id="Globus-BasicUse-Registration">Preliminaries:</h2>
<h3>1)  register with Globus for an ID</h3>
<p>To use Globus from within NeSI, you need a globus ID. If you do not have one, sign up at <a class="external-link" href="https://www.globusid.org/" rel="nofollow"> https://www.globusid.org</a> , following the instructions at <a href="#Globus-BasicUse-Registration" data-linked-resource-id="109903937" data-linked-resource-version="7" data-linked-resource-type="page"> Register for a Globus ID</a>.</p>
<h3>2) Identify NeSI Data Transfer Nodes</h3>
<p>The NeSI cluster machines have been configured to act as Globus Data Transfer Nodes (or endpoints). Associate your cluster filesystem with the following Globus DTN names:</p>
<div class="table-wrap">
<table class="table table-striped table-bordered">
<colgroup> <col style="width: 284.0px;"> <col style="width: 537.0px;"> </colgroup>
<thead>
<tr class="tablesorter-headerRow">
<th class="tablesorter-header sortableHeader tablesorter-headerUnSorted" style="user-select: none;" tabindex="0" scope="col" data-column="0">Globus DTN</th>
<th style="user-select: none;" tabindex="0" scope="col" data-column="1">NeSI Filesystem</th>
</tr>
</thead>
<tbody>
<tr>
<td>nesi#pan_auckland</td>
<td>Pan cluster fileystem</td>
</tr>
<tr>
<td>nesi#otago-dtn01</td>
<td>High Capacity Research Storage Cluster, U of Otago</td>
</tr>
<tr>
<td>nesi#otago-dtn02</td>
<td>High Capacity Research Storage Cluster, U of Otago</td>
</tr>
<tr>
<td>nesi#otago-dtn03</td>
<td>High Capacity Research Storage Cluster, U of Otago</td>
</tr>
<tr>
<td>nesi#otago-dtn04</td>
<td>Otago AWS Endpoint</td>
</tr>
<tr>
<td>nesi#otago-dtn-chc01</td>
<td>High Capacity Research Storage Cluster, Christchurch Campus</td>
</tr>
<tr>
<td>nesi#otago-dtn-wlg01</td>
<td>High Capacity Research Storage Cluster, Wellington Campus</td>
</tr>
<!--tr role="row">
<td> nesi#fitzroy_niwa</td>
<td> Data Transfer Node at NIWA serving the Fitzroy cluster</td>
</tr-->
<tr>
<td>Plant and Food Research iRODS instance</td>
<td>Plant and Food Research iRODS instance</td>
</tr>
</tbody>
</table>
</div>
<h3> </h3>
<h3>3) Be aware of Globus paths (see <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000216815-Globus-Paths-Permissions-Storage-Allocation">Globus-Paths-Permissions-Storage-Allocation</a>  if necessary).</h3>
<p>4)  Note:  If you are accessing data on the Otago HCS, use the endpoint nesi#otago-dtn01  but in order to access this filesystem, you will need to <a style="background-color: #ffffff;" href="https://www.otago.ac.nz/its/forms/otago604826.html">register for access to nesi#otago-dtn01</a></p>
<h2 class="auto-cursor-target"> </h2>
<h2 id="Globus-BasicUse-TransferDatabetweenclusternodes" class="auto-cursor-target">Transfer Data between cluster nodes</h2>
<ol>
<li>Sign in to <a class="external-link" href="https://www.globusid.org/" rel="nofollow"> https://www.globus.org</a> with your id. You will be taken to the transfer page <a href="https://www.globus.org/app/transfer" rel="nofollow"> https://www.globus.org/app/transfer</a>
</li>
<li>
<p>Select the endpoints you wish to move files between (start typing <mark> "nesi#"</mark> to see the list of NeSI DTNs to select from).  Authenticate via Tuakiri.    </p>
</li>
<li>
<em> Globus defaults to your home directory (maximum storage 2GB)</em> . Navigate your path to an appropriate directory (see <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000216815" data-linked-resource-id="150077518" data-linked-resource-version="20" data-linked-resource-type="page"> Globus Paths, Permissions, Storage Allocation</a> ).</li>
<li>Transfer the files.</li>
<li>Check your email for confirmation the job has succeeded.</li>
</ol>
<div data-hasbody="true" data-macro-name="info">
<div>NOTE: Until mid-2018, your cluster may be on an older filesystem: check with <a class="external-link" href="mailto:support@nesi.org.nz" rel="nofollow"> support@nesi.org.nz</a> about when to move more than 0.5TB of data if using Pan.</div>
</div>
<h2> </h2>
<h2 id="Globus-BasicUse-TransferDatabetweenyourpersonalcomputerandclusternodes">Transfer Data between your personal computer and cluster nodes</h2>
<p>Install a <a href="https://nznesi.atlassian.net/wiki/spaces/nesiproj/pages/104955907/Personal+Globus+Endpoint"> personal globus DTN</a> on your personal computer (instructions at <a href="https://nznesi.atlassian.net/wiki/spaces/nesiproj/pages/104955907/Personal+Globus+Endpoint"> Personal Globus Endpoint</a> ), and use globus to transfer files to/from there.</p>
<p>At Otago and Auckland Universities, you cannot currently transfer files between your <a style="text-decoration: none;" href="https://nznesi.atlassian.net/wiki/spaces/nesiproj/pages/104955907/Personal+Globus+Endpoint" rel="nofollow"> personal globus endpoint</a> and the local NeSI cluster endpoint from within the University (behind firewall).</p>