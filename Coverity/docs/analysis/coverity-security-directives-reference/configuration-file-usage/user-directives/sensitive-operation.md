---
title: "sensitive_operation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sensitive_operation.html"
content_id: "hiVlXNMiZkRianL4V3pUoQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:02.393025+00:00"
---

# sensitive_operation

**Languages: Java**

The `sensitive_operation` directive promotes a defect found by the
WEAK_GUARD checker to high impact in programs where a weak guard is used to control the
execution of a sensitive operation.

## Fields

This directive uses the following field:

`sensitive_operation`
:   Specifies a MethodSet value to identify those methods that
    should be treated as sensitive operations.

## Examples

**Configuration example:**

```
{
    "sensitive_operation" : { 
        "named" : examples.WeakGuard.secretOperation()void" 
    }
},
```

**Java code example:**

```
package examples;

public class WeakGuard {
    native void secretOperation();

    void test(HttpServletRequest request) throws IOException {
        String sourceIP = request.getRemoteAddr();
        if (sourceIP != null && sourceIP.equals("134.23.43.1")) {
               secretOperation();
        }
    }
}
```
