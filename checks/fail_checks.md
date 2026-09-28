---
created_at: 2025-01-28
template: not_a_template
not_a_parameter: This isn't valid
tags:
  - chemistryies
  - move data
  - gibberjabber
  - mostly nonsense
---



This page is meant for testing the linting checks. For all checks to run properly this file should be moved under `docs`.

It should produce warnings or errors from `meta-checks`, `proselint-checks`, `spelling-checks`, `slurm-lint`, and `test-build`,
and each of them should exit `1` when run with `CHECKS_STRICT=1`.

Add tests here as needed.

Somee tpyos for the spelchecker. Wiht `CHECKS_STRICT=1` evn one keybored whopser shuold maek it fial.

``` as
typos shuold be igonred in code blokcs 
```

!!! warning "some admonistion"
    contents of admonition

Typos should `be igonred` in inline code blocks.

Typos should [be ignored](https://www.docs.nesi.org.nz)
Typos should [be ignored](../docs/General/FAQs/How_do_I_request_memory.md)


links shouldn't be called [here](../docs/General/FAQs/How_do_I_request_memory.md)
but can be called [where](../docs/General/FAQs/How_do_I_request_memory.md)



Bad formatting for markdownlint 

  * bullet points
- bullet points

### Improper

## Header nesting
 

bad Slurm script

```sl
!#/bin/bash


#SBATCH -j short-option
#SBATCH --not-a-real-flag=not_real

module load something

```

[bad link](../docs/General/not-a-page.md)
[bad link](not-a-page.md)

[bad internal link](#impropers)

Very very bad prose shit this is probably very unproper language sorry about that hopefully the chairman doesn't see lets circle back around.

The following checks will only work if moved into a subdir of `docs/`

https://www.nesi.org.nz/deadlink


{{broken_macro()}}

{% include "not-real.md" -%}


{{broken_macro()}}


{% set app_name = page.no_a_variable | trim %}
