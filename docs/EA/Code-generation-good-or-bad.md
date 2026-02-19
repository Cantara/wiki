# Code generation - good or bad?

Despite the core instincts of many geeks, it is difficult to argue that the principle of code generation hasn't been effective. A compiler is a code generator, transforming a human (well, geek) understandable model to a CPU (or VM) understandable representation. The CS community has done that successfully for almost as long as it has existed.

The reason so many developers dislike code generation is that we associate it with generating geek understandable code from a model, _and then mutating the result_. Since we don't want to lose those mutations when we update our model, it requires a fully functional [ARE](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B75H1<sub>~4DDWKC8</sub>~J4&_user=10&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_version=1&_urlVersion=0&_userid=10&md5=6e9c64004886aece02bf676e24815937) (automatic roundtrip engineering) system.

This is actually different, in principle, from compiler-style code generation and has probably never been done successfully. Thus rationalizing the core instinct most geeks have to reject code generation. This was a big deal to me, since I hate following instincts that I can't rationally explain. Wee.
