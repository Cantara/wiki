# Web Application JigZaw

## Why is [JigZaw](JigZaw.md) good for webapps?

Because:
- There are lots of test-categories for webapps alone
- We need quick rountrips
- We need control, configuration, web.xml

**For web testing implementations, see [Web testing](Web-testing.md).**

### JigZaw 
    - Common test problems and how to solve them (**programming**)
    - Complete solution for using embedded **webservices** for service/system testing. (**programming**)
    - Complete solution for using embedded **database** for service/system testing. (**programming**)

### Flow report
- Different browser results
- Test reports
- Screenshots

### Test kinds:

- HTML
- JavaScript
- System
- Interceptors
- Action (input, validation) (unit tests)
- Action execution (remember to mock 

the underlying services and reponses!)
- Action Data Passing?

### How to test long flows?
Answer: Well, it will just have to be a unit-test.

We like frameworks that let us test

- Sequence
- Data passing
- (Exception)
- (Transactions/rollback)

## JigZaw applied to the classic webapp

A typical three layered web app has the following layers: 

- **Web** layer
- **Business Logic layer (BL)**
- **Data Access** layer (DA, persistence, CRUD) 

The web layer is only responsible for the **VIEW**. 

The service layer is really, really thin, no complex business logic at all. 

The data access layer is reponsible for CRUD operations against an ER-database. 85% of the functionality of the application is pure CRUD. 

We will here try to explain how OW test model can be applied to this kind of model. 

## Suggested solution:

Service tests that cover the BL-layer and DA-layer. The service layer is so thin that there is little here to test other than a thourough vertical. There are very few DA tests that make sense being done without a (in-memory) database, so there aren't any unit-tests.

If you can avoid business logic in the web layer you can test this in isolation from the data/service providers (BL layer).

The intention of this is to avoid complex/fragile/non-changable end-to-end tests and replace these with fewer service tests with clear and limited responsibility. This gives more changable code and tests.
