Many codes can be accelerated significantly by offloading computations
to a GPU. Some NeSI [Mahuika nodes have GPUs attached to
them](https://support.nesi.org.nz/hc/en-gb/articles/360001471955-GPU-use-on-NeSI).
If you want your code to run faster, if you\'re developing your own code
or if you have access to the source code and you feel comfortable
editing the code, read on.

Here we show how to tell the compiler which part of your algorithm you
want to run a GPU. We\'ll use OpenACC, which adds directives to your
source code. The advantages of OpenACC over other approaches is that the
source code changes are generally small and your code remains portable,
i.e. it will run on both CPU and GPU. The main disadvantage of OpenACC
is that only a few compilers support it. 

More information about OpenACC can be found
[here](http://www.icl.utk.edu/~luszczek/teaching/courses/fall2016/cosc462/pdf/OpenACC_Fundamentals.pdf).

Example
=======

In the following we show how to achieve this in the case of a reduction
operation involving a large loop in C++ (a similar example can be
written in Fortran):

    #include <iostream>
    #include <cmath>
    int main() {
     double total = 0;
     int i, n = 1000000000;
    #pragma acc parallel loop copy(total) copyin(n) reduction(+:total)
     for (i = 0; i < n; ++i) {
       total += exp(sin(M_PI * (double) i/12345.6789));
     }
     std::cout << "total is " << total << '\n';
    }

Save the above code in file total.cxx.

Note the pragma

    #pragma acc parallel loop copy(total) copyin(n) reduction(+:total)

We\'re telling the compiler that the loop following this pragma should
be executed in parallel on the GPU. Since GPUs have hundreds or more
threads, the speedup can be significant. Also note that `total` is
initialised on the CPU (above the pragma) and should be copied to the
GPU and back to the CPU after completing the loop. (It is also possible
to initialise this variable on the GPU.) Likewise the number of
iterations `n` should be copied from the CPU  to the GPU. 

Compile
=======

We can use the NVIDIA compiler

`module load NVHPC`

and type

`nvc++ -Minfo=all -acc -o totalAccNv total.cxx`

to compile the example.

Alternatively, we can use the Cray C++ compiler to build the executable
but first we need to load a few modules:

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
`--gpus-per-node=P100:1` in the case of the executable that offloads to
the GPU):

    time srun --ntasks=1 --cpus-per-task=1 ./total
    time srun --ntasks=1 --cpus-per-task=1 --gpus-per-node=P100:1 ./totalAccGpu

+-----------------------------------+-----------------------------------+
| executable                        | time \[s\]                        |
+-----------------------------------+-----------------------------------+
| total                             | 7.6                               |
+-----------------------------------+-----------------------------------+
| totalAccGpu                       | 0.41                              |
+-----------------------------------+-----------------------------------+

 

Check out [this
page](https://support.nesi.org.nz/hc/en-gb/articles/360001127856-Offloading-to-GPU-with-OpenMP-)
to find out how you can offload computations to a GPU using OpenMP.
