---
title: "Model for sources of untrusted (tainted) data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/model-for-sources-of-untrusted-tainted-data.html"
content_id: "6KL7PEcpnyaNMs8_XKgYwA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:57.985829+00:00"
---

# Model for sources of untrusted (tainted) data

If the analysis fails to report security defects, there are several possible causes
and workarounds.

This situation primarily involves the checkers SQLI, XSS, and OS_CMD_INJECTION.

False negatives can occur when the analysis does not recognize a source of tainted data.
If a method in your program returns tainted data, but the analysis does not discover
that issue, you need to write a model for that method. Similarly, if a method takes a
`StringBuffer` (or similar object) and appends tainted data to it,
you can model that behavior, as well.

For example, the following model informs the analysis that the
`MyClass.returnsTainted` method returns tainted data and that the
`MyClass.appendsTainted` method taints its argument (presumably by
inserting a tainted string into it).

```
public class MyClass {
    // The return value of returnsTainted() is tainted.
    String returnsTainted() {
        return com.coverity.primitives.SecurityPrimitives.asserted_source();
    }
    
    // A call to appendsTainted taints its argument.
    void appendsTainted(StringBuffer sb) {
        com.coverity.primitives.SecurityPrimitives.asserted_source(sb);
    }
}
```

**See also:**
The '@Tainted' and '@NotTainted' attributes for Java code.

To generate models for Web application security checkers only, see Generating Java Web application security models.
