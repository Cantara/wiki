# Qi4j ordering concern stack and call stack revisited  (Rickard - this is homework for you...

the left and up principle...

(the most specific ones will be called first -  which is in most cases (but nok all) wrong...

/**
 * Alternative strategies
 */

// Inheriting @Concerns, imporant.. super concerns first
@Concern(Security.class,Transaction.class)
public interface MyCompanyComposite{}

@Concern(MyApplicationConcern.class)
public interface MyApplicationComposite extends MyCompanyComposite{}

// Inheriting @Concerns not allowed
@Concern(Security.class,Transaction.class)
public @interface MyCompanyConcerns{}

@MyCompanyConcern
@Concern(MyApplicationConcern.class)
public interface MyApplicationComposite extends MyCompanyComposite{}

// Explicit ordering with implicit super concerns as first element if omitted
@Concern(Security.class,Transaction.class)
public interface MyCompanyComposite{}

@Concern(Security.class,MyApplicationConcern.class,SuperConcerns.class)
public interface MyApplicationComposite extends MyCompanyComposite{}
