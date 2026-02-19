# devops

Scripts related to continouous deploy and DevOps/NoOps

| Field | Value |
| --- | --- |
| **GitHub** | [https://github.com/Cantara/devops](https://github.com/Cantara/devops) |
| **Language** | Batchfile |
| **Stars** | 3 |
| **Last updated** | 2022-01-12 |

---

## README

Scripts for automatically run Update/New Installation 
===================
These scripts will query Nexus for the latest verision found on your maven repository (nexus).
When the version on nexus is different than the version currently installed, or when no version is actually installed:
* The artifact will be downloaded
* Java Service Wrapper will install this artifact on your Windows machine.

Windows
============

See pull_deploy/win directory.



