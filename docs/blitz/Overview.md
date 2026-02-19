# Overview

### Blitz - Javaspaces Made Simple

The Blitz JavaSpaces <sup>TM</sup> implementation aims to provide a rich set of features to make the development & deployment of JavaSpaces technology easier, more efficient and more fun to experiment with.

The Blitz Project is the first Jini <sup>TM</sup> 2.x compliant JavaSpace to be made available under an OpenSource [license](http://dancres.org/bjspj/docs/docs/LICENSE.TXT) .

#### Key features

    * Ease of installation.
    * Jini 2.x enabled.
    * Use of established VM principles.
    * Smart indexing.
    * Tuneable persistence.
    * Tools.
    * Entry Browsing.
    * Embeddable Space support.
    * Active/Passive/Manual lease cleanup.
    * Built for experimentation and expansion.
    * Easy integration with the Inca X IDE & Runtime Environment.

#### Ease of installation

Blitz aims to make installation simpler by not relying on other visible services such as RDBMS products (which tend to require significant admininistration knowledge of both the RDBMS and the OS) and providing default configurations which make it useful out of the box.

#### JINI 2.x Enabled

First-class support for a variety of security configurations and deployment environments.
Use of established VM Principles

Blitz's central abstraction for Entry storage is based on the classic Virtual Memory (VM) concept such that a set of Entry's are cached in memory at any one time and then paged, as required, according to an algorithm which typically bases it's decisions on usage patterns.  In addition, readahead can be supported such that we can fault in a collection of potentially matching Entry's when the cache has provided no suitable candidates.

This re-use of an OS concept allows Blitz to take advantage of a huge body of existing research with respect to effective caching in the face of varying application behaviour (some will have hotspots, some will be random, some will reference things strictly in order).

Different JavaSpace applications will have common sets of behaviour from a cache usage perspective. Blitz architecture makes it possible to support several different cache management strategies and allow an astute user to pick the one most suited to their application behaviour.

#### Smart Indexing

Blitz uses on disk and in-memory Entry storage, which is fully indexed automatically and keeps search times to a minimum.
Tunable persistence

Disk space is now cheap & efficient both in speed and reliability which reduces the motivation for developing a memory<sub>~only JavaSpace. The basic performance limit for a persistent space is related to guarenteeing consistency which is determined by the speed with which a system can force log entries to disk. Blitz tackles these problems by providing a range of profiles (Storage Models) giving different tradeoffs between data</sub>~integrity and speed.

    * VM-style caching with full consistent logging to ensure all changes are durable - full persistence.
    * VM-style caching with periodic flushing (after x seconds) - ensuring all changes x seconds ago are persistent.
    * VM<sub>~style caching with no logging - if your cache is big enough to hold the working</sub>~set of Entry's for your application, no paging occurs so all work is performed in memory with no disk access required - transient.

#### Tools

A selection of tools are provided to assist developers and administrators:

   1. Dashboard - GUI tool which displays useful information such as the number of instances of each type, number of currently active transactions, operation totals and memory consumption.
   2. SyncAndShutdown - Flushes all updates to disk and shuts down a Blitz JavaSpaces instance.
   3. DumpEntries - Displays the current contents of a Blitz JavaSpaces instance optionally unpacking and displaying each Entry.
   4. Cleanup - Clears all Entry's from the Blitz JavaSpaces instance and removes all schema information allowing for re-definition of Entry structure with no restart required.
   5. EntrySizer - assists in calculating Blitz JVM memory footprint

#### Entry Browsing

Blitz JavaSpaces supports com.sun.jini.outrigger.JavaSpaceAdmin allowing appropriate Service Browsers (e.g. Inca X's community browser) to view and manipulate the Entry's within an instance.

#### Embeddable Space support

Certain multi-threaded applications, running in a single JVM, can benefit from the use of JavaSpaces. In these situations, having the JavaSpace available as a remote service is undesirable. This feature allows an application to run Blitz locally, within it's own JVM, providing a performance boost.
Active/Passive lease cleanup

In high<sub>~performance applications, the cost of tracking lease expiry and clearing expired entries from disk may affect throughput sufficiently that it is more economical to accept that some disk</sub>~space will be lost to expired entries. Conversely, in environments where disk-space is at a premium, it may be more appropriate to expend processor and disk time doing full cleanup of expired entries.

Blitz provides three options for handling lease expiry processing:

   1. When an expired entry is loaded into cache-memory, it will be marked for deletion at the next cache flush. This has the effect of cleaning up entries which are slowing down the speed of searches. (passive cleanup)
   2. Occasional background scans of disk storage to find and remove expired entry's that never get into cache. This has the effect of conserving disk space. (active cleanup)
   3. User requested background scans of disk storage to find and remove expired entry's. (manual cleanup)

Note: the active cleanup code by default, is turned off. It can be turned on by setting the leaseReapInterval variable in the configuration file to a non-zero value.

Note: the manual cleanup code by default, is turned off. It can be turned on by setting the leaseReapInterval variable in the configuration file to org.dancres.blitz.lease.LeaseReaper.MANUAL_REAP.
Built for experimentation and expansion
Because Blitz is open-source, should the need arise, you can make whatever changes you desire. The design is based on a small number of generic abstractions making it easy (hopefully) to get to grips with the code.
Easy integration with the Inca X IDE & Runtime Environment
The Inca X team have been testing Blitz and have built an installer to integrate it into all versions of their IDE & 
Runtime Environment.

#### Maturing with further development

Looking at RDBMS technology, one can see that it has reached maturity - these are some of the defining characteristics of such a market:

    * A few dominant vendors.
    * A large body of technical research.
    * Established benchmarks.
    * Large number of common features between vendors.
    * A large body of knowledge with respect to application development and how to get appropriate performance.

The maturity of the RDBMS market is in marked contrast to the JavaSpaces technology where there's still a substantial amount of work to be done.

Blitz is intended to be a vehicle for furthering the development of JavaSpaces technology covering issues as diverse as internal implementation, application development (usage patterns, frameworks etc) and administration/deployment.

#### About Blitz

The Blitz project was started by Dan Creswell.

#### Credits

Blitz uses:

   1. Doug Lea's util.concurrent package
   2. TeaTrove
   3. Prevayler
   4. Berkeley Db and Berkeley Db Java Edition
