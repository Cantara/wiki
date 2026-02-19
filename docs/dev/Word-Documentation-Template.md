# Word Documentation Template

Scratch area, needs clean-up

### What do we want? 

- Must be printable 
- Must be under version control and follow the same release cycle as the application 
- To minimize time spent on writing documentation 

### How 

Geir Hedemark's suggested template: http://hedemark.net/templates/inst_template/

##### 1. Application description	
1.1 Functional description	
1.2 Delivery format and deliverables	
1.3 Other documents	
1.4 Application contacts for installation questions	

##### 2. External software packages used by this system	

##### 3. Installation of external packages	
3.1 Package 1	
3.2 Miscellaneous installation tasks	

##### 4. External data channels	
4.1 <Channel description>	

##### 5. Application configuration	
5.1 JDK environment settings	
5.2 Tomcat JNDI server	
5.3 <Config 2>	

##### 6. Error handling	
6.1 JMX endpoints and sources	
6.2 JMS queues	
6.3 Log files	
6.4 Detection of installation difficulties	
6.5 Application start	
6.6 Rudimentary application operation	

##### 7. Upgrading the application	
7.1 Upgrade from version <x> to <y>	
7.2 Downgrade from version <y> to <x>	

##### Glossary	

### Questions 

- "1.4 Application contacts for installation questions" <- This can be highly dynamic information and can thus be hard to keep synchronized. Can it be set to a _department_ or group, not individuals? 

- "3. Installation of external packages" <- I don't want to maintain this. Can we let this section contain links to guides maintained by the external package vendor? 

- I hate to repeat myself. Large parts of the installation guide above will be identical for multiple applications in a system. How can we avoid duplication? I want to reduce the manual labor as much as possible. 

- To me an installation can be split into the following components: 
    - Prepare the environment (install java, create users etc.) 
    - Obtain software to install 
    - Install the package 
    - Configure 

In a large distributed system the different applications might be configured by a separate configuration system. Should this system be explained in every installation package? 

- The documentation must follow the installation package. Can it be _included_ in the package or must it be attached separately? E.g. can we put it _into_ the rpm package or must we create an archive which only includes the rpm and the documentation? 

- I think it is huge advantage that the documentation can be read from a shell window. This limits the format of the documentation to plain text. Do we need more advanced formatting options which force us to use PDF, doc or html?
