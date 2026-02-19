# Web testing

## Strategies and tactics

### To web-test or not to web-test

It depends. Remember that even though web-tests may seem easy and quick, they are expensive compared to unit-tests. However, you can get pretty far with just having a single test or script that attempts to do some scraping of your webapp.

### Keep them outside the normal build

Cause they're slow.

### Choose tools carefully

Depending on the nature of your web application, different tools will suit you. Try out different ones and see what works for you.

## [Web test tools](Web-test-tools.md)

### Headless (these use virtual buffer browsers, like the HttpClient library)
- JWebUnit
- HttpUnit
- Canoo
- Celerity

### Browser JS-engine piggybackers

- JSUnit
- Selenium
- Sahi

### Native binders (these adapt directly to the browsers)

- Watir/FireWatir
- WebDriver

## Resources

- [Talk about web testing in general at JavaZone 2008](http://javazone.no/incogito/session/How+I+learned+to+love+and+hate+web-testing.html)
