# CASE2 - Reusabillity of domain objects in the enterprise

Responsible: Erik 

## Feedback

Add your comments, opinions and observations as children to this page.

## Automatic meter reading introduction 
Automatic meter reading, or AMR, is the technology of automatically collecting data from water meter or energy metering devices (water, gas, electric) and transferring that data to a central database for billing and/or analyzing. This saves employee trips, and in the case of estimates, billing can be based on actual consumption rather than on an estimate based on previous consumption, giving customers better control of their use of electric energy, gas usage, or water consumption.

AMR technologies include handheld, mobile and network technologies based on telephony platforms (wired and wireless), radio frequency (RF), or powerline transmission.

Source: [wikipedia](http://en.wikipedia.org/wiki/Automatic_meter_reading) 

## Simplified scenario 

Terminals are off-line most of the time and connect to a concentrator/server at regular intervals with GPRS. When they come online their different registers must be read and the values persisted. Registers can hold a three days worth of readings, so there is a chance that readings can be recovered if a terminal is unavailable one or two days. Bad terminal configuration, weak antennas, power outages, bad software, etc. are typical problems. Because GPRS is used, adequate bandwidth is only available 5 hours every night. Every month the AMR service provider deliver meter readings to Customers. Missing readings incur economical penalty. 

**Meter** (== terminal for our use case) and **meter reading result** (readings from a meter) are two central domain objects used in some way by all hardware and software components. It might to possible to introduce a CORE DOMAIN and force all systems to share it. This is not trivial since there are so many different companies and components involved. Yes, the system is distributed, its big, its complex and performance and availability/reliability is critical. 

> ℹ️ Can Qi4j, EDR or other technologies alleviate the situation?  

## System description

#### Companies/stakeholders

In an AMR setup there are multiple companies/stakeholders involved: 

- Terminal hardware manufacturers  

- Terminal software manufacturers  

- AMR service provider 

- Customer (electricity company) 

- End-customer (companies and private households that use water, gas, electricity) 

#### Hardware 

- Different terminal types with different (proprietary) protocols  

- Different communication media: 
    - GPRS 
    - LAN 
    - Wireless

#### Software 

- Terminal specific software 

- AMR service software (4 subsystems) 

- Customer software 

#### Numbers

- 10 million meters
- Hourly readings from two registers (48 values every night) 
- Transmission medium is available 5 hours every night 

###### Derived numbers

480 000 000 values every night => 26 667 values per second (ignored the fact that an actual session takes some time) 

10 000 000 * 48 * 30 = 14 400 000 000 values per month
