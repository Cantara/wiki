# Kjartans notes from Rickards talk

It might be quite obvious but I think **spend time on what actually matters and not boiler plate stuff** is a good one (when talking about generic concerns).

Rickard Öberg - Qi4j notes
- dont expose your internals
- try to be as non-invasive as possible
- what we're doing today is class oriented programming
- focus on what is important of an modelling perspective
- objects are good - classes are evil
- **spend time on what actually matters and not boiler plate stuff** (referring to generic concerns)
- gui components that only work with interfaces
- Role concept
- Mixins stand alone
- collaboration of roles in different objects
- change is good

- Concerns are defined explicitly -> you need to define it in the interface annotation (@Concern) to use it
- Qi4J concerns vs "traditional" aop/aspects -> application specific composite (interface) that you put all the common stuff into and extend
- generic concers comes before domain specific concerns (not quite sure if this discussion ever ended :-) )
- create a "super" concern that defines the common concerns and reuse it in all the sub composites..

- Mixins (the "good old class" split into reusable parts)
- qi4j tries to be as static as possible 

- UnitOfWork and not transactions (like many other frameworks)
 

**Modules**
- rooms == modules
- share between modules is possible
- modules are more like packages
 

I think this was Kaares response to the alternative lunch options :-)
"This is a geek cruise for f****** sake we dont like buffets we eat pizza"

**Mixin example**
- Access control list aspect
- Parent/Children
