---
title: "local_callback"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/local_callback.html"
content_id: "6ti_ByhvNK0Sb~W0M6GiSA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:44.483991+00:00"
---

# local_callback

**Languages: JavaScript**

The `local_callback` directive identifies a callback function that is
called immediately (usually by some API) and provides details about the arguments with
which the function is called. This directive is similar to the async_method directive, but it deals with
callbacks that are called immediately, as opposed to asynchronously.

## Fields

This directive uses the following fields:

`local_callback`
:   Specifies a to_callsite
    WritableProgramData value that identifies the callback
    function that is called immediately.

`input_tags`
:   (Optional) Specifies a non-empty JSON array of InputTag
    values that identify callback functions to indicate that particular
    parameters to the callback function have particular tags.

`input_taints`
:   (Optional) Specifies a non-empty JSON array of InputValue values that describe how arguments
    at the call site that registers the callback (that is, the call site specified by
    `local_callback`) flow to parameters of the callback.

## Examples

**JavaScript Example:**

The following directive indicates that passing a function as the first argument of
`doCallWithArg()` invokes it immediately and passes the second
argument of `doCallWithArg()` to its first argument.

```
{
    "local_callback" : {
        "to_callsite" : {
            "call_on" : {
                "read_path_off_global" :  [{ "property" : "doCallWithArg" }],
            }
        },
        "input" : "arg1",
    },
    "input_values" : [
        {
            "value" : "arg2",
            "input" : "arg1"
        }
    ]
}
```

For example, because of the directive, the analysis sees the call to
`doCallWithArg(callback, x)` as making the following function
call: `callback(x)`.

```
function callback(arg) {
    // arg === x
}
doCallWithArg(callback, x);
```
