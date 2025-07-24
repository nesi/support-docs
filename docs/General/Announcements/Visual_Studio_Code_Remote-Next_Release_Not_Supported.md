---
created_at: 2025-01-24
tags:
- announcement
- vscode
title: 'Visual Studio Code Remote: Next Release Not Supported'
search:
  boost: 2
---

VSCode will be dropping support for glibc < 2.28 [starting Feburary 2025](https://code.visualstudio.com/docs/remote/faq#_can-i-run-vs-code-server-on-older-linux-distributions).

*This means future releases of VSCode may not be able to connect to the NeSI cluster*

This problem will eventually be resolved once NeSI moves to new login nodes as part of our
[Platform Refresh](platform_refresh_updates.md), however in the meantime we recommend disabling automatic updates.

## Disabling Automatic Updates

To modify the update mode, go to File > Preferences > Settings, search for 'update mode' and change the setting to 'none'.

## Rolling Back Version

If you already have a newer version of VSCode and cannot connect to the NeSI login nodes, please roll back to the [previous release
(1.9.6)](https://code.visualstudio.com/updates/v1_96).

You will also have to roll back the 'Remote - SSH' plugin. This can be
done by selecting the plugin in the Extension Marketplace, clicking on
the 'Uninstall' dropdown and choosing 'Install another version'.
