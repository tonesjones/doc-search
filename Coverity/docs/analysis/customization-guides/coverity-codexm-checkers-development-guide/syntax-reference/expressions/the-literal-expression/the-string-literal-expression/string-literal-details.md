---
title: "string-literal details"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/string-literal-details.html"
content_id: "uKLFXclrco2inbB3gNFMug"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:46.622919+00:00"
---

# string-literal details

A string can contain any allowable CodeXM character, but certain situations
must be handled specially, as described in this section.

- To include a double quotation mark in a string, you must precede it ("escape" it) by a backslash
  ( `\` ).
  Otherwise, the double quote is parsed as an end-of-string marker, and the remainder of the string is most likely parsed as nonsense.

The following string uses correct syntax to include double quotation marks:

`"This is a string that contains \"quoted\" text"`

- In the CodeXM source file, a string *literal* can span multiple lines.
  This syntax is like C++.

For example, if the source contains the following lines:

[image: CXM code follows]

```
let str =
    "This is "
    "a"
    " multi-line string"
```

... then the variable `str` is assigned the string value
`"This is a multi-line string"`.

CAUTION:

You *cannot* concatenate string variables in this way.

- Conversely, a string itself can specify multiple lines. To do so, use the newline sequence ( `\n` ),
  as the following example shows:

`"The first line\nAnd the second line"`

- Once a string has been converted to an eventstring,
  it is no longer a string literal.
- Finally, be aware that the way a string value is being used can impose further constraints on what the string contains.
  For example, a string used to include a CXM source file must contain a valid path, according to the conventions
  of the operating system on which your code is running, and the name of the file to include must end in .cxm.
