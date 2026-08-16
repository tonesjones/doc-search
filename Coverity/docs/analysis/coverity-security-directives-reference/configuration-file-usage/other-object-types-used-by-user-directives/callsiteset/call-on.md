---
title: "call_on"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/call_on.html"
content_id: "jK9yhWE_T4YJz~ZiislzlA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:11.557869+00:00"
---

# call_on

**Languages: JavaScript**

A `call_on CallsiteSet` matches call sites where the function value itself
(not the result of the call, but the expression being called) matches a specified ReadableProgramData value.

## Fields

`call_on`
:   Specifies a `ReadableProgramData` value that the function
    value at a call site must match, in order to be included in this
    `CallsiteSet`.

`when`
:   (Optional) If present, specifies a CallsiteCondition that a call site
    must satisfy to be included in this `CallsiteSet`.

## Examples

**JavaScript example:**

```
{
    "call_on" : {
        "read_off_any" : [ {"property" : "addEventListener"} ]
    },
    "when" : {
        "only_if_arg_index" : 1,
        "iequals_string" : "click"
    }
}
```

The `CallsiteSet` above matches the JavaScript call site this call
site:

```
anything.addEventListener("CLICK", x);
```

However, it does not match the following call sites because they do not satisfy the
CallsiteCondition.

```
anything.addEventListener("CLACK", x);
anything.addEventListener();
```

`call_on` will also match call sites using `new` with a
construction function. Consider the following Node.js JavaScript example:

```
{
    "from_callsite" : {
        "call_on" : {
            "read_from_js_require" : "myLib",
            "path" : [ { "property" : "myCtor" } ]
        }
    },
    "output" : "arg1"
}
```

The `CallsiteSet` above inside `from_callsite` matches
the `new myLib.myCtor` call site in this Node.js JavaScript code:

```
var myLib = require("myLib");
var myObject = new myLib.myCtor(myParam)
```

The example also shows that `ParamOut` values such as
`arg1` can be used when using the `call_on` field
to match a constructor call (this differs from using the `new_on
CallsiteSet`, which only allows the `return`
`ParamOut` value).
