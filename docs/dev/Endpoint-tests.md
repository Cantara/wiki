# Endpoint tests

The responsibility of endpoint tests is to verify that the wiring and configuration of the endpoints works as intended. 

It is often a good idea to use stubs instead of the actual services. We recommend [Mockito](http://mockito.github.io/mockito/docs/current/org/mockito/Mockito.html#2) for stubbing the services behind the endpoints. 

#### JMS 

- [Embedded ActiveMQ JMS Server (Spring)](Embedded<sub>~ActiveMQ</sub><sub>JMS</sub><sub>Server</sub>~Spring.md)

- Start ActiveMQ (in-mem) programmatically 

#### HTTP 

To verify that the HTTP endpoints work as expected it is of course necessary to start a web server. The approach taken here is to run the application (which embeds a web server), but override the implementation behind the endpoints. 

###### REST 

1. [Start Jetty application with stubbed services](Start<sub>~Jetty</sub><sub>application</sub><sub>with</sub>~stubbed-services.md)
1. Run requests against the service and verify the expected response (both response code and content). 
    1. [REST<sub>~assured](https://code.google.com/p/rest</sub>~assured/) can simplify the request and assert parts of this. 

###### SOAP 

1. [Start Jetty application with stubbed services](Start<sub>~Jetty</sub><sub>application</sub><sub>with</sub>~stubbed-services.md)
1. Run requests against the service and verify the expected response (both response code and content). 

CXF example: 
```
@BeforeMethod
public void setUpWSClient() {
    ReceiptControlService_Service ss = new ReceiptControlService_Service(wsdlLocation, serviceName);
    port = ss.getReceipt();

    Client client = ClientProxy.getClient(port);
    Endpoint cxfEndpoint = client.getEndpoint();

    Map<String,Object> outProps = new HashMap<>();
    outProps.put(WSHandlerConstants.ACTION, WSHandlerConstants.USERNAME_TOKEN);
    outProps.put(WSHandlerConstants.USER, "userNameTestUser");
    outProps.put(WSHandlerConstants.PASSWORD_TYPE, WSConstants.PW_TEXT);
    //Password in WSClientPasswordHandlerForTests must match password known/added to WS-server 
    outProps.put(WSHandlerConstants.PW_CALLBACK_CLASS, WSClientPasswordHandlerForTests.class.getName());
    WSS4JOutInterceptor wssOut = new WSS4JOutInterceptor(outProps);
    cxfEndpoint.getOutInterceptors().add(wssOut);
}

@Test
public void testPing() throws Exception {
    final String pingResponse = port.ping();
    assertEquals(pingResponse, "pong");
}

class WSClientPasswordHandlerForTests implements CallbackHandler {
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        WSPasswordCallback pc = (WSPasswordCallback) callbacks[0];
        pc.setPassword("someTestPasswordHere");
    }
}
```

See also [http://stackoverflow.com/questions/5906154/apache<sub>~cxf</sub><sub>credentials</sub><sub>not</sub><sub>being</sub><sub>sent</sub><sub>from</sub><sub>wss4joutinterceptor](http://stackoverflow.com/questions/5906154/apache</sub><sub>cxf</sub><sub>credentials</sub><sub>not</sub><sub>being</sub><sub>sent</sub><sub>from</sub>~wss4joutinterceptor).
