# Dot syntax for stores graph example

```title
digraph G {

	subgraph NationalBrand {
		style=filled;
		color=lightgray;
		node [style=filled,color=lightblue];
		ng [label="National Brand"]
		ng -> Kiwi [label="Franchise", fontcolor=darkgreen] // edge ng -- Kiwi
		ng -> Meny [label="ownes", fontcolor=darkgreen] // edge ng -- Meny
		ng -> Joker [label="Franchise", fontcolor=darkgreen] // edge ng -- Joker
		ng -> Ultra [label="ownes", fontcolor=darkgreen] // edge ng -- Ultra
		Kiwi -> NordNorge;
		Kiwi -> SørNorge;
		NordNorge -> Store1
		NordNorge -> Store2
		Store1 -> Freezeer1
		Store1 -> Freezeer2
		SørNorge -> Store3
		SørNorge -> Store4
		Meny -> Store5
		Joker -> Store6
		Ultra -> Store7
		Ultra -> Store8
		label = "process #1";
	}

	subgraph InternationalBrand {
		style=filled;
		color=lightgray;
		node [style=filled,color=lightblue];
		l [label="International Brand"]
		l -> DE
		l -> ES
		l -> DK
		l -> NL
		l -> SE
		wg [label="West Germany"]
		DE -> wg
		wg -> Store14 [label="Owns", fontcolor=darkgreen] // edge wg -- Store14
		wg -> Store15 [label="Owns", fontcolor=darkgreen] // edge wg -- Store15
		nge [label="North Germany"]
		DE -> nge
		nge -> Store16 [label="Owns", fontcolor=darkgreen] // edge wg -- Store16
		DE -> Region1
		Region1 -> Region2
		Region2 -> Store20
		Region2 -> Store21
		Store20 -> Freezer3
		Store20 -> Freezer4
		DE -> Store17 [label="Franchise", fontcolor=darkgreen] // edge ng -- Kiwi
		
		label = "Lidl Organzing Stores";
	}

	start -> ng 
	start -> l	
	

	start [label="Orgnization of Stores",shape=Mdiamond];
	
}
```
