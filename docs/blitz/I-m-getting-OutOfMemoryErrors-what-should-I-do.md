# I'm getting OutOfMemoryErrors, what should I do?

I'm getting OutOfMemoryErrors, what should I do?

For background you should read these:

    * [JavaSpaces Fallacies](http://jroller.com/page/dancres?entry=javaspaces_fallacies)
    * [Are You Sure You're Leaking Memory?](http://www.jroller.com/page/dancres?entry=are_you_leaking_memory)

Blitz uses it's cache to hold both live and dead (taken or lease expired) Entry's. It only clears it's cache once it is full.

i.e. If you set the cache size to 100 and you have only five entry's with one writer and one taker, Blitz will have a cache containing 5 live entries and 95 dead ones after things have run for a while.

Each type of Entry is given it's own cache (there isn't one shared cache). So approximate total memory usage (to get an accurate figure would require estimating garbage requirements etc) is:

```
memory = 0;
for (X in all Entry types) {
 memory = memory + (cache_size * size_of X)
}

memory = memory + Db database cache size
```

Where Db database cache size is specified in the configuration file under dbCache

Thus in OutOfMemory situations, the correct approach is to reduce entry cache size or the db cache or increase available JVM heap or a combination of the three. Note that in the case of a persistent Blitz, you should also consider enabling log file serialization stream reset by setting the first boolean parameter to the Persistent class constructor (defined as the storageModel in the configuration file) to true.

Note that there is a tool (EntrySizer) in the Blitz distribution (see Extensions in the documentation for your chosen version) which can be used to compute the approximate size of an Entry as it will be stored in Blitz's cache.

Note also that you can specify individual cache sizes per Entry type using EntryConstraint examples of which can be found in the configuration files. A good basic approach to using these constraints would be to set entryReposCacheSize to something small like 256 or 512 and then use the EntryConstraints to allocate bigger caches (e.g. 1024, 4096) to specific Entry types.

In cases where you are submitting Blitz to high load for sustained periods of time and the CPU usage is close to 100%, consider enabling throttling to prevent overflow of internal queues. See eventQueueBound and taskQueueBound in the Installation Guide for your chosen distribution.
