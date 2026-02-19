# Last Attribute Update Wins (LAUW)

### What
The pattern describes how data can be synchronised between multiple data sources based on the latest updated data thorugh the use of [Core Services](CS.md)

### When
If the enterprise architecture does not have a distinct master per attribute due to possiblity to do [out<sub>~of</sub><sub>bounds updates](out</sub><sub>of</sub>~bounds-updates.md) to the datasources.

### How
Perform the following algorithm on get and save (probably not find(?))

```title
for each mapped attribute where providers.count > 1
   if attribute does not equal other providers attributes
      find the latest updated attribute (or provider objects)
perform save operation on other providers to ensure all providers are synchronized
```

### Advantages

Fairly high data quality

### Disadvantages

Complexity
