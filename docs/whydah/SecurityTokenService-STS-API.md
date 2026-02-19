# SecurityTokenService (STS) API

```

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<application xmlns="http://research.sun.com/wadl/2006/10">
    <doc xmlns:jersey="http://jersey.dev.java.net/" jersey:generatedBy="Jersey: 1.6 03/25/2011 01:14 PM"/>
    <resources base="http://localhost:9998/tokenservice/">
        <resource path="/">
            <method id="info" name="GET">
                <response>
                    <representation mediaType="text/html"/>
                </response>
            </method>
            <resource path="/applicationtokentemplate">
                <method id="getApplicationTokenTemplate" name="GET">
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/applicationcredentialtemplate">
                <method id="getApplicationCredentialsTemplate" name="GET">
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/usercredentialtemplate">
                <method id="getUserCredentialsTemplate" name="GET">
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/logon">
                <method id="logonApplication" name="POST">
                    <request>
                        <representation mediaType="application/x-www-form-urlencoded">
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationcredential" style="query" type="xs:string"/>
                        </representation>
                    </request>
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="{applicationtokenid}/validate">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <method id="validateApplicationtokenid" name="POST">
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
        </resource>
        <resource path="/token">
            <resource path="/usertokentemplate">
                <method id="getUserTokenTemplate" name="GET">
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/{applicationtokenid}/usertoken">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <method id="getUserToken" name="POST">
                    <request>
                        <representation mediaType="application/x-www-form-urlencoded">
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="apptoken" style="query" type="xs:string"/>
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="usercredential" style="query" type="xs:string"/>
                        </representation>
                    </request>
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/{applicationtokenid}/{ticket}/usertoken">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="ticket" style="template" type="xs:string"/>
                <method id="getUserToken" name="POST">
                    <request>
                        <representation mediaType="application/x-www-form-urlencoded">
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="apptoken" style="query" type="xs:string"/>
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="usercredential" style="query" type="xs:string"/>
                        </representation>
                    </request>
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/{applicationtokenid}/{ticket}/createuser">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="ticket" style="template" type="xs:string"/>
                <method id="createAndLogOnUser" name="POST">
                    <request>
                        <representation mediaType="application/x-www-form-urlencoded">
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="apptoken" style="query" type="xs:string"/>
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="usercredential" style="query" type="xs:string"/>
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="fbuser" style="query" type="xs:string"/>
                        </representation>
                    </request>
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/{applicationtokenid}/validateusertoken">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <method id="validateUserTokenXML" name="POST">
                    <request>
                        <representation mediaType="application/x-www-form-urlencoded">
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="usertoken" style="query" type="xs:string"/>
                        </representation>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
            <resource path="/{applicationtokenid}/validateusertokenid/{usertokenid}">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="usertokenid" style="template" type="xs:string"/>
                <method id="validateUserTokenID" name="GET">
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
            <resource path="/{applicationtokenid}/getusertokenbytokenid">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <method id="getUserTokenById" name="POST">
                    <request>
                        <representation mediaType="application/x-www-form-urlencoded">
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="apptoken" style="query" type="xs:string"/>
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="usertokenid" style="query" type="xs:string"/>
                        </representation>
                    </request>
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/{applicationtokenid}/getusertokenbyticket">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <method id="getUserTokenByTicket" name="POST">
                    <request>
                        <representation mediaType="application/x-www-form-urlencoded">
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="apptoken" style="query" type="xs:string"/>
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="ticket" style="query" type="xs:string"/>
                        </representation>
                    </request>
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
            <resource path="/{applicationtokenid}/releaseusertoken">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <method id="releaseUserToken" name="POST">
                    <request>
                        <representation mediaType="application/x-www-form-urlencoded">
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="usertokenid" style="query" type="xs:string"/>
                        </representation>
                    </request>
                    <response>
                        <representation mediaType="*/*"/>
                    </response>
                </method>
            </resource>
            <resource path="/{applicationtokenid}/transformusertoken">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="applicationtokenid" style="template" type="xs:string"/>
                <method id="transformUserToken" name="POST">
                    <request>
                        <representation mediaType="application/x-www-form-urlencoded">
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="usertoken" style="query" type="xs:string"/>
                            <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="tp_applicationtoken" style="query" type="xs:string"/>
                        </representation>
                    </request>
                    <response>
                        <representation mediaType="application/xml"/>
                    </response>
                </method>
            </resource>
        </resource>
        <resource path="/files">
            <resource path="/js/{filename}">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="filename" style="template" type="xs:string"/>
                <method id="getJsFile" name="GET">
                    <response>
                        <representation mediaType="application/x-javascript"/>
                    </response>
                </method>
            </resource>
            <resource path="/css/{filename}">
                <param xmlns:xs="http://www.w3.org/2001/XMLSchema" name="filename" style="template" type="xs:string"/>
                <method id="getCssFile" name="GET">
                    <response>
                        <representation mediaType="text/css"/>
                    </response>
                </method>
            </resource>
        </resource>
    </resources>
</application>
```
