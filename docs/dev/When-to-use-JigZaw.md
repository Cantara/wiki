# When to use JigZaw

```
{section}
{column:width=33%}
h4. Remote centric architecture
Your system has:
* Mulitiple JVM's
* Large DB's
* JMS - Eventing
* Maybe even C++ interactions

Standalone application:
* [Standalone application example] - not relevant in this form
{column}
{column:width=33%}

h4. Traditional 3 layer webserver
Fix the problem with end-to-end testing.
* Depends on data to be successfull.
* Depends on the GUI not to be altered.
* Time-consuming
* Hard to reproduce/re-run the tests.
* [Web Application JigZaw] - not relevant in this form
{column}
{column:width=33%}

h4. Enterprise Testing
Where manual testing is regarded as the only solution. How JigZaw can automate some of this testing.
* Cooperation with manual testers
* Ensure your tests are documented, automatically.
* Ensure tests are able to be re-run in later releases.
* When you are not able to alter the data in your database.

{column}
{section}
```
