Often when running an [embarrassingly parallel
problem](https://support.nesi.org.nz/hc/en-gb/articles/360000690275), or
just lots of jobs at once, the limiting factor on your throughput (work
you can get done over a set period of time) will likely be the SLURM
queue rather than the jobs execution time. 

If this is the case, you will get more work done by optimising for
efficiency rather than speed, and running on a single CPU is almost
always more efficient than any form of parallelisation. 

![*Four serial tasks run concurrently will finish faster than for
parallel 4cpu tasks CPUs one after
another. *](https://support.nesi.org.nz/hc/article_attachments/360007328695/4tasks.png)
