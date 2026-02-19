# Unitils pom.xml example

```xml
<!-- To get unitils and dbmaintain -->
<repositories>
	<repository>
		<id>sonatype-public</id>
		<name>Sonatype public repo</name>
		<url>http://oss.sonatype.org/content/groups/public/</url>
	</repository>
</repositories>

<profiles>
	<profile>
		<id>test-database-bm</id>
		<build>
			<plugins>
				<plugin>
					<artifactId>maven-surefire-plugin</artifactId>
					<configuration>
						<skip>false</skip>
						<suiteXmlFiles>
							<suiteXmlFile>src/test/resources/testng-database.xml</suiteXmlFile>
						</suiteXmlFiles>
					</configuration>
				</plugin>
			</plugins>
		</build>
	</profile>
</profiles>
<dependencies>
	<dependency>
		<groupId>org.testng</groupId>
		<artifactId>testng</artifactId>
                <version>5.14.2</version>
		<scope>test</scope>
	</dependency>
	<dependency>
		<groupId>org.unitils</groupId>
		<artifactId>unitils-dataset</artifactId>
                <version>4.0-SNAPSHOT</version>                
                <scope>test</scope>
	</dependency>
	<dependency>
		<groupId>commons-dbcp</groupId>
		<artifactId>commons-dbcp</artifactId>
                <version>1.2.1</version>
		<scope>test</scope>
	</dependency>
	<dependency>
		<groupId>com.oracle</groupId>
		<artifactId>ojdbc14</artifactId>
                <version>10.2.0.4</version>
		<scope>test</scope>
	</dependency>
</dependencies>

```
