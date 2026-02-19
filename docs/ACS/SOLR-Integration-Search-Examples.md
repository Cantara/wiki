# SOLR Integration Search Examples

**Some useful URL shortcuts**

```
http://cv.domain.org/cv/?q=solr java&fq={"department_exact":["Software Engineering"],"location_exact":["Oslo"]}&expfrom=3&expto=22
```
- List the persons which
    - Have department set to **Oslo**
    - Have Department set to **Software Engineering** (Practise)
    - Have between **3 and 22 years of experience**
    - And matches both **java** and **solr**

- http://cv.domain.ogr/cv/?q=-fulljson:"completeness+percent+100"~1

**Example queries**

```
?q=java
?q=(SOA AND Java)
?q=(Java AND maven AND Continous Production)
?q=(Java AND (Bank OR Finance OR Finans))
* Developers who have *not* worked for Telenor
?q=(java OR .net) (*:* -Telenor)^999
* List only 100% profiles  (find completeness percent and 100 within 4 words from each other in the fulljson field in the index
* ?q=fulljson:"completeness+percent+100"~1
```
Can be used both in URL-queries and in search field in GUI frontend and in solr/json integration API

**Further references:**

- [http://wiki.apache.org/solr/SolrRelevancyFAQ](http://wiki.apache.org/solr/SolrRelevancyFAQ)
- [http://wiki.apache.org/solr/CommonQueryParameters](http://wiki.apache.org/solr/CommonQueryParameters)
