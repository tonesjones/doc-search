---
title: "globalVariableDefinition"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/globalvariabledefinition.html"
content_id: "3zPCZ_Mbuya5oHGyKmxpyA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:32.485697+00:00"
---

# globalVariableDefinition

The class of a global variable definition.

| Name | Type | Description |
| --- | --- | --- |
| `variable` | `typeof(globalVariableSymbol).producedType;` | The symbol for the global variable whose definition this is. |
| `initializer` | `initializer?` | The initializer for the global variable; `null`, if none was specified. |
