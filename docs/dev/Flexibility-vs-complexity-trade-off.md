# Flexibility vs complexity trade-off

Flexibility is nice when it is needed. Unused flexibility is wasteful and adds complexity and cost. How to decide what changes we can support without exceptional high cost? It falls to the architect to weigh the drivers of the project and _choose_ where to make it possible to switch solution later on. 

**Example**: Coupling to application server. 
A tight coupling to a heavyweight application server has advantages; can utilize features and functionality only found in this product, less rules and standards to consider since anything supported by the product is allowed. Disadvantages: dependent on the choices the producer make, difficult to integrate with other products, higher learning costs, license costs, etc.  

Follow [The principle of Last Responsible Moment](http://asserttrue.blogspot.com/2009/04/principle<sub>~of</sub><sub>last</sub><sub>responsible</sub>~moment_11.html).
