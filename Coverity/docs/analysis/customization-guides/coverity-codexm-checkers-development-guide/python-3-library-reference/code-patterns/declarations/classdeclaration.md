---
title: "classDeclaration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classdeclaration.html"
content_id: "A~mvVBMozP~SuBmr5CdXiQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:30.914085+00:00"
---

# classDeclaration

Matches class declarations.

This pattern only matches nodes of type `statement`.

## Properties

`classDeclaration` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `baseClasses` | `list<variableReference>` | The base classes of this class |
| `constructor` | `symbol` | The constructor function for this class |
| `instanceMembers` | `list<statement>?` | This class's instance members and properties; `null` if there are none |
| `name` | `expression` | The name of the class |
| `staticMembers` | `list<statement>?` | This class's static methods; `null` if there are none |

**Inherits properties from:**

- astnode
- declaration

## Example

The following CodeXM pattern matches a class declaration that inherits from a class named `Foo`:

[image: CXM code follows]

```
    pattern inheritsFromFoo {
        classDeclaration as decl where (
            exists c in decl.baseClasses where
                c matches variableReference {
                    .simpleName == "Foo"
                }
        )
    };
```
