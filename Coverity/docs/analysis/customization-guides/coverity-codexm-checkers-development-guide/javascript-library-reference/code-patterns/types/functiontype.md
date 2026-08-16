---
title: "functionType"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functiontype.html"
content_id: "mHISPAGdWNJ~HvUzr~zbGw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:20.931397+00:00"
---

# functionType

Matches function types.

This pattern only matches nodes of type `type`.

## Properties

`functionType` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `parameterCount` | `int` | The number of parameters declared by this function |

## Example

In the following JavaScript source,

[image: JavaScript code follows]

```
    function f() {
        // ...
    };
```

... the type of `f` matches `functionType` with
`.parameterCount` being 2, because of the two implicit
parameters `this` and `new.target`.
