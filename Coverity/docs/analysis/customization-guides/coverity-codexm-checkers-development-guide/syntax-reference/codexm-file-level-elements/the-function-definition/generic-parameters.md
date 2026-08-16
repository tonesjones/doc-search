---
title: "Generic parameters"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generic-parameters.html"
content_id: "J_HAbbREBr1G~Qn3NV5DqQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:16.531611+00:00"
---

# Generic parameters

By specifying generic parameters, as mentioned above, you are defining a parameter type (or return type)
that can change according to the context in which the function is evaluated.

For example, consider the following declaration:

[image: CXM code follows]

```
function genericDemo<T> ( l : list<T> ) : bool ->
    // Function body here
;
```

... here `T` is the `type-parameter-identifier`. At run time, `T`
might be passed as an `int`, a `string`,
a `bool`, or any other type.
