---
title: "constructorInitializer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/constructorinitializer.html"
content_id: "g5NYibh8Mbi7uPmUgBIxyw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:56.135933+00:00"
---

# constructorInitializer

Matches cases where a class constructor (C++ only) is used to initialize an object

## Properties

`constructorInitializer` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `constructorFunction` | `functionType` | The constructor function called to initialize the object |
| `arguments` | `list<initializer>` | A list of the arguments passed to the constructor |

**Inherits properties from:**

- astnode
- ctorinit

## Example

The `constructorInitializer` pattern matches the following target code:

  
 [image: C++ code follows]   

```
T t(0);
T t();
```

... such that the `.arguments` list holds a single argument
(for example, `0`) for the first instance and an empty list for the second.

Here is a CodeXM pattern that matches a constructor that has no arguments:

  
 [image: C/C++ code follows]   

```
    pattern defaultConstructor {
        constructorInitializer as i
            where i.arguments.length == 3
    };
```
