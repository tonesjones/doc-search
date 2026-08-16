---
title: "assignmentMemberInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/assignmentmemberinitializer.html"
content_id: "_eVceBrKHp0oFBfRH72cOg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:18.163456+00:00"
---

# assignmentMemberInitializer

Matches object initializers that set the value of their members.

Object initializers let you assign values to any accessible fields or
properties of an object at creation time. If you use an object initializer, you don't have to invoke a
constructor followed by lines of assignment statements. For example:

  
 [image: C# code follows]   

```
  Cat cat = new Cat { Age = 10, Name = "Fluffy" };
```

This pattern only matches nodes of type addMemberInitializer,
`assignmentMemberInitializer`,
or nestedMemberInitializer.

## Properties

`assignmentMemberInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression for the initial value. |
| `fieldOrSetter` | `bool` | Whether we are setting via a field (`true`) or via a getter (`false`) |
| `typeArguments` | `list<type>?` | The type argument if `Generic` is involved; `null` otherwise |

**Inherits properties from:**

- astnode
- initializer

## Example

The following CodeXM pattern matches the C# example shown in the
"Detail" section,
above:

  
 [image: CXM code follows]   

```
    pattern objectInitializerWithNull {
        objectInitializer {
            .memberInitializers == assignmentMemberInitializer {
                .expression = nullLIteral
            }
        }
    };
```

## See also

addMemberInitializer,
nestedMemberInitializer,
objectInitializer
