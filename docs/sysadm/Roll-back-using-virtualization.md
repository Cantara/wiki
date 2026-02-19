# Roll-back using virtualization

- Create a new default zone/virtual machine. 
- Install the new version of the service. 
- Copy data from the currently running service. 
- Test that it works. 
- Test integration 
    - DNS
    - Firewall
    - Communication with collaborating services and systems 
- Switch from the old version to the new version using [Dynamic addressing with service names](Dynamic<sub>~addressing</sub><sub>with</sub><sub>service</sub>~names.md)
- Migrate changes from your last copy and up until the actual switch. 

Some steps related to data migration can be simplified/omitted if the persistence technology is chosen wisely. E.g. easier with repositories based on Java spaces or distributed hashmaps than when based on RDBSs.
