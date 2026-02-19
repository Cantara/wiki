# Repository Management

#### Repository Manager

Maven artifacts can be downloaded from multiple sources: 

- Central repository (repo1)
- Company repository (shared code)
- Project repository (project specific code)
- Other external repository (3rd party)
- Other external code not in repository (also 3rd party)

We need to be able to handle all these in a reliable way. The best suggestion is a [repository manager](http://www.sonatype.com/products/nexus/whitepapers/intro-repoman). This allows us to:

- Proxy remote repositories
    - Behind the scenes connection to multiple external repositories allowing for both central and other third party artifacts. 
- Publish and store company, project dparty artifacts
    - To be able to structure projects the way we want. (E.g. refactor code into library projects)
    - To be able to use Maven deploy and release plugins => proper versioning
    - Use artifacts not found in any public Maven repository
- Search for artifacts
- Access control

Read more about [repository management](http://maven.apache.org/repository-management.html).

#### Repository layout 

There are three types of repositories; **remote**, **local** and **virtual**. 

###### Remote repositories

The Build Artifact Repository Manager acts as a _proxy_ for remote repositories, while local repositories are repositories stored locally. A list of typical remote repositories is shown below: 

- repo1
- repo1-snapshots
- codehaus
- codehaus-snapshots
- apache-snapshots
- jboss
- java.net (both m1 and m2) 
- java.net.glassfish
- mergere
- apache-incubating

###### Remote repositories

There are no one-size-fits-all guide lines for which local repositories to use, but the following conventions might be worth following: 

- For artifacts developed in-house (all employees have access)
    - libs-releases
    - libs-snapshots

- Third party artifacts not available in a public repo
    - ext-releases
    - ext-snapshots

- Project-specific artifacts (only project team members have access)
    - <projectName>-releases
    - <projectName>-snapshots

> ℹ️ With Artifactory a user needs deploy permissions on remote repositories in order to add new artifacts to the cache. 

###### Virtual repositories

Each project has a release and a snapshot repository configured in the releaseManagement section of the project pom to support deploy and release. 
In addition, we override central to force all queries to go to the company internal repository (override _central_). This is used for fetching both snapshots and releases of both libs and plugins.

The virtual repository provides a single-point-of-entry to all available artifacts and can fetch artifacts from any number of local and remote repositories behind the scenes.
