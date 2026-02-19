# Scaling high computation load wrt. the middleware

Four paradigms:
 - Map-Reduce/offline/batch for latency insensitive cases
 - Shared caches for low-latency computations + naturally partitionable data
 - Tuplespaces/Grid movable code (at least for JavaSpaces or LISP-based solutions), customizable logic etc.
 - Traditional messaging systems for ordering-sensitive data, coordination 
 - Start hacking your own (Cassandra?), custom aggregation trees

 - Use a wiki (padded room option)

Group G1, Dan and Kjetil
