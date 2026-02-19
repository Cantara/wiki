# Data Mapping in EDR

### Definition:

Mapping data between Provider Objects and a Domain Object.

- Data Mapping should also be able to reverse, from the Domain Object to the Provider Object.

### Reason:

A clear statement on how data should be mapped will ease the implementation of EDR. This statement will also simplify the transition from basic to advanced mapping strategies.

### Enforcement:

We recommend using data mapping. Data Mapping is a extension to EDR, not mandatory.

### Strategies:

- Objects dedicated for Mapping
- XSLT - Using XML and XSL to transform data from one object to the other
- External tool to perform the mapping.
- Mapping service (advanced mapping)

We do not recommend that the Service Factory or Repository Controller contains the code to perform the Data Mapping for the following reasons:

- Cluttering of concerns
- Harder to let the code evolve as experience with the functionality is gained.  
  [Mapping New Object based on two domain objects]  
  [Mapping Update with simple rules]  
  [Mapping Merge Contact Person]

  ### Mapping New Object based on two domain objects

  Address from CRM  
  Account number from ERP system (eg. SAP)

### Merge a contact person that are defined in both systems

### Update

### Mapping service

Why:

- Handle advanced mappings of datatypes.
- Handle that one or more sub systems are unavailable for read and update.
- Decision rules for update.
- Detect inconsistency in the same data, in different subsystems.
- Automatically update or report findings of inconsistent data.
- Single point of entry for all data mappings, regardless of service used.
