---
title: "objectLiteral"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/objectliteral.html"
content_id: "i2g9pdVh9y7BuxyaGxvkyA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:46.527942+00:00"
---

# objectLiteral

Matches object literals.

An *objectLiteral* (as specified in ECMAScript 2015, 12.2.6.) is an expression that describes the initialization of an object.

This pattern only matches nodes of type `expression`.

## Properties

`objectLiteral` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `propertyDefinitionList` | `list<propertyAssignment>` | The list of property assignments |

**Inherits properties from:**

- astnode
- expression

## Example

The `objectLiteral` pattern matches the initializer of `obj`:

[image: JavaScript code follows]

```
    var obj = {a: 'hello', b: 1, c: {}};
```

The `.propertyDefinitionList` property is a list of three elements.
For the first element, its `propertyName` is a string `"a"`,
and its `value` is a string literal `"hello"`.
