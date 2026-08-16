---
title: "async_method"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/async_method.html"
content_id: "LE9_NAZ6bXNUdmRl9Scwnw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:36.395928+00:00"
---

# async_method

**Languages: JavaScript**

The `async_method` directive identifies callback functions such as event
handlers, Web application entry points, or other callbacks that some framework or
runtime system calls asynchronously. It also provides details about the arguments with
which the function is called. This directive is similar to the local_callback directive, but it is for callbacks that
are called asynchronously instead of immediately.

## Fields

This directive uses the following fields:

`async_method`
:   Specifies a WritableProgramData value to identify
    the callback function that is called later.

`handler_kind`
:   Specifies a JSON string to describe the kind of callback being called.
    This field can have one of the following values:

    `event_listener`
    :   The callback might be called many times, as part of an event
        loop.

    `async_method`
    :   The callback is called once; for example, after an
        asynchronous operation completes.

    `webapp_entry_point`
    :   The callback might be called many times, in response to
        requests from a client.

`input_tags`
:   (Optional) Specifies a non-empty JSON array of InputTag
    values. These values indicate that particular parameters to the callback
    have particular tags.

`input_taints`
:   (Optional) Specifies a non-empty JSON array of InputTaint
    values. These values indicate that particular parameters to the callback
    are tainted.

`input_values`
:   (Optional) Specifies a non-empty JSON array of InputValue
    values. If this field is present, `async_method` must be
    a to_callsite
    WritableProgramData value. The
    InputValue elements describe how
    arguments at the call site that registers the callback (that is, the
    call site specified in the to_callsite
    sub-element of `async_method`) flow to parameters of the
    callback.

## Examples

**JavaScript example 1:**

The following directive indicates that any function assigned to the
`onkeydown` property of any object is an event listener (and thus
potentially invoked many times in the event loop). For example, the anonymous
function in `element.onkeydown = function () { flag = true; }` would
be registered as an event handler.

```
{
    "async_method": {
        "write_off_any": [ { "property": "onkeydown" } ]
    },
    "handler_kind" : "event_listener"
}
```

**JavaScript example 2:**

The following is a simplified version of an `webapp_entry_point
async_method` directive for Express.js.

Directive:

```
{
    "tag" : "ExpressApp",
    "data_has_tag" : {
        "from_callsite" : {
            "call_on" : {
                "read_from_js_require" : "express"
            }
        },
        "output" : "return"
    }
},
{
    "async_method" : {
        "to_callsite" : {
            "call_on" : {
                "read_from_object_with_tag" : "ExpressApp",
                "path" : [ { "property" : "post" } ]
            }
        },
        "input" : "arg2"
    },
    "input_tags" : [
        {
            "input" : "arg1",
            "tag" : "ExpressRequest"
        },
        {
            "input" : "arg2",
            "tag" : "ExpressResponse"
        }
    ],
    "handler_kind" : "webapp_entry_point"
}
```

The first directive says that `app` in the code below has the tag
`ExpressApp`. The `async_method` directive uses
this tag to recognize the anonymous function in the code below as a Web application
entry point and to tag its parameters with `ExpressRequest` (for
`req`) and `ExpressResponse` (for
`res`). Other directives might build on these tags to define
sources or sinks.

```
var app = require("express")();
app.post("/path1", function (req, res) {
   // ...
}
```

**JavaScript example 3:**

Directive:

```
{
    "async_method" : {
        "to_callsite" : {
            "call_on" : {
                "read_path_off_global" : [ { "property" : "dbQuery" } ]
            }
        },
        "input" : "arg3"
    },
    "handler_kind" : "async_method",
    "input_taints" : [ {
        "input" : "arg2",
        "taint_kind" : "database",
        "is_deep_taint" : true
    } ]
}
```

This directive indicates that the global function `dbQuery` registers its third
argument as a callback and that the second parameter of that callback is deeply
tainted with a `database` taint. For example, in the code below, the
anonymous function is the callback, and `data` is deep tainted with
database data. That is, `data.firstName`,
`data.address.city`, and so on are tainted with database
data.

```
dbQuery(connectionString, "SELECT * FROM user", function (result, data) {
  // ... data.firstName ... data.address.city
});
```
