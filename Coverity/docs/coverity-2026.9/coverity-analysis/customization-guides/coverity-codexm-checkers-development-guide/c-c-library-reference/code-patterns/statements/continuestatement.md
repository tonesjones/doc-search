---
title: "continueStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/continuestatement.html"
content_id: "qmyBbDZ78LKSD~5zVUtrKw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:17.153349+00:00"
---

# continueStatement

Matches `continue` statements.

## Properties

`continueStatement` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `controlStatement` | `statement` | The loop statement for which the `continue` statement occurs. |

**Inherits properties from:**

- astnode
- statement

## Example

A `continueStatement` pattern matches the `continue` statement in the following example
(`.controlStatement` is the outer `for` loop):

  
 [image: C/C++ code follows]   

```
for ( int count = 0; count < 10; count++ ) {
    if ( count == 5 ) {
        continue;        // continueStatement matches this
    }
};
```

To detect all `continue` statements, you can use the following pattern:

  
 [image: CXM code follows]   

```
    for c in codes {
        where c matches continueStatement
            // ...
    };
```
