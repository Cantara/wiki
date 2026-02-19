# Per-deployment projects

## What is it? 

This approach is aimed at what I like to call product lines. I.e., the goal is to deliver multiple different products with similar functionality. 

The general idea is to write libraries that are easy to integrate and reuse. Each product can then depend on any subset of all the libraries, potentially include additional code AND have its own custom configuration. The resulting project can be viewed as a _wrapper_ and is also known as a _per-deployment project_. 

## Pros and cons

- Pro
    - Often useful for creating specialized webapps for clients
    - The Maven artifacts are resusable blobs
- Con
    - Not trivial to make all Maven artifacts easily reuseable. 

## Examples 

**TODO** Does anybody have an example that demonstrates how this can be implemented?
