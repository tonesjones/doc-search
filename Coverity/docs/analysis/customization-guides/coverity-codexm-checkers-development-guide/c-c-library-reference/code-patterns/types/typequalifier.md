---
title: "typeQualifier"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/typequalifier.html"
content_id: "YvSD1NQyGAgxPQB_gjMZTQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:21.545062+00:00"
---

# typeQualifier

Matches C-language type qualifiers, such as `const`,
`volatile`, or `restrict`.

This pattern *does not* match the C++ qualifier `_Atomic`.

## Properties

`typeQualifier` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `qualifierList` | `list<enum qualifierEnum>` | The qualifiers of the type: Items in the list can be `` `const` ``, `` `volatile` ``, or `` `restrict` ``; see qualifierEnum |
| `targetType` | `type` | The type the qualifier is applied to |

## Example

Given the following target code snippet:

  
 [image: C/C++ code follows]   

```
const int i = 1;
```

... the following CodeXM pattern:

  
 [image: CXM code follows]   

```
    node matches expression as e
        && e.type matches typeQualifier as ty
            where ty.qualifierList.contains( `const` );
```

... matches the variable `i`, because this variable's declaration
is qualified by `const`.
