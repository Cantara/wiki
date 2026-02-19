# Working with Solr

### Recomended Reading
- [Thinking like Solr<sub>~its not an rdms](http://bibwild.wordpress.com/2011/01/24/thinking</sub><sub>like</sub><sub>solr</sub><sub>its</sub><sub>not</sub>~an-rdbms/)
- [http://boxesandarrows.com/faceted<sub>~finding</sub><sub>with</sub><sub>super</sub><sub>powered</sub><sub>breadcrumbs/](http://boxesandarrows.com/faceted</sub><sub>finding</sub><sub>with</sub><sub>super</sub><sub>powered</sub>~breadcrumbs/)

### Normalization of data

Fields we need:
- Name
- Technology (multi value)
- Company (multi value)
- Intustry (mulit value)
- Experience (multi value)
- (TODO)Competence Entry
    - Rating
    - Used for relevant boosting and/or sorting.

Boost = input enhancement.
Rank = output enhancement.

We start by havning no boost. Do enhancement on search results (vekting) rank.

### Add
http://wiki.apache.org/solr/UpdateXmlMessages

`curl http://localhost:8983/solr/update?commit=true -H "Content<sub>~Type: text/xml" -</sub>~data-binary '<add><doc><field name="id">testdoc</field></doc></add>'`

### Query 
http://wiki.apache.org/solr/SolrQuerySyntax

- http://altubuntu01.cloudapp.net/solr/select?q=totto
- http://altubuntu01.cloudapp.net/solr/collection1/select?q=**%3A**&wt=json&indent=true

### Faceting
http://searchhub.org/2009/09/02/faceted<sub>~search</sub>~with-solr/

- http://altubuntu01.cloudapp.net/solr/select?q=java&facet=true&facet.field=technology

### Boosting
**simple boosts by popularity**
```
  defType=lucene&df=text&q=%2Bsupervillians+_val_:"popularity"
  defType=dismax&qf=text&q=supervillians&bf=popularity
  q={!boost b=popularity}text:supervillians
```

**boosts based on complex functions of the popularity field**
```
  defType=lucene&q=%2Bsupervillians+_val_:"sqrt(popularity)"
  defType=dismax&qf=text&q=supervillians&bf=sqrt(popularity)
  q={!boost b=sqrt(popularity)}text:supervillians
```
