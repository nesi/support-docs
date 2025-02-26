---
hidden: false
label_names:
- release-note
position: 2
title: Research Developer Cloud updates and fixes v0.10 - 20231205
---

##Cloud services

####Images
* UPDATE: Standard images provided are now regularly patched and updated via behind the scenes automated build process
* FIX: Uploading custom images via the dashboard is now fixed

####Block storage
* FIX: Issues with detaching volumes has now been fixed

##Infrastructure

* [Yoga<sup>1</sup>](https://docs.openstack.org/yoga/index.html) containers have been updated to the latest patched versions within the release, which fixed bugs and patched security vulnerabilities
* Significant improvements have been made on our infrastructure testing mechanism to enable more automated processes of testing and improved resilience and visibility to incidents

##Other updates
* Our security documentations have been updated. See here for more details
* Proof of concept usage of GPU accelerated compute flavors. We’ve worked with partners at AgResearch to test a Windows server instance supporting a GPU accelerated Proteomics workload, using the [flavor name], which includes passthrough of 2x NVIDIA A40 GPUs into the instance
* Prototyped a managed identity solution with KeyCloak

We will continue to improve our services and we are currently testing object storage functionalities before releasing. The Research Developer Cloud has SLA of 9-5 weekdays, with best effort response time. Our team will be away during the Christmas and New Years holidays, so we may not respond to your requests on the last week of December and the first week of January. Have a wonderful holiday!

<br><br>

<sup>1 Yoga is the version of OpenStack our services are on. OpenStack is an open source cloud computing infrastructure software project adopted by many different research institutions and public cloud providers.</sup>