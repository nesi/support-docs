---
created_at: '2023-02-02T03:42:47Z'
tags:
- releasenote
title: jupyter.nesi.org.nz release notes 02/02/2023
vote_count: 0
vote_sum: 0
zendesk_article_id: 6325030048655
zendesk_section_id: 360001150156
search:
  boost: 0.1
---

## New and Improved

- Improved Email Handling: Existing members will no longer receive duplicate emails when the gateway pipeline is rerun to update membership.  
- Resilient Provisioning: If one member encounters provisioning issues, the system will continue to provision other members without interruption.
- Validation Before Provisioning: Provisioning will now be blocked if the allocation is missing or contains incorrect values, ensuring data integrity and preventing errors.
- Internal Test Environment Cleanup.  

If you have any questions about any of the fixes,
please [contact NeSI Support](mailto:support@nesi.org.nz "mailto:support@nesi.org.nz").
