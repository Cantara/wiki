# How to use JUnit Categories to implement JigZaw

It finally seems like the Surefire plugin does handle categories. 
Please read this link, it show how to simplify your setup.
http://johndobie.blogspot.com/2012/04/unit-and-integration-tests-with-maven.html

# At last - categories are possible to use in JUnit
Since the 4.8 version

Hope this will ease the implementation of using test-grouping :-)

> ℹ️ Thanks to [David Saff](http://david.saff.net/) for helping us reach this solution.
#### 1. We will need a Suite to be run for each category.
Example for  slow tests:
```java
@RunWith(Categories.class)
@Categories.IncludeCategory(SlowTests.class)
@Suite.SuiteClasses({AllTests.class})
public class OnlySlowTests {
}
```

#### 2.  "Proxy" to include all tests:
The Challenge: "@Suite.SuiteClasses" need to specify which classes to be included. 
What we want is to run all tests that has a given category. This challenge will be solved
by using [ClasspathSuite extension to JUnit](http://www.johanneslink.net/projects/cpsuite.jsp)
```java
@RunWith(ClasspathSuite.class)
public class AllTests {
}
```
#### 3. Example of Test class:
```java
public class AppTest {   
    @Test
    @Category({FastTests.class})
    public void fast() {
        assertEquals("Fast test", 1,2);
    }

    @Test
    @Category({SlowTests.class})
    public void slow() {
        assertEquals("Slow test", 1,2);
    }
}
```

> 📝 If you add  @Category()
> 📝 public class AllTests {..  to your test class definition, all test-methods in that class
> 📝 will be run by the SlowTests category. This will happen even if the method only is marked with the FastTests category.

#### Category markers

SlowTests category
```java
public interface SlowTests {
}
```

FastTests category
```java
public interface FastTests {
}
```
