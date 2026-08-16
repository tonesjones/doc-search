---
title: "The 'defineIssueType()' function"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-defineissuetype-function.html"
content_id: "wkflXrfIJngG4CpADP_0iA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:13.669836+00:00"
---

# The 'defineIssueType()' function

Sets the value of a checker's optional
`reports` > `issueType` component.
The `issueType` describes the purpose of the checker.

Here is an example of a call to `defineIssueType()`:

```
    let myIssueType = defineIssueType(
        {
            type         = "floating_point_equality";
            name         = "Bad comparison of floating-point expressions";
            description  = "Floating-point expressions shall not be directly"
                           + " or indirectly tested for equality or inequality.";
            localEffect  = "Unexpected behavior. Depending on the implementation,"
                           + " the comparison result may vary.";
            impact       = `Medium`;
        }
    )
```

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| `type` | `symbol` | A type identifier for the checker Like the name of a checker, this string must be unique within the CXM file. |
| `subtype` | `symbol?` | (Optional) A subtype identifier for the checker; `null` if not specified |
| `name` | `string` | A short description of the checker's issue type. This is the issue name that Coverity Connect will display. |
| `description` | `string` | A longer description of the checker's issue type |
| `localEffect` | `string` | The consequence that the detected issue has, or might have |
| `impact` | `enum` | The severity of the detected issue Possible `impact` values are `` `High` ``, `` `Medium` ``, `` `Low` ``, and `` `Audit` ``. |

The `type` and `subtype` values are
identifiers, not strings. They must conform to customary rules for identifiers:
have a leading alphabetical character, followed by letters or digits or the underscore
( `_` ). These rules are summarized
by the regular expression `^[a-zA-Z_][a-zA-Z0-9_]*$`. In addition, these identifiers must be
no longer than 64 characters.
