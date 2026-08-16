---
title: "SymbolPattern Superclass"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/symbolpattern-superclass.html"
content_id: "1EH9D5tgwqOOuFHx0xWYUw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:21.326800+00:00"
---

# SymbolPattern Superclass

SymbolPattern matches symbols. Like the TypePattern
class, SymbolPattern cannot be used directly in a
MATCH or MATCH_TREE. Instead , use
SymbolPattern as a parameter to other patterns. The most common
SymbolPattern is NamedSymbol, which can be
used to match a specific function or variable.
