---
title: "method_returns_constant"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/method_returns_constant.html"
content_id: "YdQr4vLqS~uwn7aX7Gjicw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:46.474394+00:00"
---

# method_returns_constant

**Languages: C#, Java, Visual Basic**

The `method_returns_constant` directive specifies a constant for a method
to return.

In a program where dataflow follows an unwanted conditional path (for example, because
you are certain the path is impossible in a production environment), the unwanted path
can be avoided by modelling a method evaluated in the conditional expression as
returning a constant value.

## Fields

This directive uses the following fields:

`method_returns_constant`
:   Specifies a MethodSet value to identify the methods to
    which this directive applies.

`returns`
:   A ReturnConstant value to be returned by the identified
    methods.

## Examples

**Configuration example:**

```
//"method_returns_constant" directive example

{
  "method_returns_constant" :
    { "named" :
        "examples.Test_method_returns_constant.check_for_error()boolean"
    },
  "returns" : { "bool" : false }
},
```

**Java code example:**

```
//"method_returns_constant" directive example

package examples;

class Test_method_returns_constant extends HttpServlet
{
  boolean hasError;
  boolean check_for_error() { return hasError; }
  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();
    String taint = request.getParameter("taint");

    if (check_for_error()) {
      pw.println(taint); //no XSS due to directive 
    }
  }
}
```
