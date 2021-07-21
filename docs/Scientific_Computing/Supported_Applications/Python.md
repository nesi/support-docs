All versions of Python available on NeSI platforms are owned and
licensed by the Python Software Foundation. Each version is released
under a specific open-source licence. The licences are available on [the
Python documentation server](https://docs.python.org).

System Python vs Environment Modules
====================================

Our operating systems include Python but not an up to date version, so
we strongly recommend that you load one of our Python environment
modules instead.  They include optimised builds of the most popular
Python packages for computational work such as numpy, scipy, matplotlib,
and many more.

Example scripts
===============

    #!/bin/bash -e

    #SBATCH --job-name    MyPythonJob
    #SBATCH --time        01:00:00
    #SBATCH --mem         512MB

    module load Python/3.7.3-gimkl-2018b

    python MyPythonScript.py

### MPI Example

      #!/bin/bash -e
      #SBATCH --job-name=PythonMPI
      #SBATCH --ntasks=2          # Number of MPI tasks
      #SBATCH --time=00:30:00
      #SBATCH --mem-per-cpu=512MB # Memory per logical CPU

      module load Python
      srun python PythonMPI.py   # Executes ntasks copies of the script

    import numpy as np
    from mpi4py import MPI

    comm = MPI.COMM_WORLD
    size = comm.Get_size() # Total number of MPI tasks
    rank = comm.Get_rank() # Rank of this MPI task

    # Calculate the data (numbers 0-9) on the MPI ranks
    rank_data = np.arange(rank, 10, size)

    # perform some operation on the ranks data
    rank_data += 1

    # gather the data back to rank 0
    data_gather = comm.gather(rank_data, root = 0)

    # on rank 0 sum the gathered data and print both the sum of, 
    # and the unsummed data
    if rank == 0:
        print('Gathered data:', data_gather)
        print('Sum:', sum(data_gather))

The above Python script will create a list of numbers (0-9) split
between the MPI tasks (ranks). Each task will then add one to the
numbers it has, those numbers will then be gathered back to task 0,
where the numbers will be summed and both the sum of, and the unsummed
data is printed.

### Multiprocessing Example

      #!/bin/bash -e
      #SBATCH --job-name=PytonMultiprocessing
      #SBATCH --cpus-per-task=2   # Number of logical CPUs
      #SBATCH --time=00:10:00
      #SBATCH --mem-per-cpu=512MB # Memory per logical CPU

      module load Python
      python PythonMultiprocessing.py

    import multiprocessing

    def calc_square(numbers, result1):
        for idx, n in enumerate(numbers):
            result1[idx] = n*n

    def calc_cube(numbers, result2):
        for idx, n in enumerate(numbers):
            result2[idx] = n*n*n

    if __name__ == "__main__":
        numbers = [2,3,4]
        # Sets up the shared memory variables, allowing the variables to be
        # accessed globally across processes
        result1 = multiprocessing.Array('i',3)
        result2 = multiprocessing.Array('i',3)
        # set up the processes
        p1 = multiprocessing.Process(target=calc_square, args=(numbers,result1,))
        p2 = multiprocessing.Process(target=calc_cube, args=(numbers,result2,))

        # start the processes
        p1.start()
        p2.start()

        # end the processes
        p1.join()
        p2.join()

        print(result1[:])
        print(result2[:])

The above Python script will calculated the square and cube of an array
of numbers using multiprocessing and print the results from outside of
those processes, safely circumventing Python\'s [global interpreter
lock](https://wiki.python.org/moin/GlobalInterpreterLock).

For more in depth examples of and descriptions of Multiprocessing in
Python you may find [this Multithreading/Multiprocessing Youtube
tutorial
series](https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=1)
helpful

### Job Arrays

Job arrays can be handled using the Slurm environment variable
`SLURM_ARRAY_TASK_ID` as array index. This index can be called directly
from within the script or using a command line argument. In the
following both options are presented:

The job scripts calling both examples:

    #!/bin/bash -e
    #SBATCH -J test
    #SBATCH --time=00:01:00
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --array=1-2 # Array jobs

    module load Anaconda3

    echo "SLURM_ARRAY_TASK_ID $SLURM_ARRAY_TASK_ID of $SLURM_ARRAY_TASK_COUNT"

    #env variable in python
    python hello_world.py

    #as command line argument
    python hello_world_args.py -ID $SLURM_ARRAY_TASK_ID

the version getting the env variable in the python script
\"hello\_world.py\"

    #!/usr/bin/env python3

    import os
    my_id = os.environ['SLURM_ARRAY_TASK_ID']
    print("hello world with ID {}".format(my_id))

the version getting the env variable as argument in the python script
\"hello\_world\_args.py\"

    #!/usr/bin/env python3
    """
    Module for handling input arguments
    """

    import argparse

    # get tests from file
    class LoadFromFile(argparse.Action):
        """
        class for reading arguments from file
        """
        def __call__(self, parser, namespace, values, option_string=None):
            with values as F:
                vals = F.read().split()
            setattr(namespace, self.dest, vals)

    def get_args():
        """
        Definition of the input arguments
        """
        parser = argparse.ArgumentParser(description='Hello World')
        parser.add_argument('-ID', type=int, action='store', dest='my_id',
                            help='Slurm ID')
        return parser.parse_args()


    ARGS = get_args()
    print("hello world from ID {}".format(ARGS.my_id))

Python Packages
===============

Programmers around the world have written and released many packages for
Python, which are not included with the core Python distribution and
must be installed separately. Each Python environment module comes with
its own particular suite of packages, and the system Python has its own
installed packages.

The provided packages can be listed using

    module load Python
    python -c "help('modules')"

Adding packages
---------------

Additional packages can be requested via a NeSI support ticket if there
is wider need for it. If you just need it for your self or want to
provide additional packages for your project group, you can install it
using the following methods:

-   [pip install \--user in your
    `$HOME`](#h_749d9d04-30f7-41fe-8721-87b9205e1df3)
-   [pip install into your project
    directory](#h_e39fabff-952d-4fa3-8fa5-b2ff1d2990f7)
-   using and virtual environment

### Install into your `$HOME` {#h_749d9d04-30f7-41fe-8721-87b9205e1df3}

This is the simplest way to install additional packages, but you might
fill your `$HOME` quota and cannot share installations with
collaborators.

A packages prodXY can be installed using:

    pip install --user prodXY

### Install into project directory

This method is slightly more complicated, but provides the advantage
that you do not fill up your `$HOME`  directory quota and you can easily
share these installed packages with your collaborators. This method
requires:

-   installing Python package into a \"remote\" location (your project
    directory
-   define the `$PATH` and `$PYTHONPATH` in your environment (e.g. using
    a module file)

In the following we install a python3 package called  *`prodXY`* into
`/nesi/project/<projectID>/PyPackages` and create a module for it.

#### Using Easybuild

Easybuild is a Package provisioning tool, please read also
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000474535).
Therefore you need a configuration file, e.g. for PyPI python packages
(here cutadapt), which could be located in
`/nesi/project/<projectID>/easybuildinstall/easyconfigs` and the
following would be named as `cutadapt-2.3-gimkl-2018b-Python-3.7.3.eb`:

    # Easybuild Python package template
    # Author: Mandes Schoenherr
    # NeSI - the New Zealand eScience Infrastructure

    easyblock = "PythonPackage"

    name = 'cutadapt' ### specify the name here
    version = '2.3' ### specify the version

    homepage = 'https://cutadapt.readthedocs.io/' ### add a reference URL and a description below
    description = """ cutadapt removes adapter sequences
     from high-throughput sequencing data. """

    toolchain = {'name':'gimkl', 'version':'2018b'}
    source_urls = [PYPI_SOURCE]
    sources = [SOURCELOWER_TAR_GZ]

    python = 'Python'
    pyver = "3.7.3"
    pyshortver = '.'.join(pyver.split('.')[:2])
    versionsuffix = "-%s-%s" % (python, pyver)
    dependencies = [ (python, pyver) ]
    sanity_check_paths = {
     'files': ['bin/cutadapt'],
     'dirs': ['lib/python%s/site-packages/' % pyshortver],
    }

    moduleclass = 'bio' ### change the type of software

Then we can install this package using:

    export NESI_EASYBUILD_PROJECT_ID=<projectID>
    module load project
    eb cutadpt-2.3-gimkl-2018b-Python-3.7.3.eb

### After successful install we should see the module using:

    module --ignore-cache avail cutadapt

And the package can be used by all project members (after specifying the
projectID) using:

    module load project
    module load cutadapt

#### Manual install and provisioning

Depending on the package you can install packages using:

-   the Python Package Manager PIP

<!-- -->

    $ pip install --prefix /nesi/project/<projectID>/PyPackages cogent

-   use source code

<!-- -->

    $ python setup.py install --prefix /nesi/project/<projectID>/PyPackages

 Python will not find the package by default, therefore you need to add
the location of the package to the `$PYTHONPATH`. Furthermore, some
packages provide binaries, which are accessible by adding the directory
to `$PATH `

    $ export PYTHONPATH=/nesi/project/<projectID>/PyPackages/lib/python3.6/site-packages:$PYTHONPATH
    $ export PATH=/nesi/project/<projectID>/PyPackages/bin:$PATH

NOTE: If you install multiple packages in the same location, e.g.
`/nesi/project/<projectID>/PyPackages`, you just need to set these
environment variable once.

#### Creating a modulefile

These environment variables can be handled in a module file. Thus the
packages (and others if desired) can be accessed by you and the project
collaborators.

Therefore we create a modulefile let\'s say at
`/nesi/project/<projectID>/modulefiles/PyXtra` and assume we installed a
Python package into `/nesi/project/<projectID>/PyPackages`:

    #%module
    module load Python/3.7.3-gimkl-2018b
       # provide a description
    whatis "The packageXY for python."
    proc ModulesHelp { } {  puts stderr "This module loads the packageXY. It requires python3." }

    set PKG_PREFIX /nesi/project/<projectID>/PyPackages
       # add the location of binaries to PATH, such they are immediately accessible
    prepend-path PATH $PKG_PREFIX/bin
       # add to PYTHONPATH to access python packages
    prepend-path PYTHONPATH $PKG_PREFIX/lib/python3.7/site-packages/

To use this module (and all other modules you create in that directory)
you add the following to your `$HOME/.bashrc` (need to `source` it, or
re-login to activate the changes):

    module use /nesi/project/<projectID>/modulefiles

Then you can simple load the module via:

    module load PyXtra

 

Further notes
=============

iPython
-------

iPython (*i*nteractive *Python*) is an enhanced tool for accessing a
Python command line. It is available in many NeSI Python modules.

### Starting iPython

To open an iPython console, simply run the `ipython` command:

    [jblo123@build-wm ~]$ module load Python/3.6.3-gimkl-2017a
    [jblo123@build-wm ~]$ ipython

### Listing available functions

You can use iPython to list the functions available that start with a
given string. Please note that if the string denotes a module (i.e., it
has a full stop somewhere in it), that module (or the function you want
from it) must first be imported, using either an \"import X\" statement
or a \"from X import Y\" statement.

    import os
    os.<TAB>   # List all functions in the os module
    os.O_<TAB> # List functions starting with "O_" from the os module
    len<TAB>   # List functions starting with "len"

Here,

    o<TAB>

or even

    os<TAB>

and expect to see the methods and values provided by the os module - you
have to put the full stop after the \"os\" if you want to do that.

### Getting information about an object

In iPython, you can query any object by typing the object name followed
by a question mark (?), then hitting Enter. For instance:

    In [1]: x = 5
    In [2]: x?
    Type:        int
    String form: 5
    Docstring:
    int(x=0) -> int or long
    int(x, base=10) -> int or long

    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is floating point, the conversion truncates towards zero.
    If x is outside the integer range, the function returns a long instead.

    If x is not a number or if base is given, then x must be a string or
    Unicode object representing an integer literal in the given base.  The
    literal can be preceded by '+' or '-' and be surrounded by whitespace.
    The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
    interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4

You can also do this on functions (`len?`), methods (`os.mkdir?`) and
modules (`os.path?`). If you try to do it on something that isn\'t
defined yet, Python will tell you that the object in question couldn\'t
be found.

### Quitting iPython

Just enter the `quit` command at the iPython prompt.
