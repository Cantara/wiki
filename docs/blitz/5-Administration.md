# 5. Administration

Blitz supports JoinAdmin, DestroyAdmin, JavaSpaceAdmin and two custom management interfaces (BlitzAdmin and StatsAdmin and, therefore, can be managed by a variety of browser tools.

The first time a Blitz instance is started, it loads it's JINI configuration information such as lookup groups and locators from it's configuration file. These are then stored in a binary metadata file along with the serviceID and various other pieces of runtime information. **Future re-starts of the Blitz instance will read the configuration information from the binary metadata file (unless the StorageModel is Transient, in which case all state is lost and the configuration file will be read again)**. Thus, further configuration changes in respect of JINI state must be done via JoinAdmin. Other non-JINI configuration information can be changed in the configuration file and will take effect the next time the Blitz instance is restarted.

DestroyAdmin::destroy is usually defined to shutdown the service instance and remove all it's persistent state. As a convenience, Blitz provides a configuration variable, compliantDestroy, which can be used to specify whether a Blitz instance should delete or retain it's state when carrying out a destroy request. When compliantDestroy is false Blitz simply shut's down in response to a destroy call. If compliantDestroy is true Blitz will delete all state before shutting down. If compliantDestroy is not specified in the configuration file, the default is to retain state when destroy is invoked.

It is my belief that, as well as destroy, there should be an additional standardized method to trigger a shutdown whilst retaining state. As there is no such standard, the BlitzAdmin interface provides such a method.
