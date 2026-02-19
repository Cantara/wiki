# Add a process for each drone that refresh new positions every 10 seconds on server

### [Add a process for each drone that refresh new positions every 10 seconds on server](Add-a-process-for-each-drone-that-refresh-new-positions-every-10-seconds-on-server.md)

_ref:_ 

- [Drone radar design](Drone-radar-design.md)
- [Main service layout](Main-service-layout.md)
- [Track simulator](Track-simulator.md)

##### Purpose

- Simulate drone movements. 
- For ex. 100 drones frying on different spots on the world (group of 10 drones)

##### Function

- Start when service start and work continuously making positions
- Data / position is measured in longitude, latitude and altitude.
- Each 'drone' is given a unique identification

##### Issues

- Have one position list showing each positions
- One list showing on positions for all drones withing a range of 10 km (and number of drones)
- One list showing on positions for all drones withing a range of 10 miles (and number of drones)
- One list showing on positions for all drones withing a range of 100 miles (and number of drones)

(maybe some advanced calculations, but we try)

Thai must relate to this different list when retrieving positions consider the current map view size

### Initial specs, no longer relevant (solved)

##### Solution

Make a class for one drone that calculate movement on each. Current position is stored into the current positions list for retrieval to map.

**Simplified:**

```

interface DroneSimulate {

   DroneSimulate(String Id, int calcfrequence, double startLong, double startLat, double startAlt)  

   DronePosition currentPosistion;   
   DronePosition getPosistion(); 

   void calculate();

   -- Run a tread inside each object to calculate

}

interface DronePosition {

   String ID;
   Double Latutude;
   Double Longiture;
   Double Altiture;

}
 
```
