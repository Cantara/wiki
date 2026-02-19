# At-least once semantics

#### Categories of Message Delivery Reliability

**at-most-once** delivery means that for each message handed to the mechanism, that message is delivered zero or one times; in more casual terms it means that messages may be lost.  
**at-least-once** delivery means that for each message handed to the mechanism potentially multiple attempts are made at delivering it, such that at least one succeeds; again, in more casual terms this means that messages may be duplicated but not lost.  
**exactly-once** delivery means that for each message handed to the mechanism exactly one delivery is made to the recipient; the message can neither be lost nor duplicated.

The first one is the cheapest—highest performance, least implementation overhead—because it can be done in a fire-and-forget fashion without keeping state at the sending end or in the transport mechanism. The second one requires retries to counter transport losses, which means keeping state at the sending end and having an acknowledgement mechanism at the receiving end. The third is most expensive—and has consequently worst performance—because in addition to the second it requires state to be kept at the receiving end in order to filter out duplicate deliveries.

Direct quote from [Akka, Message Delivery Reliability](http://doc.akka.io/docs/akka/2.3.4/general/message-delivery-reliability.html). Other introductions: [Kafka Message Delivery Semantics](http://kafka.apache.org/documentation.html#semantics) or [Distributed systems – theory](http://web.info.uvt.ro/~petcu/distrib/SD5.pdf).

#### Why at-least once semantics is popular

- At-most-once semantics can only be used if it is acceptable to lose messages. To guarantee data delivery, exactly or at-least once semantics must be used.

- Exactly-once semantics makes it easier for application developers, because they can ignore duplicates. The cost is poor scalability, because implementations often rely on transactional serializability across distributed systems, aka. distributed transactions.
  - [Exactly-once semantics in a replicated messaging system](http://ilpubs.stanford.edu:8090/483/)
  - [Distributed transactions is the main evil of scalability](http://ivoroshilin.com/2014/03/18/distributed-transactions-and-scalability-issues-in-large-scale-distributed-systems/)

- At-least once semantics is much easier to scale than exactly once.
  - [Life beyond Distributed Transactions](http://www.ics.uci.edu/~cs223/papers/cidr07p15.pdf)
  - [Amazon SQS](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/DistributedQueues.html)
  - Kafka: <https://kafka.apache.org/08/design.html>, [Idempotent Producer](https://cwiki.apache.org/confluence/display/KAFKA/Idempotent+Producer)
