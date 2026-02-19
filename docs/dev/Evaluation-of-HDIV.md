# Evaluation of HDIV

What HDIV provides:

HDIV provides a state management mechanism which adds a hashed state of parameters sent to the client which makes it possible to detect any alterations a client makes to so-called "non editable" data (combobox, hidden fields etc.)

The problem of editable data, textfields, textareas etc must be managed by additional xml configuration.

What does not HDIV provide (of OWASP top ten):

- A1 It does not give you protection against XSS and input validation "out of the box".
- A1 It does not do output encoding
- A2 As with A1, you have to make your own rules.
- A7 Gir deg ikke noe session management eller authentication funksjonalitet.
- A8 HDIV har ikke noe krypteringsfunksjonalitet.
- A9 HDIV ser ikke på SSL/ikke SSL, eller krypteringsalgoritme
