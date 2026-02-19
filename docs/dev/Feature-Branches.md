# Feature Branches

_Keep the main branch in a working state, develop new features in branches._

The agile manifesto states Working Software as a value. This implies that we keep the mainline of the code (known to many as the stable branch) in a working state. A good way to keep it that way is by making sure that only safe changes make it into the mainline. If you've got developers continuously working on the mainline to create new features piece by piece, chances are the code is in a broken state every now and then.

In order to remedy this, lots of companies (including ours) have decided that the team should maintain two versions:

one experimental, where new features are developed, and 
one stable, which should always be in a working state. 

This is a bit of an expensive practice, because you end up with long rounds of verification before the experimental branch can be released, replacing the stable version. You also have to continuously merge back bugfixes from the stable branch to the experimental branch.

So, the idea of feature branches is to keep new development out of the way until it is ready to go out in the mainline. When the feature is complete, you test it well. You then merge the feature into the mainline, do some quick verification that it is still in a working state, and then you release. Much smoother (agile) than releasing an entire experimental branch.

### See also

- [Distributed Revision Control](Distributed-Revision-Control.md)

### Resources

- http://martinfowler.com/bliki/FeatureBranch.html
- http://blog.tfnico.com/2010/08/why-distributed-revision-control.html
