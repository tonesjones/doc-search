---
title: "functionOrStaticVariableDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionorstaticvariabledefinition.html"
content_id: "tvqYL53fTH3OGesnYj9VdQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:15.197737+00:00"
---

# functionOrStaticVariableDefinition

Describes a function or a statically declared variable.

## Properties

`functionOrStaticVariableDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `allCode` | `set<astnode>` | All nodes within a function. For a variable this is usually just the initialization. |
| `location` | `sourceloc` | The location in the code, used for defect reporting |
| `paths` | `executionPaths` | The execution paths used for path-sensitive analysis |
