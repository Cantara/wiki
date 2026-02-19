# Generating OpenESB artifacts with Maven 2

> ℹ️ 

# A very brief introduction to OpenESB

OpenESB provides a JBI Runtime Environment for plugging in JBI components which interact with each other using message exchanges. JBI components can only listen for messages and forward them to other components while the actual generating and processing of messages is delegated to business services. JBI components that supply or consume services locally (within the JBI environment) are termed Service Engines (SE). JBI components that provide or consume services using some sort of communications protocol are called Binding Components (BC).

### Service Unit

A particular JBI interaction scenario is described in terms of "wired" Service Units (SU). A SU consists of following parts:
- Reference to JBI component (either SE or BC)
- Components role in communication (message provider, message consumer, or both)
- Business service which is trigged by JBI component
- WSDL for communication protocol

It follows that designing a JBI communication involves several tasks. First, a set of business services must be identified and prepared. Then each service must be associated with a JBI component which can feed the service with input data. OpenESB ships with a big number of ready<sub>~to</sub>~use JBI components which are sufficient in most use cases. Probably the most important example of SE is _[_Sun Java EE Engine_](http://java.sun.com/developer/technicalArticles/J2EE/sunjavaee_engine/)_ which acts as a bridge to JAX-WS web services deployed in the same JavaEE environment. If no existing JBI component meets the needs then a special one must be developed and installed in OpenESB. The last task is interconnecting of Service Units.

### Service Assembly

Service Assembly (SA) is a deployable artifact which defines Service Units and optionally describes message flows between them (associates message providers and consumers). There are no boundaries between Service Assemblies which reside within the same JBI environment. A Service Assembly can define connections from its own Service Units to Service Units deployed in the other Service Assembly within the same JBI environment. This can be used to partition big Service Assemblies into smaller ones.

A SA consists of multiple JBI descriptors (one for each SU and one for SA itself) packaged in a special way. JBI descriptors are written in XML format and can be very large and complex when number of Service Units is big and especially when some of Service Units use BPEL SE. Designing SA can be very hard without good tooling support. The only known such tool is NetBeans 6.x.

# Developing OpenESB artifacts using Netbeans 6.x

Netbeans 6.x provides several project types for OpenESB development. Composite Application (CA) project type is used for projects which generate Service Assemblies. Its central part is [Composite Application Service Assembly (CASA) Editor](http://www.netbeans.org/kb/60/soa/casa<sub>~quickstart.html) which is a visual drag</sub>~and-drop tool for connecting Service Units. Netbeans 6.1 has some [bugs](http://wiki.netbeans.org/SoaFaqUseExternalServiceUnit) in the CASA editor which makes it sometimes impossible to connect certain Service Units. These bugs are fixed in later versions of Netbeans but they are currently very unstable as they are still under development.

Netbeans dictates its own catalog structure for different types of projects which doesn't conform to Maven2 conventions. Its is possible to install a Maven plugin in Netbeans and import Maven projects to Netbeans. Unfortunately, Netbeans doesn't recognize such 'foreign' projects as SU candidates and they can't be imported as JBI modules to CA projects. The solution is to use Maven to package individual web services into separate Service Assemblies (containing nothing but single web services) and deploy them in OpenESB. After that we can just refer from Netbeans CA projects to already deployed Service Units.

The next figure shows an example deployment consisting of three Service Assemblies. Two of them contain only web services and don't depend on Netbeans. The last SA which defines JBI communication and relies on existing web services must refer to the external SAs where the necessary web services are located. &nbsp;
![Service_Units.jpg](Service_Units-jpg.md)(Service_Units.jpg)

# Using Maven to generate Service Assemblies

There are several reasons for why one would like to use Maven as part of the development process when creating OpenESB artifacts:
- automating the build process and thus speeding up the development process
- giving more freedom to developers regarding what tools they use when developing OpenESB artifacts (developers are often most effective when they can use their tools of choice)
- strong configuration management support in Maven

OpenESB is a relatively new technology and there are currently no Maven2 plugins for generating OpenESB Service Assemblies. One possible reason for that is that OpenESB provides very many extensions and customizations to standard JBI descriptors and these extensions are very poorly documented. When a CASA editor is used, the Netbeans takes care of all such things automatically. It is fine in some circumstances when all development is done in Netbeans but makes it extremely difficult to edit JBI descriptors outside Netbeans. The only way to learn how OpenESB JBI descriptors should look like is to make sample projects in Netbeans and examine the generated JBI files.

To make a JAX-WS web service available for JBI runtime, it must be deployed as a part of a SA. The next figure shows the structure of a Service Assembly containing a web service and a possible structure of Maven project.
![SA_structure.jpg](SA_structure-jpg.md)(SA_structure.jpg)
As the above figure shows, the JBI descriptors are located in a separate catalog. In this way we can hold all JBI<sub>~specific artifacts outside the web service code. Such project organization allows easily to generate not only the SA containing the web service but also a stand</sub><sub>alone JBI</sub><sub>unaware web service. Such web service can be deployed in a non</sub>~JBI environment if necessary. For example for integration tests.

The Maven _install_ task should produce two artifacts: the SA containing the web service and the stand-alone web service (an ordinary war). The last artifact is generated as normally. However, to generate the SA the following instructions must be included in pom.xml:
- A JBI<sub>~aware war file must be generated with _maven</sub>~war-plugin_. This file differs from the original war in that it contains a JBI descriptor from _src/jbi/su_. This file will not be deployed in the repository. It is only used for generating SA in the next step.
- SA must be generated with _maven<sub>~assembly</sub>~plugin_. It is an ordinary zip file which contains JBI descriptor from _src/jbi/sa_ and a JBI-aware war file from the previous step.

```title
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-war-plugin</artifactId>
    <version>2.0</version>
    <executions>
        <execution>
            <id>jbi</id>
            <phase>package</phase>
            <goals>
                <goal>war</goal>
            </goals>
            <configuration>
                <primaryArtifact>false</primaryArtifact>
                <warName>${artifactId}-${version}-su</warName>
                <webResources>
                    <resource>
                        <directory>src/jbi/su</directory>
                    </resource>
                </webResources>
            </configuration>
        </execution>
    </executions>
</plugin>
```
```title
<plugin>
    <artifactId>maven-assembly-plugin</artifactId>
    <executions>
        <execution>
            <id>generate-jbi-service-assembly</id>
            <phase>package</phase>
            <goals>
                <goal>attached</goal>
            </goals>
            <configuration>
                <filters>
                    <filter>src/jbi/filter.properties</filter>
                </filters>
                <descriptors>
                    <descriptor>src/jbi/distribution.xml</descriptor>
                </descriptors>
            </configuration>
        </execution>
    </executions>
</plugin>
```
