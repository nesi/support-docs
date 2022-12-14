---
created_at: '2020-08-26T01:22:12Z'
hidden: true
label_names: []
position: 5
title: Offloading to a GPU with OpenACC using the PGI compiler
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001815716
zendesk_section_id: 360000040056
---

With OpenACC it is possible to offload computations from the CPU to a
GPU,
see <http://www.icl.utk.edu/~luszczek/teaching/courses/fall2016/cosc462/pdf/OpenACC_Fundamentals.pdf>.

# Example

In the following we show how to achieve this in the case of a reduction
operation involving a large loop:

    #include <iostream>
    #include <math.h>
    int main() {
     int n = 1000000000;
     double total = 0;
     int i;
    #pragma acc parallel loop copy(total) copyin(n) reduction(+:total)
     for (i = 0; i < n; ++i) {
      total += exp(sin(M_PI * (double) i/12345.6789));
     }
     std::cout << "total is " << total << '\n';
    }

Save the above code in file total.cxx.

Note the pragma

    #pragma acc parallel loop copy(total) copyin(n) reduction(+:total)

which moves variables `total` and `n` to the GPU and creates teams of
threads to compute the total sum in parallel. 

# Compile

We'll use the PGI C++ compiler to build the executable but first we need
to load a few modules:

`module load PGI CUDA`

To compare the execution times between the CPU and GPU version, we build
two executables:

    pgc++ -fast -acc -ta=multicore -Minfo=accel -o totalAccMulticore total.cxx
    pgc++ -fast -acc -ta=tesla -Minfo=accel -o totalAccGpu total.cxx

Note that the PGI compiler can target CPU and GPU devices (-ta option).
The -Minfo=all option provides information about vectorization and
offloading.

# Run

The following commands will submit the runs to the Mahuika queue
(note `--partition=gpu --gres=gpu:1` in the case of the executable that
offloads to the GPU):

    time srun --ntasks=1 --cpus-per-task=1 ./totalAccMulticore
    OMP_NUM_THREADS=8 && time srun --ntasks=1 --cpus-per-task=$OMP_NUM_THREADS --hint=nomultithread ./totalAccMulticore
    time srun --ntasks=1 --cpus-per-task=1 --partition=gpu --gres=gpu:1 ./totalAccGpu

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>
