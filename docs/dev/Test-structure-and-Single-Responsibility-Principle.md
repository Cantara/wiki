# Test structure and Single-Responsibility Principle

# Part 2

## One and only one reason to change

[Single-responsibility principle (SRP)](http://www.objectmentor.com/resources/articles/srp.pdf): A test should have only one reason to change. Test code (as well as regular code) is then easier to refactor and easier to maintain. These attributes are by themselves enticing. Further, tests should be structured in such a way that if one test fails you know exactly where the problem is. This simplifies debugging, since the error message produced by the failed test explains what failed in a precise manner.

## Refactorization boundary

With refactoring support in most IDEs, most code refactorings are easy and low-risk changes. However, not everything should be subject to frequent refactorings. A public API is a typical example of an interface we want to be stable and may thus be considered _{+}refactorization boundaries{+}_. Easy refactoring without compromising the stability of the API can be achieved by enforcing the following guidelines: 

- Write _intention revealing interfaces_. (**TODO**: ref to DDD) 
- Keep interfaces free from implementation specific naming. 
- When implementing a method defined in a interface within the refactorization boundary, don't put functionality directly in that method, but use it as a wrapper for calls to separate methods. These separate methods and their tests can thus easily be refactored without compromising the stability of the public API. 

Structuring code in this matter not only facilitate refactoring, but it adds a level of indirection that makes it easier to structure the tests. 
1. Each separate method can be tested in isolation. If the code is trivial, the method can have _private_ access modifier and a separate test can be omitted. If the code is non-trivial, the method can be given _protected_ access modifier and tested in a separate method. (Testability trumphs encapsulation.)
2. Since the interface is stable, the test for this functionality is also stable. The test for the interface, or service, is loosely coupled to the implementation. 

The advantage of adding this level of indirection high cohesion between the test and the code that is tested in 1 and loose coupling between the system/acceptance test for stable interface and the actual implementation.  

###### Example 

The code snippet to the left shows how retrieve-functionality for a User can be designed. Switching from database to file based storage will force the developers to
a) rename _fetchUserFromDatabase_\-meimplements UserManagerthod or
b) do nothing and accept inconsistency between what the interface communicates and what the code actually does. 
(Break backward compatibility is not an option.)

In the code snippet to the right, the interface reveals only intent and gives no hint as to how this should be implemented. The implementation can thus be refactored easily, without changing the interface. 

```
public interface UserManager() {
  User fetchUserFromDatabase(String userId);
}

public class UserManagerImpl implements UserManager {
  private UserDao userDao;

  public User fetchUserFromDatabase(String userId) {
    return userDao.fetchUser(userId);
  }
}
```

```
public interface UserManager implements UserManager {
  User fetchUserFromDatabase(String userId);
}

public class UserManagerImpl() {
  private UserDao userDao;

  public User findUser(String userId) {
    return fetchUserFromDatabase(userId);
  }
  private User fetchUserFromDatabase(String userId){
    return userDao.fetchUser(userId);
  }
}
```

While the example is overly simplistic, it should illustrate how the indirected recommended above can be implemented. 

## Dependent tests

If you want to test your database implementation you will need a database. If the database is unavailable, all database tests will fail. A developer with in<sub>~depth knowledge of the application will probably quickly come to the conclusion that the database is unavailable if a hundred DAO</sub>~tests fail. However, why do 100 tests fail due to a single failure?

The solution is to introduce dependencies between tests. E.g., create at _testDatabaseConnectionTest_ and let all DAO<sub>~tests depend on it. All DAO</sub>~tests can thus be skipped if the _testDatabaseConnectionTest_ fail. This makes the test failure easier to debug.

**TODO**: ref to the Advanced Java testing book.

## Mapping between user requirements and tests 

While made more explicit in BDD methodology, the concept of using the name of a method to reveal its purpose is nothing new. In fact, it might be considered a common, good programming practice. Nevertheless, by putting some effort into good naming, both code and tests alike become easier to interpret for both technical and non-technical personell.  

A mapping between tests and user requirements (hopefully in the format of user stories) can be made more explicit if tests are grouped according to which requirement or user story they are relevant for. A test report sorted by group can thus be used as a means of communication between the customer and the developers. While it may be a bit optimistic, it should be possible to define a set of groups that combined defines the acceptance criteria for the system. This requires a high degree of involvement from the customer and a certain minimum level of mutual trust. These two prerequisites are probably the only blockers for realizing this _**acceptance test report**_, the technical support already exists. 

The _**acceptance test report**_ and the inverse of this report should make it possible to identify functionality and tests that can safely be removed. 

**TODO**: Utdype hvorfor dette er så viktig?
