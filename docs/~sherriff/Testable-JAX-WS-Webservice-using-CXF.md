# Testable JAX-WS Webservice using CXF

#### Description 

- Framework: [CXF](http://cxf.apache.org/docs/index.html)

- Front end: [JAX<sub>~WS](http://cxf.apache.org/docs/jax</sub>~ws.html)

- Protocol (WSDL) binding: [Soap 1.2](http://cxf.apache.org/docs/soap-12.html)

- Data binding: [JaxB](http://cxf.apache.org/docs/jaxb.html) or XPath 
    - XPATH rett på XML payloaden gir løsere kobling enn JaxB
    - en annen fordel med å splitte endepunkt og payload på denne måten er at samme test/klient plutselig støtter flere transportmekanismer, og man kan teste klientene lokalt
    - det kan virke som det ikke oppleves som naturlig å skille for prosjekter som bruker jaxb, siden payloaden blir generert på den ene siden og auto-mappet på den andre siden, som gjør at folk driter i hvordan payloaden faktisk ser ut
    - mindre fingerfeil med xpath enn med jaxb, skjemaer, jaxb, soap og navnerom skaper trøbbel for de fleste ferske
    - [Why StAX?](http://download.oracle.com/docs/cd/E17802_01/webservices/webservices/docs/1.6/tutorial/doc/SJSXP2.html) - StAX gir først mening på monstermeldinger og det å plukke ut payloaden i en String/stream som xpath parser er jo ikke heavy

- Versioning 
    - med xpath så komemr det ann på.... som konsument så kommer det ann på hvordan du skriver uttrykkene.... i.e. ren [duck typing](http://en.wikipedia.org/wiki/Duck_typing) vil fungere helt til parametrene endrer navn/semantikk
    - evt. så kan du skrive uttrykk mhhp versjonstagger i dokumnetet 

#### Tests 

###### Test integration between client and endpoint 

- Out<sub>~of</sub>~process using separate Jetty server 

###### Test payload parsing 

- In-process
    - JaxB: a single test, since the interpretation is static 
    - XPath: one test per client as each client can choose to use a different set of elements from the payload.
