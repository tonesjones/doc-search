---
title: "incDecStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/incdecstatement.html"
content_id: "e_gdkhIRvnc7n3Opn_nwjw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:33:14.784654+00:00"
---

# incDecStatement

Matches IncDec statements: That is, statements that use either the
incrementOperator, `++`, or the
decrementOperator, `--`.

This pattern only matches nodes of type `statement`.

## Properties

`incDecStatement` produces a record that contains the following property:

| Name | Type | Description |
| --- | --- | --- |
| `expression` | `expression` | The expression; for example, a function call, an assignment, or (frequently) a *post* clause in a simple `for` loop. |

**Inherits properties from:**

- astnode
- statement
