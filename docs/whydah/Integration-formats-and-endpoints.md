# Integration formats and endpoints

To achieve clearly defined responsibility for each module, clearly defined contracts between the components is necessary.
The following decisions have been made with regards to data formats in Whydah: 

- Authentication and session APIs: XML 
    - XML was chosen to not limit interoperability with other IAM products. E.g. SAML/SAML2 are XML based. XML is also the _old and conservative_ choice which might make it easier to accept for conservative organizations. 
- Administration APIs: JSON 
    - JSON is the natural choice for administration APIs because this is the most popular format used for web applications used by humans. 

**Session and Authentication flow**
- Optional HTTP redirect between Application and SSOLoginWebApp.
- XML between client applications and SecurityTokenService.
- XML between SSOLoginWebApp and SecurityTokenService.
- XML between SecurityTokenService and UserAdminService.

**User and Application administration flow**
- JSON between UserAdminWebApp and UserAdminService.
- JSON between client applications with UserAdmin enabled and UserAdminService.

See also [Key Whydah Data Structures](Key<sub>~Whydah</sub>~Data-Structures.md) for a description of the data formats used. 

---

TODO: Rydde 

siden UAS har aksesskontroll ansvar, så kan det være greit at den har et tydelig skille på auth/sesjons API-er  (xml)  og admin apier (JSON)
helt forskjellige usecases..  selvom de kanskje i noen tilfeller trenger metoder som tilsynelatende er like
i UIB kan det være samme metode/API...     for å tenke på dette...   hvis UAS bruker samme metode....  og vi går til DEFCON 3/4...  da blir implementasjonskompleksiteten i den metoden veldig vanskelig å forstå....  i.e.  at en usersesjon skal være lov for XML-varianten men ikke for JSON varianten.. bortsett fra dersom osv  osv..
men det er mulig at vi pakekstrukturmessig kanskje bør organisere dette ryddigere  (og muligens i URI patterns)

kontrakt og forvantningsegenskapene er også forskjellige...  brekker man et XML format, så påvirkes  alle Whydah applikasjoner direkte, også 3 parts apper... brekker man et admin JSON API, så er det hovedsaklig whydah moduler som påvirkes
så i praksis bør XML API<sub>~ene ha et tydelig og eksplisitt on</sub><sub>the</sub><sub>wire format/kontrakt med tilhørende eksplisitte mapping... mens man kan forenkle mappingen til auto</sub>~mapping for json
	
One version of applicationdata is shipped to the collaborating whydah apps, and that contract should be XML
på application auth (ApplicationCredential)  så returneres ApplicationToken (som vil inneholde endel av det nye fra ApplicationData)
men det er egentlig STS sitt ansvar
