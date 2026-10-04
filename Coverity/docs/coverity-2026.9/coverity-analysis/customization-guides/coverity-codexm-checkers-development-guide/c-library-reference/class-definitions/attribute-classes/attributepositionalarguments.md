---
title: "attributePositionalArguments"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/attributepositionalarguments.html"
content_id: "kFBDJu~sWjew0nvQjW9dpg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:24.024737+00:00"
---

# attributePositionalArguments

Describes the positional arguments in an attribute.

## Properties

`attributePositionalArguments` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `arguments` | `list<expression>` | The positional arguments to the attribute |
| `constructorFunction` | `functionSymbol` | The symbol of the constructor function that retrieves the positional arguments |

**Inherits properties from:**

- attributeArgument
