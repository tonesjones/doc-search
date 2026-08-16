---
title: "tainted_data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tainted_data.html"
content_id: "fEqjVn3St5qHvOQwzguS8A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:04.323216+00:00"
---

# tainted_data

**Languages: JavaScript**

The `tainted_data` directive identifies tainted data, which is data that
an attacker can influence to cause security vulnerabilities.

## Fields

This directive uses the following fields:

`tainted_data`
:   Specifies a ReadableProgramData value that
    indicates which data to consider tainted.

`taint_kind`
:   Specifies a TaintKind string that indicates the kind of
    taint with which `tainted_data` is tainted.

    The analysis considers any program data (global variable, function
    return value, and so on) that matches `tainted_data` to
    be tainted with a taint of kind `taint_kind`.

`is_deep_taint`
:   (Optional) A JSON Boolean value. When `is_deep_taint` is
    set to `true`, then properties of the
    `tainted_data` (array elements, properties of the
    properties, and so on) are considered to be similarly tainted.

    If this value is not specified, or if it is set to
    `false`, then properties of
    `tainted_data` are not themselves considered to be
    tainted.

## Examples

**Configuration example:**

The following is an example of using this directive for client-side JavaScript code.
This example marks global variable `myLibrary.queryParam` as tainted
with kind `js_client_url_query_or_fragment` (similar to the
JavaScript `window.location.query`).

```
{
    "taint_kind" : "js_client_url_query_or_fragment",
    "tainted_data" : {
        "read_path_off_global" : [
            { "property" : "myLibrary" },
            { "property" : "queryParam" }
        ]
    }
}
```

**JavaScript code example:**

The following client-side JavaScript code illustrates the effect of this
directive.

```
function tainted_data_client() {
    var t = myLibrary.queryParam;
    document.write(t);    // DOM_XSS

    var n = myLibrary.somethingElse;
    document.write(n); //no DOM_XSS
}
```

The local variable `t` is tainted because of the directive, but local
variable `n` is not. When `t` flows into the first
argument of a call to `document.write`, the analysis reports a
DOM_XSS defect (this checker reports cross-site scripting via the Document Object
Model).

The following is an example that uses this directive for server-side JavaScript code.
This directive says that the return value of
`require('myLib').getObjectFromRequestParam()` contains deeply
tainted data from HTTP request parameters; in other words, that it was entirely
constructed (or deserialized from) data in an HTTP request.

```
{
    "taint_kind" : "http",
    "is_deep_taint" : true,
    "tainted_data" : {
        "output" : "return",
        "from_callsite" : {
            "call_on" : {
                "read_from_js_require" : "myLib",
                "path" : [ { "property" : "getObjectFromRequestParam" } ]
            },
        }
    }
},
```

The following Node.js code illustrates the effect of this directive. In this example,
the local variable `o` is deeply tainted because of the directive.
The effect of the deep taint is that `o.s.cmd` is tainted, so its
flow into the argument of `exec` results in an OS_CMD_INJECTION
defect report.

```
function node() {
    var myLib = require("myLib");
    var o = myLib.getObjectFromRequestParam();
    // Because 'o' is deeply tainted, 'o.s.cmd' is tainted.
    // Hence, passing it to an API that executes it results in a
    // OS_CMD_INJECTION defect report.
    require("child_process").exec(o.s.cmd); // OS_CMD_INJECTION
}
```
