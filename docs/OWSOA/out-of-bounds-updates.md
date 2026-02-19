# out-of-bounds updates

# Definition of [out-of-bounds updates](out-of-bounds-updates.md)
Updates done one data out-of-bounds from [Core Services](CS.md). 
_Example_
_Users updates data through ERP system own UI._

## Explanation
Out-of-bounds creates is not considered an issue if the entity only is created in one system, and therfore does not require syncronization. Out-of bounds creates will probably be syncronized if a get or save call is performed at a later stage.
