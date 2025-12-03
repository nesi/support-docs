---
created_at: '2019-05-05T23:39:05Z'
tags: []
description: Potential causes of program crashes
---

There are many different reasons why an application could crash. We
cannot list all the different possibilities, but we will help you to
investigate.

## OOM

One common reason is a limited amount of memory. Then the application
could crash with an [Out Of Memory exception](What_does_oom_kill_mean.md).

## Debugger

Another common issue is an error in the code. For example an application
could (may to unexpected input and missing error handling) call a
division by 0. Debugger can help to find the source of the issue. On the
NeSI systems are different debuggers available.
For serial application the [Gnu debugger gdb](https://sourceware.org/gdb/download/onlinedocs/gdb/index.html) is
available. Furthermore, the [ARM DDT debugger](https://developer.arm.com/docs/101136/latest/ddt/getting-started)
is available, which can handle, parallel, serial, applications, written in C/C++, Fortran, and Python (limited support).
