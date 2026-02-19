# Auto-Taxonomy Implementation

# Examples

[Work in Process - data mapping](/web/20230203132424/https://wiki.cantara.no/display/EA/Work+in+Process+-+data+mapping "Work in Process - data mapping")  
[Tools](/web/20230203132424/https://wiki.cantara.no/display/EA/Auto-Taxonomy+Tools "Auto-Taxonomy Tools")

# Scenario for example implementation

### Task:

|  | Improved marketing, better targeted to each customers need. |

### How:

- Find relations between personnel employed by your customers.
- Find challenges your customers are struggling with.
- Find the hype-factor of your customers interests.
- Being able to **segmentize** your customers.

### Input

- Google search on customer name, crawl and push to Calais.
- Customers´s web page(s)

(Naturally in real world we will also use internal input like)

- Information stored in your customer database.
- Information stored in your production database.
- Information stored in your sales system.
- All documents on *internal file-server* - sales, offers, e-mail communication.. the works

### Output

Enable a **linked map** based on relevance.

|  | **Relevance implementation strategy** Here are some ideas of what we look for, but since we want to use computers for all work, the case will use the taxonomy from Calais as it is, and use simple hit-ratio selections on the (from a system point of view) generic taxonomy element. Presentation will then use the generic taxonomy element as link metadata in the presentation and scale the node according to the combined sum of (taxonomy element \* hit ration) for all links between to companies. |

Unknown macro: {gliffy}

Eg.  
Sales representative use a tool to view the hype-factor of his customers.   
He will do so by first finding which terms are most hype´ed, and drill down.

**Close collaborating companies**

- partner X (partner count: 2.000, mention count: 13.000)
- partner Y (..)
- company Z (mention count 30:000)

Data retreived from a few companies main website,and about pages. The  
categories are then automatically created from the Calias webservice.  
Each color represents a different company. Black is "all other companies".

**Hyped terms**

- Industry Term (total count 10.000)
  - effective financial solutions ( count 2.000)
    - IBM (count 1.200)
    - Skattedirektoratet (count 500)
  - SOA (count 1.500)
    - ...

**Combinatorials**

- Partner X, hype term 1 - group
- hype term 1, sortet company list - grpup

# Extention points

- Enable notification when public information indicate one of your customers are struggeling with a problem you can solve for them.
