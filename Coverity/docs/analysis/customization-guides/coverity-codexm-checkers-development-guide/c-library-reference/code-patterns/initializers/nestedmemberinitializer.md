---
title: "nestedMemberInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nestedmemberinitializer.html"
content_id: "FkPrnRz~_0K3G6iyATLiHA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:21.984220+00:00"
---

# nestedMemberInitializer

Matches object initializers that allow further nesting of initializers.

You can apply an initializer to a field or value obtained from a getter, as in the following C# example:

  
 [image: C# code follows]   

```
    var t = new T {
        nestedItem =        // nestedMemberInitializer
            {                   // addMemberInitializer
                { x, y }
            }
    };
```

This pattern only matches nodes of type addMemberInitializer,
assignmentMemberInitializer,
or `nestedMemberInitializer`.

## Properties

`nestedMemberInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `fieldOrGetter` | `bool` | Whether we are setting the value by using a field (`true`) or by using a getter (`false`) |
| `initializer` | `initializer` | The initializer used. **Note:** You can use any kind of initializer, not just member initializers. |
| `typeArguments` | `list<type>?` | The type arguments if `Generic` is involved; `null` otherwise |

**Inherits properties from:**

- astnode
- initializer

The following CodeXM pattern would match the C# example shown above:

  
 [image: CXM code follows]   

```
    pattern nestingWithAddInitializer {
        objectInitializer {
            .memberInitializers == nestedMemberInitializer {
                .initializer == objectInitializer {
                    .memberInitializers == addMemberInitializer
                }
            }
        }
    };
```

## See also

addMemberInitializer,
assignmentMemberInitializer,
objectInitializer
