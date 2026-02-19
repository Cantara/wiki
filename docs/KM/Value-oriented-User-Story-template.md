# Value-oriented User Story template

### User story template

Adopted from

- [James Carr](http://blog.james-carr.org/2009/10/02/feature-injection-putting-the-value-first-in-your-user-stories/) - [Dan North](http://dannorth.net/whats-in-a-story) - [Cantara](https://wiki.cantara.no/pages/editpage.action?pageId=16515480)

**Title** (one line describing the story)

Narrative:

- To realize [benefit]
- I, as a [role]
- want [feature]

**Norsk eksempel**

- **For**
- **ønsker jeg som**
- **at**

### Acceptance criteria scenario templates

- [In Cucumber BDD](http://cukes.info/) and [Example](https://github.com/cucumber/cucumber/blob/master/examples/i18n/en/features/addition.feature)

**Acceptance Criteria:** (presented as Scenarios)

- Scenario 1: Title
- Given [context]
  - And [some more context]...
- When [event]
- Then [outcome]
  - And [another outcome]...

**Norsk eksempel**  
\*Scenario 1: \*

- **Gitt**
  - **og**
- **når**
- **så**
  - **og**

---

- **An example**:

Story: Account Holder withdraws cash

To *get money when the bank is closed*  
I, as a *As an Account Holder*

- want *withdraw cash from an ATM*

**Acceptance criteria**

**Scenario 1**: Account has sufficient funds  
Given the account balance is **$100**  
And the card is valid  
And the machine contains enough money  
When the Account Holder requests **$20**  
Then the ATM should dispense **$20**  
And the account balance should be **$80**  
And the card should be returned

**Scenario 2**: Account has insufficient funds  
Given the account balance is **$10**  
And the card is valid  
And the machine contains enough money  
When the Account Holder requests **$20**  
Then the ATM should not dispense any money  
And the ATM should say there are insufficient funds  
And the account balance should be **$20**  
And the card should be returned

**Scenario 3**: Card has been disabled  
Given the card is disabled  
When the Account Holder requests **$20**  
Then the ATM should retain the card  
And the ATM should say the card has been retained
