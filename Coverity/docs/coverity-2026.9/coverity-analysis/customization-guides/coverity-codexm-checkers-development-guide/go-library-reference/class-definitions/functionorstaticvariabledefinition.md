---
title: "functionOrStaticVariableDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/functionorstaticvariabledefinition.html"
content_id: "zOb9M3XbLmEUZJVVfdsabA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:32.444567+00:00"
---

# functionOrStaticVariableDefinition

Describes a function or a statically declared variable.

## Properties

`functionOrStaticVariableDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `allCode` | `set<astnode>` | A list of all the nodes within the function. For a variable, this is usually just the variable's initialization. |
| `location` | `sourceloc` | The function's location in the code. This value is used in error reports. |
| `paths` | `executionPaths` | The execution paths used for path-sensitive analysis. |
