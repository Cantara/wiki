# Soft eller Hard koding?

Arkitekter hater dette, right?

```
private void attachSupplementalDocuments()
{
  if (stateCode == "AZ" || stateCode == "TX") {
    //SR008-04X/I are always required in these states
    attachDocument("SR008-04X");
    attachDocument("SR008-04XI");
  }

  if (ledgerAmnt >= 500000) {
    //Ledger of 500K or more requires AUTHLDG-1A
    attachDocument("AUTHLDG-1A");
  }

  if (coInsuredCount >= 5  && orgStatusCode != "CORP") {
    //Non-CORP orgs with 5 or more co-ins require AUTHCNS-1A
    attachDocument("AUTHCNS-1A");
  }
}
```

**Arkitektens favorittalternativer:**
1. Enterprise Rules Engine
1. Just Configure It!

Og, da ender vi jo lett opp slik:

```

<SUPPLEMENTAL_DOCUMENTS>
  <CONDITION TYPE="stateCode" VALUE="AZ" OPERATION="=">
    <ATTACH DOCUMENT="SR008-04X" />
    <ATTACH DOCUMENT="SR008-04XI" />
  </CONDITION>

  <CONDITION TYPE="stateCode" VALUE="TX" OPERATION="=">
    <ATTACH DOCUMENT="SR008-04X" />
    <ATTACH DOCUMENT="SR008-04XI" />
  </CONDITION>

  <CONDITION TYPE="ledgerAmnt" VALUE="500000" OPERATION=">=">
    <ATTACH DOCUMENT="AUTHLDG-1A" />
  </CONDITION>

  <MULTICONDITION>
    <CONDITIONS OPERATION="AND">
      <CONDITION TYPE="coInsuredCount" VALUE="5" OPERATION=">=" />
      <CONDITION TYPE="orgStatusCode" VALUE="CORP" OPERATION="!=" />
    </CONDITIONS>

    <ATTACHMENTS>
      <ATTACH DOCUMENT="AUTHCNS-1A" />
    </ATTACHMENTS>

  </MULTICONDITION>

</SUPPLEMENTAL_DOCUMENTS>

private DocumentRules LoadSupplementalDocumentRules()
{
  /* ... Load above configuration ... */
}

private void AttachDocuments(Document[] docs)
{
  /* ... Attach documents ... */
}

private void AttachSupplementalDocuments()
{
  DocumentRules rules = LoadSupplementalDocumentRules();  

  foreach(Rule rule in rules)
  {
    Document[] docs = EvaluateRules(rule);    

    if (docs != null)
    {
      AttachDocuments(docs);
    }
  }
}

private Document EvaluateRules(Rule rule, DataObject data)
{
	Condition cond = rule.Condition;
  MultiCondition mc = cond as MultiCondition;
  Document result = null;

    if (mc == null)
  {
    // Rule is not compound.  Simple evaluation.
    result = EvaluateCondition(cond, data) ? cond.Documents : null;
  }
  else
  {
    // Rule is compound. Complex evaluation.
    if (mc.MultiConditionOperation == MultiConditionOperation.And)
    {
    	result =
    		EvaluateCondition(mc.Condition1, data) &&
    		EvaluateCondition(mc.Condition2, data) ? 
    		cond.Documents : 
    		null;
    }
    else
    {
    	result = 
    		EvaluateCondition(mc.Condition1, data) ||
    		EvaluateCondition(mc.Condition2, data) ? 
    		cond.Documents : 
    		null;
    }
  }
  return result;
}

private bool EvaluateCondition(Condition cond, DataObject data)
{
  object value =
    cond.Type == "stateCode"      ? data.StateCode      :
    cond.Type == "ledgerAmnt"     ? data.LedgerAmnt     :
    cond.Type == "coInsuredCount" ? data.CoInsuredCount	:
    cond.Type == "orgStatusCode"  ? data.OrgStatusCode	:
    string.Empty;
  return
    ( (cond.Operation == Operation.EqualTo              && value == cond.Value) ||
      (cond.Operation == Operation.NotEqualTo           && value != cond.Value) ||
      (cond.Operation == Operation.LessThan             && value <  cond.Value) ||
      (cond.Operation == Operation.GreaterThan          && value >  cond.Value) ||
      (cond.Operation == Operation.LessThanOrEqualTo    && value <= cond.Value) ||
      (cond.Operation == Operation.GreaterThanOrEqualTo && value >= cond.Value) ||
      (cond.Operation == Operation.IsNull               && value == null      ) ||
      (cond.Operation == Operation.IsNotNull            && value != null      )
    );
}
```

Noen som føler seg truffet?  **Varmer opp til Geek Cruise til helgen :)**

Ref:
- [http://thedailywtf.com/Comments/Soft_Coding.aspx#131288](http://thedailywtf.com/Comments/Soft_Coding.aspx#131288)
- [http://thedailywtf.com/Articles/Programming-Sucks!~~Or-At-Least,-It-Ought-To~~.aspx](http://thedailywtf.com/Articles/Programming-Sucks!~~Or-At-Least,-It-Ought-To~~.aspx)
- [http://wiki.cantara.no/display/PE/Geek+Cruise+23-25+May+2009+-+Architects+in+deep+water...](http://wiki.cantara.no/display/PE/Geek+Cruise+23-25+May+2009+-+Architects+in+deep+water...)
