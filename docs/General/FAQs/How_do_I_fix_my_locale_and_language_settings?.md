---
created_at: '2022-02-15T04:10:09Z'
hidden: false
label_names: []
position: 0
title: How do I fix my locale and language settings?
vote_count: 0
vote_sum: 0
zendesk_article_id: 4416829135887
zendesk_section_id: 360000039036
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    When logging in to NeSI from some systems, such as Windows Subsystem for
Linux, you might get messages like the following while using NeSI (the
following message is obtained when running `man`):

    man: can't set the locale; make sure $LC_* and $LANG are correct

To get rid of this message, save a text file called `.i18n` in your home
directory, with the following contents:

    LC_ALL="en_US.UTF-8"
    LC_ADDRESS="en_US.UTF-8"
    LC_COLLATE="en_US.UTF-8"
    LC_CTYPE="en_US.UTF-8"
    LC_IDENTIFICATION="en_US.UTF-8"
    LC_MEASUREMENT="en_US.UTF-8"
    LC_MESSAGES="en_US.UTF-8"
    LC_MONETARY="en_US.UTF-8"
    LC_NAME="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_PAPER="en_US.UTF-8"
    LC_TELEPHONE="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"

If you know what you're doing, you can replace each instance of
"en\_US.UTF-8" with a different locale. You can get a list of available
locales by running `locale -a`. Use a different locale at your own risk,
however.
