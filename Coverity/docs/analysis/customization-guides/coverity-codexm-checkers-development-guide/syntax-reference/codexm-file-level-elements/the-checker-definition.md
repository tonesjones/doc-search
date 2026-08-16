---
title: "The checker-definition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-checker-definition.html"
content_id: "fUlsUpVbbf9Y_eoQoXUWcw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:12.315808+00:00"
---

# The checker-definition

Most of a typical CodeXM file consists of `checker-definition` elements.

A checker element defines what the checker is searching for. It also specifies the report to generate when the examined target code
is found to match the pattern described by this definition. Other CodeXM elements work to support the logic embodied by checkers.

## Syntax

A checker is defined using the keyword `checker` followed by a record-expression.

When used to define a checker (as opposed to simply structuring data), a `record-expression`
must contain a specific set of elements, structured in a specific way. These requirements are described in the
"Details" section that follows.

  
 [image: Syntax diagram, the checker-definition]   

```
checker-definition ::=
    'checker' record-expression
```

## Details

The names of these elements are as follows:

`name`
:   A string that names the checker

    This string must be unique within the CXM file.

`reports`
:   A record that defines the checker's behavior.

    The `reports` record contains the following components:

    A for-loop expression (required)
    :   The `for-loop expression` defines the pattern for which this checker searches.
        This expression must declare a variable to represent the portion of the code that is being searched.
        Typically this portion is in the range `globalset`—which, if not qualified,
        indicates all target-language code within the target source file.

    `events` (required)
    :   A list that contains at least one record (and that usually contains only a single record).
        The `events` records specify what to report when a search is successful.

        Each record in the `events` list contains the following components:

        `description` (required)
        :   A string or eventstring that the checker will display when it finds an issue.
            This text should describe the issue that was found.

        `location` (required)
        :   The `location` property must be assigned the `.location` property of the variable
            declared in the `reports`-level `for` loop.

        `tag` (optional)
        :   A string to identify this particular `events` record.
            For example, you might use `tag` values to facilitate searches in a .cxm file that contains multiple checkers.

    `issueType` (optional)
    :   A user-defined record that describes the checker.
        This record's `type` and `subtype` fields can be used to categorize the checker's purpose.
        Other fields can be used in the messages displayed by the record's `events` component.
        To set the

        ```
        issueType
        ```

        you need to call `defineIssueType()`:
        See "The 'defineIssueType' Function".
