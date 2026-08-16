---
title: "constructorInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/constructorinitializer.html"
content_id: "wbLol9Z1MgwOWELzShOTAQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:35:28.135051+00:00"
---

# constructorInitializer

Matches cases where a constructor is used to initialize an object.

This pattern only matches nodes of type `initializer`.

## Properties

`constructorInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `arguments` | `list<expression>` | A list of arguments passed to the constructor |
| `constructorFunction` | `symbol` | A symbol that represents the constructor function used |
| `enclosingClassReference` | `expression>` | Non-null when there is an inner class used. For example, in the initializer `y.new X()` this value would represent `y`. `null` if there is no inner class. |

**Inherits properties from:**

- astnode
- ctorinit

## Example

Given the following Java initialization:

  
 [image: Java code follows]   

```
ExampleObj o = new ExampleObject(5);
```

... you can use the following CodeXM pattern to match it. The example pattern below matches a constructor that uses an integer literal for its argument:

  
 [image: CXM code follows]   

```
    pattern ExampleObjectInitlizeLiteral {
        constructorInitializer as c where
            exists e in c.arguments where
                e matches integerLiteral
    };
```
