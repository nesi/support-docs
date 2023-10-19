---
created_at: '2021-09-30T22:51:02Z'
hidden: false
label_names: []
position: 3
title: Improved data management & efficient use of NeSI HPC storage
vote_count: 0
vote_sum: 0
zendesk_article_id: 4407274387599
zendesk_section_id: 200732737
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p data-renderer-start-pos="2171">A growing number of research projects are storing large amounts of data on NeSI systems. To better support this growth, as well as optimise the performance and availability of our filesystems, we are introducing new data management policies and best practices for our HPC facilities.</p>
<p data-renderer-start-pos="2767">By adopting these measures to regularly audit, clean and manage the amount of data on our filesystems, we’ll ensure they remain high-performing and responsive to your research computing workloads and data science workflows.<br><br></p>
<h2 id="Programme-timeline" data-renderer-start-pos="2992">Upcoming changes to data management processes for project directories</h2>
<p data-renderer-start-pos="2992"><strong><u data-renderer-mark="true"><span id="a1a537f0-110e-4494-81ec-4a9681856e97" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="a1a537f0-110e-4494-81ec-4a9681856e97"><br>4-15 October 2021</span></u></strong></p>
<p data-renderer-start-pos="3070"><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af">The NeSI project filesystem is becoming critically full, however it is currently storing a large amount of dormant data that has not been accessed for more than 12 months. We need your help to free up space on the project filesystem as soon as possible. </span><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af">Please review the data you are currently storing in any  </span><code class="code css-9z42f9" data-renderer-mark="true"><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af">/nesi/project/</span></code><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af"> directories and <strong>delete or relocate</strong> any files that are no longer required for ongoing computational and/or analytics work on NeSI.</span></p>
<p data-renderer-start-pos="3070"><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af">We have started regular audits of data stored in project folders, using the same format as our nobackup auto cleaning (<a href="https://support.nesi.org.nz/hc/en-gb/articles/360001162856" target="_self">described here</a>). See the file <code class="code css-9z42f9" data-renderer-mark="true">/nesi/project/&lt;project_code&gt;/.policy.test/scan485/latest.summary.txt</code> for a summary of the number and size of files within each project that have not been accessed for more than 485 days (this is ~15 months, and is the draft auto cleaning timeframe under consideration for the project filesystem).</span></p>
<p data-renderer-start-pos="3070"><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af">If you need assistance with this, </span><a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new" href="https://support.nesi.org.nz/hc/en-gb/requests/new" data-renderer-mark="true"><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af">contact Support </span></a><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af">and we’d be happy to help or answer questions.</span><span class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af"></span></p>
<p data-renderer-start-pos="3375">If you have data that may be used again on NeSI later, <a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new" href="https://support.nesi.org.nz/hc/en-gb/requests/new" data-renderer-mark="true">let us know</a> and we will consider whether a <a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service" href="https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service" data-renderer-mark="true">Nearline</a> storage allocation would be appropriate to manage this.</p>
<p data-renderer-start-pos="3375"> </p>
<p data-renderer-start-pos="3375"><strong><span class="wysiwyg-underline">18 October 2021</span></strong></p>
<p data-renderer-start-pos="3630">We will begin a limited roll-out of a new feature to automatically identify inactive files in  <code class="code css-9z42f9" data-renderer-mark="true">/nesi/project/</code> directories and schedule them for deletion. Generally, we will be looking to identify files that are inactive / untouched for more than 12 months. </p>
<p data-renderer-start-pos="3630">A selection of active projects will be invited to participate in this first phase of the programme. If you would like to volunteer to be an early tester / participant, please <span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af"> </span><a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new" href="https://support.nesi.org.nz/hc/en-gb/requests/new" data-renderer-mark="true"><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af">contact Support</span></a>. Otherwise, we will be in touch with projects directly to onboard them.</p>
<p data-renderer-start-pos="3630">Insights from this initial phase will inform the criteria and processes of the programme prior to it being released to the broader user community.</p>
<p data-renderer-start-pos="3630"><span id="3710db4f-8652-4386-845a-7ffe2b4a7960" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="3710db4f-8652-4386-845a-7ffe2b4a7960">Alongside this work, we will also adopt a new policy on how long inactive data may be stored on NeSI systems, particularly once a research project itself becomes inactive.</span></p>
<p data-renderer-start-pos="3375"> </p>
<p data-renderer-start-pos="3573"><strong><u data-renderer-mark="true"><span id="4fb7b80b-c0d5-4347-8013-9e253da33947" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="4fb7b80b-c0d5-4347-8013-9e253da33947">January 2022</span></u></strong></p>
<p data-renderer-start-pos="3914">Starting in January 2022, we will expand the<span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af"> </span><code class="code css-9z42f9" data-renderer-mark="true"><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af">/nesi/project/</span></code><span id="865dfa52-8d33-4a95-86b1-fcfae6f336af" class="inline-highlight" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="865dfa52-8d33-4a95-86b1-fcfae6f336af"> directory </span> data management programme to include all active projects on NeSI. Additional Support documentation and user information sessions will be hosted prior to wider implementation, to provide advance notice of the change and to answer any questions you may have around data lifecycle management. </p>
<p data-renderer-start-pos="3914"> </p>
<h2 id="Frequently-asked-questions" data-renderer-start-pos="4158"><span id="702d765e-b997-426f-99cb-22eb71272264" data-renderer-mark="true" data-mark-type="annotation" data-mark-annotation-type="inlineComment" data-id="702d765e-b997-426f-99cb-22eb71272264">Frequently asked questions</span></h2>
<p data-renderer-start-pos="4158"><strong>1) Why are you introducing these new data management processes?<br></strong>We want to avoid our online filesystems reaching critically full levels, as that impacts their performance and availability for users. We also want to ensure our active storage filesystems aren't being used to store inactive data. This new data management feature for <code class="code css-9z42f9" data-renderer-mark="true">/nesi/project/</code> directories will complement our existing programme of <a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/articles/360001162856" href="https://support.nesi.org.nz/hc/en-gb/articles/360001162856" data-renderer-mark="true">automatic cleaning of the /nobackup file system</a>.</p>
<p data-renderer-start-pos="4158"> </p>
<p data-renderer-start-pos="4158"><strong>2) Can I check how much storage I’m currently using on NeSI systems?</strong></p>
<p data-renderer-start-pos="4258">You can query your actual usage and disk allocations at any time using the following command: </p>
<p data-renderer-start-pos="4354"><code class="code css-9z42f9" data-renderer-mark="true">$ nn_storage_quota</code></p>
<p data-renderer-start-pos="4374">The values for 'nn_storage_quota' are updated approximately every hour and cached between updates.</p>
<p data-renderer-start-pos="4474"> </p>
<p data-renderer-start-pos="4476"><strong data-renderer-mark="true">3) Can I recover data that I accidentally delete from my /project directory? </strong></p>
<p data-renderer-start-pos="4555">Perhaps. We regularly make read-only copies of the file system and save them for up to seven days. For more information, <a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/articles/360000207315-File-Recovery" href="https://support.nesi.org.nz/hc/en-gb/articles/360000207315-File-Recovery" data-renderer-mark="true">refer to our File Recovery page</a>.</p>
<p data-renderer-start-pos="4710"> </p>
<p data-renderer-start-pos="4712"><strong data-renderer-mark="true">4) Where should I store my data on NeSI systems?</strong></p>
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
<p data-renderer-start-pos="5297">In general, the <strong>project directory</strong> should be used for reference data, tools, and job submission and management scripts. The <strong>nobackup directory</strong> should be used for holding large reference working datasets (e.g., an extraction of compressed input data) and as a destination for writing and modifying temporary data. The nobackup directory can also be used to build and edit code, provided that the code is under version control and changes are regularly checked into upstream revision control systems. The <strong>long-term storage service</strong> should be used for <span>larger datasets that you only access occasionally and do not need to change in situ. </span></p>
<p data-renderer-start-pos="5776"> </p>
<p data-renderer-start-pos="5778"><strong data-renderer-mark="true">5) What should I do if I run out of storage space?</strong></p>
<p data-renderer-start-pos="5830">There are two tracked resources in the NeSI filesystem, <em data-renderer-mark="true">disk space</em> and <em data-renderer-mark="true">inodes (number of files)</em>. If you run into problems with either of these, <a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/articles/360001125996-I-ve-run-out-of-storage-space" href="https://support.nesi.org.nz/hc/en-gb/articles/360001125996-I-ve-run-out-of-storage-space" data-renderer-mark="true">refer to this Support page for more information</a>.</p>
<p data-renderer-start-pos="6024"> </p>
<p data-renderer-start-pos="6026"><strong data-renderer-mark="true">6) I have questions that aren’t covered here. Who can I talk to?</strong></p>
<p data-renderer-start-pos="6093"><a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new" href="https://support.nesi.org.nz/hc/en-gb/requests/new" data-renderer-mark="true">Contact Support</a>. No question is too big or small and our intention is always to work with you to find the best way to manage your research data.</p>
<p data-renderer-start-pos="3914"> </p>
<h2 id="Programme-timeline" data-renderer-start-pos="2992">More information</h2>
<p data-renderer-start-pos="4117">This page will continue to be updated in the coming months with more information. If you have questions at any time, don’t hesitate to <a class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new" href="https://support.nesi.org.nz/hc/en-gb/requests/new" data-renderer-mark="true">contact Support</a>.</p>