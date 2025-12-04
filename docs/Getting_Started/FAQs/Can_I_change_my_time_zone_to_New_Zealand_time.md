---
created_at: '2018-09-20T23:52:07Z'
tags: []
description: Information on the system timezone and how to make changes
---

The time displayed in your shell is controlled by a system variable
called `TZ`. To change to New Zealand time you need to set the variable
as follows:

```sh
export TZ="NZ"
```

This setting will automatically adjust for daylight saving, since the
`tzdata` package is installed at the system level. Our system engineers
will keep the `tzdata` package up to date.

## Making the change persistent

You can make your time zone setting persistent by adding the above line
to your `~/.bashrc`. If you do this, we recommend adding the following
line to your `~/.bash_profile`, or to your `~/.profile` if you have the
latter but not the former:

```sh
test -r ~/.bashrc && . ~/.bashrc
```

Please see the article, [.bashrc or.bash profile?](What_are_my-bashrc_and-bash_profile_for.md)
for more information.

## What about cron jobs?

To have the specifications in your crontab file interpreted as NZ times
start it with:

```sh
CRON_TZ=NZ
```

Also note that cron does not source either `~/.bashrc` or
`~/.bash_profile`, so most environment variables will not be set,
including TZ.
