# Next step simulation, make and save flights

### [Next step simulation, make and save flights](Next<sub>~step</sub><sub>simulation</sub><sub>make</sub><sub>and</sub><sub>save</sub>~flights.md)

Determine when drone are making a flight or not.

When drone is going from zero speed to moving a certain amount of time, the drone is on flight. When drone is going from moving to zero speed a certain amount of time, the flight end.

##### refs: 

- [Main service layout](Main<sub>~service</sub>~layout.md)

##### Function

Save all position of a flight to database with time and place for the flight.

This must work both for simulated drones and real ones (when we get real feed)
