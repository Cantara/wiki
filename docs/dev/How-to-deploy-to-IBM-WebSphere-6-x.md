# How to deploy to IBM WebSphere 6.x

It is not possible to deploy directly to IBM WebSphere 6.x by regular file transfer protocols, and it is not currently supported by [Cargo](http://cargo.codehaus.org/). The way of deploying to a cluster recommended by IBM, is by executing the file wsadmin.bat on the deployer's end with a number of parameters. The bat file is a facade for classes from IBMs JRE, J9, that transfer the file to the cluster manager (via SOAP or RMI), along with a Jython/JACL configuration script. The cluster manager then executes the configuration script.

## Deploy directly from Maven by executing wsadmin.bat

wsadmin.bat is included in RAD/WSAD and takes a number of parameters for host, port, protocol, script file etc. _How to deploy_ can thus be rephrased as _how to run bat scripts_?

### How to run bat scripts from Maven?

Use [exec-maven-plugin](http://mojo.codehaus.org/exec-maven-plugin). There has been reported problems when a new thread is spawned. (Running it from Continuum @ Windows has been a problem.) See [http://svn.objectware.no/repos/objectware-public/examples/maven-exec-example/](http://svn.objectware.no/repos/objectware-public/examples/maven-exec-example/) for a demo.

Thus, the problem at hand can be solved with exec-maven-plugin by including the following in the POM:
(!) Not complete!
```
<plugin>
<groupId>org.codehaus.mojo</groupId>
<artifactId>exec-maven-plugin</artifactId>
<!--<executions>
<execution>
<goals>
<goal>exec</goal>
</goals>
</execution>
</executions>-->
<configuration>
<executable>D:\WebSphere\AppServer\bin\wsadmin</executable>
<workingDirectory>.</workingDirectory>
<commandlineArgs>
-lang jython -f update.py -conntype SOAP -host clustermanager.company.com -port 8879 -username <USERNAME> -password <PASSWORD>
</commandlineArgs>
</configuration>
</plugin>
```

### How to run bat scripts from Maven on a remote host? TODO link to a working example
Call for clarification by [~erik.drolshammer](erik-drolshammer.md).
Run a script locally that logs into the remote host and executes the relevant scripts there. 

## Deploy directly from Maven by using maven-was6-plugin
[maven-was6-plugin](http://jira.codehaus.org/browse/MOJO-1010)

## Deploy using a pull strategy from the company maven repo

[Scripting pull-deployment with Jython in WebSphere](http://wiki.community.objectware.no/display/smidigtonull/WebSphere+deployment+from+a+CI+environment)

## Decouple build from WebSphere deployment -- scripting and a common middle ground
This has not been confirmed. Inquire [~thomas.nicolaisen](thomas-nicolaisen.md).
The above solutions imply a tight coupling between a Maven build process and the deployment to WebSphere -- all initiated from a [Continuous Integration](Continuous-Integration.md) server. This coupling can be loosened by letting Maven transfer the file to a intermediary location, being agnostic about the existence of a WebSphere cluster. This middle ground is being monitored by some script, the purpose of which is to initiate the WebSphere-specific part of the deployment process.
