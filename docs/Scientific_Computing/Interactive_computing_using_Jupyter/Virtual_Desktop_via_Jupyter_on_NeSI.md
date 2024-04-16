---
created_at: '2020-07-08T01:45:40Z'
tags: []
title: Virtual Desktop via Jupyter on NeSI
vote_count: 2
vote_sum: 2
status: deprecated
zendesk_article_id: 360001600235
zendesk_section_id: 360001189255
---

A virtual desktop provides a graphical interface to using the cluster.
Desktops are hosted within Singularity containers, so not all of the
NeSI software stack is supported. If you would like to build your own
desktop containers with the code
[here](https://github.com/nesi/nesi-singularity-recipes).

Rendering is done cluster-side, and compressed before being sent to your
local machine. This means any rendering should be significantly more
responsive than when using X11 on its own (approximately 40 times
faster).

The quickest and easiest way to get started with a desktop is through
Jupyter on NeSI, [connect here](https://jupyter.nesi.org.nz/).

## Connecting

Click the icon labelled 'VirtualDesktop', The desktop instance will last
as long as your Jupyter session.

## Customisation

Most of the customisation of the desktop can be done from within,  
panels, desktop, software preferences.

### `pre.bash`

Enviroment set in `singularity_wrapper.bash` can be changed by creating
a file `$XDG_CONFIG_HOME/vdt/pre.bash` Anything you want to run
*before* launching the container put in here.

``` sl
export VDT_BASE_IMAGE="~/my_custom_container.sif" # Use a different image file.
export VDT_RUNSCRIPT="~/my_custom_runscript" # Use a different runscript.

export OVERLAY="TRUE"
export BROWSER="chrome" # Desktop session will inherit this

module load ANSYS/2021R2 # Any modules you want to be loaded in main instance go here.
```

### `post.bash`

Environment set in `runscript_wrapper.bash` can be changed by creating a
file `$XDG_CONFIG_HOME/vdt/post.bash`

Things you may wish to set here are:  
`VDT_WEBSOCKOPTS`, `VDT_VNCOPTS`, any changes to the wm environment, any
changes to path, this include module files.

``` sl
export VDT_VNCOPTS="-depth 16" # This will start a 16bit desktop
export BROWSER="chrome" # Desktop session will inherit this.

module load ANSYS/2021R2 # Any modules you want to be loaded in main instance go here.
```

## Custom container

You can build your own container bootstrapping off
`vdt_base.sif`/`rocky8vis.sif` and then overwrite the default by setting
`VDT_BASE_IMAGE` in `pre.bash`.

*You can help contribute to this project [here](https://github.com/nesi/nesi-virtual-desktops/projects/1).*
