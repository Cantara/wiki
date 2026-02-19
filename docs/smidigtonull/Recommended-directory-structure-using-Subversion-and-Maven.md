# Recommended directory structure using Subversion and Maven - Cantara Community Wiki

Maven can be configured to use almost any directory structure and so can the scm plugin. However, in the spirit of *convention over configuration* we strongly recommend that you follow the trunk, tags, branches convention when using Subversion. See [SVN best practices](http://svn.collab.net/repos/svn/trunk/doc/user/svn-best-practices.html) , [Choosing a Repository Layout](http://svnbook.red-bean.com/en/1.0/ch05s04.html#svn-ch-5-sect-6.1)  and [Release Branches](http://svnbook.red-bean.com/en/1.1/ch04s04.html#svn-ch-4-sect-4.4.1)  for more on this convention.

We have also found it convenient to separate products or deployment units to a separate folder. This is partly because it is easier to see what products non-technical people must know of and partly because the deployment units (rpm, dpkg, deb and sometimes war) often use different build definitions than the standard libraries (jar, war, etc.).

The following structure can thus be a good starting point.

- lib
  - libProject1
    - trunk/pom.xml
    - trunk/module1/pom.xml
    - trunk/module2/pom.xml
    - tags
    - branches
  - libProject2
    - trunk/pom.xml
    - trunk/module1/pom.xml
    - trunk/module2/pom.xml
    - tags
    - branches

- products
  - product1
    - trunk/pom.xml
    - trunk/module1/pom.xml
    - trunk/module2/pom.xml
    - tags
    - branches
  - product1
    - trunk/pom.xml
    - trunk/module1/pom.xml
    - trunk/module2/pom.xml
    - tags
    - branches
