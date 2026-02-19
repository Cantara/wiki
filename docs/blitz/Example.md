# Example

# Blitz HelloWorld Example

### Introduction

This example provides a simple demonstration of how to use a JavaSpace (it is not Blitz specific).
Compiling
The example consists of four classes:

   1. [Lookup.java](Lookup-java.md) which handles service lookup.
   2. [Writer.java](Writer-java.md) which generates Entry's.
   3. [Taker.java](Taker-java.md) which takes Entry's.
   4. [TestEntry.java](TestEntry-java.md) which is the Entry class.

In order to compile these classes you will require the following .jar's:

    * jsk<sub>~lib.jar, jsk</sub>~platform.jar from the JINI 2.x distribution.

Assuming that your JINI 2.1 distribution is in /jini2_1 and your Blitz distribution is in /blitz, you can compile the example as follows:

```
cd /blitz/examples/helloworld

javac -classpath /jini2_1/lib/jsk-lib.jar:/jini2_1/lib/jsk-platform.jar *.java
```

### Running

Before starting the example, ensure that you have a Blitz instance running in a public lookup group - see the Installation Guide. This is necessary because the Lookup class does a single lookup and discover step - it does not register with discovered lookup services. Thus, if a Blitz instance isn't registered beforehand, it will not be found (I'll fix this in a future release!).

We are now ready to run the example. First, we'll start the taker - open a new terminal window and then:

```
cd /blitz

java -Djava.security.policy=config/policy.all -classpath /jini2_1/lib/jsk-lib.jar:/jini2_1/lib/jsk-platform.jar:/blitz/examples/ helloworld.Taker
```

Now we'll run the Writer - open a new terminal window and then:

```
cd /blitz

java -Djava.security.policy=config/policy.all -classpath /jini2_1/lib/jsk-lib.jar:/jini2_1/lib/jsk-platform.jar:/blitz/examples/ helloworld.Writer
```

The Taker will exit automatically when it hasn't taken an Entry in the last 60 seconds.

### More Material

For more examples see:

   1. [JavaSpaces in Practice Examples](http://www.incax.com/examples.htm#jsip)
   2. [Bodega Project](https://bodega.dev.java.net/)

For JavaSpaces resources see [here](http://www.dancres.org/cottage/javaspaces.html)
