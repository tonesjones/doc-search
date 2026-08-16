---
title: "fieldAccess"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fieldaccess.html"
content_id: "fHVsia1id9BOWVra4_qvzw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:02.653997+00:00"
---

# fieldAccess

Matches all accesses to fields.

This pattern only matches nodes of type `expression`.

## Properties

`fieldAccess` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `field` | `symbol` | The symbol of the field being accessed |
| `objectExpression` | `expression` | The object that owns the field being accessed |

**Inherits properties from:**

- astnode
- expression

## Example

For a Java `class` like this:

  
 [image: Java code follows]   

```
Example {
    public int myPublicInt;
};
```

... and an access like this:

  
 [image: Java code follows]   

```
Example e;
    int i = e.myPublicInt;
```

... the following CodeXM pattern finds the access:

  
 [image: CXM code follows]   

```
    pattern accessToExamplePublicInt {
        fieldAccess {
            .objectExpression == expression {
                .type == classType { .simpleName == "Example" }
            };
            .field == symbol { .simpleName == "myPublicInt" }
        }
    };
```
