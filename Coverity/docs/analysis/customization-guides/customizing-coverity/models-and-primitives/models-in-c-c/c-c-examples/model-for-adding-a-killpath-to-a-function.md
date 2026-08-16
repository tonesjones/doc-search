---
title: "Model for adding a killpath to a function"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/model-for-adding-a-killpath-to-a-function.html"
content_id: "qIDLwKlLgtyan6dJhDjWvw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:34.450811+00:00"
---

# Model for adding a killpath to a function

If Coverity Analysis generates many false positives after you
analyze your code, there might be missing *killpath* function models. A killpath
function is a function that terminates execution.

Missing killpath functions cause false positives when Coverity Analysis
uses an `assert()` to infer that a condition is possible, but the
`assert()` actually says it is impossible. For example:

```
int test1(int *p) {
    assert(p != NULL);
    return *p;
}
```

If killpath functions are modeled correctly, Coverity Analysis sees this
assertion:

```
    assert(p != NULL)
```

... and realizes that `p` must be non-`NULL` to continue
execution. However, if a killpath is missing, when Coverity Analysis
analyzes `test1()` it will treat it the same as the following code:

```
int test1(int *p) {
    if (p != NULL) {}
    return *p;
}
```

Coverity Analysis assumes that the killpath is missing if the program
does not use the standard library `assert()` function, but instead uses
an `assert()` function that a developer wrote and that does not actually
abort execution (or is coded in such a way that Coverity Analysis does
not see that it aborts). In either case, Coverity Analysis concludes
that `p` can be `NULL` (otherwise why test it with the
`if` statement?), and it reports the subsequent dereference as a
`FORWARD_NULL`. Missing killpaths lead to false positives when Coverity Analysis treats an asserted condition as plausibly being
false.

Most functions that abort execution, such as `exit()` and
`kabort()`, are modeled using the library mechanism described earlier
and by the modeling primitive `__coverity_panic__()`. The file
<install_dir>/library/generic/common/killpath.c lists
those types of functions that are currently modeled in the system. In general, the best
way to add more functions with killpaths is to enhance the library by writing stubs that
call the either the primitive or one of the existing library functions.

Alternatively, you can use function
annotations to specify that all paths through a function are killpaths.
