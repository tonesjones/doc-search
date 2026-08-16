---
title: "The property-access-expression"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-property-access-expression.html"
content_id: "Jb_4Inc2y2vMXMkny4UyFw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:52.278523+00:00"
---

# The property-access-expression

Allows you to access individual proprties within a record.

## Syntax

An expression that refers to a collection of properties is followed by a dot ( `.` ),
and then by the name of the property to access.

  
 [image: Syntax diagram, property-access-expression]   

```
property-access-expression ::=
    property-producing-expression '.' identifier
```

The `property-producing-expression` can simply be the name of an existing record.
It can itself be a `property-access-expression`: This lets you write code that accesses the properties of a property.

The `property-producing-expression` can also be a `function`,
a `pattern`,
an `astnode`, or any other CodeXM type that has properties.
