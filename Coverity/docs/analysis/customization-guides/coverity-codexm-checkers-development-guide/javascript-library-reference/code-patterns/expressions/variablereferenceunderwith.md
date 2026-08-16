---
title: "variableReferenceUnderWith"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variablereferenceunderwith.html"
content_id: "8xFY7m9lJKQqYjsKsDTkWg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:36:41.764700+00:00"
---

# variableReferenceUnderWith

Matches JavaScript variable references under `with` statements.

A variable under a `with` statement can only be resolved at run time.
This pattern distinguishes such variables from regular ones.

This pattern only matches nodes of type `expression`.

## Properties

`variableReferenceUnderWith` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `identifier` | `string` | The identifier of the variable referenced |

**Inherits properties from:**

- astnode
- expression

## Example

In the following JavaScript example:

[image: JavaScript code follows]

```
    var a;
    with (Math) {
        a = PI;
    };
```

... the expression `PI` matches `variableReferenceUnderWith`,
and the `.identifier` property is `"PI"`.

## See also

withStatement
