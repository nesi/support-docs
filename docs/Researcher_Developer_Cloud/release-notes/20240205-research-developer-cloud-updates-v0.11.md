---
hidden: false
label_names:
- release-note
position: 3
title: Research Developer Cloud updates v0.11 - 20240205
---

##Cloud services

####Images
* UPDATE: [Rocky<sup>1</sup>](https://rockylinux.org/) images are now available for tenants to use on VMs

####Object Storage
* UPDATE: Now operational and is in a user-testing phase. Please reach out if you would like some quota and help getting started! Early documentation can be found here: 
[Create and Manage Object Storage - Research Developer Cloud](../user-guides/create-and-manage-object-storage/index.md) 

##Blueprints

On top of ongoing development of our Cloud Services, we are now working towards building Blueprints for useful patterns that can support your research applications and pipelines. If you’ve a specific use case in mind, let us know.

####Kubernetes

We are starting out with K8s (Kubernetes, a container orchestration system). Deploying your applications on top of K8s can support gains in scalability, robustness, portability, and more. Starting with the basics, the following blueprint GitHub repositories support setting up a K8s management cluster and a workload cluster.

* Management Cluster: [GitHub - nesi/nesi.rdc.kind-bootstrap-capi](https://github.com/nesi/nesi.rdc.kind-bootstrap-capi)
* Workload Cluster: [GitHub - nesi/nesi.rdc.capi.workload](https://github.com/nesi/nesi.rdc.capi.workload)

More guides around when and how to use K8s with your application are under development. Watch this space!

##Infrastructure

####Platform testing

A full suite of CI/CD functional testing is now running hourly 24 x 7 against our core Research Developer Cloud infrastructure, supporting early identification of any emerging problems or incidents.

####Infrastructure observability

There is a common need to understand utilisation of resources for any cloud use case. We are in the process of creating a per tenant view of utilisation, which will be delivered via dashboards (using Grafana). We are prototyping this through our collaboration with AgResearch, to inform options towards more visibility for regular research developer cloud tenants in the future. Let us know of your needs for infrastructure observability.

####Platform maintenance

We are almost finished upgrading the operating systems of all hosts in our Ceph-based storage and OpenStack-based hosting platform (in both data centers) to Rocky Linux 9.2 from CentOS Stream 8. This upgrade improves maintainability, supportability, security, performance, and hardware compatibility. This is a significant upgrade and is in preparation for our next regular update to the newest versions of core OpenStack services, tentatively scheduled before mid-year.

<br><br>

<sup>1 Rocky Linux is an open-source enterprise operating system designed to be 100% bug-for-bug compatible with Red Hat Enterprise Linux.</sup>
