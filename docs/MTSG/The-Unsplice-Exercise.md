# The Unsplice Exercise

### The Unsplice Exercise

The unsplice exercise is very simple. Your task is to write a function that removes all occurences of the two characters \ (backslash) and \n (newline) when they occur consecutively in an array of chars.

Example 1: Before: abc\\\ndef After: abcdef

The unsplice operation has removed one occurence of the backslash newline pair.

Example 2: Before: abc\\d\nef After: abc\\d\nef

The unspliced version is unchanged because the backslash and newline characters are not consecutive.

Example 3: Before: abc\n\\def After: abc\n\\def

The unspliced version is unchanged because the backslash and newline characters are in the wrong order.

Example 4: Before: abc\\\\\n\ndef After: abc\\\ndef

The unspliced operation has removed one occurence of the backslash newline pair. Note that another occurence of the backslash newline pair remains. This is because the unsplice operation is "one-pass only".
