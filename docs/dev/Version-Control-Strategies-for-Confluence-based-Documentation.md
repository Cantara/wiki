# Version Control Strategies for Confluence-based Documentation

#### Export space and check-in to regular VCS 

Export to xml, html or pdf and check into a version control system. 

- **xml** export makes roll-back possible, but is not very viewing friendly standalone. 
- **html** is viewing friendly, but does not support roll<sub>~back. This option must thus be considered a read</sub>~only solution for historical documentation.  
- **pdf** is analogous to the html approach. The difference is that pdf is better for printing, but lacks the user friendliness of hyper links when viewing electronically. (tags) 

A variant of this approach is using **RSS**-feed. While a bit harder to setup, this gives better diffs and layout compared to the xml export.

#### Clone space 

Cloning a space for each version can quickly become cumbersome, but this should not be a problem. The trick is to look at the actual use pattern and not only the limitations of the approach, in other words **backward compatibility**. While not always achievable, we always strive for backward compatibility. This means that for every minor and micro release the wiki space will represent the most current release. In addition, we must keep a migration guide up to date, but this is a good idea regardless. 

#### Clone page tree 

The [Copy Pages Plugin](http://wiki.saikore.com/display/theme/Copy+pages) supports copying a page and all its children. The trick to make this work is to use a common key or prefix on all pages so the plugin can substitute this key with a new key. For example App1 SomePageName becomes App1_v1 SomePageName and is thus still unique (the page name is as identifier in Confluence). 

The greatest advantage to this approach is that it greatly reduces the number of spaces. The disadvantage is the number of _almost_ identical pages. Maintenance can quickly become a big problem! 

#### Comment 

Clone space and clone page tree can be compared to the _branches_ concept found in Subversion. Export to pdf and html provides historical snapshots and might thus be called _read-only tags_.
