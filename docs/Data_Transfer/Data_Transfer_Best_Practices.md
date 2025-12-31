---
created_at: '2025-12-28T14:00:00Z'
tags:
- transfer
- copying
- download
title: Data Transfer Best Practices
---

## Avoid Transferring Temporary Files

It is best to avoid transferring temporary files. This is because temporary files:

1. Can take up a large amount of space and contain a huge number of files.
2. Are only used *temporarily* by the program that creates it and then not used again, so are not needed.

It is recommended that before you transfer files that you either **delete all temporary files** or **avoid transferring temporary files**, it will take longer for your files to transfer and take up unnecessary space on your host drive.

Transferring lots of files using Globus can also have detrimental effects on this service. Avoid transferring temporary files when using Globus.
