# Build C (plusplus) code for multiple platforms with Maven

#### Project description 

We have a C++ project and cannot standardize the [GCC](http://gcc.gnu.org/) version of the runtime environment. This means that we must build binaries for each target  platform. This gives us the following two dimensions: 

- 32 and 64 bits 
- different gcc versions 

The deployment platform is Red Hat. We want to integrate with the package system on Red Hat, namely RPM. 

#### Maven project setup 

- app1/trunk
    - [pom.xml](C<sub>~parent</sub>~pom.md)
    - src/main/native
    - [app1<sub>~i686/pom.xml](C</sub>~i686-pom.md)
    - [app1<sub>~x86_64/pom.xml](C</sub>~x86_64-pom.md)
    - [app1<sub>~rpm/pom.xml](C</sub>~rpm-pom.md)

The 32/64 bits dimension is handled with profiles and different artifactIds. The gcc dimension is managed by building the project on each relevant target platform. Perhaps [chroot](http://en.wikipedia.org/wiki/Chroot) can be used instead of multiple environments for each platform? 

Packages to compile 32 and 64 bits and build rpms on RedHat. 
```
yum install gcc.x86_64 gcc-c++ glibc-devel.i386 rpm-build.x86_64
```

We do the following to distinguish between the generated binaries and RPMs: 
1. Extract the version (no decimals) from /etc/issue. 
1. Use this integer prefixed with _"RH"_ as classifier to create unique artifacts. We assume that all releases will be made on Red Hat boxes. This makes the setup rather fragile, but it is acceptable since the production and test environments only run Red Hat. 

#### How to share code between C++ projects? 

Sharing code between C++ projects can be achieved using [Static Libraries, Shared Libraries or Dynamically Loaded (DL) Libraries](http://www.dwheeler.com/program<sub>~library/Program</sub><sub>Library</sub><sub>HOWTO/). If you can standardize on one compiler and linker version, these approaches will probably work fine. However, if you need binaries for multiple platforms, the number of binaries quickly becomes hard to manage. There was a problem that the native</sub><sub>maven</sub><sub>plugin did not support classifiers! See jira issue [MOJO</sub>~433](http://jira.codehaus.org/browse/MOJO-433). **TODO**: Verify classifier support. 

For our use case static libraries seem most appropriate, since we want to automate the installation. The libraries themselves are thus only a technical tactic to share code, not a goal by themselves. We have therefore chosen a simpler approach based on [svn:externals](http://svnbook.red-bean.com/en/1.1/ch07s04.html). There are some pitfalls to be aware of, but compared to building loads of binaries, this approach is a lot less complex. 

Lets continue the example above and assume we have code in lib/lib1 that is needed in _src/main/native/lib1_. 

###### 1. Set up svn:external
See [howto subversion externals basics](http://jeremyknope.com/2006/06/23/howto<sub>~subversion</sub>~externals-basics/). 
 
```
app1/trunk$ svn propedit svn:externals .
```
and add something like 

```
src/main/native/lib1 svn+ssh://svn.company.com/var/local/repos/app1/lib/lib1
```

###### 2. Verify that it looks OK 

```
app1/trunk$ svn up 
diff -u <(ls -1 src/main/native/lib1) <(svn list svn+ssh://svn.company.com/var/local/repos/app1/lib/lib1)
```
If nothing is output by diff, then the to lists are equal and svn:externals is set up correctly. 

###### 3. Verify that maven release works 

svn:externals behave differently with the different types of source and target options to _svn copy_. It seems that _svn copy WC WC_ works and that Maven use this style during release. Regardless, to be confident that the solution works, do a release: 

```
mvn release:prepare 
mvn release:perform
svn list svn+ssh://svn.company.com/var/local/repos/app1/tags/theTagFromTheRelease/src/main/native/lib1
```

and verify that the output from the svn list command returns the expected file list.
