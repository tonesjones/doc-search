---
title: "yieldOperator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/yieldoperator.html"
content_id: "2lIpXoN6jkAgoW1qD2c92Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:37:00.859169+00:00"
---

# yieldOperator

Matches `yield` or `yield*` (delegate) expressions in a generator.

This pattern only matches nodes of type `expression`.

## Properties

`yieldOperator` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isDelegate` | `bool` | Whether this is a delegate yield |
| `operandExpression` | `expression` | The expression that returns an iterable object |

**Inherits properties from:**

- astnode
- expression

## Example

The `yieldOperator` pattern matches the following yield operators:

[image: JavaScript code follows]

```
    function* f1() {
        yield 1;              // Case 1
    };

    function* f2() {
        yield* f1();          // Case 2
    };
```

For the first instance in `f1`, the `.isDelegate` property is `true`.
For the second instance in `f2`, it is `false`.
