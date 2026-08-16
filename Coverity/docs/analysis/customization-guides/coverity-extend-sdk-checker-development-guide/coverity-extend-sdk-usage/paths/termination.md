---
title: "Termination"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/termination.html"
content_id: "9Ou_11aE6_Wg0VEt7JrLPQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:49.975301+00:00"
---

# Termination

Any function that has a loop will have an infinite number of apparent paths. Even with
FPP enabled, there might still be no bound on the number of paths. For example, consider
the following loop:

```
void foo(int n)
  {
    for (int i=0; i<n; i++) {
      // ...
    }
  }
```

**How does the Coverity Extend SDK engine avoid running forever checking an example
like this?**

The Coverity Extend SDK engine notices that the second and subsequent paths
through the loop are not significantly different from the first iteration, and stops
analyzing the loop. This condition is called a fixpoint of the loop.

The concept of *significantly different* is difficult to describe, and is not
necessary to understand fully to write a checker. You must be aware that the contents of
the store is the key determiner of whether something is considered different by the
Coverity Extend SDK; engine. As a first approximation: exploration of the
loop terminates if and only if two different iterations produce the same store. Although
the actual rule for this behavior is more complex, this abstraction is generally
accurate.

What this means for a checker writer is that you must not try to track values too
precisely, otherwise you risk putting the Coverity Extend SDK engine into an
infinite loop. You must choose abstractions that are precise enough to check the
property of interest, but sufficiently *imprecise* to allow termination.

A simple example of the imprecise concept is integers. If you track integer values
exactly, then you have an infinite abstract domain and hence the analysis does not
terminate. But by abstracting this down to just three values (negative, zero, and
positive), you can ensure termination.

If you track values of arbitrarily complex expressions, then there is no guarantee of reaching
a fixpoint in a loop, so the abstract interpretation could go on forever. As another
example, when tracking values in the heap, you should avoid tracking information about
arbitrarily deep nested pointer dereference expressions. For example, tracking
`p->field` is usually fine, but tracking
`p->field1->field2->field3` is not, since the latter has
enough precision to take considerable (infinite) time exploring all of its variations.
