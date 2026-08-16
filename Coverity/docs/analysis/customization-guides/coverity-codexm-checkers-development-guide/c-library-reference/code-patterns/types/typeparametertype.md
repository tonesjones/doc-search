---
title: "typeParameterType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/typeparametertype.html"
content_id: "iXLv8bDFAFi1ojk8w4Cs5g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:31:25.122081+00:00"
---

# typeParameterType

Matches all C# parameter types.

This pattern only matches nodes of type `type`.

## Properties

`typeParameterType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name of the parameter type |

## Example

The following CodeXM pattern matches all parameters whose type is `Element`:

  
 [image: CXM code follows]   

```
    t matches typeParameterType {
        .name == "Element"
    };
```

## See also

genericType
