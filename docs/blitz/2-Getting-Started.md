# 2. Getting Started

First, ensure that you have installed the [required packages](http://dancres.org/bjspj/docs/docs/required_packages.html).

Second, if you are going to run blitz on JDK 1.4 you will need to modify the configuration files (located in the config directory), substituting **backport<sub>~util</sub><sub>concurrent50.jar** with **backport</sub><sub>util</sub>~concurrent.jar**.

Blitz is fully integrated with JINI 2.1 so the preferred method of startup is via the ServiceStarter. However, it's possible to run Blitz, for test purposes, in a standalone mode.

If you've downloaded the source distribution, please read the [Developer's Guide](http://dancres.org/bjspj/docs/docs/dev_guide.html) and ensure you've compiled the Blitz .jar's (once you've done the necessary editing of build.xml you can create the .jar's with a simple ant all.

#### Assumptions
For the purposes of the following examples, I assume that:

    * You've unpacked the distribution in /home/dan/src/jini/space
    * You've installed JINI 2.1 in /home/dan/jini/jini2_1
    * You've installed Brian Murphy's starter kit in /home/dan/jini/jini2_1/jini-start
    * Your machine's name is yakuza

#### Configuration Basics

Blitz is configured via a configuration file such as the example [blitz.config](http://dancres.org/bjspj/docs/config/blitz.config) file. This file contains options for determining security configuration, remote functions and core functions such as the storage model (see above).

Blitz implements a concept of Storage Models which allows the user to customize the level of persistence provided. The default setting is transient but, should you wish to change this, please read [Appendix A - Storage Models](Appendix<sub>~A</sub>~Storage-Models.md).

Additional configuration files are required for use with the ServiceStarter:

    * [activatable<sub>~group.config](http://dancres.org/bjspj/docs/config/activatable</sub><sub>group.config) and [start</sub><sub>act</sub><sub>blitz.config](http://dancres.org/bjspj/docs/config/start</sub><sub>act</sub>~blitz.config) are examples of configuration files suitable for starting an Activatable instance of Blitz.
    * [start<sub>~trans</sub><sub>blitz.config](http://dancres.org/bjspj/docs/config/start</sub><sub>trans</sub>~blitz.config) is an example configuration file suitable for starting a non-Activatable instance of Blitz.

Regardless of the storage model chosen, Blitz may need to, at least temporarily, persist it's state so ensure that you have properly configured the appropriate entries in the core config file (these are the configuration parameters persistDir and logDir in the configuration file). This is also important should you wish to "clean up" after a Blitz instance as you must delete the contents of the persistence and log directories specified by the configuration parameters.

Note: You must configure the persistence and log directories as described above. Other default settings can be left alone though you should probably review the initialGroups setting (particularly if you choose to not use Brian Murphy's scripts). You should also look at increasing the cache sizes to suit your hardware.
