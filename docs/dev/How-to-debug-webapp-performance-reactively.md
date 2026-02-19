# How to debug webapp performance reactively?

#### Strategy

There are of course many strategies for finding and fixing performance issues in any application. The most common is probably 

###### Classic performance debugging 

1. Find the bottle-neck 
1. Fix the bottle-neck 
1. Repeat 

###### Do some initial cleanup to eliminate stupid issues 

However, locating the precise bottle-neck might be difficult and/or time consuming. A more brute force approach is therefore often useful: 

1. Roughly where is the problem? 
1. Look for obvious mistakes and fix them 
1. Implement cheap, non-intrusive measures which fix common performance issues 

If this solves the problem, NICE! Communicate the errors/mistakes so they are not repeated and you are done. 
If not, try classic performance debugging as described above. 

#### Concrete tips on how to find the bottle-neck 

Use case: Three tier Java webapp (silo) with RDBMS as backend. The webapp utilize one external webservice. The database, the webapp and the webservice are deployed on three different hosts. 

Possible problems: 

- Slow web layer 
- Slow business layer 
- Slow persistence layer 
- Slow database 
- Slow webservice 
- Network 

Strategy: Divide & conquer 

- Start with the web page and locate the function call that is slow. (Measurements are required yes.) 
- Partition the problem: measure time spent in webapp, by database and by webservice. 
- Investigate each in turn to check for possible (cheap) improvements. 

If no simple improvements/fixes can be found, evaluate a new implementation, design or architecture. 

If you suspect the network to be the problem, try measuring the time it takes to fetch a static resource. On *nix based platforms {} and {} can give an indication: 

```
time wget -O /dev/null --server-response http://wiki.community.objectware.no/includes/css/master.css
```
