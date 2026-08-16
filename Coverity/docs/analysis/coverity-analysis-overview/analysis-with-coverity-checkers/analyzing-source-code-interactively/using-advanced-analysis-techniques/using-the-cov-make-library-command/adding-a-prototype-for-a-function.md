---
title: "Adding a prototype for a function"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-prototype-for-a-function.html"
content_id: "STqZPEqu71bARYkGP9pugw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:21.037913+00:00"
---

# Adding a prototype for a function

Suppressing macro expansion (see Suppressing macro expansion to improve modeling) might require an
additional step of adding a prototype for the function if a function of the same name is
not declared; otherwise, the function cannot be called in C++, and in C will cause
PW.IMPLICIT_FUNC_DECL warnings. The prototype can be placed in
user_nodefs.h so that only Coverity Analysis builds will see
the prototype instead of the macro.

To increase the accuracy of the analysis, you might want to create a model for a
prototype and register it with Coverity Analysis. For example, if you have a macro
assertion such as:

```
#nodef my_assert
    void my_assert(int x);
```

... then you can create a model in a separate source file, such as:

```
void my_assert(int x) {
    if (!x)
    __coverity_panic__();
}
```

... and use the `cov-make-library` command to build a model from this source.
For more information about models, see "Models and primitives" in Customizing Coverity.
