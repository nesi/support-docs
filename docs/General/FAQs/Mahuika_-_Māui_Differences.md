Aside from differences in software stack there are a few other
differences between the platforms to be aware of.

# Logging in

Both Mahuika and Māui require logging in to the Lander node first.

    ssh user123@lander.nesi.org.nz

As you log in to the Lander node, you can expect to receive the
following prompts:

    Login Password (First Factor):

    Authenticator Code (Second Factor):

Note that being prompted for `Authenticator Code (Second Factor)` does
not prove that the system has accepted your
`Login Password (First Factor)` as correct. If you enter either
incorrectly, you will be prompted again for both.

## Mahuika

Mahuika follows the same procedure as the lander node, except that it
doesn't ask for a second factor.

    ssh login.mahuika.nesi.org.nz

You will be prompted:

    Login Password:

At this prompt, enter only your password (a.k.a. first factor).

## Māui

Māui differs slightly in how you are authenticated.

    ssh login.maui.nesi.org.nz

You will be prompted.

    Password:

Unlike on Mahuika, `Password` is equal to `First Factor` +
`Second Factor` e.g. `password123456`

# Job Limits

Both Māui and Mahuika have limits on the size and types of jobs you can
run, but the limits on each machine is different.

## Mahuika

Mahuika is made up of several [partitions which have different resources
and different
limits](https://support.nesi.org.nz/hc/en-gb/articles/360000204076). A
job can request up to 20,000 CPU core hours, running up to 3 weeks with
up to 576 CPU cores (equivalent to eight full nodes). Furthermore, there
are special nodes available with high memory (up to 6 TB) or GPUs.
Depending on what resources you are requesting and for how long, your
jobs will be automatically assigned to the most suitable partition.
Mahuika allows the submission of jobs with variable numbers of CPUs and
amounts of RAM (memory). The nodes your job is running on will probably
be shared with other jobs.

## Māui

Māui only has a [single partition to which NeSI users are permitted to
submit
work](https://support.nesi.org.nz/hc/en-gb/articles/360000204116). For
your job, you can request a maximum of 24 hours or a maximum of 240
nodes, however no job may request more than 1,200 Māui node-hours in
total. (This means that if you request more than 50 nodes, your maximum
allowed time will start decreasing.) Māui only allows submission of jobs
in units of nodes, so the smallest possible job takes a whole node, and
there can never be more than one job on a node at a time.

Additionally, projects with valid allocations on Māui will also have
access to [Māui's ancilliary
nodes,](https://support.nesi.org.nz/hc/en-gb/articles/360000203776)
where jobs requiring up to 768 GB of memory or jobs that require GPUs
can be run. When submitting a job to the Māui ancillary nodes you may
also request parts of nodes, rather than needing to use the entire node.
Because there are relatively few Māui ancillary nodes, if you require
substantial amounts of time on nodes like the Māui ancillary nodes, we
may grant your project an additional allocation on Mahuika. If we do so,
we will not forbid you from using the Māui ancillary nodes while your
Māui allocation remains valid and you are permitted to access NeSI
clusters.
