# Extentions - Advanced Scenarios

# Extensions / Advanced Scenarios

Extensions are optional strategies that can provide your EDR strategy with more benefits.

The discussions on Data Mastering and the other extensions are not concluded. Join in on those discussions on the [Mailing lists](/web/20210922172913/https://wiki.cantara.no/display/EDR/Mailing+lists "Mailing lists").

\*[Data Mapping](/web/20210922172913/https://wiki.cantara.no/display/EDR/Data+Mapping+Extension "Data Mapping Extension")  
\*Data Master Strategy  
\*Merge Strategy Pattern  
\*Moderator  
\*Recording Command Pattern

### Data Master Strategy

An advantage using EDR is the possibility of discovering that different providers have different values for the same field values.

One exampel might be that the same customer has different street address in billing and CMS applications.

### Merge Strategy Pattern

Responsible for mapping strategies on field value level.

### Moderator

Moderator strategy for allowing updates from users that does not have update privleges in one or more providers.

The moderator strategy can also verify automatic updates where difference in data are found between providers.

### Recording Command Pattern

The Recording Command Pattern may be used to extend the Providers used by the Enterprise Domain Respository. A Recording Gateway will keep track of all executed commands and record all responses to these requests. This enables the gateway to go into offline mode and do playback of the traffic should the provided system be unavailable.
