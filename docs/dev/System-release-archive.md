# System release archive

- Use a separate Maven project with **pom** packaging. Ideally this should be zip, tar.bz2, tar.gz. 

- List the different deployment units. 

- List the relevant site artifacts. 

- Include an html export from confluence. Ideally this export should be automated by maven. 

- Use the maven-release-plugin to automate the release process and achieve proper versioning. 

### Resources 

[maven-assembly-plugin](http://maven.apache.org/plugins/maven-assembly-plugin/)
[build-helper-maven-plugin](http://mojo.codehaus.org/build-helper-maven-plugin)

[maven-zip-plugin in sandbox](https://svn.apache.org/repos/asf/maven/sandbox/trunk/plugins/maven-zip-plugin/)
[MNG-1683 - type for zip packaging](http://jira.codehaus.org/browse/MNG-1683)'

- Mail threads 
    - [Maven - Confluence integration](http://www.mail-archive.com/users@maven.apache.org/msg09995.html) 
    - [confluence maven plugin](http://www.mail-archive.com/cayenne-dev@incubator.apache.org/msg01284.html)
