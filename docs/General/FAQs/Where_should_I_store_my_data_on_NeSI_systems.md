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

<div class="pm-table-container  sc-jKJlTe loXQau" data-layout="default">
<div class="pm-table-wrapper">
<table data-number-column="false">
<colgroup>
<col>
<col>
<col>
</colgroup>
<tbody>
<tr>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="4765"><strong data-renderer-mark="true">How often will my team's HPC jobs be accessing the data?</strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="4825"><strong data-renderer-mark="true">How often will my team's HPC jobs be modifying the data? </strong></p>
</td>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="4886"><strong data-renderer-mark="true">Recommended option </strong></p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="4911">Often</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="4920">Often (at least once every two months)</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="4962">Store in your /nobackup/&lt;projectcode&gt; directory (but ensure key result data is copied to the persistent project directory).</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="5090">Often</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="5099">Seldom</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="5109">Store in your /project/&lt;projectcode&gt; directory.</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="5161">Seldom</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="5171">Seldom</p>
</td>
<td colspan="1" rowspan="1" data-colwidth="226.67">
<p data-renderer-start-pos="5181">Apply for an allocation to use NeSI’s <a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service" href="https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service" data-renderer-mark="true">long-term storage service </a>or store elsewhere (e.g. at your institution).</p>
</td>
</tr>
</tbody>
</table>
</div>
</div>
<p data-renderer-start-pos="5297"> </p>
<p data-renderer-start-pos="5297">In general, the <strong>project directory</strong> should be used for reference data, tools, and job submission and management scripts. The <strong>nobackup directory</strong> should be used for holding large reference working datasets (e.g., an extraction of compressed input data) and as a destination for writing and modifying temporary data. The nobackup directory can also be used to build and edit code, provided that the code is under version control and changes are regularly checked into upstream revision control systems. The <strong>long-term storage service</strong> should be used for <span>larger datasets that you only access occasionally and do not need to change in situ. </span></p>
<p data-renderer-start-pos="5776"> </p>