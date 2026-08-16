---
title: "constructorInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/constructorinitializer.html"
content_id: "nMmZ7LFbaAHM41z5nfau1A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:19.836209+00:00"
---

# constructorInitializer

Matches cases where a constructor is used to initialize an object.

This pattern only matches nodes of type `initializer`.

## Properties

`constructorInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `arguments` | `list<expression>` | A list of the arguments passed to the constructor |
| `constructorFunction` | `symbol` | The symbol that represents the constructor function used |
| `enclosingClassReference` | `expression?` | Non-null when an inner class is used. For example, in the initializer `y.new X()` this value would be `"y"`. |

**Inherits properties from:**

- astnode
- ctorinit

## Example

Given the following C# initialization:

  
 [image: C# code follows]   

```
    ExampleObj o = new ExampleObject(5);
```

... the following CodeXM code can be used to match it. The example pattern matches a constructor that takes an integer literal as its argument:

  
 [image: CXM code follows]   

```
    pattern ExampleObjectInitlizeLiteral {
        constructorInitializer as c where
            exists e in c.arguments where
                e matches integerLiteral
    };
```
