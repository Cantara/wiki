# Test structure

With refactoring support in most IDEs, most code refactorings are easy and low-risk changes. However, not everything should be subject to frequent refactorings. A public API is a typical example of an interface we want to be stable and may thus be considered a _{+}refactorization boundary{+}_. Easy refactoring without compromising the stability of the API can be achieved by enforcing the following guidelines: 

#### Guidelines 

1. Write [_intention revealing interfaces_](http://domaindrivendesign.org/discussion/messageboardarchive/IntentionRevealingInterfaces.html) 

2. Keep interfaces free from implementation details. 

3.  When implementing a method defined in a interface within the refactorization boundary, don't put functionality directly in that method, but use it as a wrapper for calls to separate methods. These separate methods and their tests can thus easily be refactored without compromising the stability of the public API. 

Structuring code in this matter not only facilitates refactoring, but it adds a level of indirection that makes it easier to structure the tests. 

When designing/refactoring it can be beneficial to keep abstraction levels in mind so readers can understand the code at one level, before he(r) is required to dive into all the details. 

#### Multiple smaller tests instead of a few big ones 

1. Each separate method can be tested in isolation. If the code is trivial, the method can have _private_ access modifier and a separate test can be omitted. If the code is non-trivial, the method can be given _package local_ or _protected_ access modifier and tested in a separate method. **Testability trumps encapsulation!** 
1. Since the interface is stable, the test for this functionality is also stable. The test for the interface, or service, is loosely coupled to the implementation. 

The advantage of adding this level of indirection gives high cohesion between the test and the code that is tested in 1 and loose coupling between the system/acceptance test for stable interface and the actual implementation.  

#### Example 

The code snippet to the left shows how retrieve-functionality for a User can be designed. Switching from database to file based storage will force the developers to
a) rename _fetchUserFromDatabase_ or 
b) do nothing and accept inconsistency between what the interface communicates and what the code actually does. 
(Forsaking backward compatibility is not an option.)

In the code snippet to the right, the interface reveals only intent and gives no hint as to how this should be implemented. The implementation can thus be refactored easily, without changing the interface. 

```
public interface UserManager {
  User fetchUserFromDatabase(String userId);
}

public class UserManagerImpl implements UserManager {
  private UserDao userDao;

  public User fetchUserFromDatabase(String userId) {
    return userDao.fetchUser(userId);
  }
}
```

```
public interface UserManager {
  User findUser(String userId);
}

public class UserManagerImpl implements UserManager {
  private UserDao userDao;

  public User findUser(String userId) {
    return fetchUserFromDatabase(userId);
  }
  private User fetchUserFromDatabase(String userId){
    return userDao.fetchUser(userId);
  }
}
```

While the example is overly simplistic, it should illustrate how the extra level of indirection described above can be implemented. 

---
**Erik Drolshammer:**

I java så må man på et eller annet nivå teste en _metode_. Det er enkelt å bytte navn på denne metoden, men å splitte den i to krever manuell fiksing. Dvs. her kan man ikke benytte refaktorisering og kjøring av tester for verifisere arbeidet. "Toppnivå"-metoder begrenser altså hva som er enkelt å refaktorisere. 

For å håndtere dette så bør "toppnivå"-metoder gis et tydelig ansvar, og navnet på metoden bør gjenspeile dette ansvaret. (Dette gir bl.a. stabile interface.) 

Videre så kan man med fordel strukturere toppnivå-metoden til å kalle andre metoder som er mer implementasjonsspesifikke. Disse metodene kan man skrive egne tester for. 

En test av denne toppnivå-metoden skal ikke endres om man endrer implementasjonen. Denne testen skal fokusere på ansvar og forventet oppførsel. Testene av metodene som _kalles_ fra denne toppnivåmetoden, derimot, er tett knyttet til hver enkelt metode og skal endres når disse "submetodene" endres. 

Toppnivå-metoder er typisk public i java, mens de andre har tilgangsmodifikator "protected". (Mange ville sagt private her, men testbarhet er mer verdifullt enn enkapsulering, så derfor protected.)

Tester av toppnivå<sub>~metoder bør forøvrig fungere som regresjonstester for _funksjonalitet_ (fokus på verdi for business</sub>~siden), mens tester av "subnivå"-metoder kun tester at enEllerAnnen implementasjonsspesifikkmetode gjør den den skal (kodesentrisk). 

**Ferris:**

RSpec har blitt sterkere på dette etter at det ble slått sammen med RBehave (som igjen stammer fra JBehave), anno versjon 1.1. JBehave duden kutta visstnok ut JBehave til fordel for RBehave fordi han synes Java er så jævlig (til det formålet å skrive spec<sub>~syntax da). Ta en kikk på det nye Story Framework biten av RSpec, og håp at de gjør en slags Java</sub>~port av det (evt. så kan vi ta i bruk RSpec oppå JRuby). Les om Story Framework [her](http://rspec.info/).

---
TODO: Describe how we can make use of package-private to fully test the internal workings of a package, without exposing exposing them as public.

See http://www.brodwall.com/johannes/blog/2008/07/29/link<sub>~package</sub>~by-feature/ - I have a comment there with an example. 

Another example is the MailModule: MailService (public api), MailEngine (package private) and MailSender (void). Describe in detail later.
