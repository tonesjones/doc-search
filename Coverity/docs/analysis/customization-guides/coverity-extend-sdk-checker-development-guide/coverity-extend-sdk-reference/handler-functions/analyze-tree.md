---
title: "ANALYZE_TREE"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyze_tree.html"
content_id: "le8f7ddGJBqkiaTk4AiEFw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:12.530122+00:00"
---

# ANALYZE_TREE

**Synopsis**

```
ANALYZE_TREE() { <code> }
```

**Description**

This is one of two central checker functions (
`ANALYZE_CONDITION`
 is the other). It is called for each statement and expression, as described in
Visit order.

**Options**

Within the body of `ANALYZE_TREE`, you can use several macros to inspect
the AST fragment that is undergoing analysis:

- `CURRENT_TREE`— The AST node that is undergoing analysis. It
  has type `tree`.
- `MATCH(pat)`— Matches `CURRENT_TREE` against
  pattern `pat`, returning true if it matches. See Patterns.
- `MATCH_TREE(pat,t)`— Matches `t` against
  pattern `pat`.
