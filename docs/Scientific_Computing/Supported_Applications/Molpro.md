---
created_at: '2016-02-04T03:09:05Z'
tags:
- mahuika
- chemistry
description: Supported applications page for Molpro
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

Molpro is a complete system of *ab initio* programs for molecular
electronic structure calculations.

The Molpro home page is at <https://molpro.net>.

## Licensing requirements

Molpro is made available to researchers under commercial licence
agreements with individuals, research groups or institutions. Whether
you have access to Molpro, which versions you have access to, and under
what conditions, will vary depending on where you work or study. You
will only be permitted to access and use any given version of Molpro on
any NeSI cluster if you have a valid licence to use that version of
Molpro at your place of work or study, and if the terms of your licence
permit cluster use.

If you are unsure whether you are eligible to access Molpro or any
particular version of it on a NeSI cluster, please speak to your
supervisor, or the person with responsibility for your institution or
department's software procurement. Alternatively, you can contact [our
support desk](mailto:support@.nesi.org.nz).

### Licence tokens

Molpro controls access by means of licence tokens, which are special
files stored locally that, when available, make the Molpro executables
functional.

Because different people and research groups have different licence
tokens, it is necessary for you, as the user, to supply your own licence
key file whenever you run Molpro. To obtain a copy of your licence key,
contact the person responsible for the Molpro licence you are using. As
noted above, this person will normally be either your supervisor or a
procurement officer. NeSI does not provide copies of Molpro licence keys
to individual users.

Some builds of Molpro may allow for a custom path to a licence token on
the command line, using the `-k` command-line switch. See the example
script below. If this approach gives an error, you may have to create a
link to or a copy of your licence key as follows:

``` bash
mkdir ~/.molpro
# EITHER create a symbolic link to the licence key
ln -s /path/to/your/licence/key ~/.molpro/token
# OR copy the licence key
cp /path/to/your/licence/key ~/.molpro/token
```

We recommend creating a symbolic link where possible as this approach
will ensure that you automatically receive any replacement licence key
that your administrator chooses to deploy. If you create a copy instead,
you will need to update the key file manually from time to time.

If you are provided with a Molpro licence key file but cannot read the
file or access the directory in which it resides due to UNIX
permissions, please email [the NeSI support
desk](mailto:support@nesi.org.nz).

## Example Slurm script

```sl
#!/bin/bash -e

#SBATCH --job-name    Molpro_job
#SBATCH --account     nesi12345
#SBATCH --time        01:00:00
#SBATCH --mem-per-cpu 4G
#SBATCH --output      Molpro_job.%j.out # Include the job ID in the names
#SBATCH --error       Molpro_job.%j.err # of the output and error files

# EITHER a Molpro built from source
module load Molpro/mpp-2019.2.2.linux_x86_64_openmp
molpro -k /path/to/licence.key Molpro_job.inp
# OR a precompiled binary
module load Molpro/mpp-2019.2.2.linux_x86_64_openmp
molpro Molpro_job.inp
```

## Troubleshooting

This section describes some common Molpro problems and how to solve
them. It is not intended to be comprehensive, nor to serve as a
replacement for Molpro forums and mailing lists.

### Testing Molpro interactively

Sometimes, in order to study a problem and determine whether it comes
from Molpro itself or from an attempt to run parallel Molpro through our
job scheduler, it is useful to run Molpro on the command line.

To do so, you can run the following commands:

``` bash
module load Molpro/mpp-2019.2.2.linux_x86_64_openmp
# The '-v' flag means run verbosely, and the '--launcher ""' means run Molpro
# directly rather than through an MPI wrapper (that is, in serial mode)
molpro -v --launcher "" Molpro_job.inp
```

Once you have satisfied yourself that Molpro works correctly when run
locally in serial mode, you can take away the `--launcher ""` option to
test its MPI execution through the scheduler.

### The "!LICENCE! Password missing on licence token" error

This error could mean that you have a corrupt licence key file. Please
ensure that your licence key file is either an accurate copy of the
master licence key for your research group or institution, or that it is
a symbolic link to that master licence key file.

Alternatively, it could mean that you are trying to use the `-k`
command-line option with a version of Molpro that does not support it.
Please create a copy of (or symbolic link to) the applicable master
licence key file, saving your copy or link as `~/.molpro/token`, and
remove the `-k` switch and its argument from your Molpro command. See
[Licence tokens](#licence-tokens) for more details.
