# SaaS BI Comparison

|  |  |  |  |
| --- | --- | --- | --- |
|  | [PivotLink AnalyticsCloud](http://www.pivotlink.com/products/analyticscloud) | [BIRT OnDemand](http://www.birtondemand.com/) |  |
| Data model | Column | [Amazon RDS](http://aws.amazon.com/rds/#functionality), cubes |  |
| ETL | Flat file (CSV) -> ftp upload | [Sync between RDBMS using Talend Open Studio](http://bod-wiki.birtondemand.com/wiki/index.php?title=Synchronizing_data_to_BIRT_onDemand_RDS_using_Talend_Open_Studio), [DBSync](http://www.birt-exchange.com/be/demos/BoD11/Data/D-4_syncRDS_flash/D-4_sync.html) [Tutorial D-1](http://www.birt-exchange.com/be/demos/BoD11/Data/D-1_UploadRDS_flash/D-1_UploadDataRDS.html) |  |
| Performance / scalability | SaaS, handles big data, fast as data is kept in-mem | SaaS, claims linear scalability, limited by Amazon RDS? |  |
| IAM | [using AD via OneLogin](http://app.onelogin.com/connector/pivotlink-single-sign-on) | [Authentication and authorization](http://bod-wiki.birtondemand.com/wiki/index.php?title=Authentication_and_Authorization#3_-_Authentication.2FAuthorization_Schemes) |  |
| Cost structure |  | [Monthly fee per user + initial setup](http://www.birtondemand.com/bod/services/sign-up-for-services/) |  |
| Who creates reports | Business | Business |  |
| Documentation | Commercial | Extensive docs available for free |  |
| Integration with external webapp |  | [WebViewer](http://www.birt-exchange.org/org/wiki/index.php?title=GSG:Getting_Started_with_WebViewerExample) |  |
|  |  |  |  |
|  |  |  |  |

<http://www.gartner.com/technology/reprints.do?id=1-1DZLPEP&ct=130207&st=sb>
