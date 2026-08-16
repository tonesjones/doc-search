---
title: "ignore_method_output"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ignore_method_output.html"
content_id: "Y0l0XKTimrkLJxCZxxv8Sg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:43.829250+00:00"
---

# ignore_method_output

**Languages: C#, Java, Visual Basic**

The `ignore_method_output` directive indicates methods where the analysis
should ignore dataflow paths passing out of the method through the return value or a
particular modified parameter, as specified by the `output` field.

This directive rarely needs to be used, but it can be useful in cases where the analysis
infers incorrect data flow through a method. This directive *does not* suppress
defect reports within the methods it indicates, only those that rely on flow through the
indicated method *outputs*.

## Fields

This directive uses the following fields:

`ignore_method_output`
:   Specifies a MethodSet value that identifies the methods whose output will
    be ignored.

`output`
:   A ParamOut value that specifies the value to ignore.

## Examples

**Configuration example:**

```
//"ignore_method_output" directive example

{
  "ignore_method_output" :
    { "named" :
        "examples.Test_ignore_method_output.getTaint(javax.servlet.http.HttpServletRequest, 
          javax.servlet.http.HttpServletResponse)java.lang.String"
    },
  "output" : "return"
 },
```

**Java code example:**

```
//"ignore_method_output" directive example

package examples;

class Test_ignore_method_output extends HttpServlet
{
  boolean beSafe;

  // The directive suppresses dataflow through the return value of this method.
  public String getTaint(HttpServletRequest request, HttpServletResponse resp)
  {
    PrintWriter pw = resp.getWriter();
    String taint = request.getParameter("taint");
    pw.println(taint); //XSS reported here unaffected by the directive

    if (beSafe) return "";

    return taint; // the directive squelches this tainted dataflow
  }

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();
    String x = getTaint(request, resp); // untainted because of the directive
    pw.println(x); //no XSS due to directive 
  }
}
```
