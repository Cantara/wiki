# Error Categorization example

### Error levels

**Fatal - Crisis**
Indicates that the system is for most purposes dead. Like if no superPNR are received into the ESB, or that the ESB looses connection with critical systems

**Fatal - Severe**
Indicates that a large set of operations are failing,  i.e. That all operations against Accounting hangs in the queue.

**Error - Reduced service**	
Indicates that a small set of operations are failing, but not any essential services. Like if some simple products are failing.

### Common Error fields

```xml
<error category>
  <errorID/>
  <sessionID/>
  <severity/>
  <system/>
  <action/>
  <message/>
  <details>
    <detail key="name of key">value of detail</detail>
  </details>
  <trace> 
  <entr/> 
  </trace> 
<error category>
```

### Example errors entities

```xml

<error catefory="Booking/Payment">
  <errorID>
     ghjgjyd78678
  </errorID>
  <sessionID> 
     SPNR-2342364726
  </sessionID> 
  <severity>
    critical
  </severity>
  <system id="int_OJ_004">
     Integration/ProductTransform
  </system>
  <action>
     Transforming SuperPNR to BookingDetails
  </action>
  <message>
     Non-conformant SuperPNR received. Could not validate booked product
  </message>
  <details>
    <detail key="xxx">test for key xxx</detail>
  </details>
  <trace>
    <entry>Non-existing sub-product found when trying to add sub-product attributes </entry>
  <trace>
</error>
```
