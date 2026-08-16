---
title: "addMemberInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/addmemberinitializer.html"
content_id: "OShrk_1IQNiitESvbJsTJQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:15.940028+00:00"
---

# addMemberInitializer

Matches collection initializers.

Collection initializers let you specify one or more element initializers
when you initialize a collection type that implements `IEnumerable` and has an
add method. For example:

  
 [image: C# code follows]   

```
    List<int> digits = new List<int> { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
```

This pattern only matches nodes of type
`addMemberInitializer`,
assignmentMemberInitializer,
or nestedMemberInitializer.

## Properties

`addMemberInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `addFunction` | `functionType` | The add method used |
| `arguments` | `list<expression>` | The argument used for add |
| `typeArguments` | `list<type>?` | The type argument if `Generic` is involved |

**Inherits properties from:**

- astnode
- initializer

## Example

The following CodeXM pattern matches the C# example shown in the previous section:

  
 [image: CXM code follows]   

```
    pattern collectionInitializer {
        objectInitializer {
            .memberInitializers == addMemberInitializer
        }
    };
```

## See also

assignmentMemberInitializer,
nestedMemberInitializer,
objectInitializer
