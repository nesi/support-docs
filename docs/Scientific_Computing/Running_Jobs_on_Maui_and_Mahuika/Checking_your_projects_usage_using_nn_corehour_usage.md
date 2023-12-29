---
created_at: '2022-02-15T01:13:51Z'
hidden: false
weight: 1
tags: []
title: Checking your project's usage using nn_corehour_usage
vote_count: 0
vote_sum: 0
zendesk_article_id: 4416692988047
zendesk_section_id: 360000030876
---

To check your project's usage of Slurm-managed resources, you can use
the command `nn_corehour_usage`. This command displays usage of cluster
resources by a specific project, computed from the Slurm program
`sreport`.

## Synopsis

``` sh
nn_corehour_usage [OPTIONS...] PROJECT_CODE...
```

## Description

`nn_corehour_usage` shows a month-by-month breakdown of how the
specified project or projects have used Slurm resources. Some resources,
like disk space, are not managed by Slurm and so are excluded. Included
resources are CPU time, RAM time (also known as memory time) and GPU
time.

## Options

`-c`, `--calendar-months`

Break usage down so that the time periods are the first and last days of
the calendar months, instead  
of working back a month at a time from today.

`-n`, `--number-of-months=NUM`

Show `NUM` months back from today. Used in conjunction with `-c`, will
show `NUM` complete months plus the partial month up to when the command
is run. Default is 12 months. The results will not go further back than
when the cluster commenced operations.

`-u`, `--user=USERNAME`

Display results for the user `USERNAME`. The default user is the current
user.

Treat all subsequent entries on the command line, including those
starting with a dash (`-`), as arguments instead of as options.

## Examples

To print the last year of project `nesi12345`:

```sh
nn_corehour_usage nesi12345
```

To print the last six complete calendar months of project `nesi12345`:

``` sh
nn_corehour_usage -c -n 6 nesi12345
```
