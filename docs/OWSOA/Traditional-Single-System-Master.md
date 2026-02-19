# Traditional Single System Master

# What
In a [Traditional Single System Master](Traditional-Single-System-Master.md) scenario you get data from one or many core systems, but one of the core systems is the master and is the only system where changes are saved. There is no meaning in fetching the "same" data from more than one core system because no synchronization will be done.
# When
# How
When you map from provider objects to domain objects you use data from all provider objects. When you save you only need to map domain objects data to the provider objects that belongs to the master core system, because this is the only system that is being updated.
# Advantages
It is where simple to implement.
# Disadvantages
