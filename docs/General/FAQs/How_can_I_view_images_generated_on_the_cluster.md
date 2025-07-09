---
created_at: '2020-05-11T23:29:39Z'
tags:
- visualisation
- image
- x11
- view
title: How can I view images generated on the cluster?
vote_count: 4
vote_sum: 2
zendesk_article_id: 360001514795
zendesk_section_id: 360000039036
---

If for any reason downloading images is impractical you can view them on
the cluster using the `display` command. For example,

```sh
gm display myImage.png
```

This requires a [working X-11
server](../../Scientific_Computing/Terminal_Setup/X11_on_NeSI.md).
