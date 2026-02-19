# Package by feature

Package by layer is widely used in the Java community. Here we have gathered some resources which explain why _package by feature_ may be a good idea. 

#### Why package by feature? 

[How changing Java package names transformed my system architecture](http://johannesbrodwall.com/2012/07/10/how-changing-java-package-names-transformed-my-system-architecture/) by Johannes Brodwall

[Package by feature](http://johannesbrodwall.com/2008/07/29/link-package-by-feature/) by Johannes Brodwall

[Four harmful Java idioms, and how to fix them](http://www.javaworld.com/javaworld/jw-07-2008/jw-07-harmful-idioms.html?page=2)

[Package by feature, not layer](http://www.javapractices.com/topic/TopicAction.do?Id=205)

[Inndeling av kode - vertikalt eller horisontalt?](http://vimeo.com/49480093) by Terje Heen 

###### Relationships between technical layers

Context: Three-layer-RDBMS-java-web-application, package by feature 

- What policies do you follow with regards to what tables data access logic in a feature may use? 

- When you need information both from the Person domain and the Products domain; do you implement the join/aggregation/whatever in the database or in Java (in a service)?

Answer:

Let's say we had Orders which were given by a Person and contained Products. I would expect to see com.business.app.order.OrderController which have a reference to com.business.app.order.OrderRepository, com.business.app.person.PersonRepository and com.business.app.product.ProductRepository. Ok?
