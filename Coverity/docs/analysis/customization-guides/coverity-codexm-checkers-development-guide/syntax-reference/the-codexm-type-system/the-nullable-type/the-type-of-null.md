---
title: "The type_of_null"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-type_of_null.html"
content_id: "PXGBMpJVTTwdUlZkolaACA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:07.034231+00:00"
---

# The type_of_null

This is the type of the object `null`;
in other words, it is the type of a property that has not been specified.

## Syntax

  
 [image: Syntax diagram, type_of_null]   

```
type_of_null ::=
    'null'
```

## Details

An expression, such as a function, that accepts a nullable type will also accept an object that is `null`.
