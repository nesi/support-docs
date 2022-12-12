A Slurm configuration change has been made on Mahuika so that the 
maximum size
of <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001584875-What-is-a-core-file-" class="c-link">core file</a> that
can be generated inside a job now defaults to `0` bytes rather
than `unlimited`. 

You can reenable core dumps with `ulimit -c unlimited` .
