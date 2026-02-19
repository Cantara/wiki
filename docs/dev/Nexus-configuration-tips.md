# Nexus configuration tips

###### Use case: Open repositories and secured repositories in the same Nexus installation. 
See also https://support.sonatype.com/entries/24901127<sub>~Sonatype</sub><sub>Nexus</sub><sub>Security</sub>~Cookbook. 

1. Set up anonymous user 
    1. Remove access for the anonymous user to all repositories. 
    1. Create _privileges_ for _releases_ and _snapshots_ repositories. 
    1. Create a new role with view and read access to _releases_ and _snapshots_ repositories. 
    1. Assign this role to the anonymous user 
1. Set up repositories for a secret project 
    1. Create two new repositories (proj<sub>~releases and proj</sub>~snapshots)
    1. Create _privileges_ for both repositories. 
    1. Create a new role (read-only) with view and read access to both repositories. 
    1. Create a new role (deployment) full access to both repositores (todo add exactly which privileges are necessary for deployment)
    1. Copy _distributionManagement_ section from the repository summary page in the Nexus web console and add to the project pom.xml. 
        1. Url example: http://mvnrepo.company.no/index.html#view-repositories;releases~summary
    1. Add credentials to settings.xml or Jenkins credentials support which reference the repository id in pom.xml. 
        1. It is possible to use the same id for both snapshots and releases repo in pom.xml to have only a single entry in settings.xml if the user is given deployment privileges to both repos. 

###### Scheduled tasks run nightly 

- Remove snapshots from repository

- Rebuild Maven metadata 

- Repair Repositories Index 

Docs: http://books.sonatype.com/nexus<sub>~book/reference/scheduled</sub>~tasks.html
