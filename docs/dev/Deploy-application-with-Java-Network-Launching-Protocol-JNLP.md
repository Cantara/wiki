# Deploy application with Java Network Launching Protocol (JNLP)

### Which applications implements JNLP?

- Java Web Start

### What is Java Web Start? 

- [What is Java Web Start?](http://java.sun.com/j2se/1.5.0/docs/guide/javaws/developersguide/faq.html#101)
- [Why should I use Java Web Start?](http://java.sun.com/j2se/1.5.0/docs/guide/javaws/developersguide/faq.html#103) 

- Advantages you can get by using Java Web Start to distribute applications.
    - Easy installation. Users can install a new application by simply clicking a link on a web page.
    - Platform independence. With Java Web Start, you can place a single Java application on a web server for
  deployment to a wide variety of platforms, including Windows 98/NT/2000/ME/XP, Linux, and Solaris .
    - Java Runtime Environment management. Java Web Start supports multiple, simultaneous versions of the Java 2
  Standard Edition platform. Specific applications can request specific Java versions without conflicting with the
  different needs of other applications. Java Web Start automatically downloads and installs the correct version
  of the Java platform, as necessary, based on the application's needs and the user's environment.
    - Desktop integration. Users can access any Java Web Start application, including those that rely on the network,
  just as they can any native application, right from their familiar desktops.
    - Application updates. You can update an application for all users simply by providing an updated JAR file on
  the Web server. On each user's computer, Java Web Start checks the Web server for updates when the
  application runs.
    - Familiar Java development requirements. You develop applications you intend to deploy with Java Web Start
  just as you would any Java application, with a few familiar packaging requirements. Updating a legacy
  application to be deployed through Java Web Start is, in most cases, a simple process.
    - Security. Java Web Start takes advantage of the inherent security of the Java platform. Application users can
  be confident that a Java Web Start application is restricted to a sandbox and cannot corrupt their systems.
  If you have provided for additional functionality and signed the application's JAR files, users decide if they
  trust the application's source and, if so, allow it to run. Nothing can happen behind the scenes without the
  user's awareness and approval.
    - Performance. Applications launched with Java Web Start are cached locally, for improved performance.

From [white paper](http://java.sun.com/developer/technicalArticles/WebServices/JWS_2/JWS_White_Paper.pdf), page 13. 

## How to use 

Deploying a Java Web Start Application involves the following steps:
1. Setting up the web server
1. Creating the JNLP file
1. Placing the application on a web server

This can be achieved with two different approaches: 

- Statically generate jnlp files 
    - Requires an http server (e.g. Apache) 
    - The url to the jnlp files on the webserver must be statically defined. 
    - See [Maven Webstart - static website](Maven-Webstart-static-website.md)

- Dynamically generate jnlp files 
    - Requires a servlet container (e.g. jetty, tomcat)  
    - The url to the jnlp files on the webserver can be dynamically defined, because the jnlp files are _generated_ on the server. 
    - More flexible than the static approach, because the servlet can be used to implement a configuration scheme and simplify changing properties.  
    - See [Maven Webstart - JNLP DownloadServlet](Maven-Webstart-JNLP-DownloadServlet.md)

**Diagram: Webstart**

## Resources 

#### JNLP implementations 

See (a bit outdated comparison) [comparison](http://jnlp.sourceforge.net/netx/compare.html) 

[OpenJNLP](http://openjnlp.nanode.org/) - open-source implementation of the JNLP protocol
[Netx](http://jnlp.sourceforge.net/netx/) is a high-quality implementation of the Java Network Launching Protocol (JNLP).

#### Similar or related products 

[Rachel](http://rachel.sourceforge.net/) is an open-source resource loading toolkit for Java Web Start/JNLP.
[JNLP Wrapper](http://www.duckcreeksoftware.com/products/jnlp-wrapper/) 
[Apollo](http://ajax.sourceforge.net/apollo/) - Open Source Test Skeleton Toolkit for Java Web Start
[JDIC Packager](https://jdic.dev.java.net/documentation/packager/example.html) is a tool for putting JNLP applications into installable packages of the standard Windows, Linux, and Solaris formats — MSI, RPM and PKG, respectively.

#### Java Web Start docs from SUN

- [http://java.sun.com/products/javawebstart/](http://java.sun.com/products/javawebstart/) 
- [Java Web Start white paper](http://java.sun.com/developer/technicalArticles/WebServices/JWS_2/JWS_White_Paper.pdf)
- [Architecture JNLP Specification & API Documentation](http://java.sun.com/javase/technologies/desktop/javawebstart/download-spec.html)
- [Frequently Asked Questions (FAQ)](http://java.sun.com/j2se/1.5.0/docs/guide/javaws/developersguide/faq.html)

- [Developer's Guide](http://java.sun.com/j2se/1.5.0/docs/guide/javaws/developersguide/contents.html)
- [JnlpDownloadServlet Guide](http://java.sun.com/j2se/1.5.0/docs/guide/javaws/developersguide/downloadservletguide.html)
- [Using an enterprise configuration for Java Web Start](http://java.sun.com/j2se/1.5.0/docs/guide/javaws/developersguide/enterprise_config.03.06.html)

#### Other Java Web Start docs 

- [Java Web Start Configuration (javaws.cfg) Reference](http://lopica.sourceforge.net/conf.html)
- [Unofficial Web Start FAQ Update/Errata](http://lopica.sourceforge.net/update.html)

- [Java Deployment with JNLP and WebStart (Kaleidoscope)](http://www.amazon.com/gp/product/0672321823/ref=cap_pdp_dp_0) **book** by Mauro Marinilli
