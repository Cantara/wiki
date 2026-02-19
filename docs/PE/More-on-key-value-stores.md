# More on key-value stores

Well, the data model (e.g. key-value vs relational) is orthogonal to whether it's automagically managed. In terms of data model, I think key-value stores have at least three benefits over an RDBMS:

1. A flexible data model that can easily capture semi-structured information (increasingly relevant in a web 2.0 / UGC / decentralized-info-creation world that generates more and more such datasets).

2. A schemaless model that allows bottom-up, data-first design rather than the pre-defined and static approach of the relational database.

3. A data model that lends itself extremely well to interfacing over REST and to JSON-like serialization. See CouchDB for an excellent example of this.

[http://blog.webmynd.com/2009/02/28/databases-as-a-service-fathomdb/#comment-85](http://blog.webmynd.com/2009/02/28/databases-as-a-service-fathomdb/#comment-85)
