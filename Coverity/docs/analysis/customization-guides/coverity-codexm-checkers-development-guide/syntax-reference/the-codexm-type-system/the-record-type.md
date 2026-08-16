---
title: "The record-type"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-record-type.html"
content_id: "~5BMHLFuPOVPqLm1qHGZrQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:08.514339+00:00"
---

# The record-type

A record assembles various named properties, which can be of various types, into a single structure.

## Syntax

  
 [image: Syntax diagram, record-type]   

```
record-type ::=
    'record' ( '[' underlying-type ']' )?
    '{'
        (      property-name '?'? ':' type
            ( ';' property-name '?'? ':' type )*
              ';'?              // final semicolon is optional
            )?
    '}'
```

Each `property-name` is an identifier.

## Details

When a question mark ( `?` ) follows a `property-name`,
the usage is similar to the character's use with the name of a type,
but there is a difference.
When a type is nullable, the question mark indicates that the `property-name` must be present,
but that its *value* might be `null`.
In a record definition, on the other hand, when the question mark follows `property-name`,
it indicates that the *property itself* can be omitted.
