With OpenACC it is possible to offload computations from the CPU to a
GPU,
see <http://www.icl.utk.edu/~luszczek/teaching/courses/fall2016/cosc462/pdf/OpenACC_Fundamentals.pdf>.

Example
=======

In the following we show how to achieve this in the case of a reduction
operation involving a large loop:

    #include <iostream>
    #include <cmath>
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

which moves variables `total` and `n` to the GPU and creates teams of
threads to compute the total sum in parallel. 

Compile
=======

We\'ll use the Cray C++ compiler to build the executable but first we
need to load a few modules:

    module load craype-broadwell
    module load cray-libsci_acc 
    module load craype-accel-nvidia60 
    module load PrgEnv-cray

(Ignore warning \"[cudatoolkit \>= 8.0 is required\"). Furthermore, you
may need to load `cuda/fft` or `cuda/blas`\
]{.s1}

To compare the execution times between the CPU and GPU version, we build
two executables:

    CC -h noacc -o total total.cxx
    CC -o totalAccGpu total.cxx

with executable `total` compiled with `-h noacc`, i.e. OpenACC turned
off.

Run
===

The following commands will submit the runs to the Mahuika queue (note
`--partition=gpu --gres=gpu:1` in the case of the executable that
offloads to the GPU):

    time srun --ntasks=1 --cpus-per-task=1 ./total
    time srun --ntasks=1 --cpus-per-task=1 --partition=gpu --gres=gpu:1 ./totalAccGpu

  ------------- ------------
  executable    time \[s\]
  total         7.6
  totalAccGpu   0.41
  ------------- ------------

 

Check
out <https://support.nesi.org.nz/hc/en-gb/articles/360001127856-Offloading-to-GPU-with-OpenMP-> to
see how to offload computations onto a GPU using OpenMP.
