---
created_at: '2018-09-24T01:51:32Z'
tags: []
title: Installing (Third Party) applications
vote_count: 3
vote_sum: 3
zendesk_article_id: 360000474535
zendesk_section_id: 360000040056
---

NeSI provides a long list of various applications on its systems.
Nevertheless, if you need additional applications or libraries (below
called package), we distinguish:

- you need a **newer version** of an already installed package:  {% include "partials/support_request.html" %} for
    an update
- you need an **older version** of an installed package: please use
    the Easybuild installation procedure (below) to install it into your
    working space
- you want to test a **new (not installed)** package: below we
    collected some hints, how you can install it in your user space.

In any case, if you have issues, do not hesitate to {% include "partials/support_request.html" %}.

## Additional Packages for Python, R, etc.

See [Python](../Supported_Applications/Python.md) or [R](../Supported_Applications/R.md),
or for other languages check if we have additional documentation for it
in our [application documentation](./../Supported_Applications/index.md).

## Third party applications

Installation instruction vary from application to application. In any
case we suggest to read the provided installing instructions.
Nevertheless, the following should give you an impression which steps
you usually need to consider:

- Change into a desired source code directory. We suggest to use
    `/nesi/nobackup/<projectID>` or `/nesi/project/<projectID>`
- download the source code. This could be done via a repository
    checkout (`git clone <URL to the application source repository>`) or
    via downloading a tarball (`wget <URL to the tarball>`). Unpack the
    tarball using `tar xf <tar file name>`. Change into source
    directory.
- load compiler module and modules for additional libraries
    (`module load gimkl FFTW`)
- run the configure with appropriate options
    `./configure --prefix=<desired install directory> --use-fftw=$EBROOTFFTW  `(options
    can be listed using `./configure --help`)
- In other applications you need to adjust the provided `Makefile` to
    reflect compiler, and library options (see below)
- compile code (`make`)
- install the binaries and libraries into the specified directory
    (`make install`)

## Create your own modules (Optional)

You can create personalised module environments, which can load modules
and set up environment variables. For example, you could define a
modules in a project directory
`/nesi/project/<projectID>/modulefiles/ProdXY` as the following:

In the first lines, we can set conflicts with other modules (here named
ProdABC). Then we load some dependency modules and provide some
description. The additional lines depend on your requirements for the
module. With *set* you can define internal variables (within this module
file). The command *setenv* defines a environment variable. And
*prepend-path* and *append-path* extend an environment variable at the
front or end.

There are common environment variables like:

- *PATH* for providing executabl,
- *LD\_LIBRARY\_PATH* for self created libraries,
- *PYTHONPATH* for providing Python modules,
- *CONDA\_ENVS\_PATH* for providing Conda environments,
- etc.

And others which are very application specific.

To use the module (or all in that directory and sub-directories) we need
to register that directory to the module environment. This can be done
by setting the following environment variable:

by adding that line to your `$HOME/.bashrc` you will have the modules
always available.

The module then can be loaded by:

These modules can easily be shared with collaborators. They just need to
specify the last two steps.
