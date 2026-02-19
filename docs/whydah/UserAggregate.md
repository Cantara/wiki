# UserAggregate

```
<whydahuser>
    <identity>
        <username>admin</username>
        <cellPhone>+1555406789</cellPhone>
        <email>useradmin@getwhydah.com</email>
        <firstname>User</firstname>
        <lastname>Admin</lastname>
        <personRef>0</personRef>
        <UID>useradmin</UID>
    </identity>
    <applications>
        <application>
            <appId>19</appId>
            <applicationName>UserAdminWebApplication</applicationName>
            <orgName>Support</orgName>
            <roleName>WhydahUserAdmin</roleName>
            <roleValue>1</roleValue>
        </application>
        <application>
            <appId>19</appId>
            <applicationName>UserAdminWebApplication</applicationName>
            <orgName>Support</orgName>
            <roleName>Manager</roleName>
            <roleValue>true</roleValue>
        </application>
        <application>
            <appId>19</appId>
            <applicationName>UserAdminWebApplication</applicationName>
            <orgName>Company</orgName>
            <roleName>WhydahUserAdmin</roleName>
            <roleValue>1</roleValue>
        </application>
    </applications>
</whydahuser>
```

#### Alternative syntax (future possibility) 

1. Find name for triplet roleName, roleValue and orgName and use one entry for all three. 
1. Then each application can have a list of these triplets. 

```
<whydahuser>
    <identity>
        <username>admin</username>
        <cellPhone>+1555406789</cellPhone>
        <email>useradmin@getwhydah.com</email>
        <firstname>User</firstname>
        <lastname>Admin</lastname>
        <personRef>0</personRef>
        <UID>useradmin</UID>
    </identity>
    <applications>
        <application id="19", name="UserAdminWebApplication">
            <role name="WhydahUserAdmin", value="1", orgName="Support" />
            <role name="Manager", value="true", orgName="Support" />
            <role name="WhydahUserAdmin", value="1", orgName="Company" />          
        </application>
        ...
    </applications>
</whydahuser>
```
