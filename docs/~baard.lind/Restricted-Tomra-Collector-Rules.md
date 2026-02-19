# Restricted-Tomra Collector Rules

### Relational Model only. 
**Diagram: Architecture**
Challenge:
- Hi rate of updates on UserSessions will slow down the whole system.

### Loose Coupling - allow for unique life-cycle pr module.
**Diagram: Architecture**

---

### Accounting Module
###### AddCurrencyService
Input:
```lang
<currencies>
  <currencyEntry>
    <currencyEventId/>
    <currencyId/>
    <userId/>
    <programId/>
    <currencyTypeId/>
    <ammount/>
  </currencyEntry>
<currencies/>
```

Response:
```lang
<currencies>
  <addCurrencyEventId status="OK"/>
  <addCurrencyEventId status="FAILED">
    <failure>
      <failureTypeId/><!--Data or Technical, retry possible or not-->
      <failureUniqueId/><!--Able to see the log entry in Accounting Module-->
      <currencyEntry>
        ....
      </currencyEntry>
    <failure>
  </addCurrencyEventId>
<currencies>
```

###### Currency
```lang
<currencyEntry>
  <currencyId/>
  <userId/>
  <programId/>
  <currencyTypeId/>
  <ammount/>
</currencyEntry>
```
- One Currency entry pr Rule, and CurrencyType. 
- No automatic agregation.

###### CurrencyType
```lang
<currencyTypeEntry>
  <currencyTypeId/>
  <name/>
  <comment/>
</currencyTypeEntry>
```
- Comment is to help developers and -rule configurators use the right type. Presentation of names in correct language is the responsibility of the GUI.

###### GovernanceLog
```lang
<governanceLogEntry>
  <currencyId/>
  <userId/>
  <programId/>
  <timestamp/>
</governanceLogEntry>
```

###### ~~OUTSIDE this MODULE~~ 
```lang
<totalScoreEntry>  
  <userId/>
  <programId/>
  <currencyTypeId/>
  <amount/>
</totalScoreEntry>
```

---
### Collector Rule Module
###### AddRuleService
Input:
```lang
?
```

Response:
```lang
<rules>
  <addActiveRule templateId="12234ABF" instanceId="i45678" status="ADDED_NOT_ACTIVATED"/>
  <addActiveRule id="12234ADD" status="FAILED">
    <failure>
      <failureTypeId/><!--Data or Technical, retry possible or not-->
      <failureUniqueId/><!--Able to see the log entry in Accounting Module-->
      <ruleEntry>
        ....
      </ruleEntry>
    <failure>
  </addActiveRule >
  <addActiveRule templateId="12234ABF" instanceId="i45678" status="ADDED_NOT_ACTIVATED"/>
<rules>
```
###### ActivateRuleService

###### DeactivateRuleService

###### CreateCampaignRuleService

### Data Elements
###### Rule
Passive Rules in Template Repository
```lang
<ruleTemplate>
  <ruleId/>
  <inputParams>
    <programId/>
    <collectables> <!-- at least one, or all -->
      <item ean="ac1234"/>
        <minCount="5"/>
        <maxCount="100"/>
       </item>
      <item ean="1234"/>
      <collectableTypeId/><!--CocaCola, Can, Farris 1,5 litre ...-->
      <collectableId/>
  </inputParams>
  <outputParams>
    <currencyTypeId/>
    <amount/>
  <outputParams>
  <enabled/>
</ruleTemplate>
```
###### Campaign
```lang
<campaignRuleEntry>
  <campaignRuleId/>
  <baseRuleId/> <!--Base the campaign on this rule -->
  <currencyTypeId/>
  <collectables>
    <item typeId="ac1234" count="444"/>
    <item typeId.../>
  <ammount/>
   <activateOnDateTime/>
   <deactivateOnDateTime/>
  <enabled/>
</campaignRuleEntry>
```

###### Collectable
Might be moved to another module.
```lang
<collectable>
  <collectableId/>
  <eancodeList>
    <ean/>
    <ean/>
  </eancodeList>
  <collectableTypeId/>
  <weight/>
  <co2footprint/>
</collectable>
```
