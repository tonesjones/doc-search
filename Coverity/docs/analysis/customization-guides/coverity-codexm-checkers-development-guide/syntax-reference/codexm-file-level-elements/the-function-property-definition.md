---
title: "The function-property-definition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-function-property-definition.html"
content_id: "zDCc2eEYIyXvyl7VR6ytCw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:17.263474+00:00"
---

# The function-property-definition

A function property is, in effect, a subordinate checker that provides information about functions in the source code.
It allows the checker to match characteristics found in functions called by top-level functions.

An example might be, "Does this function, *or any function it calls,* call `system()`?".
Function properties permit a lightweight form of interprocedural analysis.
See Function properties.

## Syntax

Function properties are defined using the keyword phrase `function property`,
followed by an identifier that names the function property,
followed by a record that has a single property named `models`,
specified by a pattern.

  
 [image: Syntax diagram, function-property-definition]   

```
function-property-definition ::=
    'function' 'property' identifier '{'
        'models' '=' pattern-expression';'
    '}'
```
