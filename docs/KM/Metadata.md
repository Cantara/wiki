# Metadata

Meta data in the context of search is about classifying and tagging information that is propagated to the search index.excerpt}

Taxonomy is the practice and science of classification. (Wikipedia)

Meta data can be added manually or detected by a search engine. A search engine should for example be able to automatically tag "John Doe" as a person, employee and team leader.
An example of manually attached meta data could be writing "Our ref:" in a document sent to a customer. Entity extraction from unstructured documents is regarded as core business for search engines.

> 💡 Meta data usage can be divided into two categories :
> 💡 a) Meta data which is just structuring existing information in the data (e.gabstract from a document)
> 💡 b) Meta data which gives additional classification of data
### Meta data vs. Entity attributes

- Traditionally unstructured data -> meta data
- Traditionally structured data -> entities and attributes

Two types of meta data:
- Structured information that already exists in an unstructured information mass -> SHOULD BE AUTOMATICALLY INDUCED   
- Actual meta information: information about the information mass that does not explicitly exist within the information mass.
    - Lifecycle attributes (created, modified by)
    - The writers personal state
    - Purpose of the document

- Meta data for retrieval
- Meta data for aggregation/ reporting

### Problems of over classification 

 A (general)problem with taxonomies is that it can be over dimensioned. People tend too classify to much!

- An adequate tool support has not yet been implemented successfully.
- Unawareness to what can be automatically classified, and to what that needs to be entered manually.

There are several areas/ways that meta data strategies do not scale. If to much meta data is required it will not scale...users will not add the meta data and would rather choose not to upload documents. 

### Examples of good meta data usage

Meta data need to provide value for those entering it.

- Documents can automatically be tagged as to where they are located (saved), movements and editors.
- Meta data can be used for reporting and information retrieval. 
- Let the tree structure identify the meta data based on the placement in the tree 
- Two types of meta data
    - Structured information that already resides within the entity or other sources of information
    - Information that exists within documents and could be generated automatically. A user should not be bothered with entering this type of meta data.
- he document`s purpose is to be a good meta data candidate.
- Lifecycle attributes are typical meta data for entities.

# Example

Auto-taxonomy from search engines on the keyword **Enterprise Domain Repository**

![EDR_metadata_map.jpg](EDR_metadata_map.jpg)

Here a auto-taxonomy has been generated. It provides some exiting relations between different usages of a term used on different web pages, it is also possible to find several exiting contexts
