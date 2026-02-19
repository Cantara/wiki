# Staged Spring

## Features 

(+) Annotation based 
(+) A clean solution to the problem of how to use different beans in different environments. 
(+) Many of the more complex other tactics can be omitted. 
(-) Requires Spring 2.5
(-) How are usernames and passwords managed? 
(-) Not all of the other tactics can be omitted. E.g., a PropertyPlaceholderConfigurer is still required to share a property between multiple beans. 

En Bean konfigurer seg selv. Autowire inn et property-object. Setter default-verdi her. 

Én property-fil med prefiks foran hver property. Kun diff må endres. (ikke prefiks per _fil_) 

To strategier: 
1. Selvkonfigurerende bønner 
2. Konfigurere med placeholder i appContext. 
2a. Bruker placeholders som "vanlig" placeholderConfigurer
2b. wrappe 3rd party bønnen i en egen bønne, injecte et propertyobject og sette defaultverdier her.
                                                    

## Resources

Frontend to all resources: http://trac.kaare-nilsen.com/staged-spring

#### Direct links

[Maven site](http://trac.kaare-nilsen.com/staged-spring/maven/)

[stage-aware-spring-contexts](http://kaare-nilsen.com/index.php/2008/04/02/stage-aware-spring-contexts/)
[stage-aware-spring-contexts-part-ii](http://kaare-nilsen.com/index.php/2008/04/06/stage-aware-spring-contexts-part-ii/)

Source repository: [Mercurial repo](https://hg.kaare-nilsen.com/staged-spring/) 
Old repo: [Subversion repo](http://kaare-nilsen.com/subversion/public/labs/staged-spring/) 

[Issue tracker](http://trac.kaare-nilsen.com/staged-spring/report/3)
