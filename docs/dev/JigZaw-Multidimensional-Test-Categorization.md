# JigZaw Multidimensional Test Categorization

#### JigZaw Multidimensional Test Categorization

Classic test categorization, inspired by the V-model, often use *unit*, *integration*, *system* and *acceptance* tests as test groups. The tests are hierarchical and overlapping.

In JigZaw a multidimensional test categorization is used and a test can be given multiple tags. Overlap between tests should be kept at a minimum. The purpose of this test categorization is to support communication when designing, implementing and running tests. These characteristics can then be used to determine *who*, *where* and *when* a given test should be run. See [Timeline](/web/20210123072030/https://wiki.cantara.no/display/dev/Timeline "Timeline") for the details.

| Dimension | Description |
| --- | --- |
| **execution time** | fast or long-running tests, which restricts when it can be run |
| **data** | separate data-driven tests from regular functionality tests |
| **distribution** | in process, out-of process, distributed, in *test controlled* servlet- or application container |
| **platform** | run in environment similar/equal to production environment, including operating system, the *real* database, JMS platform, JNDI, app-server platform, ESB platform et al. |
| **integration** | integration with external services or availability of sensors or hardware components |

###### Examples

| Test description | Execution time | Data | Distribution | Platform | Integration |
| --- | --- | --- | --- | --- | --- |
| "Unit test" (plain business logic) | Fast | Controlled data | In-process, white-box | same Java and OS as production | independent of external systems |
| Algorithm correctness, complete verification | depends | Controlled data | In-process |  | no |
| Logic which use algorithm, focus in correct behaviour for a specific use case | depends | Controlled data | In-process |  | no |
| REST endpoints, verify http responses | Medium | Controlled data | out-of-process, black-box | in-mem database | independent of external systems |
| Record and replay (logic AND database) | Slow | Data-driven | In-process, white-box | real database | (database) |
| "System test": Multiple applications, queue and db infrastructure, verify functionality end-to-end | Slow | Controlled data | out-of-process (distributed) | production-like environment | yes, plenty |
| "System regression test" - nightly/weekly re-run of a set of the most common end-to-end process flows | Very slow | Controlled load, and result verification | IntTest / QA environment | PreProd | full PreProd platform |

#### Other test categorizations

- Unit, component, system test
  - [In pursuit of code quality: Use test categorization for agile builds](http://www.ibm.com/developerworks/java/library/j-cq10316/)
  - [Software Testing Categorization, Misko Hevery](http://misko.hevery.com/2009/07/14/software-testing-categorization/)

---

Back to [JigZaw Design Principles and Drivers](/web/20210123072030/https://wiki.cantara.no/display/dev/JigZaw+Design+Principles+and+Drivers "JigZaw Design Principles and Drivers")
