---
title: "classDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/classdefinition.html"
content_id: "EHzJ3GSrqcErDwCVU2_DeQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:32.320012+00:00"
---

# classDefinition

Describes a Go `struct` or `interface`.

## Properties

`classDefinition` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `declaredType` | `classType` | The type of the class. |
| `fieldList` | `list<fieldSymbol>` | A list of fieldSymbols, one for each non-static field in the class |
| `location` | `sourceloc` | The location of this class in the source code |
| `memberFunctionList` | `list<functionSymbol>` | A list of functionSymbols, one for each non-static member function |
