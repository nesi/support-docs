---
created_at: '2020-05-11T22:03:36Z'
hidden: true
label_names: []
position: 0
title: 'Profiler: cProfile (Python)'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001523256
zendesk_section_id: 360000278935
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

cProfile is the recommended profiler for most users. Documentation
[here](https://docs.python.org/2/library/profile.html#module-profile).
!!! info Tip
>
> [ARM MAP](https://support.nesi.org.nz/hc/en-gb/articles/360000930396)
> can also be used to profile Python code.

# Running cProfile

Profiling your python code with cProfile is as simple as passing your
script as an argument to the cProfile module. 

It is probably a good idea to provide an output file using the -o flag
if you don't want the profiling data sent to your stdout in string
format. 

``` sl
module load python
python -m cProfile -o myCode.prof myCode.py
```

The output will be a binary file.

# Visualising

There are several different packages that can be used to better
visualise your profile data.

## gprof2dot

One of the simplest way to visualise your data is with
[gprof2dot](https://github.com/jrfonseca/gprof2dot) 

``` sl
pip install gprof2dot --user
```

``` sl
gprof2dot -f pstats myCode.prof | dot -Tpng -o myCode.png
```

This will generate a .png file showing a breakdown of functions run by
your code.

Either download the image, or view it on the cluster using display
myCode.png (requires X11 setup)

## snakevis

<https://jiffyclub.github.io/snakeviz/>

 
