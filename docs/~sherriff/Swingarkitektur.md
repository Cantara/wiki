# Swingarkitektur

10:47 < mattis> er det Maedhros som er Swing-guruen?
10:47 <@Maedhros> der skal være noe som heter getScaledInstance eller noe slikt
10:48 <@Maedhros> nei, det var Twelvemonkeys
10:49 <@trygvis> hm
10:49 <@Maedhros> trygvis: se på denne: http://github.com/haraldk/TwelveMonkeys/blob/master/common/common-image/src/main/java/com/twelvemonkeys/image/ImageUtil.java
10:51 <@Maedhros> jo der var en getScaledInstance
10:51 <@Maedhros> http://download.oracle.com/javase/6/docs/api/java/awt/Image.html
10:51 <@trygvis> jau
10:51 <@trygvis> funket det
10:52 <@Maedhros> mattis: guru og guru fru blom.
10:52 <@trygvis> mattis: han svarer på alle mine spørsmål
10:53 <@trygvis> eller i hverfall frustrerer med meg :)
10:53 < mattis> will trade beer for Swing?
10:53 < mattis> ;)
10:55 < mattis> bruker du/dere noen spesiell arkitektur i Swing-programmene deres?
10:55 <@trygvis> jeg prøver stadig å finne ut hva den arkitekturen er
10:55 <@trygvis> swing har iofs en egen arkitektur, men den er ganskelavnivå
10:55 < mattis> opplever at det fort blir mye wireing og rot
10:55 < mattis> trygvis: da er vi i samme båt
10:55 <@trygvis> jau
10:59 < mattis> så langt virker det som det er praktisk å ha en klasse per vindu, og samle relevante listeners inne i den klassen
10:59 < mattis> men de blir fort HUGE
11:03 < mattis> Maedhros: vet du om et litt større Swing-prosjekt man kunne studert for å lære litt arkitektur
11:08 <@Maedhros> tja, EMS klienten kanskje
11:08 <@Maedhros> men jeg er ikke fornøyd med den
11:09 <@Maedhros> der er flere problemer med Swing som sådan, man må feks lage sin egen livssyklus for komponenter.
11:10 < mattis> bruker du noen spesielle teknikker/patterns når du setter sammen en Swing-app?
11:10 <@Maedhros> MVP er bra. (Model, View, Presenter)
11:11 <@Maedhros> http://www.google.no/url?q=http://martinfowler.com/eaaDev/ModelViewPresenter.html&sa=U&ei=Iya0TOmhFMWaOsmtiOcJ&ved=0CCkQFjAC&usg=AFQjCNHHRDVQyeafb_UQaJDUktZ84A1f_g
11:13 < mattis> definerer du én og én komponent som et eget view, en logisk klynge med komponenter som eget view eller et vindu som et eget view?
11:13 <@Maedhros> hvordan gjøre trådhåndtering (alle tunge ting går off-EDT) her er http://kenai.com/projects/bsaf/pages/Home ganske bra. eller http://kenai.com/projects/guts/pages/Home
11:15 <@Maedhros> det kommer helt an på applikasjonen din. som regel vil det bli en composite component.
11:15 < mattis> altså en klynge av komponenter?
11:16 <@Maedhros> jau
11:17 <@Maedhros> Hva mener man om Register objekter? feks noe som har en "public <T> T getService(Class<T> serviceType)" metode. er det dårlig design?
11:17 <@Maedhros> bør man heller ha alle dependencies til en klasse explisitte i stedet?
11:22 < mattis> bruker du noen form for Dependency Injection?
11:22 <@Maedhros> ikke rammeverk nei
11:24 < mattis> da synes jeg getService ikke virker som noen dårlig idé
11:26 < mattis> ser ikke ut som det blir noen sterkere koblinger i hvertfall
11:44 < Titan> jeg jobber mye med swing, og jeg får veldig mange små klasser =)
11:45 < Titan> jeg delegerer som regel alt ned til små views
