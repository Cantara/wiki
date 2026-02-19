# Staged Spring

## Features 

(+) Annotation based 
(+) A clean solution to the problem of how to use different beans in different environments. 
(+) Many of the more complex other tactics can be omitted. 
(-) Requires Spring 2.5
(-) How are usernames and passwords managed? 
(-) Not all of the other tactics can be omitted. E.g., a PropertyPlaceholderConfigurer is still required to share a property between multiple beans. 

En Bean konfigurer seg selv. Autowire inn et property<sub>~object. Setter default</sub>~verdi her. 

Én property-fil med prefiks foran hver property. Kun diff må endres. (ikke prefiks per _fil_) 

To strategier: 
1. Selvkonfigurerende bønner 
2. Konfigurere med placeholder i appContext. 
2a. Bruker placeholders som "vanlig" placeholderConfigurer
2b. wrappe 3rd party bønnen i en egen bønne, injecte et propertyobject og sette defaultverdier her.
                                                    

## Resources

Frontend to all resources: http://trac.kaare<sub>~nilsen.com/staged</sub>~spring

#### Direct links

[Maven site](http://trac.kaare<sub>~nilsen.com/staged</sub>~spring/maven/)

[stage<sub>~aware</sub><sub>spring</sub><sub>contexts](http://kaare</sub><sub>nilsen.com/index.php/2008/04/02/stage</sub><sub>aware</sub>~spring-contexts/)
[stage<sub>~aware</sub><sub>spring</sub><sub>contexts</sub><sub>part</sub><sub>ii](http://kaare</sub><sub>nilsen.com/index.php/2008/04/06/stage</sub><sub>aware</sub><sub>spring</sub><sub>contexts</sub>~part-ii/)

Source repository: [Mercurial repo](https://hg.kaare<sub>~nilsen.com/staged</sub>~spring/) 
Old repo: [Subversion repo](http://kaare<sub>~nilsen.com/subversion/public/labs/staged</sub>~spring/) 

[Issue tracker](http://trac.kaare<sub>~nilsen.com/staged</sub>~spring/report/3)
