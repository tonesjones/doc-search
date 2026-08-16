---
title: "defaultStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defaultstatement.html"
content_id: "fUn6zEXWTzL0HI8MG5s_Bw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:55.156292+00:00"
---

# defaultStatement

Matches the `default` statement in a `switch`.

See also caseStatement.

## Properties

`defaultStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement

## Example

Using the same source code as the `switchStatement` pattern,
`defaultStatement` would match the `default` case.

The following pattern identifies switch statements that do have `default` cases:

  
 [image: CXM code follows]   

```
    // Switch with default statement
    pattern switchWithDefault {
        switchStatement as stms
            where exists stm in stms.caseList
                where stm matches defaultStatement
    };
```
