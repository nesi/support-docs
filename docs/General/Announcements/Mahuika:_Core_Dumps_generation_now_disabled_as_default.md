A Slurm configuration change has been made on Mahuika so that the 
maximum size of [core
file](https://support.nesi.org.nz/hc/en-gb/articles/360001584875-What-is-a-core-file-){.c-link} that
can be generated inside a job now defaults to `0` bytes rather
than `unlimited`. 

You can reenable core dumps with `ulimit -c unlimited` .
