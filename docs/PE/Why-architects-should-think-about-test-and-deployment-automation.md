# Why architects should think about test and deployment automation..

#### Expectations for the architect

Unit tests and basic CI are well-known, widely adopted and should be part of any development process. If not present, you, as an architect, should introduce them, but hopefully the dev-team can take the responsibility themselves. Architects usually manage to stay out of the way and everything is fine - at the *application level*.

Developers working at an application seldom take responsibility for system-wide concerns. And they shouldn't. This is the responsibility of the system (!) architect. It thus falls to the architect to ensure that the system as a whole can be deployed and tested properly.

###### So what should an architect do?

Strive to adhere to the following guidelines:

- **Deployment should be simple**: Both system administrators and developers should be able to install and configure any service. Prefer simple to fast, because brain-time is more expensive than processing power.
  - For every new release, the application will be deployed at least once, probably a bunch of times, so the ROI is excellent.

- **Loose coupling between services**: it should be possible to test service A and service B together without deploying service C, D, E, F, G, etc. This allows iterative testing and promotes a clean design.

- **Continuously integrate services**: for each new version of a service, deploy it and test that it works together with the rest of the system.

> "First, when we deploy software, we are exposing ourselves to the accumulated technical risk embodied in the code. By deploying one component at a time, we spread technical risk out over a longer period of time. Every component has its own chance to fail in production, letting us harden each one independently."
>
> "It's rare to find a technique that simultaneously provides higher commercial value and better architectural qualities, but early deployment of individual components offers both."

Src: [Skyscrapers aren't scalable](http://97-things.near-time.net/wiki/talk-about-the-arch-but-see-the-scaffolding-beneath-it)

###### Why follow these guidelines?

Simply because it is the most efficient approach to create big systems that work. The alternatives are much more costly and take much more time.

###### Why don't architects follow these guidelines?

Probably because most architects don't know the concepts or what tool support is available.
