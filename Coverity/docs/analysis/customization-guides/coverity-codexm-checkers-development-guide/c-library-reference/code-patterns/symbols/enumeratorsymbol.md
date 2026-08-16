---
title: "enumeratorSymbol"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enumeratorsymbol.html"
content_id: "Qx3utCBGPLKfPRXODiz9rw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:32:26.132259+00:00"
---

# enumeratorSymbol

Matches the symbols in an `enum`.

This pattern only matches nodes of type `symbol`.

## Properties

`enumeratorSymbol` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `isExplicit` | `bool` | Whether this `enum` is explicit |
| `ownerEnumType` | `type` | The owner `enum` type |
| `value` | `int` | The integer value of the symbol |

**Inherits properties from:**

- symbol
