# UserToken

### What is a UserToken?

A key received by the application on behalf of a logged on user. Should contain information about the user, it's roles and parameters for access control in the application and subordinate services that the application would want to use on behalf of the logged on user.

XML for readability. 1-1 relation to a SAML2 token if that is needed.

- Customer reference
- Name (duplicate of customer name)
- username
- user credentials
- 2 factor endpoint (cell phone number)
- Email

**Security levels**

- 0. 3rd party tokens (FB, NetIQ, OAUTH2), Pin-Login, Pin-signup and persistent cookie(s)
- 1. username & password
- 2. 2 factor auth
- 3. EID
- 4. BankID

- Metadata
  - Expiry
  - (last seen)

**Main structure**

### How to extract data from a UserToken?

We recommend using [XPath](http://www.w3schools.com/xpath/) to extract data from a UserToken. Some [UserToken XPATH Examples](/web/20210922174127/https://wiki.cantara.no/display/whydah/UserToken+XPATH+Examples "UserToken XPATH Examples")  
This ensures that existing applications will not be affected when content/structure needs to be changed when introducing new applications.

### UserToken example

**Note: As of Whydah 2.1, the returned UserToken is filtered through an applicationTokenID, and will thus only return the roles of the application it is sent to**

### UserToken example
