# Solr Search

### Search installation

|  | **stop and start solr** |

- Config: /home/solr/solr
- Log: /var/log/solr

|  | **update index** |

- Rebuild index use "python manage.py rebuild\_index
- The update is also run by **chron** job. Initially every 10 min. See the crontab on server to verify.

---

### Getting started, with alterations

<http://www.alexanderinteractive.com/blog/2012/08/getting-started-with-solr-and-django/>

**Solr**  
version 4.1.0\*
<http://apache.uib.no/lucene/solr/4.1.0/solr-4.1.0.zip>

**Install Haystack**

**In-Git changes**

- cvapp/settings.py
- cv/search\_indexes.py
- templates/search/indexes/cv

**Solr - Schema.xml**

- generate via
- Edit lang/stopwords\_en.txt
- add fieldsNew note content
- copy file to solr/collection1/conf/schema.xml
- check in to cvapp/solr/conf
- restart solr

**cv/search\_indexes.py**  
Search in your code for index\_queryset, you will see that you have to add \*\*kwargs or using=None

### Solr setup

- collection1, is defaultCoreName. Ok for single core.
- Indexes are defined in: solrconfig.xml (./solr/collection1/conf/solrconfig.xml)

**Documentation on web**

- [solrconfig.xml](http://wiki.apache.org/solr/SolrConfigXml#indexConfig_Section)
  - solrconfig.xml is the file that contains most of the parameters for configuring Solr itself.
- [schema.xml](http://wiki.apache.org/solr/SchemaXml)
  - The schema.xml file contains all of the details about which fields your documents can contain, and how those fields should be dealt with when adding documents to the index, and when querying those fields.
  - We are using a schema.xml produced by Haystack, and then altered as seen above.

### lxml install

Need version 3.0.1

### Jetty install

Config are described here:
<http://wiki.apache.org/solr/SolrJetty>

**Jetty config** /etc/default/jetty

Running single instance for now
