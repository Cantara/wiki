# Agile Maven quickstart

###### Set up Enterprise Maven Infrastructure 

This step is actually a precondition. Without the Enterprise Maven Infrastructure the following steps won't make sense. 

See [Enterprise Maven Infrastructure](Enterprise-Maven-Infrastructure.md) 

###### Set up a "Maven-friendly" file structure in your version control system 

For Subversion this will be something like: 
```
app1/trunk
app1/tags
app1/branches
```
Make sure you create the tags folder, otherwise the release will fail because the scm-plugin does not create the tags folder if it does not exist. 

###### Make project build in a clean environment

Make the project build with the latest stable Maven release. Common tasks are 
- convert the project from Ant to Maven 
- inherit from company/organization parent 
- make sure all dependencies and plugins are available from public or company repositories  
- separate tests that require external resources to build from those that should run everywhere. 
    - See [How to use TestNG groups to implement JigZaw](How-to-use-TestNG-groups-to-implement-JigZaw.md) 

This part is finished when _any_ developer can checkout the project and have it build successfully with mvn clean install. The only prerequisites should be to have Maven, Java and VCS-client installed and possibly to activate a profile to download the company/organization parent if such is required. 

###### Make it releasable

- Upgrade and optimize dependencies 
    - Use the latest stabel version of dependencies if possible 
    - run mvn dependency:analyze to get some tips to what dependencies are redundant. 

- Make ALL tests run 
    - Set up the required environment on the CI-server make sure all test run green here. 

- Make sure site-deploy runs successfully. 

- Do an alpha release to verify that the project is set up correctly. 

###### Externalize configuration 

- Load properties and xml files from classpath, not from some URI. 
- Use on set of Spring application context files for all environments. Switching implementations should be done with properties, not by different beans. 

###### Integrate with Enterprise Maven Infrastructure

- basic mvn clean deploy 
- run service tests every 1-6 hours 
- deploy site 

###### Automate deployment 

When we have stable, traceable artifacts with external configuration we can create proper deployment units. The deployment unit should contain the artifact, its dependencies, configuration templates and scripts to automate the installation. 

See [Installation and Deployment Automation](Installation-and-Deployment-Automation.md) for more details. 

###### QA review 

- PMD, CPD, FindBugs, etc. all create nice reports listing some possible code improvements; FIX THEM! 
- Checkstyle is useful to ensure a consistent formatting and code style. Adhere to it! If the rules and checks are to strict for your organization, change them to something the developers can agree on. 

###### Improve tests and evaluate refactorings 

During this process it is likely that someone has spotted some important functionality that lacked proper tests or code badly in need of refactoring. Because we now have CI, automated code review and working alpha release, the risk of changing the component should be acceptable. Refactorings and better tests should thus be considered.
