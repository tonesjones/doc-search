---
title: "csrf_check_needed"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/csrf_check_needed.html"
content_id: "8BPeKpnXl0dm2zgPUCf5Kw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:37.922831+00:00"
---

# csrf_check_needed

**Languages: JavaScript**

Use the `csrf_check_needed` directive to tell the CSRF checker which
function calls require CSRF protection. The CSRF checker will report a defect on any web
application entry point that calls such functions without CSRF protection.

## Fields

This directive uses the following fields:

`csrf_check_needed`
:   Specifies a CallsiteSet that identifies
    call sites to which this directive applies.

`update_type`
:   Sets a string value that specifies the type of update made to the server.
    Valid values include `database` and
    `filesystem`.

## Examples

**JavaScript example:**

```
{
    csrf_check_needed" : {
        "call_on" : {
            "read_path_off_global" : [ { "property" : "deleteDatabase" } ]
        }
    },
    "update_type" : "database"
}
```

The `csrf_check_needed` directive above matches the
`deleteDatabase()` call site in this Node.js JavaScript code.
This will result in a CSRF defect being reported at the web application entry point
`app.get("/", function)` which calls
`deleteDatabase()`.

```
var express = require("express");
var app = express();
  
app.get("/", function(req, res) {
    deleteDatabase();
});
  
app.listen(3000, function() {
    console.log("Listening");
});
```

## See also

csrf_validator
