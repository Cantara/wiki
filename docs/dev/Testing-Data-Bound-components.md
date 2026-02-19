# Testing Data Bound components

#### Mapping between different types of tests and JigZaw categorization 

###### Test the query logic

No data (or more precisely, _known_ data), no environment (in-memory database) => tests should be fast enough to run before checkin. 

**Responsibility**: 

- CRUD, best case (with empty and pre-populated database) 
- CRUD, min/max values and other boundaries
- Encoding
- ordering 
- duplicates 
- lazy loading 

###### Test caching 

todo 

#### Test isolation levels 
 
todo

###### Test performance and how the DA component handles real-life input 

With data, with environment => slow tests, should be run by CI server. 

Since testing the DA service/component is so expensive it might be advantageous to include it in a full system test. Either way, it should cover the following: 

- some complex CRUD 
- Different combinations of SELECT statements
    - a single tuple (test that each field contains the expected data)
    - a list of tuples (test ordering, duplicates, lazy loading and possibly paging)

#### Concrete strategies for implementation 

###### How to test DAOs when each method in a DAO class contains concrete queries

See http://svn.abakus.no/naut/trunk/naut/src/test/java/no/abakus/naut/NautTestBase.java
 and 
http://svn.abakus.no/naut/trunk/naut/src/test/java/no/abakus/naut/da/quote/IQuoteStorageTest.java

###### Repository approach 

todo: a example that shows how the repository approach can be tested
