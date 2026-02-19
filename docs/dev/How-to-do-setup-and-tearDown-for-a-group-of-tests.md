# How to do setup and tearDown for a group of tests.

TestNG supports sorting of tests into groups. I can be convenient to be able to perform a group wide setup, before, and teardown, after, the tests in a group are run. This can be accomplished in testNG using the BeforeGroups annotation.

- [Sort your tests into logical groups.](http://wiki.community.objectware.no/display/smidigtonull/Maven+FAQ#MavenFAQ-HowtohandledifferentgroupsoftestsseparatelywithTestNG%3F)
- Write test-helper class(es) containing the setup and teardown for the test group(s).
    - It is recommended to write one test-helper for each test group, but if two groups, or more, share exactly the same setup and teardown logic the test-helper can be used by all groups.
    - As of writing, **both** the _groups_ and _value_ parameters must be set to make this configuration work. This is not what you would expected after reading the [testNG documentation of BeforeGroups](http://testng.org/javadocs/org/testng/annotations/BeforeGroups.html).

###### A test-helper class.
```
class MyDatabaseTestHelper {

  @BeforeGroups(groups = { "database"}, value = { "database"})
  public void setup() {
    //some setup logic
  }

  @AfterGroups(groups = { "database"}, value = { "database"})
  public void tearDown() {
    //some tearDown logic
  }
}

```
