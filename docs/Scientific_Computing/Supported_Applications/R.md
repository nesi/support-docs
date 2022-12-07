Description
===========

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

The R home page is at <http://www.r-project.org>.

Licence
=======

R is made available at no cost under the terms of version 2 of the GNU
General Public Licence. The full text of the R licence is available at
<https://www.r-project.org/COPYING>.

NeSI Customisations {#available-modules}
===================

-   We patch the *snow* package so that there is no need to use RMPISNOW
    when using it over MPI.
-   Our most recent R environment modules set R\_LIBS\_USER to a path
    which includes the compiler toolchain, so for
    example *\~/R/gimkl-2020a/4.1 *rather than the usual default
    of *\~/R/x86\_64-pc-linux-gnu-library/4.1*.

Related environment modules
===========================

We also have some environment modules which extend the base R ones with
extra packages:

-    *R-Geo* with rgeos, rgdal and other geometric and geospatial
    packages based on the libraries GEOS, GDAL, PROJ and UDUNITS.
-   *R-bundle-BioConductor* with many of the BioConductor suite of
    packages.

Example scripts
===============

Example R scripts
-----------------

### Example serial R script

    png(filename="plot.png")  # This line redirects plots from screen to plot.png file.

    # Define the cars vector with 5 values
    cars <- c(1, 3, 6, 4, 9)

    # Graph the cars vector with all defaults
    plot(cars)

### Example array R script

    jobid = as.numeric(Sys.getenv("SLURM_ARRAY_TASK_ID"))
    jobid

### Example parallel script using *doParallel*

    library(doParallel)
    registerDoParallel(strtoi(Sys.getenv('SLURM_CPUS_PER_TASK')))

    # 50 calculations to be done:
    foreach(z=1000000:1000050) %dopar% {
      x <- sum(rnorm(z))
    }

### Example parallel script using *doMPI*

    library(doMPI, quiet=TRUE)
    cl <- startMPIcluster()
    registerDoMPI(cl)

    # 50 calculations to be done:
    foreach(z=1000000:1000050) %dopar% {
      x <- sum(rnorm(z))
    }

    closeCluster(cl)
    mpi.quit()

### Example parallel script using *snow*

    library(snow)
    # If there are multiple tasks only one reaches here, others become slaves.

    # Select MPI-based or fork-based parallelism depending on ntasks
    if (strtoi(Sys.getenv('SLURM_NTASKS')) > 1) {
        cl <- makeMPICluster()
    } else {
        cl <- makeSOCKCluster(max(strtoi(Sys.getenv('SLURM_CPUS_PER_TASK')), 1))
    }

    # 50 calculations to be done:
    x <- clusterApply(cl, 1000000:1000050, function(z) sum(rnorm(z)))

    stopCluster(cl)

Example job submission scripts {#example-job-submission-scripts-for-the-pan-cluster}
------------------------------

### Example job submission script for a serial R job {#example-job-submission-script-for-a-serial-r-job-on-the-pan-cluster}

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

### Example job submission script for an array R job {#example-job-submission-script-for-an-array-r-job-on-the-pan-cluster}

    #!/bin/bash -e

    #SBATCH --job-name    MyArrayRJob
    #SBATCH --time        01:00:00
    #SBATCH --array       1-10
    #SBATCH --mem         512MB
    #SBATCH --output      MyArrayRJob.%j.out # Include the job ID in the names of
    #SBATCH --error       MyArrayRJob.%j.err # the output and error files

    module load R/4.0.1-gimkl-2020a

    # Help R to flush errors and show overall job progress by printing
    # "executing" and "finished" statements.
    echo "Executing R ..."
    srun Rscript MyArrayRJob.R
    echo "R finished."

### Example job submission script for an MPI R job {#example-job-submission-script-for-an-mpi-r-job-on-the-pan-cluster}

    #!/bin/bash -e

    #SBATCH --job-name      MyMPIRJob
    #SBATCH --time          01:00:00
    #SBATCH --ntasks        12
    #SBATCH --cpus-per-task 1
    #SBATCH --mem-per-cpu   512MB
    #SBATCH --output        MyMPIRJob.%j.out # Include the job ID in the names of
    #SBATCH --error         MyMPIRJob.%j.err # the output and error files

    module load R/4.0.1-gimkl-2020a

    # Help R to flush errors and show overall job progress by printing
    # "executing" and "finished" statements.
    echo "Executing R ..."
    # Our R has a patched copy of the snow library so that there is no need to use
    # RMPISNOW.
    srun Rscript doMPI
    echo "R finished."

Further notes
=============

Generating images and plots
---------------------------

Normally when plotting or generating other sorts of images, R expects a
graphical user interface to be available so it can render and display
the image on the fly. However, it is possible to instruct R to export
the image directly to a file instead of displaying it on the screen,
using code like the following:

    png(filename="plot.png")

This statement instructs R to export all future graphical output to a
PNG file named `plot.png`, until a different device driver is selected.

For more information about graphical device drivers, please see [the R
documentation](https://cran.r-project.org/doc/manuals/R-intro.html#Device-drivers).

Dealing with packages
---------------------

Much R functionality is not supplied with the base installation, but is
instead added by means of packages written by the R developers or by
third parties.  We include a large number of such R packages in our R
environment modules

### Getting a list of installed packages {#getting-a-list-of-available-packages}

It is best to view the list of available R packages interactively. To do
so, call up the package library:

    $ 
    $ module load R/4.0.1-gimkl-2020a
    $ R
    ...
    > library()

or just use the module command:

    $ module show R/4.0.1-gimkl-2020a

Please note that different installations of R, even on the same NeSI
cluster, may contain different collections of packages. Furthermore, if
you have your own packages in a directory that R can automatically
detect, these will also be shown in a separate section.

### Getting a list of available libraries

You can print a list of the library directories in which R will look for
packages by running the following command:

    > .libPaths()

### Specifying custom library directories

You can add your own custom library directories by putting a list of
extra directories in the `.Renviron` file in your home directory. This
list should look like the following:

    export R_LIBS=/home/jblo123/R/foo:/home/jblo123/R/bar

Note that, of the contents of the `R_LIBS` variable, only those
directories that actually exist will show up in the output of
`.libPaths()`.

Alternatively, you can specify in your R script:

    dir.create('/nesi/project/<projectID>/Rpackages', showWarnings = FALSE, recursive = TRUE)
    .libPaths(new='/nesi/project/<projectID>/Rpackages')

 

### Downloading and installing a new package

To install a package into R, use the install.packages command.

For example, to install the sampling package:

    $ module load R/4.0.1-gimkl-2020a
    $ R
    ...
    > install.packages("sampling")

You will most likely be asked if you want to use a personal library and,
if you have not previously done so, whether you wish to create a new
personal library. Answer \"y\" to both questions.

Enter the number for one of the Australian sites from the list of
download mirrors that will appear, as the lone New Zealand mirror site
is more often out of date.

R will then download, compile and install the new package for you.

You can confirm the package has been installed by using the library()
command:

    > library("sampling")

If the package has been correctly installed, you will get no response.
On the other hand, if the package is missing or was not installed
correctly, an error message will typically be returned:

    > library("foo")
    Error in library("foo") : there is no package called ‘foo’

### Compiling a C library for use with R

You can compile custom C libraries for use with R using the R shared
library compiler:

    $ module load R/4.0.1-gimkl-2020a
    $ R CMD SHLIB mylib.c

This will create the shared object mylib.so. You can then reference the
library in your R script:

    $ R
    ...
    > dyn.load("~/R/lib64/mylib.so")

Quitting an interactive R session
---------------------------------

At the R command prompt, when you want to quit R, type the following:

    > quit()

You will be asked \"Save workspace image? \[y/n/c\]\". Type n.
