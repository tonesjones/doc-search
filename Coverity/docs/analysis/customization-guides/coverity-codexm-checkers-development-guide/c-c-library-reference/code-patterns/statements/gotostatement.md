---
title: "gotoStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gotostatement.html"
content_id: "tmoEozlxh8s7jT1stIyv8A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:00.564102+00:00"
---

# gotoStatement

Matches `goto` statements.

## Properties

`gotoStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `labelStatement` | `statement` | The labeled statement to which the `goto` jumps. |

**Inherits properties from:**

- astnode
- statement

## Example

The CodeXM pattern `gotoStatement` matches `goto` in source code.
When matched, the pattern's `.labelStatement` property indicates the target label.

Consider the following target code:

  
 [image: C/C++ code follows]   

```
if ( i == 5 ) {
    goto flag;
}
    // ...
flag:
    count = 2;
```

In this example, `gotoStatement` matches the
`goto flag;` statement
and the pattern's `.labelStatement` is set to
`flag:`.
