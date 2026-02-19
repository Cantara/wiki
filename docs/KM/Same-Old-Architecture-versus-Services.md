# Same Old Architecture versus Services

### Intro

It has been almost 10 years since the term SOA was introduced as a strategy to build a better future for enterprises. Most people have learned that [skyscrapers don't scale](http://97-things.near-time.net/wiki/talk-about-the-arch-but-see-the-scaffolding-beneath-it) and was looking for a better way to create solutions.

### Let's look at the typical SOA approach.

Most SOA strategies can be described as putting some services on top of existing legacy applications and standard software. These services do most often live in some kind of enterprise service bus. If we analyze this, we realize that we have spent most of our effort in solving the simple stuff. We have actually integrated applications for the last 30-40 years. Having software exchange data is mostly trivial. We have implemented SOA as **same old architecture**. If we take an economical view on this, we can at most claim to have archived a technological shift, thus responding to this cost graph.

### So what should we have been doing?

To be direct and precise, we should have realized that we need to understand the concept of a service. If we explore the successful work in [building services the last 15+ years](/web/20211206032258/https://wiki.cantara.no/pages/viewpage.action?pageId=2065043 "building services the last 15+ years"), we will end up with something like the [Service Manifest](/web/20211206032258/https://wiki.cantara.no/display/KM/Service+Manifest "Service Manifest"). In short, the service manifest defines the responsibility of a service, where the most important stuff is the *single responsibility principle*, mainly to ensure that our **services are good building-blocks** for our solution.

Taking this reflection a bit further, we quickly realize that we need some way of categorizing/grouping your services from a non-functional dimension. A great example of such categorization can be found in [Service categorization](/web/20211206032258/https://wiki.cantara.no/display/KM/Service+categorization "Service categorization"). If we do a good job at categorizing our services, we will be able to add requirements and rules for the different categories of services, as you can see in this [Design-Time Governance](/web/20211206032258/https://wiki.cantara.no/display/KM/Design-Time+Governance "Design-Time Governance") example.

### Conclusion

This short article is meant to be a short introduction to the current state of the SOA business, and to pinpoint what most SOA practitioners are struggling with. Hopefully this will be of some sort of inspiration into rethinking how you approach SOA, and move away from Same Old Architecture to a service oriented approach which should provide a better chance of success.

We can take this strategy much further by [re-introducing Business Objects as first-class citizens of the architecture](/web/20211206032258/https://wiki.cantara.no/display/KM/re-introducing+Business+Objects+as+first-class+citizens+of+the+architecture "re-introducing Business Objects as first-class citizens of the architecture") and [combining a SOA strategy with enterprise search and BI DWH](/web/20211206032258/https://wiki.cantara.no/display/KM/combining+a+SOA+strategy+with+enterprise+search+and+BI+DWH "combining a SOA strategy with enterprise search and BI DWH"), but I'll have to save that for another time

**References:**

- [http://wiki.cantara.no](http://wiki.cantara.no/)
- <http://www.infoq.com/articles/intel-services-economics>
- [http://wiki.community.objectware.no](http://wiki.community.objectware.no/)
