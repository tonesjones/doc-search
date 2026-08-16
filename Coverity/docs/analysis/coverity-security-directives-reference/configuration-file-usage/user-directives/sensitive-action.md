---
title: "sensitive_action"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sensitive_action.html"
content_id: "fCk1gXBWSKErqlobyoQXqA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:01.752415+00:00"
---

# sensitive_action

**Languages: JavaScript**

Use the `sensitive_action` directive to tell the MISSING_AUTHZ checker
which function calls perform a sensitive action that requires an authorization check.
The MISSING_AUTHZ checker reports a defect on code that performs a sensitive action that
isn’t protected by an authorization check.

## Fields

This directive uses a single field:

`sensitive_action`
:   Specifies a CallsiteSet that identifies
    calls to functions that perform sensitive operations that require
    authorization.

## Examples

**JavaScript example:**

```
{
    sensitive_action" : {
        "call_on" : {
            "read_path_off_global" : [ { "property" : "addUser" } ]
        }
    },
}
```

The `sensitive_action` directive above matches the
`addUser()` call site in the following Node.js JavaScript code.
If such a call is not guarded by an authorization check, MISSING_AUTHZ reports a
defect on it.

```
addUser("guest");
```

The `addAdminUser()` function is also considered a sensitive action
because it calls a function that performs a sensitive action. MISSING_AUTHZ reports
a defect on the call to `addAdminUser()` unless it is guarded by an
authorization check.

```
function addAdminUser() {
    addUser("admin");
}
// …
addAdminUser();
```
