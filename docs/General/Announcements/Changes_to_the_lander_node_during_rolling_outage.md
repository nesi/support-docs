---
created_at: '2019-11-19T00:12:50Z'
hidden: true
label_names: []
position: 16
status: new
title: Changes to the lander node during rolling outage
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001253175
zendesk_section_id: 200732737
---

Please be aware that on 12/11/2019 an improved (highly available) NeSI
SSH Lander service was deployed at `lander.nesi.org.nz`. We advise that
all users should alter their SSH connection settings to use this new
service.

Note that the IP address of this service is different from the old
`lander02.nesi.org.nz` (though `lander02.nesi.org.nz` currently acts as
an alias to the new lander service), so if your network imposes outgoing
connection restrictions then you may need to update your firewall rules.

If your organisation wishes to avoid being effected by potential IP
address changes like this one in the future then whitelisting the NIWA
subnet (202.36.29.0/24) in your local firewall should avoid this issue
in the future.
