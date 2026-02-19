# REST

SOA - integrasjonsverktøy  
REST - applikasjonsprotokoll

REST is fine if the distributed application none of the following requirements:

- High-volume and low-latency distributed messaging
- Asynchronous messaging
- Where distributed transaction boundaries are needed
- Where the message consumers are slower than the producers
- Guaranteed deliver and/or only once delivery of messages
- Publish/subscribe
- Distributed peer systems that might at times be disconnected

Reference: <http://it.toolbox.com/blogs/the-soa-blog/is-woa-simpler-than-soa-26765>  
**Classification: <http://www.nordsc.com/ext/classification_of_http_based_apis.html>**

### REST resources

- [Roy Fielding's disertation, where REST was defined](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)
- [What defines a REST API, Roy Fielding](http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven)

- <http://www.jroller.com/rickard/entry/the_domain_model_as_rest>

- [REST intro, Stefan Tilkov](http://www.infoq.com/articles/rest-introduction)

- [Addressing Doubts about REST](http://www.infoq.com/articles/tilkov-rest-doubts)

- <https://github.com/ivarconr/jersey2-spring3-webapp/>

###### SIREN VS Collection+json

- <http://sookocheff.com/posts/2014-03-11-on-choosing-a-hypermedia-format/>
- <https://github.com/kevinswiber/siren/issues/15>

- <https://github.com/hamnis/json-collection>
  - <https://gist.github.com/hamnis/7004900>
  - <https://github.com/bjartek/sensors>

- <https://github.com/HalBuilder>

###### Siren

<https://groups.google.com/forum/#!msg/siren-hypermedia/EEEv6ZSo5U8/5jJnTxxQbkoJ>
