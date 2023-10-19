---
created_at: '2020-05-07T02:51:35Z'
hidden: false
label_names:
- git
- github
- version control
- repository
position: 2
title: 'Git: Reference Sheet'
vote_count: 11
vote_sum: 11
zendesk_article_id: 360001508515
zendesk_section_id: 360000278975
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p>Git is the most universally adopted version control software and is often used alongside remote repositories like GitHub and GitLab for developing, managing and distributing code.</p>
<p>Full Git documentation can be found <a href="https://git-scm.com/docs/git" target="_self">here</a>, or using <code>man git</code>.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360004194235/Git_Diagram.svg" alt="Git_Diagram.svg"></p>
<h2>Authentication</h2>
<p>In order to pull from a private repo, or push changes to a remote, you need to authenticate yourself on the cluster.</p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">Password authentication</h3>
<p>GitHub removed support for password authentication on August 13, 2021. Using a SSH key is now the easiest way to set up authentication.</p>
</blockquote>
<h3>SSH Authentication (GitHub)</h3>
<p>More information can be found in the <a href="https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent" target="_self">GitHub documentation</a>.</p>
<ul>
<li>On the NeSI cluster, run the command 
<pre><code class="hljs language-shell">ssh-keygen -t ed25519 -C "your_github_account@example.com"</code></pre>
</li>
<li>When prompted for a file name, press <code>enter</code>. When prompted for a passcode, press enter twice more.</li>
<li>Open up the newly created .pub key with the command 
<pre>cat ~/.ssh/id_ed25519.pub</pre>
(or whatever you named the key). It should look something like: 
<pre>ssh-ed25519 ABCDEFGKSAfjksjafkjsaLJfakjJF <code class="hljs language-shell">your_github_account@example.com</code></pre>
Copy the whole key.</li>
<li>
<p>Now log in to your github account. In the upper-right corner of any page, click your profile photo click <span></span><strong>Settings</strong>.</p>
<p><span class="procedural-image-wrapper"><img src="https://docs.github.com/assets/cb-34573/images/help/settings/userbar-account-settings.png" alt="Settings icon in the user bar"></span></p>
</li>
<li>
<p>In the "Access" section of the sidebar, click <span></span><strong><span></span>SSH and GPG keys</strong>.</p>
</li>
<li>
<p>Click <span></span><strong>New SSH key </strong><span></span>or <span></span><strong>Add SSH key</strong>.</p>
<p><span class="procedural-image-wrapper"><img src="https://docs.github.com/assets/cb-28257/images/help/settings/ssh-add-ssh-key-with-auth.png" alt="SSH Key button"></span></p>
</li>
<li>
<p>In the "Title" field, put "Mahuika" or "NeSI".</p>
</li>
<li>
<p>Paste your key into the "Key" field.</p>
<p><span class="procedural-image-wrapper"><img src="https://docs.github.com/assets/cb-47495/images/help/settings/ssh-key-paste-with-type.png" alt="The key field"></span></p>
</li>
<li>
<p>Click <span></span><strong>Add SSH key</strong>.</p>
</li>
<li>Switching back to your terminal on the cluster, you can test your connection with the command 
<pre>ssh -T git@github.com</pre>
You may be promted to authenticate, if so type 'yes'<br>If everything is working, you should see the message 
<pre>Hi User! You've successfully authenticated, but GitHub does not provide shell access.</pre>
</li>
</ul>
<h2>Basics</h2>
<p>You can create a repository with either of the following commands.</p>
<table style="height: 153px; width: 972px;">
<tbody>
<tr style="height: 22px;">
<td style="width: 184.031px; height: 63px;">clone</td>
<td style="width: 442.969px; height: 63px;"><code>git clone https://github.com/nesi/perf-training.git</code></td>
<td style="width: 310px; height: 63px;">Copies a remote repository into your current directory.</td>
</tr>
<tr style="height: 22px;">
<td style="width: 184.031px; height: 61.1719px;">init</td>
<td style="width: 442.969px; height: 21px;"><code>git init</code></td>
<td style="width: 310px; height: 21px;">Creates a new empty repo in your current directory.</td>
</tr>
</tbody>
</table>
<p> </p>
<table style="height: 678px; width: 974px;">
<tbody>
<tr style="height: 89px;">
<td style="width: 142px; height: 89px;" rowspan="2">add</td>
<td style="width: 310px; height: 89px;"><code><span class="c">git add &lt;file1&gt; &lt;file2&gt;</span></code></td>
<td style="width: 513px; height: 89px;">Adds <code>&lt;file1&gt;</code> and <code>&lt;file2&gt;</code> to the staging area.</td>
</tr>
<tr style="height: 89px;">
<td style="width: 310px; height: 89px;"><span class="c"><code>git add *.py</code></span></td>
<td style="width: 513px; height: 89px;"> Adds all python files in the current directory to the staging area.</td>
</tr>
<tr style="height: 41px;">
<td style="width: 142px; height: 41px;">status</td>
<td style="width: 310px; height: 41px;"><span class="c"><code>git status</code></span></td>
<td style="width: 513px; height: 41px;">Lists changes in working directory, and staged files.</td>
</tr>
<tr style="height: 39px;">
<td style="width: 142px; height: 39px;" rowspan="3">commit </td>
<td style="width: 310px; height: 39px;"><code><span class="c">git commit</span></code></td>
<td style="width: 513px; height: 39px;">Records everything in the staging area to your repository. The default text editor will prompt you for a commit message.</td>
</tr>
<tr style="height: 39px;">
<td style="width: 310px; height: 39px;"><span class="c"><code>git commit -m "Commit message"</code></span></td>
<td style="width: 513px; height: 39px;">Records everything in the staging area to your repository with the commit message "Commit message"</td>
</tr>
<tr style="height: 39px;">
<td style="width: 310px; height: 39px;"><span class="c"><code>git commit --amend</code></span></td>
<td style="width: 513px; height: 39px;">Modify last commit instead of creating a new one. Useful for fixing small mistakes.</td>
</tr>
<tr style="height: 41px;">
<td style="width: 142px; height: 41px;" rowspan="2">log </td>
<td style="width: 310px; height: 41px;"><code>git log</code></td>
<td style="width: 513px; height: 41px;">Prints commit history of repo.</td>
</tr>
<tr style="height: 41px;">
<td style="width: 310px; height: 41px;"><code>git log &lt;filename&gt;</code></td>
<td style="width: 513px; height: 41px;">Prints commit history of <code>&lt;filename&gt;</code>.</td>
</tr>
<tr style="height: 41px;">
<td style="width: 142px; height: 41px;" rowspan="2">reset </td>
<td style="width: 310px; height: 41px;"><code>git reset</code></td>
<td style="width: 513px; height: 41px;">Removes all files from staging area. (Opposite of <code>git add</code>)</td>
</tr>
<tr style="height: 41px;">
<td style="width: 310px; height: 41px;"><code>git reset &lt;filename&gt;</code></td>
<td style="width: 513px; height: 41px;">Removes <code>&lt;filename&gt;</code> from staging area.</td>
</tr>
</tbody>
</table>
<h2>Remote</h2>
<p>By default, fetch, pull and push will operate on the origin repo. This will be the repo you cloned from, or set manually using <code> git branch --set-upstream-to
  &lt;origin&gt;</code>.</p>
<table style="height: 76px; width: 1050px;">
<tbody>
<tr>
<td style="width: 136px;" rowspan="2">fetch </td>
<td style="width: 565.701px;"><code>git fetch</code></td>
<td style="width: 310.299px;">Gets status of 'origin'. git fetch <strong>does not </strong>change your working directory or local repository (see <code>git pull</code>). </td>
</tr>
<tr>
<td style="width: 565.701px;"><code>git fetch &lt;repo&gt; &lt;branch&gt;</code></td>
<td style="width: 310.299px;">Get status of <code>&lt;repo&gt;</code> <code>&lt;branch&gt;</code>.</td>
</tr>
<tr>
<td style="width: 136px;" rowspan="2">pull </td>
<td style="width: 565.701px;"><code>git pull</code></td>
<td style="width: 310.299px;">Incorporates changes from 'origin' into local repo. </td>
</tr>
<tr>
<td style="width: 565.701px;"><code>git pull &lt;repo&gt; &lt;branch&gt;</code></td>
<td style="width: 310.299px;">Incorporates changes from <code>&lt;repo&gt;</code> <code>&lt;branch&gt;</code> into local repo.</td>
</tr>
<tr>
<td style="width: 136px;" rowspan="2">push </td>
<td style="width: 565.701px;"><code>git push</code></td>
<td style="width: 310.299px;">Incorporates changes from local repo into 'origin'. </td>
</tr>
<tr>
<td style="width: 565.701px;"><code>git push &lt;repo&gt; &lt;branch&gt;</code></td>
<td style="width: 310.299px;">Incorporates changes from local repo into <code>&lt;repo&gt;</code> <code>&lt;branch&gt;</code>
</td>
</tr>
</tbody>
</table>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tip</h3>
<p>If you are working without collaborators, there should be no reason to have a conflict between your local and your remote repo. Make sure you always git pull when starting work on your local and git push when finished, this will save you wasting time resolving unnecessary merges.</p>
</blockquote>
<h2>Branches</h2>
<p>At an introductory level, it is best to avoid workflows that lead to multiple branches, or requires merging.</p>
<table style="height: 76px; width: 966px;">
<tbody>
<tr>
<td style="width: 136px;" rowspan="2">branch </td>
<td style="width: 303px;"><code>git branch</code></td>
<td style="width: 489px;">List branches.</td>
</tr>
<tr>
<td style="width: 303px;"><code>git branch &lt;branch-name&gt;</code></td>
<td style="width: 489px;">Create new branch <code>&lt;branch-name</code>
</td>
</tr>
<tr>
<td style="width: 136px;">checkout</td>
<td style="width: 303px;"><code>git checkout &lt;branch-name&gt;</code></td>
<td style="width: 489px;">Switch to editing branch <code>&lt;branch-name&gt;</code>
</td>
</tr>
<tr>
<td style="width: 136px;">merge</td>
<td style="width: 303px;"><code>git merge &lt;branch-name&gt;</code></td>
<td style="width: 489px;">Merge <code>&lt;branch-name&gt;</code> into current branch.</td>
</tr>
</tbody>
</table>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">Other Resources</h3>
<ul>
<li><a href="https://ohshitgit.com/">https://ohshitgit.com/</a></li>
</ul>
</blockquote>