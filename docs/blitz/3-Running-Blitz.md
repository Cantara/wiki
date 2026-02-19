# 3. Running Blitz

### Starting JINI

Before starting Blitz, you should start up the necessary JINI services. We can do this using Brian Murphy's starter kit scripts as follows:

```
cd /home/dan/jini/jini2_1/jini-start/example/scripts

./urun httpd

./urun jeri-transient-reggie

./urun jeri-transient-mahalo
```

You may also find it useful to run the ServiceBrowser so you can check that things are performing as expected:

```
./urun jeri-browser
```

Now we must start a codebase server for Blitz:

```
./urun httpd -port 8081 -dir /home/dan/src/jini/space/lib
```

If you plan to deploy an Activatable Blitz instance you will also need to start either Phoenix or RMID. Assuming you choose to use RMID (note that there are various security options that RMID doesn't support):

```
rmid -J-Djava.security.policy=/home/dan/src/jini/space/config/policy.all
```

### Using ServiceStarter

First, edit the configuration files as desired (you will almost certainly need to alter the blitzCodebase, jiniRoot, dbLib, blitzRoot variables and possibly dbVersion). To start an Activatable Blitz instance:

```
cd /home/dan/src/jini/space/

java -Djava.security.policy=config/policy.all -jar /home/dan/jini/jini2_1/lib/start.jar config/start-act-blitz21.config
```

Note that the default configuration files expect to create a log for the shared activation group in /tmp/sharedvm.log which you will need to delete if you wish to start again from scratch, re-registering the Blitz instance etc. To start a non-activatable instance:

```
cd /home/dan/src/jini/space/

java -Djava.security.policy=config/policy.all -jar /home/dan/jini/jini2_1/lib/start.jar config/start-trans-blitz21.config
```

### A Word on Configuration Files

Example configurations for JINI 2.1 can be found in the config directory and have a 21 subscript. Those configurations without the subscript are examples of scripts which provide backward compatibility with JINI 2.0. Note that existing Blitz scripts from releases prior to Blitz Pure Java 1.13 will need modifications in line with these examples.
