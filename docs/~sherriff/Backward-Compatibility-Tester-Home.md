# Backward Compatibility Tester Home

Project requested and approved at java.net: [https://bct.dev.java.net/](https://bct.dev.java.net/)

## Detailed project description

The goal of the project is to add support for testing backward compatibility of services to an existing continuous integration server. The general idea is to build/integrate the new version (of the service we want to test) against projects that use the old version.

We already have a Proof<sub>~of</sub><sub>Concept implementation that shows how this can be achieved with Continuum and Maven2 projects. See my [Master thesis](http://folk.ntnu.no/drolsham/diplom/master</sub><sub>CI</sub>~erik.drolshammer.pdf) for a thorough description.

#### Overview of PoC

###### Part 1: Create derived projects 
The PoC create a new, _derived_ project where the original dependency have been replaced by the new version of the dependency. For each project that use this dependency, there will be one new, derived project. If we want to test multiple services for backward compatibility, derived projects that cover all _combinations_ of original and derived dependencies will be created. 

###### Part2: Build the derived projects 
The derived projects are built by Continuum like any other Continuum project. A successful build means that the new version of the service is backward compatible with regards to the projects in y our CI server. To improve coverage and accuracy, simply add more projects that depend on the service. A build _failure_ means that the service is definitely not backward compatible, and the output from the build and tests should indicate why. 

(Under the cover we make sure that the derived projects don't interfere with the version control system, and that the our changes are not overwritten when Continuum updates the original project from version control.)

## Other project information 

- **Source Code**: [http://jira.codehaus.org/secure/attachment/29379/2007.09.11_poc<sub>~ed.patch](http://jira.codehaus.org/secure/attachment/29379/2007.09.11_poc</sub>~ed.patch)

- **License**: [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

## Pages

[BCT TODO](BCT-TODO.md)

[Rules](Rules.md)

## Resources

[Presentation at JavaZone2007](http://svn.objectware.no/repos/objectware<sub>~public/presentations/2007/javazone/javazone2007</sub>~erik.drolshammer.ppt)
[Continuum jira issue](http://jira.codehaus.org/browse/CONTINUUM-1342)
[Research options for testing dependency version ranges](http://jira.jboss.org/jira/browse/JBBUILD-378)
[Master thesis](http://folk.ntnu.no/drolsham/diplom/master<sub>~CI</sub>~erik.drolshammer.pdf)

[AlphaWorks Backward Compatibility Tester](http://www.alphaworks.ibm.com/tech/backcompatibility) - A Java-based tool for testing the backward compatibility of JAR files.
[Backword Testing](http://www.testinggeek.com/backword.asp)
