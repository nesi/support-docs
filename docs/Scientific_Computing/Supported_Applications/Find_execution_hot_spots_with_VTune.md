What is VTune?
--------------

VTune is a tool that allows you to quickly identify where most of the
execution time of a program is spent. This is known as profiling. It is
good practice to profile a code before attempting to modify the code to
improve its performance. VTune collects key profiling data and presents
them in an intuitive way.  Another tool that provides similar
information is [ARM
MAP](https://support.nesi.org.nz/hc/en-gb/articles/360000930396-Profiler-ARM-MAP).

How to use VTune
----------------

We\'ll show how to profile a C++ code with VTune - feel free to choose
your own code instead. Start with 

    git clone https://github.com/pletzer/fidibench

and build the code using the \"gimkl\" tool chain

    cd fidibench
    mkdir build
    cd build
    module load gimkl CMake
    cmake ..
    make

This will compile a number of executables. Note that VTune does not
require one to apply a special compiler switch to profile. You can
profile an existing executable if you like. We choose \"upwindCxx\" as
the executable to profile. It is under upwind/cxx, so

    cd upwind/cxx

Run the executable with 

    module load VTune
    srun --ntasks=1 --cpus-per-task=2 --hint=nomultithread amplxe-cl -collect hotspots -result-dir vtune-res ./upwindCxx -numCells 256 -numSteps 10

Executable [\"upwindCxx\" takes arguments \"-numCells 256\" (the number
of cells in each dimension) and  \"-numSteps 10\" (the number of time
steps). ]{.s1}Note the command \"[amplxe-cl -collect hotspots
-result-dir\" which was inserted before the executable. The output may
look like]{.s1}

[Top Hotspots]{.s1}

[Function[                                   
]{.Apple-converted-space}Module[          ]{.Apple-converted-space}CPU
Time]{.s1}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--[ 
]{.Apple-converted-space}\-\-\-\-\-\-\-\-\-\-\-\-\--[ 
]{.Apple-converted-space}\-\-\-\-\-\-\--]{.s1}

[Upwind\<(unsigned long)3\>::advect.\_omp\_fn.1[ 
]{.Apple-converted-space}upwindCxx[       
]{.Apple-converted-space}25.979s]{.s1}

[\_int\_free [                                 
]{.Apple-converted-space}libc.so.6 [       
]{.Apple-converted-space}9.170s]{.s1}

[operator new[                               
]{.Apple-converted-space}libstdc++.so.6[   
]{.Apple-converted-space}6.521s]{.s1}

[free[                                       
]{.Apple-converted-space}libmpi.so.12[     
]{.Apple-converted-space}0.300s]{.s1}

[indicating that the vast majority of time is spent in the \"advect\"
method (26s), with significant amounts of time spent allocating (6.5s)
and deallocating (9.2s) memory. ]{.s1}

 Drilling further into the code
-------------------------------

[Often this is enough to give you a feel for where the code can be
improved. To explore further you can fire up]{.s1} 

    amplxe-gui &

[Go to the bottom and select \"Open Result\...\", choose the directory
where the profiling results are saved and click on the .amplxe file. The
summary will look similar to the above table. However, you can now dive
into selected functions to get more information. Below we see that 16.5
out of 26 seconds were spent starting the two OpenMP threads.  \
\
]{.s1}

![Screen\_Shot\_2020-01-16\_at\_11.06.53\_AM.png](https://support.nesi.org.nz/hc/article_attachments/360003239635/Screen_Shot_2020-01-16_at_11.06.53_AM.png) 

 
