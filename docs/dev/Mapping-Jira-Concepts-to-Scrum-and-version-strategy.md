# Mapping Jira Concepts to Scrum and version strategy

#### Projects 

...
introduction from BG

main challenges (from HRA side view, applies mostly to MSB too)
1. Managing multiple projects
2. Release management
3. Reporting/ time tracking

hra
capacity plan... mapping projectst to components in Jira
issue with components in tracking

msb
separata projects for tracking major work items. good tracking, but issues with several backlogs
issue workflow

#### Version
A +_sprint_+ is a central concept in SCRUM. Iteration is not natively supported by Jira, but we can model it by using the _version_ concept. 
The version on in Jira should further be coupled to the release numbering of the product. The versioning schema for the product is controlled by Maven using the [release plugin](http://maven.apache.org/guides/mini/guide-releasing.html). A Maven release entails creation of binaries, deployment to a repository and creating a tag in the version control system. Several version schemes is possible, see [Maven Project Versions](http://www.sonatype.com/books/mvnref-book/reference/pom-relationships-sect-pom-syntax.html#pom-reationships-sect-versions) for further details. For this article the a major, minor, micro/incremental scheme  (x.y.z) is assumed as described in [APR's Version Numbering](http://apr.apache.org/versioning.html). 

As a general rule of thumb there should be a 1-1 relationship between sprints and versions. However, sometimes it is sufficient to limit the granularity to only major.minor to reduce overhead for patching of bugs. The rationale is 
that an organisation will always deploy the latest patch version of the chosen major.minor version and that is trivial to detect differences between x.y.z and x.y.z+1 because there should always be few changes. 

The same rationale is applicable for Confluence; one space per minor versjon (x.y). 
Note that this is the version strategy used by Atlassion for their [product documentation](http://confluence.atlassian.com). 

#### Components
Start with none and add components when needed. 

Components can for example be used to add some default grouping to be used in reporting, statistics and general project management. 
It may also be used for QA purposes. 

#### Type
1. Features
1. Bugs
1. Technical work
1. Knowledge acquisition

Suggested by [mountaingoatsoftware](http://www.mountaingoatsoftware.com/scrum/product-backlog).
