# Principles for clear and consistent architecture

# Main principles
1. All architecture artifacts must have a clear responsibility 
    1. Investigate artifacts that have more than 1 responsibility. Divide and conquer.
    1. Artifacts that has no clear responsibility must be removed
1. Ensure consistency
    1. All artifacts must support the architecture's goal
    1. Avoid architectural deviation and fragmentation

_perfection is attained not when there is nothing more to add, but when there is nothing more to remove._ - Antoine de Saint Exupéry

# Supporting principles
- Create a plan
    - Without a plan there is disorder and arbitraryness

- Value simplicity over complexity
    - Use well known patterns and basic building blocks that keeps things simple
    - Only allow complexity when no other options are available
    - Simplicity enables flexibility to implement what provides greatest value

- Do not allow architectural enthropy
    - Retire and refactor to comply with Main principles
    - Keep the architecture fit, and avoid immature decisions

- Empower the user
    - Interacting with the system should be obvious and frictionless
    - Architecture is the user's information processing supporting structure.

- Say No to requests for functionality that can not be supported well by the architecture or of little value

## Further Reading
[Technology must be self-evident](http://blogs.techrepublic.com.com/hiner/?p=6305&tag=nl.e101)
[Antoine de Saint Exupéry](https://secure.wikimedia.org/wikiquote/en/wiki/Antoine_de_Saint-Exup%C3%A9ry)
