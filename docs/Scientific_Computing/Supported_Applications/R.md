---
created_at: '2015-09-07T00:34:30Z'
hidden: false
tags:
- mahuika
- R
vote_count: 7
vote_sum: 3
zendesk_article_id: 209338087
zendesk_section_id: 360000040076
---

## Description

R is a language and environment for statistical computing and graphics.
It is a GNU project which is similar to the S language and environment,
itself developed at Bell Laboratories (formerly AT&T, now Lucent
Technologies) by John Chambers and colleagues. R can be considered as a
different implementation of S. There are some important differences, but
much code written for S runs unaltered under R.

R provides a wide variety of statistical (linear and nonlinear
modelling, classical statistical tests, time-series analysis,
classification, clustering, and so forth) and graphical techniques, and
is highly extensible. The S language is often the vehicle of choice for
research in statistical methodology, and R provides an Open Source route
to participation in that activity.

## Licence

R is made available at no cost under the terms of version 2 of the [GNU
General Public Licence](https://www.r-project.org/COPYING).

## NeSI Customisations

- We patch the *snow* package so that there is no need to use RMPISNOW
  when using it over MPI.
- Our most recent R environment modules set R\_LIBS\_USER to a path
  which includes the compiler toolchain, so for
  example *~/R/gimkl-2022a/4.2* rather than the usual default
  of *~/R/x86\_64-pc-linux-gnu-library/4.2*.

## Available Modules

### R Base

{% set app_name = "R" -%}
{% include "partials/app/app_version.html" -%}

We also have some environment modules which extend the base R ones with
extra packages:

### R-Geo

Includes rgeos, rgdal and other geometric and geospatial
packages based on the libraries GEOS, GDAL, PROJ and UDUNITS.

{% set app_name = "R-Geo" -%}
{% include "partials/app/app_version.html" -%}

### R-bundle-Bioconductor

Includes many of the BioConductor suite of
packages.

{% set app_name = "R-bundle-Bioconductor" -%}
{% include "partials/app/app_version.html" -%}

## Example R scripts

=== "Serial"

    ``` R
    png(filename="plot.png")  # This line redirects plots from screen to plot.png file.

    # Define the cars vector with 5 values
    cars <- c(1, 3, 6, 4, 9)

    # Graph the cars vector with all defaults
    plot(cars)
    ```

=== "Array"

    ``` R
    jobid <- as.numeric(Sys.getenv("SLURM_ARRAY_TASK_ID"))
    jobid
    ```

=== "Parallel with 'doParallel'"

    The following example sums 50 normally distributed random value vectors
    of sizes 1 million to 1000050. Set the number of workers in your
    submission script with `--cpus-per-task=`... Note that all workers run on
    the same node. Hence, the number of workers is limited to the number of
    cores (physical if --hint=nomultithread or logical if using
    `--hint=multithread`).

    ``` R
    library(doParallel)
    registerDoParallel(strtoi(Sys.getenv("SLURM_CPUS_PER_TASK")))

    # 50 calculations, store the result in 'x'
    x <- foreach(z = 1000000:1000050, .combine = 'c') %dopar% {
      sum(rnorm(z))
    }

    print(x)
    ```

=== "Parallel with 'doMPI'"

    This example is similar to the above except that workers can run across
    multiple nodes. Note that we don't need to specify the number of workers
    when starting the cluster -- it will be derived by the mpiexec command,
    which slurm will invoke. You will need to load the gimkl module to
    expose the MPI library.

    ``` R
    library(doMPI, quiet=TRUE)
    cl <- startMPIcluster()
    registerDoMPI(cl)

    # 50 calculations, store the result in 'x'
    x <- foreach(z = 1000000:1000050, .combine = 'c') %dopar% {
      sum(rnorm(z))
    }

    closeCluster(cl)
    print(x)
    mpi.quit()
    ```

=== "Parallel with 'snow'"

    ``` R
    library(snow)
    # If there are multiple tasks only one reaches here, others become slaves.

    # Select MPI-based or fork-based parallelism depending on ntasks
    if(strtoi(Sys.getenv("SLURM_NTASKS")) > 1) {
        cl <- makeMPIcluster()
    } else {
        cl <- makeSOCKcluster(max(strtoi(Sys.getenv('SLURM_CPUS_PER_TASK')), 1))
    }

    # 50 calculations to be done:
    x <- clusterApply(cl, 1000000:1000050, function(z) sum(rnorm(z)))

    stopCluster(cl)
    ```

## Example Slurm Scripts

=== "Serial"

    ``` sl
    #!/bin/bash -e

    #SBATCH --job-name    MySerialRJob
    #SBATCH --time        01:00:00
    #SBATCH --mem         512MB
    #SBATCH --output      MySerialRJob.%j.out # Include the job ID in the names of
    #SBATCH --error       MySerialRJob.%j.err # the output and error files

    module load 4.2.1-gimkl-2022a

    # Help R to flush errors and show overall job progress by printing
    # "executing" and "finished" statements.
    echo "Executing R ..."
    srun Rscript MySerialRJob.R
    echo "R finished."
    ```

=== "Array"

    ``` sl
    #!/bin/bash -e

    #SBATCH --job-name    MyArrayRJob
    #SBATCH --time        01:00:00
    #SBATCH --array       1-10
    #SBATCH --mem         512MB
    #SBATCH --output      MyArrayRJob.%j.out # Include the job ID in the names of
    #SBATCH --error       MyArrayRJob.%j.err # the output and error files

    module load R/4.2.1-gimkl-2022a

    # Help R to flush errors and show overall job progress by printing
    # "executing" and "finished" statements.
    echo "Executing R ..."
    srun Rscript MyArrayRJob.R
    echo "R finished."
    ```

=== "Parallel with MPI"

    ``` sl
    #!/bin/bash -e

    #SBATCH --job-name      MyMPIRJob
    #SBATCH --time          01:00:00
    #SBATCH --ntasks        12
    #SBATCH --cpus-per-task 1
    #SBATCH --mem-per-cpu   512MB
    #SBATCH --output        MyMPIRJob.%j.out # Include the job ID in the names of
    #SBATCH --error         MyMPIRJob.%j.err # the output and error files

    module load R/4.2.1-gimkl-2022a
    # need MPI
    module load gimkl/2022a

    # Help R to flush errors and show overall job progress by printing
    # "executing" and "finished" statements.
    echo "Executing R ..."
    # Our R has a patched copy of the snow library so that there is no need to use
    # RMPISNOW.
    srun Rscript doMPI
    echo "R finished."
    ```

## Generating images and plots

Normally when plotting or generating other sorts of images, R expects a
graphical user interface to be available so it can render and display
the image on the fly. However, it is possible to instruct R to export
the image directly to a file instead of displaying it on the screen,
using code like the following:

``` R
png(filename="plot.png")
```

This statement instructs R to export all future graphical output to a
PNG file named `plot.png`, until a different device driver is selected.

For more information about graphical device drivers, please see [the R
documentation](https://cran.r-project.org/doc/manuals/R-intro.html#Device-drivers).

## Dealing with packages

Much R functionality is not supplied with the base installation, but is
instead added by means of packages written by the R developers or by
third parties.  We include a large number of such R packages in our R
environment modules.

### Getting a list of installed packages

It is best to view the list of available R packages interactively. To do
so, call up the package library:

``` sh
module R/4.2.1-gimkl-2022a
R
```

```r
library()
```

or just use the module command:

``` sh
module show R/4.2.1-gimkl-2022a
```

Please note that different installations of R, even on the same NeSI
cluster, may contain different collections of packages. Furthermore, if
you have your own packages in a directory that R can automatically
detect, these will also be shown in a separate section.

### Getting a list of available libraries

You can print a list of the library directories in which R will look for
packages by running the following command in an R session:

``` R
.libPaths()
```

For R/4.2.1 the command `.libPaths()` will return the following:

``` R
.libPaths()
```

```stdout
[1] "/home/YOUR_USER_NAME/R/gimkl-2022a/4.2"                            
[2] "/opt/nesi/CS400_centos7_bdw/R/4.2.1-gimkl-2022a/lib64/R/library"
```

When using the `library()` function R will first look to your
Home/Personal library for the package and then to the Systems Library
provided by NeSI. This can be used in conjuction with
`installed.packages()` to see what is available in a specific library.
eg:

``` R
installed.packages("/home/YOUR_USER_NAME/R/gimkl-2022a/4.2")
...
ggplot2 NA NA NA "no" "4.2.1"
ggrepel NA NA NA "yes" "4.2.1"
etc...
```

### Specifying custom library directories

You can add your own custom library directories by putting a list of
extra directories in the `.Renviron` file in your home directory. This
list should look like the following:

```sh
export R_LIBS=/home/jblo123/R/foo:/home/jblo123/R/bar
```

Note that, of the contents of the `R_LIBS` variable, only those
directories that actually exist will show up in the output of
`.libPaths()`.

Alternatively, you can specify in your R script:

``` R
dir.create("/nesi/project/<projectID>/Rpackages", showWarnings = FALSE, recursive = TRUE)
.libPaths(new="/nesi/project/<projectID>/Rpackages")
```

### Downloading and installing a new package

To install a package into R, use the install.packages command.

For example, to install the sampling package:

``` sh
module load R/4.2.1-gimkl-2022a
R
```

```R
install.packages("sampling")
```

You will most likely be asked if you want to use a personal library and,
if you have not previously done so, whether you wish to create a new
personal library. Answer "y" to both questions.

Enter the number for one of the Australian sites from the list of
download mirrors that will appear, as the lone New Zealand mirror site
is more often out of date.

R will then download, compile and install the new package for you.

You can confirm the package has been installed by using the `library()`
command:

``` R
library("foo")
```

If the package has been correctly installed, you will get no response.
On the other hand, if the package is missing or was not installed
correctly, an error message will typically be returned:

``` R
library("foo")
```

```stderr
Error in library("foo") : there is no package called ‘foo’
```

### Compiling a C library for use with R

You can compile custom C libraries for use with R using the R shared
library compiler:

``` sh
module load R/4.2.1-gimkl-2022a
R CMD SHLIB mylib.c
```

This will create the shared object mylib.so. You can then reference the
library in your R script:

``` sh
R
```

```R
dyn.load("~/R/lib64/mylib.so")
```

## Quitting an interactive R session

At the R command prompt, when you want to quit R, type the following:

```r
quit()
```

You will be asked "Save workspace image? \[y/n/c\]". Type n.

## Troubleshooting

### Missing *devtools*

Package installation will occasionally fail due to missing system
libraries (eg *HarfBuzz, FriBidi or devtools)*, this is resolved by
loading the *devtools* module prior to the version of R you require.

``` sh
module load devtools
module load R/4.2.1-gimkl-2022a
```

### Can't install *sf, rgdal* etc

Use the R-Geo module

``` sh
module load R-Geo/4.2.1-gimkl-2022a
```

### Cluster/Parallel environment variable not accessed

Depending on the working environment, registering of a cluster and
accessing the `SLURM_CPUS_PER_TASK` environment variable may not return
an integer, in particular the function `strtoi` (string to integer)
doesn't work correctly. Instead use `as.numeric`

Options:

- `strtoi(Sys.getenv("SLURM_CPUS_PER_TASK"))`
- `as.numeric(Sys.getenv("SLURM_CPUS_PER_TASK"))`
