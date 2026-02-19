# Atom for Event-Driven Systems

- trade scalability for latency

- inappropriate for very low-latency notifications

- seconds (or minutes or hours) between events being produced and consumed

- Suited for many consumers, guaranteed delivery, but latency-tolerant

- Clients poll the service feed, use caching to reduce workload. Clients responsible for retrieving (inverse of many alternatives)

- Messages will never arrive out-of-order.

- Easy to replay entire history.

- This linking and caching strategy trades efficiency for generalization.

- Read more
  - REST in Practice, chapter 7: The Atom syndication format
  - <http://answers.oreilly.com/topic/2153-rest-in-practice-how-to-use-atom-for-event-driven-systems/>
  - <http://www.imc.org/atom-syntax/mail-archive/msg15957.html>
  - <https://www.safaribooksonline.com/library/view/rest-in-practice/9781449383312/ch07s03.html>
