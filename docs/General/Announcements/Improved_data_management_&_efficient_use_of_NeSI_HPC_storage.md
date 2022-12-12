A growing number of research projects are storing large amounts of data
on NeSI systems. To better support this growth, as well as optimise the
performance and availability of our filesystems, we are introducing new
data management policies and best practices for our HPC facilities.

By adopting these measures to regularly audit, clean and manage the
amount of data on our filesystems, we’ll ensure they remain
high-performing and responsive to your research computing workloads and
data science workflows.  
  

## Upcoming changes to data management processes for project directories

**<span class="underline"><span class="inline-highlight">  
4-15 October 2021</span></span>**

<span class="inline-highlight">The NeSI project filesystem is becoming
critically full, however it is currently storing a large amount of
dormant data that has not been accessed for more than 12 months. We need
your help to free up space on the project filesystem as soon as
possible. </span><span class="inline-highlight">Please review the data
you are currently storing in any  </span>`/nesi/project/`<span
class="inline-highlight"> directories and **delete or relocate** any
files that are no longer required for ongoing computational and/or
analytics work on NeSI.</span>

<span class="inline-highlight">We have started regular audits of data
stored in project folders, using the same format as our nobackup auto
cleaning ([described
here](https://support.nesi.org.nz/hc/en-gb/articles/360001162856)). See
the file
`/nesi/project/<project_code>/.policy.test/scan485/latest.summary.txt`
for a summary of the number and size of files within each project that
have not been accessed for more than 485 days (this is ~15 months, and
is the draft auto cleaning timeframe under consideration for the project
filesystem).</span>

<span class="inline-highlight">If you need assistance with this,
</span><a href="https://support.nesi.org.nz/hc/en-gb/requests/new" class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new"><span class="inline-highlight">contact Support </span></a><span
class="inline-highlight">and we’d be happy to help or answer
questions.</span><span class="inline-highlight"></span>

If you have data that may be used again on NeSI later,
<a href="https://support.nesi.org.nz/hc/en-gb/requests/new" class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new">let us know</a>
and we will consider whether a
<a href="https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service" class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/articles/360001169956-Long-Term-Storage-Service">Nearline</a>
storage allocation would be appropriate to manage this.

 

**<span class="wysiwyg-underline">18 October 2021</span>**

We will begin a limited roll-out of a new feature to automatically
identify inactive files in  `/nesi/project/` directories and schedule
them for deletion. Generally, we will be looking to identify files that
are inactive / untouched for more than 12 months. 

A selection of active projects will be invited to participate in this
first phase of the programme. If you would like to volunteer to be an
early tester / participant, please <span class="inline-highlight">
</span><a href="https://support.nesi.org.nz/hc/en-gb/requests/new" class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new"><span class="inline-highlight">contact Support</span></a>.
Otherwise, we will be in touch with projects directly to onboard them.

Insights from this initial phase will inform the criteria and processes
of the programme prior to it being released to the broader user
community.

<span class="inline-highlight">Alongside this work, we will also adopt a
new policy on how long inactive data may be stored on NeSI systems,
particularly once a research project itself becomes inactive.</span>

 

**<span class="underline"><span class="inline-highlight">January
2022</span></span>**

Starting in January 2022, we will expand the<span
class="inline-highlight"> </span>`/nesi/project/`<span
class="inline-highlight"> directory </span> data management programme to
include all active projects on NeSI. Additional Support documentation
and user information sessions will be hosted prior to wider
implementation, to provide advance notice of the change and to answer
any questions you may have around data lifecycle management. 

 

## Frequently asked questions

**1) Why are you introducing these new data management processes?  
**We want to avoid our online filesystems reaching critically full
levels, as that impacts their performance and availability for users. We
also want to ensure our active storage filesystems aren't being used to
store inactive data. This new data management feature
for `/nesi/project/` directories will complement our existing programme
of
<a href="https://support.nesi.org.nz/hc/en-gb/articles/360001162856" class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/articles/360001162856">automatic cleaning of the /nobackup file system</a>.

 

**2) Can I check how much storage I’m currently using on NeSI systems?**

You can query your actual usage and disk allocations at any time using
the following command: 

`$ nn_storage_quota`

The values for 'nn\_storage\_quota' are updated approximately every hour
and cached between updates.

 

**3) Can I recover data that I accidentally delete from my /project
directory?**

Perhaps. We regularly make read-only copies of the file system and save
them for up to seven days. For more information,
<a href="https://support.nesi.org.nz/hc/en-gb/articles/360000207315-File-Recovery" class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/articles/360000207315-File-Recovery">refer to our File Recovery page</a>.

 

**4) Where should I store my data on NeSI systems?**

<table>
<tbody>
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

 

**5) What should I do if I run out of storage space?**

There are two tracked resources in the NeSI filesystem, *disk
space* and *inodes (number of files)*. If you run into problems with
either of these,
<a href="https://support.nesi.org.nz/hc/en-gb/articles/360001125996-I-ve-run-out-of-storage-space" class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/articles/360001125996-I-ve-run-out-of-storage-space">refer to this Support page for more information</a>.

 

**6) I have questions that aren’t covered here. Who can I talk to?**

<a href="https://support.nesi.org.nz/hc/en-gb/requests/new" class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new">Contact Support</a>.
No question is too big or small and our intention is always to work with
you to find the best way to manage your research data.

 

## More information

This page will continue to be updated in the coming months with more
information. If you have questions at any time, don’t hesitate to
<a href="https://support.nesi.org.nz/hc/en-gb/requests/new" class="sc-cHGsZl lirsdj" title="https://support.nesi.org.nz/hc/en-gb/requests/new">contact Support</a>.
