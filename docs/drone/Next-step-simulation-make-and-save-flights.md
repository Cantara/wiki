# Next step simulation, make and save flights

### [Next step simulation, make and save flights](Next-step-simulation-make-and-save-flights.md)

Determine when drone are making a flight or not.

When drone is going from zero speed to moving a certain amount of time, the drone is on flight. When drone is going from moving to zero speed a certain amount of time, the flight end.

##### refs: 

- [Main service layout](Main-service-layout.md)

##### Function

Save all position of a flight to database with time and place for the flight.

This must work both for simulated drones and real ones (when we get real feed)
