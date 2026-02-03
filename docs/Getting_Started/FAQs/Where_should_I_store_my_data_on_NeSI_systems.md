---
created_at: '2022-06-15T00:53:58Z'
tags: []
description: Information on where to store data in the NeSI systems
---

| Frequency of data being read | Frequency of data being written        | Recommended option                                                                                                            |
| ---------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Often                        | Often (at least once every two months) | Store in your `/nobackup/<projectcode>` directory (but ensure key result data is copied to the persistent project directory). |
| Often                        | Seldom                                 | Store in your `/project/<projectcode>` directory.                                                                             |
| Seldom                       | Seldom                                 | Apply for an allocation to use NeSI’s long-term storage service or store elsewhere (e.g. at your institution).                |

In general, the **project directory** should be used for reference data,
tools, and job submission and management scripts. The **nobackup
directory** should be used for holding large reference working datasets
(e.g., an extraction of compressed input data) and as a destination for
writing and modifying temporary data. The nobackup directory can also be
used to build and edit code, provided that the code is under version
control and changes are regularly checked into upstream revision control
systems. The **long-term storage service** should be used for larger
datasets that you only access occasionally and do not need to change in
situ.

For more information, please see our [Filesystems and Quotas](../../Storage/Filesystems_and_Quotas.md) page.
