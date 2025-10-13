---
created_at: '2025-06-23T03:42:47Z'
tags:
- freezer
- release notes
title: 2025/06/23
description: Freezer upgrade release notes
search:
  boost: 0.1
---

## New and Improved

- Region update: Replacing region as us-east-01 with the correct region of akl-1 region. NB this is a config change, to reflect where the data is actually stored. No data was ever being transferred to us-east-01.
- Improved email handling: Existing members will no longer receive duplicate emails when the gateway pipeline is rerun to update membership.
- Resilient provisioning: If one member encounters provisioning issues, the system will continue to provision other members without interruption.
- Validation before provisioning: Provisioning will now be blocked if the allocation is missing or contains incorrect values, ensuring data integrity and preventing errors.

If you have any questions about any of the fixes, please [contact NeSI Support](mailto:support@nesi.org.nz "mailto:support@nesi.org.nz").
