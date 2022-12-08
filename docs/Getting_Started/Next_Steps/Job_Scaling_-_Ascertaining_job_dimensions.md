[When you run software in an interactive environment such as your
ordinary workstation (desktop PC or laptop), the software is able to
request from the operating system whatever resources it needs from
moment to moment. By contrast, on our HPC platforms, you must request
your needed resources *when you submit the job*, so that the scheduler
can make sure enough resources are available for your job during the
whole time it is running, and also knows what resources will be free for
others to use at the same time.]{.wysiwyg-color-black}

The three resources that every single job submitted on the platforms
needs to request are:

-   CPUs (i.e. logical CPU cores), and
-   Memory (RAM), and
-   Time.

Some jobs will also need to request GPUs.

# What happens if I ask for the wrong resources?

When you are initially trying to set up your jobs it can be difficult to
ascertain how much of each of these resources you will need. Asking for
too little or too much, however, can both cause problems: your jobs will
be at increased risk of taking a long time in the queue or failing, and
your project\'s [fair share
score](https://support.nesi.org.nz/hc/en-gb/articles/360000743536) is
likely to suffer.  Y[our project\'s fair share score will be reduced in
view of CPU time spent regardless of whether you obtain a result or
not.]{.wysiwyg-color-black} 

+-----------------------+-----------------------+-----------------------+
| **Resource**          | **Asking for too      | **Not asking for      |
|                       | much**                | enough**              |
+-----------------------+-----------------------+-----------------------+
| Number of CPUs        | -   The job may wait  | -   The job will run  |
|                       |     in the queue for  |     more slowly than  |
|                       |     longer.           |     expected, and     |
|                       | -   Your fair share   |     so may run out of |
|                       |     score will [fall  |     time and get      |
|                       |     rapidly (your     |     killed for        |
|                       |     project will be   |     exceeding its     |
|                       |     charged for CPU   |     time limit.       |
|                       |     cores that it     |                       |
|                       |     reserved but      |                       |
|                       |     didn\'t           |                       |
|                       |     use)]{.wysiwyg-co |                       |
|                       | lor-black}            |                       |
+-----------------------+-----------------------+-----------------------+
| Memory                | -   The job may wait  | -   Your job will     |
|                       |     in the queue for  |     fail, probably    |
|                       |     longer.           |     with an \'OUT OF  |
|                       | -   Your fair share   |     MEMORY\' error,   |
|                       |     score will fall   |     segmentation      |
|                       |     more than         |     fault or bus      |
|                       |     necessary. (see   |     error. This may   |
|                       |     [here](https://su |     not happen        |
|                       | pport.nesi.org.nz/hc/ |     immediately.      |
|                       | en-gb/articles/360000 |                       |
|                       | 204076) and           |                       |
|                       |     [here](https://su |                       |
|                       | pport.nesi.org.nz/hc/ |                       |
|                       | en-gb/articles/360000 |                       |
|                       | 204116)               |                       |
|                       |     for information   |                       |
|                       |     about how memory  |                       |
|                       |     use is charged to |                       |
|                       |     projects)         |                       |
+-----------------------+-----------------------+-----------------------+
| Wall time             | -   The job may wait  | -   The job will run  |
|                       |     in the queue for  |     out of time and   |
|                       |     longer than       |     get killed.       |
|                       |     necessary         |                       |
+-----------------------+-----------------------+-----------------------+

It is therefore important to try and make your jobs resource requests
reasonably accurate. In this article we [will discuss how you can scale
your jobs to help you better estimate your jobs resource
needs.]{.wysiwyg-color-black}

# Job Scaling

Before you start submitting the main bulk of your jobs, it is [advisable
to first submit a *test job*. ]{.SDZsVb tabindex="0"
data-term-for-update="advisable"
data-ved="2ahUKEwj-0-zoj-fhAhXCfX0KHYH_DJYQ_SowAHoECAwQDA"}

[A test job should be representative of the main body of your work,
scaled down (e.g. a small subset of your data or a low number of job
steps). Aim for your test job to run for around 10 minutes, too much
shorter and your job will be spending a high proportion of its time on
overhead and therefore be less accurate for the purposes of
scaling.]{.SDZsVb tabindex="0" data-term-for-update="advisable"
data-ved="2ahUKEwj-0-zoj-fhAhXCfX0KHYH_DJYQ_SowAHoECAwQDA"}

[Keeping your test job small ensures a short queue time, short run time
and that minimal resources are expended.]{.SDZsVb tabindex="0"
data-term-for-update="advisable"
data-ved="2ahUKEwj-0-zoj-fhAhXCfX0KHYH_DJYQ_SowAHoECAwQDA"}

[When scaling your jobs, one of the most beneficial things you can do is
to first scale down your data and calculations to as small as you can.
Whether this means only computing on a few rows and columns of your
data, or only doing a subset of the calculations you intend to do in the
complete jobs, cutting your initial test jobs down in size means that
they will both queue faster and run for less time. Also, if one of these
jobs fails due to not asking for enough resources, a small scale job
will (hopefully) not have waited for hours or days in the queue
beforehand.]{.wysiwyg-color-black}

> ### Examples {#prerequisites}
>
> [Multithreading
> Scaling](https://support.nesi.org.nz/hc/en-gb/articles/360001173895)
>
> [MPI
> Scaling](https://support.nesi.org.nz/hc/en-gb/articles/360001173875)
