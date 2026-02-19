# Input Validation

## Input validation in webapplications.

Good ideas:

- Use whitelisting
- Strictly define what you expect. Take some time and identify what the properties of your legal data is.
- Centralize rules, make sure you don't define them more than one place.
- Apply the rules always.
- Validate early

Bad ideas:

- Defining your own rules for well known concepts like email, dates, credit cards.
- Blindly trust application firewalls to wash your input.

These are concepts which are incorporated in many frameworks. A well tested and standard framework can make sure you centralize rules, apply the rules for you, validates as a part of filters or interceptors and provides some standard validation rules.

Enterprise Security API (ESAPI) from OWASP aims to provide you with most of what you would need of predefined standard rules. Struts2 also comes with standard validators.

For instance if you are using Struts2 or some other web application framework there should be some standard integration points for your validation. Struts2 comes with validation as interceptor. Every time you post, the request will be intercepted and processed by the validation rules. If there is any void input the interceptor will, based on your selection, continue to validate all fields and return all errors or return at once with the error.
