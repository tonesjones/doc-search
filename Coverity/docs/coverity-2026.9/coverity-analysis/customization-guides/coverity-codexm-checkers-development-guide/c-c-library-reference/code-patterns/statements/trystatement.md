---
title: "tryStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/trystatement.html"
content_id: "CGDNXLsdl3MCbDxmnxDyww"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:17.861611+00:00"
---

# tryStatement

Matches `try` statements (C++ only), including any catch blocks associated with the try.

## Properties

`tryStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `bodyStatement` | `statement` | The statement in the body of the `try` statement |
| `catchBlockList` | `list<record>` | The list of catch blocks |

**Inherits properties from:**

- astnode
- statement

## Example

The `tryStatement` pattern matches target source code such as this:

  
 [image: C++ code follows]   

```
try {
    int i = 1;
}
catch(Exception1 e1) {
}
catch(Exception2 e2) {
}
catch(Exception3 e3) {
}
```

... where in this example, `.bodyStatement` refers to
`int i = 1;`
and `.catchBlockList` is a list that contains
`Exception1`, `Exception2`, `Exception3`.
