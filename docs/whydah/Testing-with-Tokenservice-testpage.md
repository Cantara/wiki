# Testing with Tokenservice testpage

Example of using built in testpage of Tokenservice.

#### Demonstration
Location: [https://demo.getwhydah.com/tokenservice/](https://demo.getwhydah.com/tokenservice/)

##### Step 1
```title
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
     <applicationcredential>
        <params>
            <applicationID>99</applicationID>
            <applicationSecret>33879936R6Jr47D4Hj5R6p9qT</applicationSecret>
        </params> 
    </applicationcredential>
```

##### Step 2
```title
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <usercredential>
    <params>
        <username>testuser</username>
        <password>testuser</password>
    </params> 
</usercredential>
```

##### Step 3

Fetch UserTokenID from response from above query.
Example: 
```title
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><usertoken xmlns:ns2="http://www.w3.org/1999/xhtml" id="0b3701ec-619b-4c7b-9519-2d8123798009">
    <uid>testuser</uid>
    <timestamp>1423643172070</timestamp>
    <lifespan>1209600000</lifespan>
    <issuer>https://demo.getwhydah.com/tokenservice/user/ac627ab1ccbdb62ec96e702f07f6425b/validate_usertokenid/0b3701ec-619b-4c7b-9519-2d8123798009</issuer>
    <securitylevel>1</securitylevel>
    <DEFCON/>
    <username>testuser</username>
    <firstname>Testuser</firstname>
    <lastname>Testuser</lastname>
    <email>testuser@getwhydah.com</email>
    <personRef>0</personRef>
    <application ID="19">
        <applicationName>UserAdminWebApp</applicationName>
        <organizationName>Support</organizationName>
        <role name="WhydahUserAdmin" value="1"/>
    </application>

    <ns2:link type="application/xml" href="https://demo.getwhydah.com/tokenservice/user/ac627ab1ccbdb62ec96e702f07f6425b/validate_usertokenid/0b3701ec-619b-4c7b-9519-2d8123798009" rel="self" />
    <hash type="MD5">ee33ba5d3c8976f9ecf7477fac8928a8</hash>
</usertoken>
```
Use id-field, named **id**, similar to 0b3701ec-619b-4c7b-9519-2d8123798009 to paste into field **Usertokenid**

#### Turning on tokenservice test-functionality in Whydah SecurityTokenService instance
```title
testpage=enabled
```
