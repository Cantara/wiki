# Database versioning

## How to track and control changes to databases? 

#### Versioning and sorted changes 

You should have the complete schema in its latest version. You will also have changes separate, and they must be stored in a sequenced way. Database changes is _not_ mutual independent.

#### Release for a group of artifacts 

>> How to make sure that artifact that belongs to a specific version 
>> of the database and its composition is kept together?
> 
> Good question. I like the idea that the application by itself recognizes the
> database version (by using a table in the database or something) and
> exerts changes by itself. I would never have done it 
> if a lot of money is at stake. Database changes does not run in a
> transaction, and it is relative catastrophic if it is done in
> a high traffic period or if it faults and no one is there to notice.
> 
> Atlassian is doing it that way. I am not aware of any standard tools that
> does that for you, but I have not been searching for those kind of tools.
> 
> As a minimum the application should kill itself if it wants a newer
> database version than it has.

The latter sounds like a good suggestion. The first sounds a little risky by my taste. (It is always much traffic and money involved when we speak big Oracle-clusters. :P)
