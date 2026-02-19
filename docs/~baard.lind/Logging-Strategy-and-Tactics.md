# Logging Strategy and Tactics

# Logging Strategy - What we want to accheive.

Vi vil logge at noe har skjedd. Meldingen som flyter oppover skal inneholde informasjon om hva som har skjedd,   
hvilken informasjon som var tilgjengelig da episoden inntraff og log-nivået på eventen.

# Logging Tactics - How to implement

- Omfang
- Paramtere
- identifikator - UUID

### References

- Kelvin Hennie - ["Why is logging such a design and code quality blind spot?"](https://twitter.com/KevlinHenney/statuses/392730782751391744)
- Kelvin Hennie - [Seems to be an overlooked topic. Most stuff on logging seems to be about framework usage or invention.](https://twitter.com/KevlinHenney/statuses/392998610125615106)
- Erik Drolshammer p. 64 onwards <http://org.ntnu.no/feta/report.pdf>
  - "A Log entry must thus be self-explanatory; all information relevant to the incident  
    should be included."
  - **Debug** Debug should therefore be focused on input and  
    choices that was made. Log messages like “entered while loop” is not useful  
    and only clutters your logs. A better entry is “Started iteration over 54 news  
    articles checking for expired date before ’2006-10-10’“. p 67
- <http://www.javacodegeeks.com/2011/01/10-tips-proper-application-logging.html>
