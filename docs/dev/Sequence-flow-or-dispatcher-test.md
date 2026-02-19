# Sequence, flow or dispatcher test

The goal of a sequence/flow test is to verify that a service calls methods in the expected sequence. The actual processing _within_ each step is not important and the service can thus be stubbed. The same concept can also be used to test typical dispatcher logic.
