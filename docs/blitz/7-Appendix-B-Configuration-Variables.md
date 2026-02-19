# 7. Appendix B - Configuration Variables

### Basic Setup

    * persistDir=<string> - the directory in which blitz will keep checkpointed state.
    * logDir=<string> - the directory in which blitz will keep it's log files. If all log files are present, Blitz can reconstitute the checkpointed state.
    * storageModel=<type> - see Appendix A.

### JINI-related options

    * name=<string> - configures the name of the Blitz Instance. This value is made available on the proxy as a Name attribute
    * loginContext=<LoginContext> - sets the identity the Blitz instance will take on when it starts up. Many security configurations will require this to be set.
    * compliantDestroy=<Boolean> - see Administration section above.
    * initialGroups=<String[]> - defines the collection of LUS groups under which a Blitz instance will register on initial startup (after initial startup, groups are held in an internal database which can be reconfigured via JoinAdmin.
    * initialLocators=<LookupLocator[]> - set this to configure registration with specific LUS. This value is only used for initial startup as initialGroups.
    * initialAttrs=<Entry[]> - the Entry attributes to make available on the proxy as part of initial startup. Behaviour is the same as for initialGroups and initialLocators.
    * serverExporter=<Exporter> - configures the JERI endpoint to be used by the Blitz instance. Allows for configuration of tcp, ssl, https etc as the transport.
    * *preparer=<ProxyPreparer> - defines the proxy preparer to be used to verify various remote references which may be passed to a Blitz instance.
    * *recoveredPreparer=<ProxyPreparer> - defines the proxy preparer to be used to verify a remote instance recovered from the log/checkpoint storage during a restart.
    * loopbackTxnExporter=<Exporter> - configures and enables the loopback transaction manager which can be used to accelerate transactions against this Blitz instance.  Note it cannot be used to co-ordinate transactions amongst multiple participants nor does it yet support security options. [BETA](BETA.md)

### Notify Subsystem

    * syncNotifyOnWrite=<boolean> - when enabled forces writes to wait until all associated events have been processed. *IfExists is a significant performance drain and by default Blitz aggressively optimizes event delivery for those calls such that events from writes close to the resolution point may be ignored. If you are using *IfExists and require completely deterministic behaviour, enable this option. For those not using *IfExists leave this option disabled for better performance.
    * maxEventProcessors=<int> - defines the maximum number of threads to be used to empty the notify event queue and perform matching against notify templates. Defaults to 1.
    * eventgenSaveInterval=<int> - the number of events to be generated against an event registration before logging to disk.
    * eventgenRestartJump=<int> - the number by which to advance the sequence number of an event registration at recovery time. This "jump" is designed to allow an end-user application to detect the fact that recovery has been performed and that events may have been lost/never generated.

### Lease Subsystem

Allows control of leasing operation such as assigning a maximum allowable lease time.

    * entryLeaseBound=<long> - sets the maximum lease permissible for an Entry. Set this to zero to allow Lease.FOREVER
    * notifyLeaseBound=<long> - sets the maximum lease permissible for a notify registration. Set this to zero to allow Lease.FOREVER
    * leaseReapInterval=<long> - the time between active scans for lease expired resources. Value should be ms (0 disables active cleanup). Normally, Blitz uses read/take activity to do cleanup (passive). If memory or disk resource is scarce, configure this to non-zero to activate more aggressive cleaning (which, in turn, is more CPU aggressive). Alternatively, you can enable manual lease cleanup (via execution of org.dancres.blitz.tools.RequestReap by setting this to org.dancres.blitz.lease.LeaseReaper.MANUAL_REAP

Advanced Setup

    * loadBackoff=<int[]> - configures the deadlock avoidance timings for loading entry's. Requires a two int array consisting of base_backoff and the random jitter to apply to that backoff.
    * maxOidAllocators=<int> - the maximum number of allocators to use per Entry type for id generation. Ids are never reused thus a small number of allocators may run out of ids in highly concurrent take/write scenarios. More allocators also improves concurrency.
    * maxWriteThreads=<int> - should not be changed from the default value of 1.
    * threadKeepAlive=<long> - ms before a write thread will be killed rather than pooled.
    * maxTaskThreads=<int> - the maximum number of threads allowed for a task pool.
    * entryReposReadahead=<int> - the maximum number of Entry's to fault in should the cache provide no matches. Zero means readahead should be disabled. This is a global setting which can be overidden with individual Entry constraints - see the Javadoc for org.dancres.blitz.config.EntryConstraint.
    * agents=<ColocatedAgent[]> - is an array of initializers to be run against the Blitz proxy before it is published via a join manager to lookup services. See the javadoc for org.dancres.blitz.remote.user.ColocatedAgent.
    * updateContents=<boolean> - Determines whether the contents methods on JavaSpaceAdmin and JavaSpace05 update their working match sets with entry's written after the set was created. Note enabling this can mean that one never reaches the end of the match set or that the match set overflows memory if it fills faster than a client empties it.

Memory Management

    * desiredPendingWrites=<int> - the number of writes to batch for disk update.
    * throttlePendingWrites=<int> - the maximum number of writes to batch for disk update. If the queue fills beyond this threshold (perhaps due to slow disks) throttling is applied to foreground operations whilst disk catches up.
    * dbCache=<int> - the max size of cache Db is allowed (bigger being better).
    * maxDbTxns=<int> - the maximum number of transactions Db should support concurrently. Under highly concurrent loads, increase this number.
    * entryReposCacheSize=<int> - the maximum number of Entry's (per type) to cache. This is a global setting which can be overidden with individual Entry constraints - see the Javadoc for org.dancres.blitz.config.EntryConstraint.
    * eventQueueBound=<int> - limits the maximum size of the notify event queue - once full, writing threads will be throttled down to prevent overflow. Defaults to 0(disabled)
    * taskQueueBound=<int> - limits the maximum size of the task queue (used for processing new writes against blocked takes or reads) - once full, writing threads will be throttled down to prevent overflow. Defaults to 0(disabled)

Debug Options

    * ignoreLogConfig=<Boolean> - when true, causes Blitz to ignore any logger Level entrys in it's configuration file. This allows a developer to use the standard logger configuration approach when appropriate.
    * logCkpts=<Boolean> - if true, causes Blitz to generate a log message at each checkpoint
    * statsDump=<long> - pause in milliseconds which determines how often the stats are dumped to console. Setting this to zero disables stats dumping.
    * stats=<Switch[]> - Defines the default settings for stats gathering. See the Javadoc for org.dancres.blitz.stats. This information is processed by Dashboard.
