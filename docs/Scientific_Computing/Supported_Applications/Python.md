---
created_at: '2015-08-18T05:16:01Z'
hidden: false
position: 44
tags:
- ml
- language
title: Python
vote_count: 0
vote_sum: 0
zendesk_article_id: 207782537
zendesk_section_id: 360000040076
---

All versions of Python available on NeSI platforms are owned and
licensed by the Python Software Foundation. Each version is released
under a specific open-source licence. The licences are available on [the
Python documentation server](https://docs.python.org).

## System Python vs Environment Modules

Our operating systems include Python but not an up to date version, so
we strongly recommend that you load one of our Python environment
modules instead.  They include optimised builds of the most popular
Python packages for computational work such as *numpy*, *scipy*,
*matplotlib*, and many more.

### NeSI Customisations

Our most recent Python environment modules have:

- `multiprocessing.cpu_count()` patched to return only the number of
    CPUs available to the process, which in a Slurm job can be fewer
    than the number of CPUs on the node.

- `PYTHONUSERBASE` set to a path which includes the toolchain, so that
    incompatible builds of the same version of Python don't attempt to
    share user-installed libraries.

## Example scripts

=== "Serial Job"

    ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name    Python_Serial
    #SBATCH --time        01:00:00
    #SBATCH --mem         512MB
    
    module load Python/{{applications.Python.machines.mahuika.versions | last}}
    
    python MyPythonScript.py
    ```

=== "Distributed Memory Job"

    ```sl
    #!/bin/bash -e
    #SBATCH --job-name=PythonMPI
    #SBATCH --ntasks=2          # Number of MPI tasks
    #SBATCH --time=00:30:00
    #SBATCH --mem-per-cpu=512MB # Memory per logical CPU
    
    module load Python
    srun python PythonMPI.py   # Executes ntasks copies of the script
    ```

    ```py
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
    ```

    The above Python script will create a list of numbers (0-9) split
    between the MPI tasks (ranks). Each task will then add one to the
    numbers it has, those numbers will then be gathered back to task 0,
    where the numbers will be summed and both the sum of, and the unsummed
    data is printed.

=== "Shared Memory Example"

    ``` sl
      #!/bin/bash -e
      #SBATCH --job-name=PytonMultiprocessing
      #SBATCH --cpus-per-task=2   # Number of logical CPUs
      #SBATCH --time=00:10:00
      #SBATCH --mem-per-cpu=512MB # Memory per logical CPU

      module load Python
      python PythonMultiprocessing.py
    ```

    ```py
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
    ```

    The above Python script will calculated the square and cube of an array
    of numbers using multiprocessing and print the results from outside of
    those processes, safely circumventing Python's [global interpreter lock](https://wiki.python.org/moin/GlobalInterpreterLock).

    For more in depth examples of and descriptions of Multiprocessing in
    Python you may find [this Multithreading/Multiprocessing Youtube
tutorial
series](https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN&index=1)
helpful

=== "Job Arrays"
    
    Job arrays can be handled using the Slurm environment variable
    `SLURM_ARRAY_TASK_ID` as array index. This index can be called directly
    from within the script or using a command line argument. In the
    following both options are presented:
    
    The job scripts calling both examples:

    ``` sl
    #!/bin/bash -e
    
    #SBATCH -J test
    #SBATCH --time=00:01:00
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --array=1-2 # Array jobs
    
    module load Anaconda3

    echo "SLURM_ARRAY_TASK_ID.$SLURM_ARRAY_TASK_ID of $SLURM_ARRAY_TASK_COUNT"
    
    #env variable in python
    python hello_world.py
    
    #as command line argument
    python hello_world_args.py -ID $SLURM_ARRAY_TASK_ID
    ```

    the version getting the env variable in the python script
    `hello_world.py`
    
    ```py
    #!/usr/bin/env python3

    import os
    my_id = os.environ['SLURM_ARRAY_TASK_ID']
    print("hello world with ID {}".format(my_id))
   ```
    
    the version getting the env variable as argument in the python script
`hello_world_args.py`
    
    ``` sl
    #!/usr/bin/env python3
    """
    Module for handling inpu arguments
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
    ```

## Python Packages

Programmers around the world have written and released many packages for
Python, which are not included with the core Python distribution and
must be installed separately. Each Python environment module comes with
its own particular suite of packages, and the system Python has its own
installed packages.

The provided packages can be listed using

``` bash
module load Python/3.10.5-gimkl-2022a
python -c "help('modules')"
```

### Installing packages in your $HOME

This is the simplest way to install additional packages, but you might
fill your `$HOME` quota and cannot share installations with
collaborators.

``` bash
module load Python/3.10.5-gimkl-2022a
pip install --user prodXY
```

If you are working on multiple projects, this method will cause issues
as your projects may require different versions of packages which are
not compatible.

We **strongly** recommend using separate [Python virtual
environments](https://docs.python.org/3/library/venv.html) to isolate
dependencies between projects, avoid filling your home space and being
able to share installation with collaborators

### Installing packages in a Python virtual environment

A Python virtual environment is lightweight system to create an
environment which contains specific packages for a project, without
interfering with the global Python installation. Each virtual
environment is a different directory.

To create a Python virtual environment, use the `venv` module as follows

``` sl
module load Python/3.10.5-gimkl-2022a
python3 -m venv /nesi/project/PROJECT_ID/my_venv
```

where `PROJECT_ID` is your NeSI project ID.

Note that you need to *activate* the virtual environment before using it
(to run a script or install packages)

``` sl
source /nesi/project/PROJECT_ID/my_venv/bin/activate
```

Then you can install any pip-installable package in the virtual
environment using

``` sl
pip install prodXY
```

Then a Slurm job submission script running your Python script would look
like

``` sl
#!/bin/bash -e
#SBATCH --job-name    MyPythonJob
#SBATCH --time        01:00:00
#SBATCH --mem         512MB

module purge
module load Python/3.10.5-gimkl-2022a
source /nesi/project/PROJECT_ID/my_venv/bin/activate
python MyPythonScript.py
```

### Python virtual environment isolation

By default, Python virtual environments are fully isolated from the
system installation. It means that you will not be able to access
packages already prepared by NeSI in the corresponding Python
environment module.

To avoid this, use the option `--system-site-packages` when creating the
virtual environment

``` sl
module load Python/3.10.5-gimkl-2022a
python3 -m venv --system-site-packages /nesi/project/PROJECT_ID/my_venv
```

A downside of this is that now your virtual environment also finds
packages from your `$HOME` folder. To avoid this behavirour, make sure
to use `export PYTHONNOUSERSITE=1` before calling pip or running a
Python script. For example, in a Slurm job submission script

``` sl
#!/bin/bash -e
#SBATCH --job-name    MyPythonJob
#SBATCH --time        01:00:00
#SBATCH --mem         512MB

module purge
module load Python/3.10.5-gimkl-2022a
source /nesi/project/PROJECT_ID/my_venv/bin/activate
export PYTHONNOUSERSITE=1
python MyPythonScript.py
```

## Further notes

### iPython

iPython (*i*nteractive *Python*) is an enhanced tool for accessing a
Python command line. It is available in many NeSI Python modules.

#### Starting iPython

To open an iPython console, simply run the `ipython` command:

``` sl
[jblo123@build-wm ~]$ module load Python/3.6.3-gimkl-2017a
[jblo123@build-wm ~]$ ipython
```

#### Listing available functions

You can use iPython to list the functions available that start with a
given string. Please note that if the string denotes a module (i.e., it
has a full stop somewhere in it), that module (or the function you want
from it) must first be imported, using either an "import X" statement or
a "from X import Y" statement.

``` sl
import os
os.<TAB>   # List all functions in the os module
os.O_<TAB> # List functions starting with "O_" from the os module
len<TAB>   # List functions starting with "len"
```

Here,

``` sl
o<TAB>
```

or even

``` sl
os<TAB>
```

and expect to see the methods and values provided by the os module - you
have to put the full stop after the "os" if you want to do that.

#### Getting information about an object

In iPython, you can query any object by typing the object name followed
by a question mark (?), then hitting Enter. For instance:

``` sl
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
    >> int('0b100', base=0)
4
```

You can also do this on functions (`len?`), methods (`os.mkdir?`) and
modules (`os.path?`). If you try to do it on something that isn't
defined yet, Python will tell you that the object in question couldn't
be found.

#### Quitting iPython

Just enter the `quit` command at the iPython prompt.
