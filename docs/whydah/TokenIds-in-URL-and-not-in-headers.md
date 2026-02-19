# TokenIds in URL and not in headers

ApplicationTokenId and UserTokenId must be attached to every request. This is necessary for authentication and authorization of the request. 

There are several technical possibilities; 
- HTTP headers
- in body
- path parameters in the URL
- request parameters in the URL 

In Whydah, applicationTokenId and userTokenId are sent as the two first parts of the path in the URL. 
- Attempts to add these id's int the "x<sub>~auth</sub>~token" header will cause conflicts. Other IAM providers will use these headers, and effectively rewrite the content of the header.

It's a design trade-off. 
1. Header management can be difficult/not possible in several languages/libraries/technology which potential users of Whydah may consider to use. 
1. Increase session visibility and awareness amongst developers and users. 
1. Simple partitioning. - (read: session partitioning/balancing to different service instances)
