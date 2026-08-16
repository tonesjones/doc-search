---
title: "labelStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/labelstatement.html"
content_id: "iTw5m10hWa__cKKGp01bAw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:02.108060+00:00"
---

# labelStatement

Matches statements that have a label.

## Properties

`labelStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `nameString` | `string` | The value of the label |
| `targetStatement` | `statement` | The statement to which this label is assigned |

**Inherits properties from:**

- astnode
- statement

## Example

Using the same source code as the `gotoStatement` pattern,
the `labelStatement` pattern matches the `flag: target`,
and `.targetStatement` contains the statement that follows;
specifically, the assignment `count = 2;`/:

  
 [image: C/C++ code follows]   

```
if ( i == 5 ) {
    goto flag;
}
    // ...
flag:
    count = 2;
```
