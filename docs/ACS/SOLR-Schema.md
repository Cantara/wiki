# SOLR Schema

```
 <fields>
    <!-- general -->
    <field name="id" type="string" indexed="true" stored="true" multiValued="false" required="true"/>
    <field name="django_ct" type="string" indexed="true" stored="true" multiValued="false"/>
    <field name="django_id" type="string" indexed="true" stored="true" multiValued="false"/>

    <dynamicField name="*_i"  type="int"    indexed="true"  stored="true"/>
    <dynamicField name="*_s"  type="string"  indexed="true"  stored="true"/>
    <dynamicField name="*_l"  type="long"   indexed="true"  stored="true"/>
    <dynamicField name="*_t"  type="text_en"    indexed="true"  stored="true"/>
    <dynamicField name="*_b"  type="boolean" indexed="true"  stored="true"/>
    <dynamicField name="*_f"  type="float"  indexed="true"  stored="true"/>
    <dynamicField name="*_d"  type="double" indexed="true"  stored="true"/>
    <dynamicField name="*_dt" type="date" indexed="true" stored="true"/>
    <dynamicField name="*_p" type="location" indexed="true" stored="true"/>
    <dynamicField name="*_coordinate"  type="tdouble" indexed="true"  stored="false"/>
    
    <field name="_version_" type="long" indexed="true" stored ="true"/>

    <field name="rendered" type="string" indexed="false" stored="true" multiValued="false" />
    <field name="name" type="text_en" indexed="true" stored="true" multiValued="false" />
    <field name="department_exact" type="string" indexed="true" stored="true" multiValued="false" />
    <field name="fulljson" type="string" indexed="false" stored="true" multiValued="false" />
    <field name="text" type="text_en" indexed="true" stored="true" multiValued="false" />
    <field name="location_exact" type="string" indexed="true" stored="true" multiValued="false" />
    <field name="location" type="text_en" indexed="true" stored="true" multiValued="false" />
    <field name="name_exact" type="string" indexed="true" stored="true" multiValued="false" />
    <field name="department" type="text_en" indexed="true" stored="true" multiValued="false" />
    <field name="years_of_experience" type="long" indexed="true" stored="true" multiValued="false" />
    <field name="technology" type="text_en" indexed="true" stored="true" multiValued="true" />
    <field name="years_of_experience_exact" type="long" indexed="true" stored="true" multiValued="false" />
  </fields>
```

### Example data (fulljson field)

```
{
   "id":"2",
   "name":"Per Olsen",
   "title":"Consultant",
   "linkedin":"http://www.linkedin.com/profile/view?id=4010000",
   "phone":"+47 4000 50000",
   "mail":"per@olsen.com",
   "image":"photos/Per_3.JPG",
   "birthdate":"04/05/1979",
   "last_edited":"05/28/2013",
   "location":"Oslo",
   "department":".NET",
   "country":"no",
   "has_cv":"True",
   "completeness":{
      "percent":"100",
      "comment":[

      ]
   },
   "technology":[
      {
         "id":"2",
         "title":"Nøkkelkompetanse",
         "title_en":"Key Skills &amp; Expertise",
         "data":"Distributed Systems, Linux, Workshop Facilitation, Solution Architecture, Strategy",
         "data_en":"Cloud Computing, Software Design, Spring, XML, Distributed Systems, Linux, Workshop Facilitation, Solution Architecture, Strategy",

      }
   ],
   "experience":[
      {
         "id":"1",
         "title":"Utvikler",
         "title_en":"Developer",
         "from_year":"2010",
         "from_month":"0",
         "to_year":"2012",
         "to_month":"0",
         "description":"Ipsum lorum",
         "description_en":"",
         "company":"HomeMase Inc",
         "company_en":"",
         "techs":".NET, MS SQL",
         "techs_en":"",

      }
   ],
   "workplace":[
      {
         "id":"1",
         "title":"Utvikler",
         "title_en":"",
         "from_year":"1992",
         "from_month":"0",
         "to_year":"1993",
         "to_month":"0",
         "description":"databasesystemer",
         "description_en":"",
         "company":"Husmorbanken",
         "company_en":"",

      }
   ],
   "education":[
      {
         "id":"1",
         "title":"Skole",
         "title_en":"",
         "from_year":"1988",
         "from_month":"0",
         "to_year":"1990",
         "to_month":"0",
         "description":"Linje, fag.",
         "description_en":"",
         "school":"Husmorskolen",
         "school_en":"",

      }
   ],
   "other":[
      {
         "id":"1",
         "title":"Publikasjoner",
         "title_en":"",
         "data":"Et litt knippe.. ",
         "data_en":"",

      }
   ],
   "cv":[
      {
         "id":"8",
         "last_edited":"05/28/2013",
         "tags":"profil",
         "title":"Utvikler",
         "title_en":"Developer",
         "profile":"Ipsum lorum",
         "profile_en":"",
         "technology":[
            "2"
         ],
         "experience":[
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "29"
         ],
         "workplace":[
            "2"
         ],
         "education":[
            "1",
            "2",
            "3"
         ],
         "other":[
            "1",
            "2",
            "3"
         ],
         "is_recent":"True",
         "status":{
            "percent":"100",
            "complete":"True",
            "comment":"Your CV is complete! Give yourself a pat on the back!"
         }
      },
      {
         "id":"5",
         "last_edited":"12/11/2012",
         "tags":"Empty CV",
         "title":"None",
         "title_en":"None",
         "profile":"None",
         "profile_en":"None",
         "technology":[

         ],
         "experience":[

         ],
         "workplace":[

         ],
         "education":[

         ],
         "other":[

         ],
         "is_recent":"False",
         "status":{
            "percent":"",
            "complete":"",
            "comment":""
         }
      }
   ]
}
```
