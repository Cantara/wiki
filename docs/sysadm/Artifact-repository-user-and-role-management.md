# Artifact repository user and role management

| Description | Nexus Roles | Users |  |
| --- | --- | --- | --- |
| Admin users | **Nexis Administrator Role** | only a few selected super users |
| Deployment users | **Nexus Deployment Role** and **Repo: All Repositories (Full Control)** | CI-servers |
| Read-only users | Roles: one per project/company | one user per environment to be able to fetch artifacts when installing services. |

**TODO**: Stig will add link to page describing how to configure Jenkins CI server to support mvn release. 

More fine<sub>~grained control can be added when needed. I.e. deployment users with read/write access only to selected repositories or read</sub>~only users which only can download from a few repositories. 

###### Changes 

1. Set new admin password 
1. Disable the Anonymous user 
1. Set new password for deployment role 
1. Create new _Repository target privilege_ 3rd party repo. 
1. Create new _hosted_ repositories: project1<sub>~releases and project1</sub>~snapshots 
    1. Create new _Repository target privilege_ for each of these. 
    1. Create new role with only read and view privileges 
        1. read and view on both repositories 
        1. read and view on thirdparty 
        1. Artifact download 
        1. UI: Search 
        1. UI: Base UI privileges 
        1. UI: Repository browser 
    1. Create new read only user and give this user this role. 

[http://books.sonatype.com/nexus<sub>~book/reference/security</sub><sub>privileges.html](http://books.sonatype.com/nexus</sub><sub>book/reference/security</sub>~privileges.html)
