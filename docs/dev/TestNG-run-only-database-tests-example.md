# TestNG run only database tests example

###### Annotation

```xml
@Test(groups = "database-productA")
```

###### TestNG config

```xml
 <test name="testng-env-db" verbose="3">
    <groups>
      <run>
        <exclude name="disabled" />
        <include name="database-productA" />
      </run>
    </groups>

    <packages>
      <package name="com.company.producta.*"/>
    </packages>
  </test>
```
