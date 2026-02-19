# EDR Simple Master Mapping

# What
In an [EDR Simple Master Mapping](EDR-Simple-Master-Mapping.md) scenario the concept of [MasterPerAttribute](MasterPerAttribute.md) is used. To get the "same" data from more than one core system is bloating the code because no synchronization will be done.
# When
# How
When you map from provider objects to domain objects you use data from all provider objects.
When you map from domain objects to provider objects you map to all the provider objects that contains master fields.
# Advantages
# Disadvantages
