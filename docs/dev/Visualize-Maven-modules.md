# Visualize Maven modules

To quickly get a overview of a big Maven project it is often useful to get a visual view of the modules and their dependencies. 
The Maven [Dependency graph plugin](http://el4j.sourceforge.net/plugins/maven<sub>~depgraph</sub>~plugin/index.html) generates such a dependency graph as a png-file. 

```xml
<!--
sudo aptitude install graphviz
Artifact javax.inject:javax.inject:1 is named javax.inject:inject:1.0 in maven-depgraph-plugin.
This artifact must thus be manually added to your repository manager.

mvn depgraph:depgraph -P depgraph
-->
<profile>
    <id>depgraph</id>
    <activation>
        <property>
            <name>depgraph</name>
        </property>
    </activation>
    <pluginRepositories>
        <pluginRepository>
            <id>elca-services</id>
            <url>http://el4.elca-services.ch/el4j/maven2repository</url>
            <releases>
                <enabled>true</enabled>
            </releases>
        </pluginRepository>
    </pluginRepositories>
    <build>
        <plugins>
            <plugin>
                <groupId>ch.elca.el4j.maven.plugins</groupId>
                <artifactId>maven-depgraph-plugin</artifactId>
                <version>3.1</version>
                <configuration>
                    <!--<groupFilter>com.company</groupFilter>-->
                    <outDir>${project.build.directory}</outDir>
                    <outFile>${project.artifactId}-depgraph.png</outFile>
                </configuration>
                <dependencies>
                    <dependency>
                        <groupId>javax.inject</groupId>
                        <artifactId>javax.inject</artifactId>
                        <version>1</version>
                    </dependency>
                </dependencies>
            </plugin>
        </plugins>
    </build>
</profile>
```
