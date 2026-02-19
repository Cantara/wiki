# Dot syntax for Production company graph example

```
digraph G {

	subgraph productionfirm {
		style=filled;
		color=lightgrey;
		node [style=filled,color="#0080FF"];
		pf [label="Freecer manufacturer"]
		dev [label="Development"]
		prod [label="Production"]
		pm [label="Product Management"]
		sup [label="Support"]
		pf -> dev
		pf -> prod
		pf -> pm
		pf -> sup
		pm -> Peter
		dev -> Wendy
		dev -> Charlie
		sup -> Martin

	}

	

	start -> pf 	
	

	start [label="Orgnization of Production Company",shape=Mdiamond];
}
```
