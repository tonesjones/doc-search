---
title: "objectInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/objectinitializer.html"
content_id: "Mh43XvvoNleQuKMSXNPHrw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:22.824734+00:00"
---

# objectInitializer

Matches object initializers used in variable declarations and temporary constructions.

The constructor is called first, then additional initializers are called.
A user can specify a series of field or property assignments. For example:

  
 [image: C# code follows]   

```
    Cat cat = new Cat { Age = 10, Name = "Fluffy" };
```

Also, collections can have multiple values which are all added via calls to
collection, as in the following code:

  
 [image: C# code follows]   

```
    List<int> digits = new List<int> { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
```

This pattern only matches nodes of type `initializer`.

## Properties

`objectInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `initializer` | `initializer` | The constructor used |
| `memberInitializers` | `memberInitializer` | The member initializer used |

**Inherits properties from:**

- astnode
- initializer

## Example

The following CodeXM pattern matches a collection initializer:

  
 [image: CXM code follows]   

```
    pattern collectionInitializer {
        objectInitializer {
            .memberInitializers == addMemberInitializer
        }
    };
```

## See also

addMemberInitializer,
assignmentMemberInitializer,
nestedMemberInitializer,
temporaryConstruction,
temporaryExpression,
variableDeclaration
