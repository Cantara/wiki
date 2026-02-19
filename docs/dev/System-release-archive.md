# System release archive

- Use a separate Maven project with **pom** packaging. Ideally this should be zip, tar.bz2, tar.gz. 

- List the different deployment units. 

- List the relevant site artifacts. 

- Include an html export from confluence. Ideally this export should be automated by maven. 

- Use the maven<sub>~release</sub>~plugin to automate the release process and achieve proper versioning. 

### Resources 

[maven<sub>~assembly</sub><sub>plugin](http://maven.apache.org/plugins/maven</sub><sub>assembly</sub>~plugin/)
[build<sub>~helper</sub><sub>maven</sub><sub>plugin](http://mojo.codehaus.org/build</sub><sub>helper</sub><sub>maven</sub>~plugin)

[maven<sub>~zip</sub><sub>plugin in sandbox](https://svn.apache.org/repos/asf/maven/sandbox/trunk/plugins/maven</sub><sub>zip</sub>~plugin/)
[MNG<sub>~1683 - type for zip packaging](http://jira.codehaus.org/browse/MNG</sub>~1683)'

- Mail threads 
    - [Maven - Confluence integration](http://www.mail-archive.com/users@maven.apache.org/msg09995.html) 
    - [confluence maven plugin](http://www.mail<sub>~archive.com/cayenne</sub>~dev@incubator.apache.org/msg01284.html)
