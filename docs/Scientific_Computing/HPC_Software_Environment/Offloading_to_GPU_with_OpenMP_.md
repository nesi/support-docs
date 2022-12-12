With OpenMP 4.5, it has become possible to offload computations from the
CPU to a GPU,
see <https://www.openmp.org/wp-content/uploads/SC18-BoothTalks-Jost.pdf>

# Example

In the following we show how to achieve this in the case of a reduction
operation involving a large loop:

    #include <iostream>
    #include <cmath>
    int main() {
     int n = 1000000000;
     double total = 0;
    #pragma omp target teams distribute \
    parallel for map(tofrom: total) map(to: n) reduction(+:total)
     for (int i = 0; i < n; ++i) {
     total += exp(sin(M_PI * (double) i/12345.6789));
     }
     std::cout << "total is " << total << '\n';
    }

Save the above code in file total.cxx.

Note the pragma

    #pragma omp target teams distribute parallel for map(tofrom: total) \
    map(to: n) reduction(+:total)

which moves variables `total` and `n` to the GPU and creates teams of
threads to perform the sum operation in parallel. 

# Compile

We'll use the Cray C++ compiler to build the executable but first we
need to load a few modules:

    module load cray-libsci_acc/18.06.1 craype-accel-nvidia60 \
     PrgEnv-cray/1.0.4 cuda92/blas/9.2.88 cuda92/toolkit/9.2.88

(Ignore warning "<span class="s1">cudatoolkit &gt;= 8.0 is
required").</span>

To compare the execution times between the CPU and GPU version, we build
two executables:

    CC -h noomp -o total total.cxx
    CC -o totalOmpGpu total.cxx

with executable `total` compiled with `-h noomp`, i.e. OpenMP turned
off.

# Run

The following commands will submit the runs to the Mahuika queue (note
`--partition=gpu --gres=gpu:1` in the case of the executable that
offloads to the GPU):

    time srun --ntasks=1 --cpus-per-task=1 ./total
    time srun --ntasks=1 --cpus-per-task=1 --partition=gpu --gres=gpu:1 ./totalOmpGpu

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
</tbody>
</table>
