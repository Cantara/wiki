# High reads in the middleware

# Case - At newspaper

A newspaper can have many readers and can have many rss-clients polling it as well.

### How do we scale for the reader - the enterprise way

Put your reverse proxy with cache as the gate to your middleware. Behind this we can hide the load balancer to take care of cache misses.

Issue when doing html caching is personlized pages can not be cached. A bleeding edge to work around this is caching a non-logged in page and having javascript personalize it using cookie variables or ajax. 

Static content on separate nodes (without cookies).

Throttling might be a solution in extreme peak situations. A customer should either be shut out or let in. Throttling a reader "a little bit" gives the reader a bad customer experience. It also lets you collect statistics more effectively (how many % of current users can I serve)

Generate static pages on writes.

### How do we scale for the reader - the bleeding edge way

Ruby has introduced using a page cache on the web server. You can use this instead of using a cache in front of your load balancer. Enables fragmented caching. Not seen much in practical use.

RSS clients can deal with very slow responses. Often problems with clients and cache controlling headers.

### How do we scale for the rss-clients - the enterprise way

Throttling is advised to avoid the rss-clients stealing all your resources. Throttling should be done based on frequency and not on the client identifier. ETag and ifModifiedSince http headers can be used to distribute cache further into to network.

The RSS feed can often be out of date without being a problems for the client.

### How do we scale for the rss-clients - the bleeding edge way

A useful header could be onlyModificationsSince. Is this really useful?

### Common stupidities

Don't think about scaling. For the High Reads scenenarios, this is not too bad as long as you make a business decision about it. You can scale up afterwards without the need for rearchitecture.

Volatile data changes everything.

Group 4: Ørjan and Johannes
