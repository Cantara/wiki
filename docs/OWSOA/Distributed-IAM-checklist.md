# Distributed IAM checklist

### Stage 1: Intra<sub>~org Web Single Sign</sub>~on - Central Identity Provider
        
- Policy Steps                     
    - Define who establishes various policies related to single sign-on (SSO) and authentication                  
    - Have basic identity management policies in place, including data and service stewardship responsibilities and use of the system                     
    - Have policy in place specifying whether NONE/SOME/ALL campus authenticated web sites are REQUIRED to use the central single sign-on system        
- Business Practice Steps
    - Create Help desk support for users encountering problems accessing central web sites protected by SSO                     
    - Reliably issue credentials to on-campus faculty/staff/students                     
    - Create Help desk support for users encountering problems accessing department web sites protected by SSO        
- Technical - Basic Identity and Access Management Steps                     
    - Provision/de<sub>~provision accounts for and authenticate on</sub>~campus faculty, staff, and students                     
    - Provision/de-provision accounts for and authenticate other constituencies (e.g. applicants, alums, affiliates)
- Technical - Software Steps
    - Install/operate/manage Identity provider software
                                                                                                              1

### Stage 1: Intra<sub>~Web Single Sign</sub>~on - Central and Department Service Provider
- Policy Steps
    - Define how often department service providers should refresh their metadata
    - Promulgate policy describing process and constraints when the service provider is compromised
    - Define minimum operational and environmental requirements for the remote server/application
    - Define policies on log retention at service providers
- Business Practice Steps
    - Create process to register a new service providers (e.g. site inspection requirements)
    - Create problem resolution process for when users cannot access department-supported service provider
    - Create process for service providers to report abuse of their site (e.g. such as by anonymous users)
- Technical - Basic Identity and Access Management Steps
    - Provide tech support to department service provider sites, including documentation  describing the web SSO service (description, process to participate, etc)
- Technical - Software Steps
    - Manage the metadata describing department service providers and provide mechanism for distribution
    - Choose approach to PKI trust within the campus federation (rooted, self-signed)
    - Provide installation instructions, configuration files and other local files (e.g. error pages, logos ) customized to the org for the department sysadmins
                                                                                                                     2

### Stage 2: Attribute Delivery - Central Identity Provider
- Policy Steps
    - Identify attribute source systems and define and describe the set of attributes that are available
    - Identify who governs the decision to release attribute X to service provider Y
    - Develop policy defining, in a general way, which services are eligible to receive which attributes
    - Achieve buy in to attribute release process from Identity stakeholders
- Business Practice Steps
    - Define problem escalation procedure, such as when the wrong attributes are sent to a service provider
    - Define process to follow when n service provider requests an attribute that is not currently available as defined by the policy above
- Technical - Basic Identity and Access Management Steps
    - Maintain a minimal set of attributes describing each user
    - Populate iamPerson attributes for each user
    - Manage entitlement values on user objects
    - Provide support for groups in the local directory and configure Shibboleth to use them
- Technical - Software Steps
    - Configure the identity provider attribute resolver for the appropriate sources
    - Identify who is responsible for editing/implementing the attribute release policies
                                                                                                                  3

### Stage 2: Attribute Delivery - Central and Department Service Providers
- Policy Steps
    - Develop policy governing use of attributes by service providers such as attribute retention, sharing, etc.
- Business Practice Steps
    - Define process an service provider would use to request attributes and the process used to respond to the request
- Technical - Software Steps
    - Document how a service provider's web server could authorize users given the provided attributes
    - Document how an application could use the supplied attributes in alternative ways, such as for customization or form completion

Source: [http://shibboleth.internet2.edu/shib<sub>~checklist</sub><sub>final</sub><sub>website.pdf](http://shibboleth.internet2.edu/shib</sub><sub>checklist</sub><sub>final</sub>~website.pdf)
