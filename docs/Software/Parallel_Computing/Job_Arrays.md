---
created_at: 2025-12-09
description: How to utilise job arrays. 
tags: 
    - slurm
    - parallel
---


Job arrays are best used for tasks that are completely independent, such as parameter sweeps, permutation analysis or simulation, that could be executed in any order and don't have to run at the same time.
This kind of work is often described as *embarrassingly parallel*.  
An embarrassingly parallel problem is one that requires no communication or dependency between the tasks (unlike distributed computing problems that need communication between tasks).

A job array will submit the same script repeatedly over a designated index using the `SBATCH` command  `--array`

For example, the following code:

``` sl
#!/bin/bash -e

#SBATCH --job-name=ArrayJob             # job name (shows up in the queue)
#SBATCH --time=00:01:00                 # Walltime (HH:MM:SS)
#SBATCH --mem=512MB                     # Memory
#SBATCH --array=1-2                     # Array jobs

pwd
echo "This is result ${SLURM_ARRAY_TASK_ID}"
```

will submit, `ArrayJob_1` and `ArrayJob_2`, which will return the results `This is result 1` and `This is result 2` respectively.

### Using `SLURM_ARRAY_TASK_ID`

Use of the environment variable `${SLURM_ARRAY_TASK_ID}` is the recommended method of variation between the jobs.

- As a direct input to a function.  

    ``` sl
    matlab -nodisplay -r "myFunction(${SLURM_ARRAY_TASK_ID})"
    ```

- As an index to an array.  

    ``` sl
    inArray=(1 2 4 8 16 32 64 128)
    input=${inArray[$SLURM_ARRAY_TASK_ID]}
    ```

- For selecting input files.  

    ``` sl
    input=inputs/mesh_${SLURM_ARRAY_TASK_ID}.stl
    ```

- As a seed for a pseudo-random number.  
    - In R

        ``` sl
        task_id = as.numeric(Sys.getenv("SLURM_ARRAY_TASK_ID"))
        set.seed(task_id)
        ```

    - In MATLAB

        ``` sl
        task_id = str2num(getenv('SLURM_ARRAY_TASK_ID'))
        rng(task_id)
        ```

    *Using a seed is important, otherwise multiple jobs may receive the
    same pseudo-random numbers.*

- As an index to an array of filenames. 

    ``` sl
    files=( inputs/*.dat )
    input=${files[SLURM_ARRAY_TASK_ID]}
    # If there are 5 '.dat' files in 'inputs/' you will want to use '#SBATCH --array=0-4' 
    ```

    This example will submit a job array with each job using a .dat file
    in 'inputs' as the variable input (in alphabetcial order).

Environment variables *will not work* in the Slurm header. In place
of `${SLURM_ARRAY_TASK_ID}`, you can use the token `%a`. This can be
useful for sorting your output files e.g.

``` sl
#SBATCH --output=outputs/run_%a/slurm_output.out
#SBATCH --output=outputs/run_%a/slurm_error.err
```

#### As an index to an array

``` bash
inArray=(1 2 4 8 16 32 64 128)
input=${inArray[$SLURM_ARRAY_TASK_ID]}
```

#### For selecting input files

``` bash
input=inputs/mesh_${SLURM_ARRAY_TASK_ID}.stl
```

#### As a seed for a pseudo-random number

In R

``` R
task_id = as.numeric(Sys.getenv("SLURM_ARRAY_TASK_ID"))
set.seed(task_id)
```

In MATLAB

``` matlab
task_id = str2num(getenv('SLURM_ARRAY_TASK_ID'))
rng(task_id)
```

*Using a seed is important, otherwise multiple jobs may receive the same pseudo-random numbers.*

#### As an index to an array of filenames

``` bash
files=( inputs/*.dat )
input=${files[SLURM_ARRAY_TASK_ID]}
```

*Note: If there are 5 `.dat` files in `inputs/` you will want to use `#SBATCH --array=0-4`.*

This example will submit a job array with each job using a .dat file in 'inputs' as the variable input (in alphabetical order).

#### Multidimensional array example

``` sl
{% raw %}
#!/bin/bash -e

#SBATCH --open-mode append
#SBATCH --output week_times.out
#SBATCH --array 0-167 #This needs to be equal to combinations (in this case 7*24), and zero based.

# Define your dimensions in bash arrays.
arr_time=({00..23})
arr_day=("Mon" "Tue" "Wed" "Thur" "Fri" "Sat" "Sun") 

# Index the bash arrays based on the SLURM_ARRAY_TASK)
n_time=${arr_time[$(($SLURM_ARRAY_TASK_ID%${#arr_time[@]}))]} # '%' for finding remainder.
n_day=${arr_day[$(($SLURM_ARRAY_TASK_ID/${#arr_time[@]}))]}

echo "$n_day $n_time:00"
{% endraw %}
```

### Avoiding Conflicts

As all the array jobs could theoretically run at the same time, it is important that all file references are unique and independent.

If your program makes use of a working directory make sure you set it e.g.

```bash
mkdir .tmp/run_${SLURM_ARRAY_TASK_ID}          # Create new directory
export TMPDIR=.tmp/run_${SLURM_ARRAY_TASK_ID}  # Set TMPDIR to point there
```

If you have no control over the name/path of an output used by a program, this can be resolved in a similar manner.

```bash
mkdir run_${SLURM_ARRAY_TASK_ID}                             # Create new directory
cd run_${SLURM_ARRAY_TASK_ID}                                # CD to new directory

bash job.sh

mv output.log ../outputs/output_${SLURM_ARRAY_TASK_ID}.log   # Move and rename output
rm -r ../run_${SLURM_ARRAY_TASK_ID}                          # Clear directory
```

See the Slurm documentation for more info on [job arrays](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/job_array.html).
