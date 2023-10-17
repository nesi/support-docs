---
created_at: '2019-06-19T10:31:21Z'
hidden: true
label_names: []
position: 6
title: How is my allocation aged under Fair Share?
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001014876
zendesk_section_id: 360000030876
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
Fair Share is an alternative to a conventional ageing model.

Under conventional ageing, your allocation would be split up into
chunks. For example, if your allocation is for 600,000 CPU core hours
for one year, it might be split up into twelve monthly chunks, each of
50,000 CPU core hours. At the end of your first month, if you had used
less than 50,000 CPU core hours thus far, your remaining allocation
would be reduced to 550,000. At the end of your second month, it would
be reduced to 500,000, and so on.

Conventional ageing thus rewards research teams who don't ask for time
until they need it right away, and who, once they have got their
allocation, hammer the machine to use as much of their allocation as
quickly as possible.

Fair Share instead rewards those research teams who use their allocation
as evenly as possible while the allocation lasts. Because of the way
Fair Share works, something like ageing is built in to it, but works
differently.

To illustrate ageing behaviour under Fair Share, we have simulated five
scenarios. These scenarios take place on a simplified version of the
Mahuika cluster, in which:

-   The cluster is being used at a consistent rate of 170,000 CPU core
    hours every day across all project teams,
-   The decay factor half life is two weeks (as it is on Mahuika),
-   The decay interval is one day, instead of the current Mahuika value
    of five minutes.

We consider these five scenarios for a project that has received a
six-month allocation, from 1 June 2018 to 30 November 2018 (a total of
183 days), and is expected to use 1% of the cluster, so that the
project's allocation is 311,100 CPU core hours (620,500 CPU core hours
per annum). For each of the scenarios, we will look at the project's
Fair Share score at midnight starting 21 November 2018, when it has ten
days left on its allocation.

## Scenario 1: Constant usage

In this scenario, the project team has used the cluster at a constant
rate of 1,700 CPU core hours per day. At the end of 20 November, the
project has used a total of 294,100 CPU core hours, just under 95% of
its total allocation. The project's Fair Share score is 0.5.

## Scenario 2: Alternating quiet and busy months

In this scenario, the project team did not use the cluster at all in the
months of June, August and October, but used the cluster at a rate of
3,400 CPU core hours per day during July, September and November. At the
end of 20 November, the project has used a total of 275,400 CPU core
hours, just under 89% of its total allocation. The project's Fair Share
score is approximately 0.38.

## Scenario 3: Three quiet months followed by three busy months

In this scenario, the project team, despite getting an allocation that
started in June, did not start using the cluster until September, when
they began using at a rate of 3,400 CPU core hours per day. At the end
of 20 November, the project has used a total of 275,400 CPU core hours,
just as in the previous scenario. But because the project's usage is
more concentrated towards the back end of the allocation, the project's
Fair Share score is approximately 0.26. By now, some difficulty in
getting jobs through the queue would be expected.

## Scenario 4: Four quiet months followed by two busy months

In this scenario, the project team did not start using the cluster until
October, and then began using at a rate of 5,100 CPU core hours per day.
At the end of 20 November, the project has used a total of 260,100 CPU
core hours, just under 84% of its total allocation. The project's Fair
Share score is less than 0.15. Jobs in the queue are likely to be
considerably delayed.

## Scenario 5: Attempting to use the entire allocation in its last 17 days

In this scenario, the project team started work on 14 November, aiming
to use through the entire 311,100 CPU core hours in 17 days, and
(implausibly) have managed to maintain a rate of 18,300 CPU core hours
per day. After seven days at that rate, during which time the project
team used 128,100 CPU core hours, only just above 40% of their total
allocation, the project's Fair Share score is only just above 0.11.
