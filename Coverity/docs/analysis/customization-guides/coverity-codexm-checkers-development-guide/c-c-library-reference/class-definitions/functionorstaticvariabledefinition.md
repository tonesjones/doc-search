---
title: "functionOrStaticVariableDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/functionorstaticvariabledefinition.html"
content_id: "QSXl2_OAKGhd4L0X3b3Ugg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:28:32.986470+00:00"
---

# functionOrStaticVariableDefinition

Describes a function or statically declared variable.

## Properties

`functionOrStaticVariableDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `allCode` | `set<astnode>` | All the nodes within a function. For a variable, this is usually just its initialization. |
| `location` | `sourceloc` | The location in the source code. This is used for defect reporting. |
| `paths` | `executionPaths` | The execution paths used for path-sensitive analysis |
