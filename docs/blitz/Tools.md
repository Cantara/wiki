# Tools

### Dashboard

Used to monitor a Blitz JavaSpaces instance as it runs. You can graphically access statistics such as memory usage, instance counts and number of active transactions. Graphing options are also provided, where appropriate. Dashboard supports lookup of a Blitz JavaSpaces instance via multicast discovery (just specify the space name) or unicast discovery (specify the lookup service host and the space name):

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:lib/dashboard.jar:lib/stats.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.dash.StartDashBoard dancres
```

or

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath lib/dashboard.jar:lib/stats.jar:/home/dan/jini/jini2_1/lib/jsk-lib.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.dash.StartDashBoard rogue:4160 dancres
```

**NOTE**: The provision of stats can be controlled programmatically or via the configuration file. Currently, for Dashboard to provide full information, you must have enabled appropriate options in the configuration file - e.g.:

```
import org.dancres.blitz.stats.Switch;
import org.dancres.blitz.stats.OpSwitch;
import org.dancres.blitz.stats.InstanceSwitch;

org.dancres.blitz {
 stats = new Switch[] {new OpSwitch(OpSwitch.ALL_TYPES,
 OpSwitch.TAKE_OPS, true),
 new OpSwitch(OpSwitch.ALL_TYPES, OpSwitch.READ_OPS, true),
 new OpSwitch(OpSwitch.ALL_TYPES, OpSwitch.WRITE_OPS, true),
 new InstanceSwitch(InstanceSwitch.ALL_TYPES, true)};
}
```

### SyncAndShutdown

Used to shutdown a Blitz instance and sync all it's state to disk. This tool works with all StorageModels including Transient. SyncAndShutdown supports lookup of a Blitz JavaSpaces instance via multicast discovery (just specify the space name) or unicast discovery (specify the lookup service host and the space name):

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.SyncAndShutdown dancres
```

or

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.SyncAndShutdown rogue:4160 dancres
```

**NOTE**:The shutdown of a Blitz instance may result in the loss of state associated with transactions active (not commited) at the time of shutdown. Typically, entries written under such transactions will be lost and any takes performed will not have been completed such that the Entrys will remain in the databases. All Entrys untouched by transactions are guarenteed to be undamaged.

### DumpEntries

Used to dump the contents of a Blitz instance's databases after it's been shutdown with SyncAndShutdown. This tool will work in combination with SyncAndShutdown against even a transient Blitz instance.

Basic usage of DumpEntries requires that you specify the blitz configuration file of the Blitz instance whose contents you wish to display.

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:dbjava/je.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.DumpEntries config/blitz.config
```

DumpEntries will display not only Blitz internal information but will also attempt to unpack the Entry instance and display it using the relevant codebase. To disable this feature (perhaps because the codebase is not available) run DumpEntries as follows:

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all -Dnounpack=true
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:dbjava/je.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.DumpEntries config/blitz.config
```

**NOTE**: Dumping the contents of a Blitz instance should only be done after it's been shutdown using SyncAndShutdown. DumpEntries is strictly read-only and, therefore, cannot damage the contents of the databases.

### HotBackup (experimental)

Used to make a hot backup of a blitz instance. Arguments are a directory to backup to and either a space name or an LUS host URL and spacename. Note that the specified directory must be available to the machine on which the Blitz instance is running.

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.HotBackup /home/dan/src/jini/space/backups dancres
```

or

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.HotBackup /home/dan/src/jini/space/backups rogue:4160 dancres
```

**Note**: the specified directory should be empty otherwise the backup will be refused.

### Entry Cleaning (experimental)

The Cleanup tool remotely connects to a specified Blitz instance causing it to clean out all old Entry's. The process performs the following steps:

   1. Kill all outstanding blocking matches
   2. Abort all outstanding transactions
   3. Delete all Entry's
   4. Checkpoint (to ensure all deletes are commited to disk)
   5. Delete all repositories

Cleanup supports lookup of a Blitz JavaSpaces instance via multicast discovery (just specify the space name) or unicast discovery (specify the lookup service host and the space name):

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.Cleanup dancres
```

or

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.Cleanup rogue:4160 dancres
```

### Manual Lease Reaping

Used to cause Blitz to perform a single lease-reaping pass clearing out all dead Entrys. Ensure that leaseReapInterval is set to LeaseReaper.MANUAL_REAP. Failure to set this option will cause manual lease cleanup to fail. This tool works with all StorageModels including Transient. RequestReap supports lookup of a Blitz JavaSpaces instance via multicast discovery (just specify the space name) or unicast discovery (specify the lookup service host and the space name):

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.RequestReap dancres
```

or

```
cd /home/dan/src/jini/space
java -Djava.security.policy=config/policy.all
 -classpath /home/dan/jini/jini2_1/lib/jsk-lib.jar:lib/blitz.jar:/home/dan/jini/jini2_1/lib/jsk-platform.jar:/home/dan/jini/jini2_1/lib/sun-util.jar
 org.dancres.blitz.tools.RequestReap rogue:4160 dancres
```

### Log Dumping

This tool can be used offline in a similar fashion to DumpEntries, to examine Blitz's activity logs allowing the user to form a picture of exactly what operations were performed during a particular run. Log Dumping can only be used for persistent instances and includes details of lease renewals, notification registrations, transactions and read/write/take.

The tool requires a single argument which is the directory specified in the logDir variable of the relevant .config. Here's an example:

```
java -Djava.security.policy=config/policy.all
 -classpath /Users/dan/jini/jini2_1/lib/jsk-lib.jar:/Users/dan/jini/jini2_1/lib/jsk-platform.jar:lib/blitz.jar
 org.prevayler.implementation.SnapshotPrevaylerImpl
 /Users/dan/blitz-install/logs/
```

Note that normally, only successful operations are logged but it can sometimes be useful to also see failed reads and takes. By default Blitz does not log these but you can enable it by adding logSearches = new Boolean(true); to your blitz configuration file.  You may also wish to enable logging of instance counts by adding logCounts = new Boolean(true); to your blitz configuration file.

### Lookup Settings Import

In accordance with the Jini specifications, Blitz will only read the initial* lookup parameters from it's configuration file on first boot (in transient mode this means the parameters are re-read every boot, whilst persistent modes will deem first boot to occur when there's no previous log or database state present).

Under various circumstances it can be desirable to reset Blitz's internal lookup settings from a configuration file post first-boot. This ReconfigLookup tool is used to perform this task providing support to selectively import settings from a specified configuration file.

ReconfigLookup accepts a path to a configuration file followed by one or more flags indicating which lookup settings to import. These flags are -groups, -attrs, -locators. An example usage of this tool appears below:

```
java -Djava.security.policy=config/policy.all
 -classpath /Users/dan/jini/jini2_1/lib/jsk-lib.jar:/Users/dan/jini/jini2_1/lib/jsk-platform.jar:lib/blitz.jar:dbjava/je.jar
 org.dancres.blitz.tools.ReconfigLookup 
 /Users/dan/blitz/config/blitz.config 
 -groups -attrs -locators
```
