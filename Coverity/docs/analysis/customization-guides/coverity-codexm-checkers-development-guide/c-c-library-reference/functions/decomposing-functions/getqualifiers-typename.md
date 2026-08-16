---
title: "getQualifiers( typeName )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/getqualifiers-typename-.html"
content_id: "eC7ycKPNUC18NDglTZPEIQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:23.069664+00:00"
---

# getQualifiers( typeName )

## Parameters and return value

| Name | Type | Description |
| --- | --- | --- |
| `typeName` | `type` | The type to match |
| ***return value*** | `set<qualifiers>` | A set whose members represent the qualifiers applied to the type |

## Example

Given the following target code snippet:

  
 [image: C/C++ code follows]   

```
volatile int a;
const char *b;
```

The following CodeXM pattern would detect the `volatile` qualifier:

  
 [image: CXM code follows]   

```
    pattern useVolatileVariable {
        pattern {
            | variableReference as vr   -> vr.type
            | pointerDereference as pd  -> pd.type
            | memberReference as mr     -> mr.field.type
            | subscriptReference as sr  -> sr.type
        }
        as t where getQualifiers( t ).contains( `volatile` )
    };
```
