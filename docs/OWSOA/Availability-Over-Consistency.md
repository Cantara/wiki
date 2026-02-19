# Availability Over Consistency

### Quote

"I am not aware of any information from Google about the cause of their outage but, again, we as an industry are still learning how to keep ever more complex applications and services available.   The article cited above, expresses the dismay of many users as a service they've grown to depend upon is simply not there for a while.

In many cases, the user would gladly take a "good enough" answer NOW rather than wait for the "correct" answer LATER.  In fact, it is MORE common to see users just want to keep going.  Right now, I am typing most of this on the bus with Windows Live Writer inserting notes to myself about the hyperlinks to fix when I am back online...  It's great to just "keep going" even with a reduced experience!

Amazon published a wonderful paper on  Dynamo at SOSP 2007.  This paper provides an excellent overview of the Dynamo storage system (which I had a role in encouraging from the sidelines -- I can't take credit for it).  Dynamo is in production with at least two running services and numerous fascinating techniques employed in its implementation.  I would encourage you to read the paper.

The reason that I raise this here is that Dynamo provides availability over consistency.  In a distributed system, it has been proven that Brewer's CAP Conjecture is true... Hence, it is now called the CAP Theory.   The idea is that you can have only two of Consistency, Availability, or Partition Tolerance.   You have have a consistent (and by this, the idea is a classic transactional ACID consistency) and partition tolerant system but it may not be available under some partitions.  Alternatively, you can have an available system which tolerates partitions but it won't have the classic notion of consistency.  Increasingly, I see applications designed with looser notions of consistency.  Most of the time, customers really want availability at the expense of classic consistency!  New means of expressing looser consistencies are emerging to provide availability even when failures occur!

I learned over 20 years ago working in transactional systems to ASK a customer what their priority was when dealing with an outage.  Indeed, some customers wanted you to ensure that every transaction was correct before bringing the system online.  At first, it shocked me to learn that many, many customers wanted the system up even if the results of the work might be somewhat "less than perfect".  Indeed, I saw this in some banking systems with humongous amounts of money being pushed around.  It wasn't that they were doing anything wrong... if the system came up, most of the transfers could be accomplished and overnight interest gathered for them.  The funds involved were large enough that hundreds of bank workers would simply stay up all night and verify the accuracy of the work, cleaning up as necessary.  The timeliness mattered more than the accuracy!

Again, more often than not, availability matters more than strict (classic) consistency!"

**From** [http://blogs.msdn.com/pathelland/archive/2008/09/01/confidence<sub>~in</sub><sub>the</sub><sub>cloud.aspx](http://blogs.msdn.com/pathelland/archive/2008/09/01/confidence</sub><sub>in</sub><sub>the</sub>~cloud.aspx)
