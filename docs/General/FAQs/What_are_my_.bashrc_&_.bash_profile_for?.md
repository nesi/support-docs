---
created_at: '2019-10-03T04:08:49Z'
hidden: false
label_names: []
position: 0
title: What are my .bashrc & .bash_profile for?
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001194536
zendesk_section_id: 360000039036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p>If you've been using Linux for a while, you'll have come across resource files. These files are typically read when you start a new instance of your <em>shell</em>, the program that interprets and executes the commands that you type in at your command prompt. But they're somewhat confusing, because there are several, and it's not obvious which are read and when.</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Warning</h3>
<p>This documentation is specific to the <em>bash</em> shell, which is our chosen default shell for all users, and is the default for most Linux machines. If you have chosen a different default shell, or have started another shell manually on the command line, these notes will apply with modifications, or not at all; please consult the documentation for your shell.</p>
</blockquote>
<h2><code>~/.bashrc</code></h2>
<p>In a standard configuration, <code>~/.bashrc</code> is read when your shell session is interactive but not a login session. Because most of your sessions on the cluster will be login sessions, <code>~/.bashrc</code> will not ordinarily be read by default. It will, however, be read if you start an interactive shell within a shell, for instance by executing <code>bash</code> at the command line.</p>
<h2>
<code>~/.bash_profile</code> (and <code>~/.profile</code>)</h2>
<p>In a standard configuration, <code>~/.bash_profile</code> is read when your shell session is a login session. When you log in to the cluster, you will get a login session by default.</p>
<p>The equivalent file in the Bourne shell (<code>sh</code>) is called <code>~/.profile</code>. Because the Bash shell is designed to be (mostly) compatible with the Bourne shell, if <code>bash</code> finds <code>~/.profile</code> but not <code>~/.bash_profile</code>, it will source <code>~/.profile</code> as if it were <code>~/.bash_profile</code>. For the rest of this article, however, we will assume that you're using <code>~/.bash_profile</code>.</p>
<h2>Can I have the same environment variables, aliases, functions, etc. whether my shell is a login shell or not?</h2>
<p>Absolutely. You can define them in both <code>~/.bashrc</code> and <code>~/.bash_profile</code>. But this isn't the best way.</p>
<h2>I thought not. I don't want to repeat myself!</h2>
<p>A wise choice. Repeating yourself is extra work, and dangerous in that if you later have to make a change, you may forget to do it everywhere it's needed.</p>
<p>Fortunately, instead of repeating yourself, you can source one file from another. Most commonly, people source <code>~/.bashrc</code>, if it exists and can be read, from <code>~/.bash_profile</code>:</p>
<pre><code># Put this code in your ~/.bash_profile
test -r ~/.bashrc &amp;&amp; . ~/.bashrc</code></pre>
<p>This statement has the effect of ensuring that <code>~/.bashrc</code> will be loaded in all interactive shells (except those launched with special options intended to prevent such loading), instead of only in non-login shells.</p>
<h2>What should go where?</h2>
<p>That's largely up to you. However, we have found the following to be useful rules of thumb:</p>
<ul>
<li>Functions and aliases go in <code>~/.bashrc</code>
</li>
<li>Modifications to <code>PATH</code> and <code>LD_LIBRARY_PATH</code> go in <code>~/.bash_profile</code>
</li>
</ul>
<p>These are guidelines only and are subject to your specific working practices and how you expect your shells to behave.</p>
<h2>Further information</h2>
<p>You can find further information in the INVOCATION section of the bash man page, accessible by typing the command <code>man bash</code> at your terminal prompt.</p>
<p>Alternatively, or for further commentary, there are many articles on the Internet that address this question in more detail. We do not vouch for the completeness or accuracy of any information published by third parties, and you rely on such information at your own risk.</p>