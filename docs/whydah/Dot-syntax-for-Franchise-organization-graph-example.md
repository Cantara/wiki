# Dot syntax for Franchise organization graph example

```
digraph G {

	subgraph franchize {
		style=filled;
		color=lightgrey;
		node [style=filled,color="#0080FF"];
		gs [label="Grocery store"]
		gss [label="Sub-store"]
		emp [label="Employee"]		
		gs -> gss
		gs ->Karen [color=White]
		Karen->gs  [label="isEmployed", fontcolor=darkgreen]
		Karen->emp  [label="isEmployee", fontcolor=darkgreen]
		Karen->gss [label="worksFor",  fontcolor=darkgreen]
	}
	

	start -> gs  
	

	start [label="Orgnization of Grocery Store",shape=Mdiamond];
}
```
