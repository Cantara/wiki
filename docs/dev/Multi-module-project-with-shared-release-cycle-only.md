# Multi-module project with shared release cycle only

On rare occasions you have a number of standalone artifacts that have the same release cycle. If these projects are _always_ releases together it is possible to add them as modules to a multi-module Maven project. This approach differs from the builder-pom in three ways 

1. All projects must be located in the same trunk in Subversion 
1. The parent pom must have scm and distributionManagement information. 
1. The modules all have the parent pom as _parent_. 

The short term benefit of making release a bit easier must be weighted against the benefit of having separate release cycles and smaller artifacts with fewer dependencies. 

This approach _might_ be appropriate in some special cases, but in general this approach is _discouraged_. If you are not a _Maven_ yourself, do not even consider this setup! 

The difference between "_inheriting from a parent project, and being managed by an multi-module project_". The difference is explained in [Maven: The Definitive Guide - 9.6.2. Multi-module vs. Inheritance](http://www.sonatype.com/book/reference/pom-relationships.html#sect-multi-vs-inherit).
