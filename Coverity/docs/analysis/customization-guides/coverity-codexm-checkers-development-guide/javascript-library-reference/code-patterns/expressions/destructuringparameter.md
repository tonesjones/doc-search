---
title: "destructuringParameter"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/destructuringparameter.html"
content_id: "VGKp~pNdQ7SBlwfopD77tw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:29.315589+00:00"
---

# destructuringParameter

Matches JavaScript destructuring parameters.

This pattern only matches nodes of type `expression`.

## Properties

`destructuringParameter` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `originalParameter` | `expression` | The reference to the original parameter |
| `parameterList` | `list<record>` | The list that contains the parameters and their default values |

**Inherits properties from:**

- astnode
- expression

## Example

Matches the declaration of the parameter in the following function:

[image: JavaScript code follows]

```
    function f({name = 'a', age}) {
        return name + age;
    };
```

In this instance, the `.originalParameter` property is a reference to parameter `{name, age}`,
and the `.parameterList` property is a list of two record elements.
The first element has the `.defaultExpression` property, which is literal `'a'`, and
the `parameter` property which is a reference to the variable `name`.
The second element has a `null` `.defaultExpression` property, and
the `.parameter` property, which is a reference to the variable `age`.
