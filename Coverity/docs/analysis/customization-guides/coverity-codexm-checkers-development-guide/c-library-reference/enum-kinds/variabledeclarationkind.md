---
title: "variableDeclarationKind"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/variabledeclarationkind.html"
content_id: "g8ytRfVqW2e23MCjJSNzfw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:30:41.275224+00:00"
---

# variableDeclarationKind

Describes how a variable has been declared.

## Details

The following values are defined:

| Name | Description |
| --- | --- |
| `` `local` `` | The variable declaration is local to a function or a class. |
| `` `static` `` | The variable declaration is static and the variable is available globally. |
| `` `tryResource` `` | The variable is declared in a block that belongs to a `try` statement. |

## See also

propertyReference,
variableDeclaration,
variableReference
