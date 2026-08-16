---
title: "OutputAndAccessPathSpecifier"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/outputandaccesspathspecifier.html"
content_id: "yWvqtSskke5DyG8EaQ0G8Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:30.373974+00:00"
---

# OutputAndAccessPathSpecifier

**Used by these directives:**
`dataflow_through_call_site`

## Fields

An `OutputAndAccessPathSpecifier` uses the following fields:

`output`
:   A ParamOut value to specify a base value that is output from
    the call site. If a `path` field is not present, this is
    the output value itself.

`path`
:   (Optional) A non-empty array of AccessPathElement
    values. When this field is present, the `output` value is
    found on this access path, using the base value.

In an `OutputAndAccessPathSpecifier` values, if the `path` field
is not specified, then `return` is the only allowed ParamOut value for the `output` field.

## Examples

Directive for JavaScript example:

```
{
    dataflow_through_callsite: {
        "call_on" : {
            "read_off_any" : [ {"property" : "returnsArgDotX"} ]
        },
    },
    from: [ {input: "arg1", path: [ {property: "x"} ] } ],
    to: [ { output: "return" } ]
}
```

The directive above indicates that a call to `returnsArgDotX()`
returns the `x` property of its argument. The following client-side
JavaScript code shows how this directive can result in a DOM_XSS defect report (this
checker reports cross-site scripting via the Document Object Model).

The directive indicates that the call to `returnsArgDotX(o)` returns
`o.x`. Since `o.x` contains tainted data and the
return value of the function flows into the argument of
`document.write()` (a DOM_XSS sink), the analysis reports a
DOM_XSS defect.

```
var o = { x: location.hash, y: "safe" };
document.write(returnsArgDotX(o)); // DOM_XSS
```
