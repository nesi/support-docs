---
created_at: 2025-01-28
template: not_a_template
---



This page is meant for testing the linting checks. For all checks to run properly this file should be moved under `docs`.

It should trigger the fail threshold for `meta-checks`, `proselint-checks`, `spelling-checks`, `slurm-lint`, and `test-build`

Add tests here as needed.

Somee tpyos for spelchecker to triger fail neeeds to be at laest fiveteen keybored whopsers whiche is qiute a hihe tolerence i thinc. I woold loweir this threshehold bute for the momenent it can be a bitte overzaelos.

``` as
typos shuold be igonred in code blokcs 
```

!!! warning "some admonistion"
    contents of admonition

Typos should `be igonred` in inline code blocks.

Typos should [be ignored](https://www.docs.nesi.org.nz)
Typos should [be ignored](../docs/General/FAQs/How_do_I_request_memory.md)



Bad formatting for markdownlint 

  * bullet points
- bullet points

### Improper

## Header nesting
 

```sl
!#/bin/bash


#SBATCH -j short-option
#SBATCH --not-a-real-flag=not_real

module load something

```

[bad link](../docs/General/not-a-page.md)

[bad internal link](#impropers)

Very very bad prose shit this is probably very unproper language sorry about that hopefully the chairman doesn't see lets circle back around.

The following checks will only work if moved into a subdir of `docs/`

https://www.nesi.org.nz/deadlink


{{broken_macro()}}

{% include "not-real.md" -%}


{{broken_macro()}}


{% set app_name = page.no_a_variable | trim %}
