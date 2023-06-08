---
created_at: '2019-07-17T00:10:27Z'
hidden: false
label_names: []
position: 0
title: "Skylake warning message on M\u0101ui"
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001053675
zendesk_section_id: 360000039036
---

## I get the following warning message, do I need to worry?

    craype-x86-skylake requires cce/8.6 or later, intel/15.1 or later, or gcc/6.1 or later

## Short:

No. This is only a warning message from an interim state. And gets
resolved immidiately afterwards.

## More details:

Our software stacks are build with easybuild. There are toolchains
defined, which wraps around the Cray `PrgEnv-???` modules. These
toolchains are called `CrayIntel` , `CrayGNU` or `CrayCCE`. Within the
procedure of swapping the Programming environments all active PrgEnv get
unloaded before loading the new on. In that meantime the module
`craype-x86-skylake` stays loaded and realizes that there is no recent
compiler version available. Immediately afterwards the new programming
environment get loaded and therewith its compiler, which solve the
issue.

You can check the actual situation by inspecting `module list`

There is a way to prevent the message: Assuming you want to load a
certain toolchain or application. Let's say
{code}VASP/5.4.4-CrayIntel-18.08{code} which is build with build Intel
18.08, we can first swap into the desired {code}PrgEnv{code}

    module switch PrgEnv-cray PrgEnv-intel
    module load VASP/5.4.4-CrayIntel-23.02-19

OR

    module unload craype-x86-skylake
    module load CrayIntel        # or any other PrgEnv change you intended to  do
    module load craype-x86-skylake
    module load VASP/5.4.4-CrayIntel-23.02-19
