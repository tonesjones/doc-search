---
title: "globalOrNonlocalDeclarationStatement"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/globalornonlocaldeclarationstatement.html"
content_id: "3dKJ71RyzTUh3L4csFDl0w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:12.300668+00:00"
---

# globalOrNonlocalDeclarationStatement

Matches `global` and Python 3 `nonlocal` declarations.

Coverity Analysis recognizes global and nonlocal declarations but it does not consider them to be statements.
Because of this, `globalOrNonlocalDeclarationStatement` matches both
`global C;` and `nonlocal D;`,
but it does not provide any way to distinguish between the two declarations.

This pattern only matches nodes of type `statement`.

## Properties

`globalOrNonlocalDeclarationStatement` does not expose any new properties.

**Inherits properties from:**

- astnode
- statement
