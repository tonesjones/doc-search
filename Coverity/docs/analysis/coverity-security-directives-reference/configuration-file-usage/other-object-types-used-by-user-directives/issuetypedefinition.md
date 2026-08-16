---
title: "IssueTypeDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/issuetypedefinition.html"
content_id: "K1uYgxiKJruwQoOlzWa6cg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:22.575669+00:00"
---

# IssueTypeDefinition

**Used by these directives:**
`dataflow_checker_name`, `dc_checker_name`,
`text_checker_name`

An `IssueTypeDefinition` value describes the sort of issues that a checker
reports. Coverity Platform and other issue-display interfaces use the fields of this
object to describe issues the checker reports, and to support sorting and filtering of
issues from this checker.

## Fields

This object uses the following fields:

`type`
:   A JSON string to be used as an opaque ID within the security directives
    file. It is not meant to be visible in the user interface.

    The `type` string must contain between one and sixty-four
    ASCII characters, each of which must be a letter, number, underscore, or
    period. In other words, the string must match the following regular
    expression `^[A-Za-z0-9_.]{1,64}$`.

    Note: The user of a prefix (such as `USER.*`) is highly
    recommended for all user-defined types. This ensures
    forward-compatibility with any new built-in issue types introduced in
    future versions of the Coverity Analysis tool.

`name`
:   A JSON string that briefly describes the kind of issue that this checker
    reports; for example, `SQL Injection`.

`description`
:   A JSON string that provides a longer description of the issue; for
    example, `Unsafe use of tainted data in constructing an SQL
    query`.

`local_effect`
:   A JSON string that explains what effect this issue might have on the
    execution of the code in which it is reported; for example `An
    attacker might be able to execute arbitrary SQL queries of their
    choice.`.

`cwe`
:   (Optional) A JSON integer value that indicates which entry in the Common
    Weakness Enumeration (CWE) best describes this issue.

`impact`
:   One of the following JSON string values: `High`,
    `Medium`, `Low`, or
    `Audit`.

`category`
:   A JSON string that describes the general class of issue that this defect
    belongs to; for example, `Injection Vulnerability` or
    `API Misuse`.

`quality_kind`
:   (Optional) A JSON Boolean value.

    If `quality_kind` is `true`, issues from
    this checker will have a `kind` that equals
    `quality`, and that appears accordingly when
    filtering issues in the user interface. You can set either, both, or
    neither of `quality_kind` and
    `security_kind` to be `true`.

`security_kind`
:   If `security_kind` is `true`, issues from
    this checker will have a `kind` that equals
    `security`, and that appears accordingly when
    filtering issues in the user interface. You can set either, both, or
    neither of `quality_kind` and
    `security_kind` to be `true`.

## Examples

```
   "new_issue_type" : {
     "type" : "leftover_debug_code",
     "name" : "Deployed test servlet",
     "description"  : "A possible test servlet will be deployed.",
     "local_effect" : "Leftover debug or test code is not intended to be deployed with the application in a production environment, and it may expose unintended functionality or bypass security features.",
 
      "cwe" : 489,
      "impact"   : "Medium",
      "category" : "Medium impact security",
      "security_kind" : true,
    }
```
