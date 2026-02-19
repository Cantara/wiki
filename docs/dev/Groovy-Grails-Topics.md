# Groovy & Grails Topics

This is work in progress

---
## Some Groovy basics

### And **that** compiles? But _some common class_ doesn't have that method?

Groovy adds utility methods to a lot of common classes. You'll find the details referred to as the GDK - and its available on http://groovy.codehaus.org/groovy-jdk/

An example:
```
"http://www.vg.no".toURL().text
```

This gives the content of the web page http://www.vg.no. Resolution is as follows.

The string is a groovy.lang.GString. This class does not have a toURL() method.

However, it has got an invokeMethod. This method does a toString, and then tries to call the method (in this case , toURL()) on the object returned from toString.

toString returns a java.lang.String. This class does not have a toURL() method. However, there are methods added by grooovy to make stuff better. These methods can be found on the GDK link above. For java.lang.String, a getURL is added which returns a java.net.URL. getText is then called on this object.

## Getting started with Grails

### Useful links

- [Grails homepage](http://grails.org/)
- [Mastering Grails tutorials by Scott Davis](http://www.ibm.com/developerworks/views/java/libraryview.jsp?search_by=mastering+grails)
- http://brainflush.wordpress.com/tag/grails/
- http://www.groovyongrails.com/
- http://www.grails<sub>~exchange.com/files/DaveSyer%20</sub>~%20Grails&Spring.pdf
 
### How do I create an application I can toy around with?

Do the following:
```
> cd <wherever>
> export GRAILS_HOME=<wherever>
> export PATH=${PATH}:${GRAILS_HOME}/bin
> grails create-app
```

See below for how to use Maven for building your Grails project.

### Removing the ~/.grails directory can sometimes solve strange errors
Try it if you don't understand why you get a strange error. 

### How do you upgrade a Grails project to a new version of the Grails framework?

1. download the new grails version
1. upgrade your grails project like this:
```
> cd <prosjektdir>
> grails clean
> grails upgrade
```

## Using Maven with Grails

### How do I use Maven with Grails?
 
Use the [Maven plugin for Grails](http://forge.octo.com/maven/sites/mtg/grails<sub>~maven</sub>~plugin/usage.html).

Create a Maven pom for your project like this: 
```
mvn grails:create-pom
```

_Note: You might need to add a log4j dependency in your pom.xml to get your project to compile._

### How do I use mysql with a maven-based grails project?

Add the mysql dependency to the POM:

```
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.6</version>
</dependency>
```

Then, update grails-app/conf/DataSource.groovy:

```
dataSource {
	pooled = true
	driverClassName = "com.mysql.jdbc.Driver"
	username = "root"
	password = ""
}
hibernate {
    cache.use_second_level_cache=true
    cache.use_query_cache=true
    cache.provider_class='com.opensymphony.oscache.hibernate.OSCacheProvider'
}
// environment specific settings
environments {
	development {
		dataSource {
			dbCreate = "create-drop" // one of 'create', 'create-drop','update'
			url = "jdbc:mysql://localhost/BuddyMap"
		}
	}
	test {
		dataSource {
			dbCreate = "update"
			url = "jdbc:mysql://localhost/BuddyMap"
		}
	}
	production {
		dataSource {
			dbCreate = "update"
			url = "jdbc:mysql://localhost/BuddyMap"
		}
	}
}
```

There is an underlying assumption here: All developers and test instances will run mysql without a root password. This might not be a good idea if tests use live data.

It is also not a good idea to let the application update the schema in production use, so switch that off.

Next, start mysql and create your database
```
$ mysql -uroot
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.0.51b MySQL Community Server (GPL)

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

mysql> create database buddymap;
Query OK, 1 row affected (0.00 sec)

mysql> 
```

I have not set the locale or character set for the database here. You should.

Next, package and run the application:

```
$ mvn package
[INFO] Scanning for projects...
(...)
$ mvn grails:run-app
(...)
[INFO] Server running. Browse to http://localhost:8080/BuddyMap
```

## Domain classes

### Which standard methods should you implement in a domain class?

It is a good idea to implement **String toString()** for instance like this:
```
class Book {
    String author
    String title
    <snip>

    String toString() {
        "${title}, ${author}"
    }
}
```

This is particularly important if you are using scaffolding - otherwise the views for the scaffolded pages will use "ID: Type" in relationships (drop<sub>~down selects and cross</sub>~reference links).

### How do you group domain classes in packages?
todo

### How do you handle non-persistent domain classes in Grails?
todo

## Services

### What are grails services used for?

They are basically used for the same things that a spring service bean, or an EJB session bean are used for, i.e. providing re<sub>~usable services for the front</sub>~end part of an application, handling transactions, and handling integration with external services. The following illustration gives one example of how they can be used in a Grails + Java context![grails_and_spring2.png](grails_and_spring2-png.md)(grails_and_spring2.png)
(Figure from http://www.grails<sub>~exchange.com/files/DaveSyer%20</sub>~%20Grails&Spring.pdf)

### How do you create a service?

Use the **grails create-service** method.
