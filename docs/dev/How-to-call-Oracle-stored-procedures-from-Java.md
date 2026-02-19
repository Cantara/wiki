# How to call Oracle stored procedures from Java

#### Using CallableStatement 

- [Using CallableStatement methods to call stored procedures](http://publib.boulder.ibm.com/infocenter/db2luw/v8/index.jsp?topic=/com.ibm.db2.udb.doc/ad/tjvcscsp.htm)

###### Get connection from Spring DataSourceUtils

```java
import org.springframework.jdbc.datasource.DataSourceUtils;

Connection con =  DataSourceUtils.getConnection(dataSource);				
String procedureRef = "somePackage" + "." + "someProcedure";
CallableStatement cstmt = con.prepareCall("{call " + procedureRef + "(?,?)" + "}");
cstmt.setInt(1, inParam1);
cstmt.setInt(2, inParam2);
cstmt.execute();
con.commit();

DataSourceUtils.releaseConnection(con, dataSource)
```

###### Get connection from HibernateDaoSupport

```java
Connection con = getSession().connection();
String procedureRef = packageName + "." + procedureName;
CallableStatement cstmt = con.prepareCall("{call " + procedureRef + "}");
cstmt.execute();		
con.commit();
```
