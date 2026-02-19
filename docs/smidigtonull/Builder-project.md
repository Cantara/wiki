# Builder project - Cantara Community Wiki

One of the reasons why some people cling to the *"Everything in one project"* approach is that it is convenient to build all code with a single command. This convenience can also be achieved with a so called builder project ("samlepom" in Norwegian).

- Create a new, empty pom project. (It should not inherit from project/company pom.)
- Add the projects you want to build as modules.

The project builder is a separate project and the modules should not be located in the same directory as the project builder pom.

Example

```
<project> 
  <modelVersion>4.0.0</modelVersion>
  <groupId>no.company.lib.builder</groupId>
  <artifactId>lib-builder</artifactId>
  <version>1</version>
  <packaging>pom</packaging>
  <name>Lib Builder</name>

  <modules>
    <module>../lib/libProject1/trunk</module>
    <module>../lib/libProject2/trunk</module>
  </modules>
</project>
```

|  | The builder pom can **not** be used to release the projects. The maven-release-plugin requires scm and distributionManagement information, which in turn means that you must create a full-blown parent pom. This in turn means that all projects must have the same subversion path, which contradicts the purpose of having separate life cycles. |
