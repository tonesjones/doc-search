---
title: "Example of a checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-of-a-checker.html"
content_id: "nuMb7DanyJDl~TTOhQHaFA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:12.992125+00:00"
---

# Example of a checker

The sample code in this section shows a simple but working checker that contains all the components that Coverity requires to run the checker successfully.

```
include `C/C++`;

checker {
    name = "NO_GOTO";
    
    reports = for g in globalset allFunctionCode % gotoStatement :
    {
        events = [
            {
                description = "Found a "
                              + "goto".formattedAsCode
                              + " statement.";
                location = g.location;
            }
        ]
    }
};
```

These components of the code are worth noticing:

`include`
:   Includes patterns specific to the C or C++ languages, and ensures that the checker tests
    *only* C code or C++ code.

`name` assignment
:   Gives a name to the checker.
    This name will appear in reports of issues found.

`for` loop
:   Scans the target source looking for the `gotostatement` pattern.

`events` list
:   If there is a find, displays an issue report
    that shows the `description` and `location` specified here.
