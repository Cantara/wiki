# Extreme Agile

*When you take agile practices to the extreme. Sandbox for new practices.*

> Joe: Hey Bill, let's list the practices that every agile project should include.  
> Bill: Well, Joe, I'm not sure there are any such practices that should apply to **every** project..  
> Joe: Well, surely iterations or sprints.. everyone need that, right?  
> Bill: Well, the reason we actually have Sprints is that we're not completely rid of waterfall-effect. We have Sprints as a workaround for traditional project managers. It's so they'll get a breather in between where they can do some estimation, planning and stuff. If we were completely agile, every commit would result in a fully tested, shipped piece of software.

Bill here is thinking *Extreme Agile*. It's a term we came up with to challenge existing agile practices, or push them to the extreme. We don't recommended that anyone actually try to enforce these practices, they're more like thought-experiments that you **might** be able to apply.

Most usefully, they challenge you: If you cannot do extreme agile practice X - why not? The answer might be something that can help you speed up your development process.

### List of Extreme Practices (feel free to add more)..

#### Developers should not run tests before committing.

In an optimal environment, the developer needs the computer for running the IDE. He shouldn't have to wait at all before committing. Even a 1 minute build (which, let's face it, is pretty seldom). Let another computer run the tests for him.

**Why isn't this possible in *our* environment?**

- There is no distributed SCM onto which the developer can commit without fear
- Lack of automated build and release
- Not enough automated testing
- No pre-commit test (the tests have to run before)

#### The optimal sprint-length is zero.

Usually, we settle for a sprint length of 4 weeks.

Sprint is actually a synthetic time box which exists because of overhead between iterations. The overhead consists of things like bureaucratic processes (review), manual testing, manual deployment, etc. This statement says that you should eliminate overhead and try to get as close to a non-existent sprint as possible. The ideal batch size is one (see [Kanban](/web/20210804164801/https://wiki.cantara.no/display/dev/Kanban "Kanban")).

**Why isn't this possible in *our* environment?**

- We need a phase for testing at the end because our test coverage is not good enough
- We don't have an automated build system
- We don't have an automated release procedure

#### Estimation is muda.

See <http://www.infoq.com/news/2008/08/estimates-wasteful>

Well, if you still estimate, make sure you use [Gummy Bears](/web/20210804164801/https://wiki.cantara.no/display/dev/Gummy+Bears "Gummy Bears").

**Why isn't this possible in *our* environment?**

- Our manager won't buy it. We **need** estimates.
- Our tasks are of very different sizes and not weighing them with estimates will disrupt our velocity!
- Our tasks are getting smaller and smaller/bigger and bigger, so we need estimates to stabilize our velocity

In [Kanban](/web/20210804164801/https://wiki.cantara.no/display/dev/Kanban "Kanban") systems, there is no estimation.

#### We deploy to production many times a day

In a classical environment we only deploy to production at the end of a long iteration finalized by a sturdy testing phase. The idea of this concept is to completely eliminate this as far as deploying every successful commit. It is closely related to Kanban and zero-sprint-length.

**Why isn't this possible in *our* environment?**

- Deployment involves downtime. We can't have that much downtime.
- We can only deploy at night.
- We don't know if the code works at any given point in time.
- Deployment takes three hours.
- Deployment involves too many manual (costly) tasks.

- [Continuous Deployment at IMVU: Doing the impossible fifty times a day., by Timothy Fitz](http://timothyfitz.wordpress.com/2009/02/10/continuous-deployment-at-imvu-doing-the-impossible-fifty-times-a-day/)

#### We don't need backlogs.

Why not have queue of outgoing features instead of having incoming requests?

- <http://www.infoq.com/news/2007/10/product-backlogs-wasteful>

**Why isn't this possible in *our* environment?**

- There are too many requests from the product owner!
- We have to do the whole backlog anyway..

#### Large Scale Agile

(maybe this deserves its own page?)

- <http://jamesshore.com/Blog/Large-Scale-Agile.html>
