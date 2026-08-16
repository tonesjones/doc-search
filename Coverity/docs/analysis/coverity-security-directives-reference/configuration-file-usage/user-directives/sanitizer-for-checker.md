---
title: "sanitizer_for_checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sanitizer_for_checker.html"
content_id: "~zqBq2qs9wV83CNqqhp0HQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:01.114662+00:00"
---

# sanitizer_for_checker

**Languages: C#, Java, Visual Basic**

The `sanitizer_for_checker` directive clears the taintedness of data tracked by
a particular checker. (See section "Tainted data overview"
in Customizing Coverity.) This directive identifies a sanitizer
method that, when passed an argument containing tainted data, updates the data to be
considered non-tainted. That checker will no longer report defects for values that are
passed through the sanitizer method. Other checkers will not be affected. Common
applications include sanitizers, encoders, and escapers.

This directive is not supported for the checkers SENSITIVE_DATA_LEAK,
SQLI, and XSS.

For the XSS checker, you can use the xss_sanitizer_method directive to describe how characters are escaped,
rather than using `sanitizer_for_checker`.

## Fields

This directive uses the following fields:

`sanitizer_for_checker`
:   A JSON string that contains the name of the checker to which this
    directive applies.

`sanitizer`
:   A to_callsite
    WritableProgramData value that
    specifies the value that will replace the tainted argument.

## Examples

**Example (Java):**

```
{
  sanitizer_for_checker : "DF.MY_CUSTOM_DATAFLOW_CHECKER",
  sanitizer : {
    to_callsite : {
      callsite_with_static_target : {
        "named" : "examples.SanitizerForChecker.Clean(java.lang.String, boolean)java.lang.String"
      },
    },
    input : "arg1"
  }
}
```

**Source code for the example:**

```
package examples;

import javax.servlet.http.HttpServletRequest;

public class SanitizerForChecker
{
    // This is defined as a sink for a custom checker 
    // through an sink_for_checker directive (not shown).
    public native void SinkStuff(String data);

    // This is defined as a sanitizer for the same custom checker 
    // through the sanitizer_for_checker directive above.
    public String Clean(String data, boolean useUnderscore) {
        if (useUnderscore) {
            return data.replaceAll(" ", "_");
        } else {
            return data.replaceAll(" ", "");
        }
    }

    public void Demonstrate(HttpServletRequest req)
    {
        // Read an untrusted HTTP request parameter.
        // This is a built-in "HTTP" taint source.
        String x = req.getParameter("unsafe");

        // It is a defect to pass 'x' to the sink!
        SinkStuff(x);

        // It is safe to pass a sanitized 'x' after calling Clean.
        SinkStuff( Clean(x, true) );
    }
}
```
