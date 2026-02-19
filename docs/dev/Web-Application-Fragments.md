# Web Application Fragments

It is possible to re-use fragments of web applications. Think two web applications being dependent on the same module of templates. However, there are some limitations:

- JSP's can generally not be packaged inside JAR-files in your classpath (they have to be located openly in the WAR-file, so they can be compiled into servlets.
- Web resources (images, JavaScript, CSS) can not be packaged inside JAR-files unless they are accessed as classpath resources (you can make a resource filter). 

**So how do we pull together JSPs from different modules?**

We have some maven alternatives:

- maven war-overlays (see maven war plugin documentation)
- maven assemblies http://books.sonatype.com/maven-book/reference/assemblies.html#d0e16265

However, these require a maven build to perform a roundtrip (for instance testing the result of changing a JSP).

One solution is to use symlinks on the file system to present files from one module inside the other. This has some drawbacks:

- Each developer must set up the symlinks accordingly
- Danger of releasing/building with symlinked resources (which are usually pointed at snapshots/trunks), instead of the dependent builds

Another solution is to use subversion externals, with similar drawbacks.

The final solution is of course to stop using JSPs and use some template technology like Velocity or FreeMarker instead.
