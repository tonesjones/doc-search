---
title: "new_on"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/new_on.html"
content_id: "uAUALsfpTU_ZPIjEwPdqxw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:12.205990+00:00"
---

# new_on

**Languages: JavaScript**

A `new_on CallsiteSet` matches constructor calls that use the
`new` operator where the constructor expression matches a specified
ReadableProgramData value.

## Fields

`new_on`
:   Specifies a ReadableProgramData
    value that the constructor expression must match to be included in this
    `CallsiteSet`

`when`
:   (Optional) If present, specifies a CallsiteCondition that a call site
    must satisfy to be included in this `CallsiteSet`.

## Using a CallsiteSet

Follow these guidelines for best results:

- When using a `new_on CallsiteSet`, only the
  `return`
  `ParamOut` value is allowed for `ParamOut`
  fields related to the call site (for example, on a `from_callsite
  ReadableProgramData` value).
- If non-`return`
  `ParamOut` values such as `arg1` are needed,
  use the `call_on` version of `CallsiteSet` to
  match the constructor call.
- Use `call_on` for `new` call sites, unless the
  directive should match only `new` call sites.

## Examples

Node.js JavaScript example:

```
{
    "from_callsite" : {
        "new_on" : {
            "read_from_js_require" : "myLib",
            "path" : [ { "property" : "myCtor" } ]
        }
    },
    "output" : "return"
}
```

The `CallsiteSet` above inside `from_callsite` matches
the `new myLib.myCtor()` call site in this Node.js JavaScript
code:

```
var myLib = require("myLib");
var myObject = new myLib.myCtor(myParam)
```

The `ParamOut`
`output` field above is restricted and can only be set to
`return` (See ParamOut). In this
example, the result of `new myLib.myCtor(...)` is matched, but the
result of a direct call to `myLib.myCtor` is not matched.
