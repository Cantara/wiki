# Role Based versus Attribute Based Access Control and Whydah access design

Attribute<sub>~based access control defines a new access control paradigm whereby access rights are granted to users through the use of policies which combine attributes together. The policies can use any type of attributes (user attributes, resource attributes, environment attribute etc.). Attribute values can be set</sub><sub>valued or atomic</sub><sub>valued. Set</sub><sub>valued attributes contain more than one atomic values. Examples are role, project. Atomic</sub><sub>valued attributes contains only one atomic value. Examples are clearance, sensitivity. Attributes can be compared to static values or to one another thus enabling relation</sub>~based access control.

Source: Wikipedia

In computer systems security, role<sub>~based access control (RBAC)[1](1.md)[2](2.md) is an approach to restricting system access to authorized users. It is used by the majority of enterprises with more than 500 employees,[3](3.md) and can implement mandatory access control (MAC) or discretionary access control (DAC). RBAC is sometimes referred to as role</sub>~based security.
....
RBAC differs from access control lists (ACLs), used in traditional discretionary access-control systems, in that it assigns permissions to specific operations with meaning in the organization, rather than to low level data objects. For example, an access control list could be used to grant or deny write access to a particular system file, but it would not dictate how that file could be changed. 

Source: Wikipedia

### Whydah's approach

Since one of Whydah's main design goals is ease of use and ease of integration, we have implemented a variation of ABAC. Like most ABAC implementations, we provide the application with several access<sub>~attributes for the user. Typically we see that the **RoleName** is used in combination with **SecurityLevel**, **ApplicationName** and properties in the **On</sub>~BehalfOf** attribute. 

As most of the Whydah developers come from a system and application development background, we know that a centralized mapping of all the Application Attribute concerns does not scale\[1\](1.md), so Whydah does not try to force the meaning of the user access attributes to the application or system, which also add ease of use and integration without scarifying security.
 

---
Notes:

\[1\](1.md) We can scale the load to Whydah, and even if this will increase the size of the UserTokens, wcan handle that. But having administrators manage this complexity in a system with tens or hundreds of applications does result in over<sub>~simplification (and less security) and lots of access</sub><sub>pains as a result or mis</sub><sub>intrepidation and lack of inner</sub>~knowledge of the specific application access properties.
