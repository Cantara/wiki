# The right tools for the job

A very important factor for practicing DDD is to use a good set of tools. The right type of libraries and frameworks makes it much simpler to develop and keep the domain model clean and less polluted by technical and infrastructural noise. Two very popular frameworks in Java are Spring and Hibernate. Both tools are non-intrusive by their very nature, and are a good starting point for developing DDD applications. Many of the descriptions and examples in the rest of this article are based on the use of both Spring and Hibernate.

The next tool in your toolkit should be an Aspect Oriented Programming (AOP) tool. For all practical purposes this would be AspectJ. The domain model is all about object-oriented design & programming, but in order to achieve this, AOP may be your friend. In combination with the Spring framework, it can remove uneccessary code in your domain model. Some advocates also the use of domain driven pointcut design for certain tasks, see for example Savenko's [presentation](http://www4.java.no/javazone/2007/show.do%3Fpage=92&articleid=5477.1.html) from Javazone 07.

Another promising framework that is specifically focused on DDD is [Qi4j](http://www.qi4j.org/). The code is yet to be released, but keep an eye on it for future work.
