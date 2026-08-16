---
title: "ignore_all_argument_dataflow_to_method"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ignore_all_argument_dataflow_to_method.html"
content_id: "u7iWlfGMDc5eu4cNrkWl_g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:42.504797+00:00"
---

# ignore_all_argument_dataflow_to_method

**Languages: C#, Java, Visual Basic**

The `ignore_all_argument_dataflow_to_method` directive applies to call
sites that match a specified MethodSet value.

The dataflow analysis ignores paths from the call site arguments to parameters of the
called method. The analysis also ignores any changes the method call appears to make to
modifiable arguments.

Effectively, the dataflow analysis act as if the call site does not exist for the
arguments, but the analysis is still capable of reporting paths within the called
method.

## Fields

This directive uses the following field:

`ignore_all_argument_dataflow_to_method`
:   Specifies a MethodSet value that identifies
    the methods whose argument dataflow will be ignored.

## Examples

**Configuration example:**

```
//"ignore_all_argument_dataflow_to_method" directive example

{
  "ignore_all_argument_dataflow_to_method" :
    { "named" :
        "examples.Test_ignore_all_argument_dataflow_to_method.appendAndPrintString(
         java.lang.StringBuffer, java.lang.String, 
         javax.servlet.http.HttpServletResponse)void"
    }
},
```

**Java code example:**

```
//"ignore_all_argument_dataflow_to_method" directive example

package examples;

class Test_ignore_all_argument_dataflow_to_method extends HttpServlet
{
  public void appendAndPrintString(StringBuffer sb,
  String str,
  HttpServletResponse resp)
  {
    sb.append(str);
    PrintWriter pw = resp.getWriter();
    //no XSS because the directive suppresses taint flow from callers into 'str'
    pw.println(str);
  }

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();

    String taint = request.getParameter("taint");

    StringBuffer sb = new StringBuffer();
    appendAndPrintString(sb, taint, resp);

    //no XSS due to the directive
    pw.println(sb.toString()); 
  }
}
```
