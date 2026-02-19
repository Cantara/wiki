# ApplicationData

**[Diagram: ApplicationDataModel](../Diagram/ApplicationDataModel.md)**

### Example Application.XML

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
<application>
  <applicationid> id </applicationid>
  <applicationname> name </applicationname>
  <defaultrolename> defaultrolename </defaultrolename>
  <defaultorganizationname> defaultorganizationname</defaultorganizationname>
  <organizationsnames>
     <organizationname> availableOrgName1 </organizationname>
     <organizationname> availableOrgName2 </organizationname>
     <organizationname> availableOrgName3 </organizationname>
  <organizationsnames>
</application> 
```

**Example Applications.JSON**
```js
[  
   {  
      "id":"id1",
      "name":"test",
      "defaultRoleName":"default1role",
      "defaultOrgName":"defaultorgname",
      "availableOrgNames":[  
         "developer@customer",
         "consultant@customer"
      ]
   },
   {  
      "id":"id2",
      "name":"test2",
      "defaultRoleName":"default1role",
      "defaultOrgName":"defaultorgname",
      "availableOrgNames":[  
         "developer@customer",
         "consultant@customer"
      ]
   }
]
```

### Example **Whydah 2.1** Application.XML

Whydah 2.1 Alpha - subject to change
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
<application>
  <applicationid> id </applicationid>
  <applicationname> name </applicationname>
  <applicationurl> http(s)://myUrl </applicationurl>
  <applicationlogo> http(s)://link_to_logo </applicationlogo>
  <applicationdescription> some short description </applicationdescription>
  <applicationauditlevel>0</applicationauditlevel>
  <usertokenfilter>true</usertokenfilter>  <!-- default = TRUE = only this applictions roles in usertoken -->
  <defaults>
    <defaultrolename> defaultrolename </defaultrolename>
    <defaultorganizationname> defaultorganizationname</defaultorganizationname>
  </defaults>
  <organizations>
     <organizationname> registeredOrgName1 </organizationname>  <!-- Do we need more data here? -->
     <organizationname> registeredOrgName2 </organizationname>
     <organizationname> registeredOrgName3 </organizationname>
  <organizations>
  <roles> 
     <rolename> employee </rolename>   <-- Do we need more data here? -->
     <rolename> manager </rolename>
     <rolename> editor </rolename>
  <roles>
  <security>
     <minimumsecuritylevel>2<minimumsecuritylevel> <!-- the higher the more secure -->
     <minimumDEFCON>4</minimumDEFCON>  <!-- lower is closer to thermal nuclear war  -->
     <minumumUpdateFrequency>60d</minumumUpdateFrequency> <!-- compliance on longlivity of botstrap secret -->
     <crypto>
        <cryptoid/><algorithm/><seed/><secret/>  <!-- need more work -->
        <cryptoid/><algorithm/><seed/><secret/>
        <cryptoid/><algorithm/><seed/><secret/>
        <cryptoid/><algorithm/><seed/><secret/>
        <cryptoid/><algorithm/><seed/><secret/>
     </crypto>

  </security>
</application> 
```
---
