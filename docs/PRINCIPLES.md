---
title: Writing Principles
description: Principles for deciding what to write in these docs, whether to write it, and how much.
search:
  exclude: true
---

**[CLICK TO VIEW THIS PAGE RENDERED IN MKDOCS](https://nesi.github.io/support-docs/PRINCIPLES/)**{ .hidden }

!!! prerequisite "See also"
    - For page structure and metadata, see [Create a New Page](NEWPAGE.md).
    - For markdown style, see [Formatting](FORMAT.md).

These principles decide _what_ to write, _whether_ to write it, and _how much_.
[Create a New Page](NEWPAGE.md) and [Formatting](FORMAT.md) cover how it should look.
They apply to everyone who writes here, people and AI agents alike.

Our readers are researchers with a wide range of HPC experience, usually in the middle of trying to get something done.

## Principles

1. **Start from a reader need.**
   If you cannot say who needs the page and what they will do with it, do not write it.
2. **One page, one job.**
   Every page is a tutorial, a how-to guide, reference or explanation ([Diátaxis](https://diataxis.fr/)).
   Do not mix them: a how-to guide that stops to explain background should link to an explanation instead.
3. **Every page is page one.**
   Most readers arrive from search, not from the previous page.
   A page must fully serve its main task on its own. State prerequisites, and use links only for tangents.
4. **Common case first.**
   Lead with what most readers need. Put edge cases and rare failures in admonitions (collapsed if long) or on linked pages.
5. **Simple and mostly right, but exact where it counts.**
   Simplify explanations freely. Commands, paths, limits and policy must be exact and work when copied.
6. **Say it once.**
   Each fact has one home. Elsewhere, give a one-line summary and link to it.
   A little repetition is fine if it saves the reader a click, but never copy the details.
7. **Plain words, and fewer of them.**
   Put the most important information first. Use active voice, short sentences, descriptive headings and NZ English.
   Cut anything that does not help the reader act or understand.
8. **Write less that lasts.**
   Every page has to be maintained. Link to vendor documentation instead of copying it.
   Leave out details that go out of date (versions, dates, screenshots of web pages) unless they are generated, for example with macros.
9. **Be findable.**
   Write titles and descriptions in the words readers search with, usually the task or the question.
   The description also feeds search, `llms.txt` and the docs search assistant.

## Should This Be Written?

- **No clear reader need:** do not write it.
- **An existing page covers it:** improve that page.
- **Vendor documentation covers it** and nothing about it is specific to Mahuika: link to the vendor documentation.
- **A one-off answer for one person:** answer the ticket. Write it up only if it is likely to come up again.
- **Only true for a short time** (an outage, a change): write a dated announcement in `docs/Announcements/`, not a permanent page.

## New Page or Existing Page?

- **The same purpose as an existing page:** add to that page.
- **A different type of page** (see principle 2), **or a separate task** readers would search for: make a new page.
- **Too long** is not a reason on its own. First move detail down the page or into admonitions. Split only when parts serve different tasks or readers.
- A new page needs a place in the nav (`.pages.yml`), links from related pages, and tags.

For tutorials, the [tutorial page structure](NEWPAGE.md#tutorial-page) follows the
[Carpentries lesson model](https://carpentries.github.io/lesson-development-training/instructor/objectives.html).

## Further Reading

- [Diátaxis](https://diataxis.fr/): the four types of documentation.
- [Progressive disclosure](https://www.nngroup.com/articles/progressive-disclosure/) (Nielsen Norman Group): showing the common case first.
- [Minimalism](https://faculty.washington.edu/farkas/dfpubs/Farkas-Williams-CarrollsNurnbergFunnel.pdf): a summary of John Carroll's _The Nurnberg Funnel_.
- [Every Page is Page One](https://everypageispageone.com/the-book/) (Mark Baker): topic-based writing for readers who arrive from search.
- [Documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/) (Write the Docs), including ARID: accept (some) repetition.
- [Planning content](https://www.gov.uk/guidance/content-design/planning-content) (GOV.UK): user needs and avoiding duplication.
- [Plain language](https://www.digital.govt.nz/standards-and-guidance/design-and-ux/content-design-guidance/writing-style/plain-language) (NZ Digital government).
