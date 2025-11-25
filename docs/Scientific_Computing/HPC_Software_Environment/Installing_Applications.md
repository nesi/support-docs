---
created_at: '2018-09-24T01:51:32Z'
tags: 
  - software
title: Installing Applications
---

Before installing your own applications, first check;

- The software you want it is not already installed. `module spider <appname>` can be used to search software, or see [Supported Applications](../Supported_Applications/index.md).
- If you are looking for a new version of existing software,
{% include "partials/support_request.html" %} and we will install the new version.
- If you would like us to install something for you or help you install something yourself {% include "partials/support_request.html" %}. If the software popular, We may decide to install it centrally, in which case there will be no additional steps for you. Otherwise the software will be installed in your project directory, in which case it is your responsibility to maintain.

In any case, if you have issues, do not hesitate to {% include "partials/support_request.html" %}.

## Packages for Existing Module

How to add package to an existing module will vary based on the language in question.

See [Python](../Supported_Applications/Python.md)
or [R](../Supported_Applications/R.md),
or for other languages check if we have additional documentation for it
in our [application documentation](../Supported_Applications/index.md).

## Other Applications

Installation instruction vary from application to application. In any
case we suggest to read the provided installing instructions.
Nevertheless, the following should give you an impression which steps
you usually need to consider:

### Install Directory

You will need to decide on where you want to install you application.
We recommend using your `project` directory i.e `/nesi/project/<projectID>`,
that way the install can be easily shared with any collaborators.
Move to the desired location and create a directory to work from `mkdir <appname>`.

### Download

Downloading the code can be done in various ways.

- Checkout a git repo `git clone <URL>`
- Downloading a tarball (`wget <URL>.tgz`). Unpack the tarball using the command `tar -xf <downloaded file>.tgz`.

### Load Dependencies

You will probably want to build your application against some of the existing NeSI software stack.
Almost certainly, this will include a toolchain.

```sh
module load foss
```

Make sure to take a note of the modules used when installing,
as there is a high chance you will need them to be loaded at runtime.

- run the configure with appropriate options
    `./configure --prefix=<desired install directory> --use-fftw=$EBROOTFFTW `(options
    can be listed using `./configure --help`)
- In other applications you need to adjust the provided `Makefile` to
    reflect compiler, and library options (see below)
- compile code (`make`)
- install the binaries and libraries into the specified directory
    (`make install`)

### Add to Path

To run your newly installed application, the process may look something like,

```sh
module load foss/{{application["foss"].latest}} FFTW
/nesi/project/nesi99991/myApplication/bin/launchApplication
```

You may want to add the newly installed application to path.
