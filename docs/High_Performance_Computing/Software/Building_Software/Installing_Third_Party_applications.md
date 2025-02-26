---
created_at: '2018-09-24T01:51:32Z'
tags: []
title: Building_Software
vote_count: 3
vote_sum: 3
---

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
