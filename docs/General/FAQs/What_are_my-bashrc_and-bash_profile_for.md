---
created_at: '2019-10-03T04:08:49Z'
hidden: false
tags: []
title: What are my .bashrc & .bash_profile for?
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001194536
zendesk_section_id: 360000039036
---

If you've been using Linux for a while, you'll have come across resource
files. These files are typically read when you start a new instance of
your *shell*, the program that interprets and executes the commands that
you type in at your command prompt. But they're somewhat confusing,
because there are several, and it's not obvious which are read and when.

!!! warning
     This documentation is specific to the *bash* shell, which is our
     chosen default shell for all users, and is the default for most Linux
     machines. If you have chosen a different default shell, or have
     started another shell manually on the command line, these notes will
     apply with modifications, or not at all; please consult the
     documentation for your shell.

## `~/.bashrc`

In a standard configuration, `~/.bashrc` is read when your shell session
is interactive but not a login session. Because most of your sessions on
the cluster will be login sessions, `~/.bashrc` will not ordinarily be
read by default. It will, however, be read if you start an interactive
shell within a shell, for instance by executing `bash` at the command
line.

## `~/.bash_profile` (and `~/.profile`)

In a standard configuration, `~/.bash_profile` is read when your shell
session is a login session. When you log in to the cluster, you will get
a login session by default.

The equivalent file in the Bourne shell (`sh`) is called `~/.profile`.
Because the Bash shell is designed to be (mostly) compatible with the
Bourne shell, if `bash` finds `~/.profile` but not `~/.bash_profile`, it
will source `~/.profile` as if it were `~/.bash_profile`. For the rest
of this article, however, we will assume that you're using
`~/.bash_profile`.

## Can I have the same environment variables, aliases, functions, etc. whether my shell is a login shell or not?

Absolutely. You can define them in both `~/.bashrc` and
`~/.bash_profile`. But this isn't the best way.

## I thought not. I don't want to repeat myself!

A wise choice. Repeating yourself is extra work, and dangerous in that
if you later have to make a change, you may forget to do it everywhere
it's needed.

Fortunately, instead of repeating yourself, you can source one file from
another. Most commonly, people source `~/.bashrc`, if it exists and can
be read, from `~/.bash_profile`:

``` sl
# Put this code in your ~/.bash_profile
test -r ~/.bashrc && . ~/.bashrc
```

This statement has the effect of ensuring that `~/.bashrc` will be
loaded in all interactive shells (except those launched with special
options intended to prevent such loading), instead of only in non-login
shells.

## What should go where?

That's largely up to you. However, we have found the following to be
useful rules of thumb:

- Functions and aliases go in `~/.bashrc`
- Modifications to `PATH` and `LD_LIBRARY_PATH` go in
    `~/.bash_profile`

These are guidelines only and are subject to your specific working
practices and how you expect your shells to behave.

## Further information

You can find further information in the INVOCATION section of the bash
man page, accessible by typing the command `man bash` at your terminal
prompt.

Alternatively, or for further commentary, there are many articles on the
Internet that address this question in more detail. We do not vouch for
the completeness or accuracy of any information published by third
parties, and you rely on such information at your own risk.
