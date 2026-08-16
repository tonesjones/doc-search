---
title: "Models for templates (C++)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/models-for-templates-c-.html"
content_id: "NhqYTBZNuXoPN~XQqFDH7w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:39.065538+00:00"
---

# Models for templates (C++)

You can write models for templates: This includes template functions and member
functions for template classes.

To model a template, write it as a nontemplate within a namespace called
`__coverity_template__`. The model must have the same number of
parameters as the template, but the types do not need to be the same: in particular
because it would be impossible to reference the template parameter in these types. As a
result, it is only possible to model a single template function overload for a given
number of parameters.

For example, to model the following template, where the call to `*alloc()`
returns allocated memory:

```
template <typename T> class MyClass {
    T *alloc();    // returns allocated memory
};
```

... you would need to write something like the following code:

```
namespace __coverity_template__ {
    class MyClass {
        void *alloc() { return __coverity_alloc_nosize__(); }
    };
}
```

It is also possible to write models for specific instantiations (overloaded or not) by
instantiating a template *within* a model file; in the example, this is the
instance of `MyClass<int>`:

```
template <typename T> class MyClass {
    T *alloc() { return 0; }
};

// Explicitly instantiate for "int"
template class MyClass<int>;
```
