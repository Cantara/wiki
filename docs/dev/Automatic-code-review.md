# Automatic code review

#### Recommendations 

- Set up rules and generate the relevant reports. 
- Modify rules and fix bugs until the whole development team agrees on the standard. 
- Be absolutely certain that the standards are _understood_, _agreed upon_ and _followed_ before continuing. 
- Add checks to the regular build to enforce that the standards are followed. In most cases it is a good idea to make the regular checks less strict than the actual standards. This does not imply that you should have two sets of rules or that developers don't have to follow all the rules. It only means that you should not break the build if some code is entirely up to the QA standards. The reasoning is that it must be possible to do quick prototyping, proof-of-concepts, etc. without the CI server firing off a bunch of angry build error emails. 

#### Available plugins 

###### Findbugs, PMD, CPD 

```
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-pmd-plugin</artifactId>
        <version>${pmdVersion}</version>
        <configuration>
          <sourceEncoding>${encoding}</sourceEncoding>
          <targetJdk>${jdkVersion}</targetJdk>
          <verbose>true</verbose>
          <failOnViolation>true</failOnViolation>
          <failurePriority>2</failurePriority>
          <excludeRoots>
            <excludeRoot>target/generated-sources</excludeRoot>
          </excludeRoots>
        </configuration>
        <executions>
          <execution>
            <goals>
              <goal>check</goal>
              <goal>cpd-check</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>findbugs-maven-plugin</artifactId>
        <version>${findbugsVersion}</version>
        <configuration>
          <xmlOutput>false</xmlOutput>
          <threshold>Normal</threshold>
          <effort>Min</effort>
          <excludeFilterFile>${generatedResourcesDir}/findbugs-exclude-company.xml</excludeFilterFile>
          <visitors>FindDeadLocalStores,UnreadFields</visitors>
          <omitVisitors>FindDeadLocalStores,UnreadFields</omitVisitors>
        </configuration>
      </plugin>
    </plugins>
  </build>
```

###### Checkstyle 

###### Cobertura, Emma, Clover 

See [Java Parent POM Example](Java-Parent-POM-Example.md) for a complete pom.
