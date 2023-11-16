---
created_at: '2015-10-14T22:58:53Z'
hidden: false
position: 35
tags:
- mahuika
- engineering
- general
title: MATLAB
vote_count: 1
vote_sum: 1
zendesk_article_id: 212639047
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->
!!! prerequisite No Licence?
     If you want to run MATLAB code on the cluster, but are not a member of
     an institution without access to floating licences, MATLAB code can
     still be run on the cluster using MCR.

## Example script
!!! prerequisite Note
     When developing MATLAB code on your local machine, take measures to
     ensure it will be platform independent.  Use relative paths when
     possible and not avoid using '\\s see
     [here](https://www.mathworks.com/help/matlab/ref/fullfile.html).

## Script Example

``` bash
#!/bin/bash -e
#SBATCH --job-name   MATLAB_job   # Name to appear in squeue 
#SBATCH --time       01:00:00     # Max walltime 
#SBATCH --mem        512MB        # Max memory

module load MATLAB/2021b
## Run the MATLAB script MATLAB_job.m 
matlab -nodisplay < MATLAB_job.m 
```

## Function Example

``` sl
#!/bin/bash -e
#SBATCH --job-name       MATLAB_job    # Name to appear in squeue
#SBATCH --time           06:00:00      # Max walltime
#SBATCH --mem            2048MB        # Max memory
#SBATCH --cpus-per-task  4             # 2 physical cores.
#SBATCH --output         %x.log        # Location of output log

module load MATLAB/2021b

#Job run 
matlab -batch "addpath(genpath('../parentDirectory'));myFunction(5,20)"
## For versions older than 2019a, use '-nodisplay -r' instead of '-batch'
```
!!! prerequisite Command Line
     When using matlab on command line, all flag options use a single '`-`'
     e.g. `-nodisplay`, this differs from the GNU convention of using `--`
     for command line options of more than one character.
!!! prerequisite Bash in MATLAB
     Using the prefix `!` will allow you to run bash commands from within
     MATLAB. e.g. `!squeue -u $USER` will print your currently queued slurm
     jobs.

## Parallelism

MATLAB does not support MPI therefore #SBATCH --ntasks should always be
1, but if given the necessary resources some MATLAB functions can make
use of multiple threads (--cpus-per-task) or GPUs (--gpus-per-node).

## Implicit parallelism.

Implicit parallelism requires no changes to be made in your code. By
default MATLAB will utilise multi-threading for a wide range of
operations, scalability will vary but generally you will not be able to
utilise more than a 4-8 CPUs this way.

## Explicit parallelism.

Explicit parallelism is when you write your code specifically to make
use of multiple CPU's. This can be done using MATLABs *parpool*-based
language constructs, MATLAB assigns each thread a 'worker' that can be
assigned sections of code.

MATLAB will make temporary files under your home directory (in
~/.matlab/local\_cluster\_jobs) for communication with worker processes.
To prevent simultaneous parallel MATLAB jobs from interfering with each
other you should tell them to each use their own job-specific local
directories:

``` sl
pc = parcluster('local')
pc.JobStorageLocation = getenv('TMPDIR')
parpool(pc, str2num(getenv('SLURM_CPUS_PER_TASK')))
```
!!! prerequisite Note
     Parpool will throw a warning when started due to a difference in how
     time zone is specified. To fix this, add the following line to your
     SLURM script: `export TZ="Pacific/Auckland'`

 The main ways to make use of parpool are;

**parfor: **Executes each iteration of a loop on a different worker.
e.g.

``` sl
parfor i=1:100

   %Your operation here.

end
```

`parfor` operates similarly to a SLURM job array and must be
embarrassingly parallel. Therefore all variables either need to be
defined locally (used internally within one iteration of the loop), or
static (not changing during execution of loop).

More info
[here](https://au.mathworks.com/help/parallel-computing/parfor.html).

**parfeval:**

`parfeval` is used to assign a particular function to a thread, allowing
it to be run asynchronously. e.g.

``` sl
my_coroutine=parfeval(@my_async_function,2,in1,in2);

% Do something that doesn't require outputs from 'my_async_function'

[out1, out2]=fetchOutputs(my_coroutine); % If 'my_coroutine' has not finished execution will pause.

function [out1,out2]=my_async_function(in1,in2)

%Your operation here.

end
```

`fetchOutputs` is used to retrieve the values.

More info
[here](https://au.mathworks.com/help/parallel-computing/parfeval.html).
!!! prerequisite Note
     When killed (cancelled, timeout, etc), job steps utilising parpool may
     show state `OUT_OF_MEMORY`, this is a quirk of how the steps are ended
     and not necessarily cause to raise total memory requested.

------------------------------------------------------------------------

Determining which of
[these](https://au.mathworks.com/help/parallel-computing/troubleshoot-variables-in-parfor-loops.html) categories
your variables fall under is a good place to start when attempting to
parallelise your code.
!!! prerequisite Tip
     If your code is parallel at a high level it is preferable to use
     [SLURM job
     arrays](https://support.nesi.org.nz/hc/en-gb/articles/360000690275-Parallel-Execution#t_array)
     as there is less computational overhead and the multiple smaller jobs
     will queue faster.

## Using GPUs

As with standard parallelism, some MATLAB functions will work implicitly
on GPUs while other require setup. More info on using GPUs with MATLAB
[here](https://au.mathworks.com/help/parallel-computing/run-matlab-functions-on-a-gpu.html),
and writing code for GPUs
[here](https://au.mathworks.com/hardware-support/nvidia-tesla.html).

MATLAB uses NVIDIA CUDA toolkit. Depending on the version of MATLAB, a
different version of CUDA is needed, see [GPU Support by
Release](https://nl.mathworks.com/help/releases/R2021b/parallel-computing/gpu-support-by-release.html)
in MATLAB documentation. Use `module spider CUDA` to list all available
CUDA modules and select the appropriate one. For example, for MATLAB
R2021a, use `module load CUDA/11.0.2` before launching MATLAB.

If you want to know more about how to access the different type of
available GPUs on NeSI, check the [GPU use on
NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360001471955)
support page.
!!! prerequisite Support for A100 GPUs
     To use MATLAB with a A100 or a A100-1g.5gb GPU, you need to use a
     version of MATLAB supporting the *Ampere* architecture (see [GPU
     Support by
     Release](https://nl.mathworks.com/help/releases/R2021b/parallel-computing/gpu-support-by-release.html)).
     We recommend that you use R2021a or a more recent version.
!!! prerequisite Note on GPU cost
     A GPU device-hour costs more than a core-hour, depending on the type
     of GPU. You can find a comparison table in our [What is an
     allocation?](https://support.nesi.org.nz/hc/en-gb/articles/360001385735)
     support page.

## GPU Example

``` sl
#!/bin/bash -e
#SBATCH --job-name       MATLAB_GPU    # Name to appear in squeue
#SBATCH --time           01:00:00      # Max walltime
#SBATCH --mem            10G           # 10G per GPU
#SBATCH --cpus-per-task  4             # 4 CPUs per GPU
#SBATCH --output         %x.%j.log     # Location of output log
#SBATCH --gpus-per-node  1             # Number of GPUs to use (max 2)

module load MATLAB/2021a
module load CUDA/11.0.2  # Drivers for using GPU

matlab -batch "gpuDevice()"
```

## Adding Support Packages

If you have X-11 set up you can install additional package through the
GUI. You can also install manually if you already have the files by
copying them into your Support Package root directory..

Support packages are usually saved in your home directory, you can see
the path using the MATLAB command
`matlabshared.supportpkg.getSupportPackageRoot` if it is unset, you can
specify it with
` matlabshared.supportpkg.setSupportPackageRoot("<path>")`

## mexopencv

mexopencv is [mex wrapper MATLAB wrapper for the openCV
library.](https://github.com/kyamagu/mexopencv)

Some of the internal MATLAB libraries clash with those used by OpenCV,
to avoid problems cause by this

-   Use a version of OpenCV built using GCC (as opposed to gimkl).
-   Compile using the -DWITH\_OPENCL=OFF flag.

Please contact support if you have any issues.

## Improving performance with mexing

Like other scripting languages, MATLAB code will generally run slower
than compiled code since every MATLAB instruction needs to be parsed and
interpreted. Instructions inside large MATLAB loops are often
performance hotspots due to the interpreter's overhead, which consumes
CPU time at every iteration.

Fortunately MATLAB lets programmers extend their scripts with C/C++ or
Fortran, which is referred to as
[mexing](https://au.mathworks.com/help/matlab/ref/mex.html).

more info about compiling software on NeSI
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000329015-Compiling-software-on-Mahuika).

## Writing mex functions

  This involves the following steps (using C++ as an example):

1.  Focus on a loop to extend, preferably a nested set of loops.
2.  Identify the input and output variables of the section of code to
    extend.
3.  Write C++ code. The name of the C++ file should match the name of
    the function to call from MATLAB, e.g. `myFunction.cpp` for a
    function named `myFunction`.
4.  Compile the extension using the MATLAB command `mex myFunction.cpp`

At the minimum, the C++ extension should contain:

``` sl
#include <mex.h>
#include <matrix.h>

void mexFunction(int nlhs, mxArray *plhs[],
                 int nrhs, const mxArray *prhs[]) {
    // implementation goes here
}
```

Note that the above function should always be called `mexFunction` and
its signature be
`int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]`.
Here, `nlhs` and `nrhs` refer to the number of output and input
arguments respectively. Access each dummy argument with index
`i = 0 ... nlhs-1` and `j = 0 ... nrhs-1` respectively. Regardless of
the type of argument, whether it is a number, a matrix or an object, its
type is `mxArray`. Often you will need to cast the argument into a
corresponding C++ type, e.g.

``` sl
// cast as a double, note the asterisk in front of mxGetPr
double x = (double) *mxGetPr(prhs[0]);
```

or

``` sl
// cast as an array of doubles
double* arr = (double*) mxGetPr(prhs[0]);
```

Use `mxCreateDoubleMatrix` and `mxCreateDoubleScalar` to create a matrix
and a number, respectively. For example:

``` sl
// function returns [plhs[0], plhs[1]]
plhs[0] = mxCreateDoubleMatrix(3, 2, mxREAL);  // 3 by 2 matrix
plhs[1] = mxCreateDoubleScalar(2);  // number
```

All numbers are doubles. Use flat array indexing `a[i + n*j - 1]` in C++
to access elements of a MATLAB matrix `a(i, j)` of size `n x m`.

MATLAB will take care of destroying matrices and other object so you
should feel free to create objects inside C++ code (required for
functions that have return values).

Some mex function source code examples can be found in the table
[here](https://au.mathworks.com/help/matlab/matlab_external/table-of-mex-file-source-code-files.html). 

## Compilation

MATLAB supports the following compilers.

|         |                          |
|---------|--------------------------|
| C++     | up to GCC 6.3.x          |
| C       | up to GCC 6.3.x          |
| FORTRAN | up to GNU gfortran 6.3.x |

The most up to date compilers supported by MATLAB can be loaded on NeSI
using `module load gimkl/2017a`

If no GCC module is loaded, the default system version of these
compilers will be used.

Further configuration can be done within MATLAB using the command
`mex -setup`

`mex <file_name>`  will then compile the mex function. 

Default compiler flags can be overwritten with by setting the
appropriate environment variables. The COMPFLAGS variable is ignored as
it is Windows specific.

|         |            |
|---------|------------|
| C++     | `CXXFLAGS` |
| C       | `CFLAGS`   |
| FORTRAN | `FFLAGS`   |
| Linker  | `LDFLAGS`  |

For example, adding OpenMP flags for a fortran compile:
!!! prerequisite Compiler Version Errors
     Using an 'unsupported' compiler with versions of MATLAB 2020b onward
     will result in an Error (previously was a 'Warning').

## Known Bugs

When using versions of MATLAB more recent than 2021a you may notice the
following warning.
