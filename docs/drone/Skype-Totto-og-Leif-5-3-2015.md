# Skype Totto og Leif 5.3.2015

```

[05.03.2015 13:04:58] Leif H. Auke: Lage droneradar siten.
[05.03.2015 13:05:02] Leif H. Auke: (cool)
[05.03.2015 13:05:29] Thor Henning Hetland: bør vel også tenke på opex for en slik løsning?
[05.03.2015 13:06:13] Thor Henning Hetland: les:  en kan sikkert få endel til å bidra gratis med litt koding... men servere/infrastruktur er løpende kostnader
[05.03.2015 13:17:22] Thor Henning Hetland: https://wiki.cantara.no/display/drone/Home
[05.03.2015 22:58:04] Leif H. Auke: Vi må skalere for 1000 droner samtidig
[05.03.2015 23:06:15] Leif H. Auke: målet til drone radar er å publisere aktivitetene offentlig
[05.03.2015 23:07:16] Leif H. Auke: Jeg er skeptisk til å bruke tid på å fikle interfase og protokoller.  mye dårlig dokumentasjon blant annet.
[05.03.2015 23:07:27] Thor Henning Hetland: mm...   og det gir typisk en "html5-tung" frontend
[05.03.2015 23:07:54] Thor Henning Hetland: med lettvekts json plott-updates
[05.03.2015 23:07:58] Leif H. Auke: Ja. muligens.  der må det gjøre noen lure valg
[05.03.2015 23:08:47] Leif H. Auke: Ja.  for eks. bør gå på alt.
[05.03.2015 23:09:05] Thor Henning Hetland: vi har bygget alle "overvåknings" arkitekturene på den måten...   enkle json plot-overlays over en javascript-tung webapp...   som betyr ingen IE6,7-støtte
[05.03.2015 23:09:31] Thor Henning Hetland: kanskje pakke det med phonegap til android og iOS apps
[05.03.2015 23:10:59] Thor Henning Hetland: et arkitekturspm...   hva med historiskk?
[05.03.2015 23:11:40] Leif H. Auke: Jeg ser for meg historikk. Iallefall en hvis tid.
[05.03.2015 23:11:58] Leif H. Auke: Det handler om å kunne gå tilbake hvis det er klager o. l
[05.03.2015 23:13:05 | Redigert 23:13:29] Leif H. Auke: igjen. dette er fir å tilfredsstille offentligheten. overvåkning av potensielle overvåkere (droner som svirrer rundt)
[05.03.2015 23:13:28] Thor Henning Hetland: ser kulhetsfaktoren med å kunne spille/se flighten/statistikk og slikt... men det blir fort et helt annet ballgame
[05.03.2015 23:14:20] Leif H. Auke: Tror det må skilles på profesjonell og recreational bruk
[05.03.2015 23:14:20] Thor Henning Hetland: blir forten "strava" for drovefolket platform..  og da blir det fort også økonomi i livsløpet
[05.03.2015 23:15:38] Thor Henning Hetland: ...men det blir jo fort ustrolig store datamengder...
[05.03.2015 23:15:40] Leif H. Auke:  For de som leker kan man lage mye kult. Stig mente bygge in gameification. konkurranser. poeng osv osv.
[05.03.2015 23:15:52] Leif H. Auke: Men det kan være delsystemer rundt
[05.03.2015 23:16:28] Leif H. Auke: Fir proff markedet tror det handler om identifikasjon.  hvem er hvor.
[05.03.2015 23:16:43] Thor Henning Hetland: ja, men spørsmålet var jo om vi trengte å ta vare på alle detastrømmene...    for en ren aggregering/visning... så kan serveren nesten være helt stateless
[05.03.2015 23:17:20] Leif H. Auke: Ja. egentlig.
[05.03.2015 23:17:57] Leif H. Auke: Men du kan feede ut til andre historie databaser og holde runtime stateless ?
[05.03.2015 23:17:58] Thor Henning Hetland: skal vi lagre strømmene...  så blir det lett 100g-1t data/mnd
[05.03.2015 23:18:33] Leif H. Auke: Hm.  ja. Jeg har ikke regnet på det skal jeg være ærlig.
[05.03.2015 23:18:34] Thor Henning Hetland: ja...    men en viktig initiell beslutning er om vi skal lagre unna fra dag 1
[05.03.2015 23:18:46] Leif H. Auke: Ja.
[05.03.2015 23:19:19] Thor Henning Hetland: jeg har heller ikke regnet på det...  men det er typisk område....    på de antallene du skisserte
[05.03.2015 23:19:21] Leif H. Auke: Jeg syntes det skal være en begrenset historikk. Den behøver heller ikke ha samme oppløsning som live feed
[05.03.2015 23:19:56] Leif H. Auke: Men vise en rute ned på en gitt oppløsning
[05.03.2015 23:20:09] Thor Henning Hetland: kommer ann på perspektivet du har på løsningen... og der er gruppa neppe enig
[05.03.2015 23:20:40] Thor Henning Hetland: det vil sikkert også være forskjell på hvor ofte sensorene sender gps readings
[05.03.2015 23:21:43] Thor Henning Hetland: ..men som du ser...  det er nok ikke-teknisk dere kan bryne dere på på første møte...  så kan vi snu bunken på møte 2 hvor vi ser på konsekvensene av ønskene.. og identifiserer hovedomponentene i arkitekturen
[05.03.2015 23:22:14] Leif H. Auke: Noe sånt.
[05.03.2015 23:23:33] Leif H. Auke: Vi har et prosjekt som bør angripes fra to ender. time to market er viktig. Det er nå det skjer, men vi må ikke låse oss inne. 

```
