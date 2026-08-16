---
title: "qualifiersOf( typeName )"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/qualifiersof-typename-.html"
content_id: "QQuM40KX5dJiM3Md~gsvWQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:23.820521+00:00"
---

# qualifiersOf( typeName )

Returns a list of the qualifiers on a type.

## Parameters and return value

The return type is `list<qualifierEnum>`.

## Example

The following C/C++ source code has declarations that are qualified:

  
 [image: C/C++ code follows]   

```
volatile int a;
const char *b;
```

You could use the following CodeXM pattern to detect the `` `volatile` `` qualifier:

  
 [image: CXM code follows]   

```
    pattern useVolatileVariable {
        pattern {
            | variableReference as vr -> vr.type
            | pointerDereference as pd -> pd.type
            | memberReference as mr -> mr.field.type
            | subscriptReference as sr -> sr.type
        } as t where getQualifiersOf(t).contains(`volatile`)
    };
```
