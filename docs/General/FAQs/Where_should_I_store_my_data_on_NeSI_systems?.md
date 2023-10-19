---
created_at: '2022-06-15T00:53:58Z'
hidden: false
label_names: []
position: 0
title: Where should I store my data on NeSI systems?
vote_count: 0
vote_sum: 0
zendesk_article_id: 4975669783951
zendesk_section_id: 360000039036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<table data-number-column="false">
<tbody>
<tr class="odd">
<td data-colwidth="226.67"><p><strong>How often will my team's HPC jobs
be accessing the data?</strong></p></td>
<td data-colwidth="226.67"><p><strong>How often will my team's HPC jobs
be modifying the data? </strong></p></td>
<td data-colwidth="226.67"><p><strong>Recommended
option </strong></p></td>
</tr>
<tr class="even">
<td data-colwidth="226.67"><p>Often</p></td>
<td data-colwidth="226.67"><p>Often (at least once every two
months)</p></td>
<td data-colwidth="226.67"><p>Store in your
/nobackup/&lt;projectcode&gt; directory (but ensure key result data is
copied to the persistent project directory).</p></td>
</tr>
<tr class="odd">
<td data-colwidth="226.67"><p>Often</p></td>
<td data-colwidth="226.67"><p>Seldom</p></td>
<td data-colwidth="226.67"><p>Store in your /project/&lt;projectcode&gt;
directory.</p></td>
</tr>
<tr class="even">
<td data-colwidth="226.67"><p>Seldom</p></td>
<td data-colwidth="226.67"><p>Seldom</p></td>
<td data-colwidth="226.67"><p>Apply for an allocation to use NeSI’s <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service"
title="https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service">long-term
storage service</a> or store elsewhere (e.g. at your
institution).</p></td>
</tr>
</tbody>
</table>

 

In general, the **project directory** should be used for reference data,
tools, and job submission and management scripts. The **nobackup
directory** should be used for holding large reference working datasets
(e.g., an extraction of compressed input data) and as a destination for
writing and modifying temporary data. The nobackup directory can also be
used to build and edit code, provided that the code is under version
control and changes are regularly checked into upstream revision control
systems. The **long-term storage service** should be used for larger
datasets that you only access occasionally and do not need to change in
situ. 

 
