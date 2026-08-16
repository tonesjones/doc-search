---
title: "csrf_validator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/csrf_validator.html"
content_id: "2aVFUyJa6hvxLBAkP5txRA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:38.572425+00:00"
---

# csrf_validator

**Languages: JavaScript**

Use the `csrf_validator` directive to tell the CSRF checker which function
calls protect Web application entry points from CSRF attacks; for example, by comparing
a CSRF token in a user’s session with the one submitted in the request. The CSRF checker
does not report defects on a Web application entry point that calls one of these
functions.

## Fields

This directive uses the following field:

`csrf_validator`
:   Sets a CallsiteSet value that identifies
    call sites to which this directive applies.

## Examples

**JavaScript example:**

```
{
    "csrf_validator" : {
        "call_on" : {
            "read_path_off_global" : [ { "property" : "myCsrfValidator" } ]
        }
    }
}
```

The `csrf_validator` directive above matches the
`myCsrfValidator()` call site in this Node.js JavaScript code.
Normally, a CSRF defect would be reported at both Web application entry points
`app.get("/a", function)` and `app.get("/b",
function)` because they both call
`db.createCollection("my_collection")`, which updates the
database. However, since `app.get("/b", function)` calls
`myCsrfValidator()`, no CSRF defect is reported for this Web
application entry point.

```
var MongoClient = require("mongodb").MongoClient;
  
var express = require("express");
var app = express();
  
var url = "mongodb://localhost:27017/myDatabase";
  
app.get("/a", function(req, res) {
    MongoClient.connect(url, function(err, db) {
        console.log("Creating new database collection");
        db.createCollection("my_collection");
        res.send("Visiting /a");
     });
});
  
app.get("/b", function(req, res) {
    MongoClient.connect(url, function(err, db) {
        console.log("Creating new database collection");
        myCsrfValidator();
        db.createCollection("my_collection");
        res.send("Visiting /b");
    });
});
  
app.listen(3000, function() {
    console.log("Listening");
});
```

## See also

csrf_check_needed.
