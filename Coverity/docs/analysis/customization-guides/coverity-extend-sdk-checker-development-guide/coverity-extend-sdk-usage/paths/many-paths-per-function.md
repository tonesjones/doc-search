---
title: "Many paths per function"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/many-paths-per-function.html"
content_id: "1ZRJJpgyREtL2Sui4zC55w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:48.000122+00:00"
---

# Many paths per function

The Coverity Extend SDK engine does not simply traverse one path through a
function; instead it traverses many paths to achieve complete coverage of all relevant
sequences of operations.

The paths are not executed in sequence, one after another. Instead, common prefixes of
paths are analyzed once with the analysis branching at conditionals to investigate each
path separately.

What this means is that your checker's handler functions such as
ANALYZE_TREE are called for expression and statement trees in
different paths at different times; from the checker's point of view, the engine seems
to be jumping from path to path unpredictably. This is why using `cout`
is misleading.

The way to keep track of separate paths is by using the store. The Coverity Extend
SDK engine will always call a handler with the same store (contents) for the
same path. Thus, all knowledge about the current path should be saved to the store.

Since the events are also in the store, using ADD_EVENT is the best
way to produce coherent, path-dependent output.
