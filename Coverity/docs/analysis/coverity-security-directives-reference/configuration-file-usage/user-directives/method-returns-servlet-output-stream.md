---
title: "method_returns_servlet_output_stream"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/method_returns_servlet_output_stream.html"
content_id: "zKaMprI4nMT2wyiM~KLA8w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:47.760327+00:00"
---

# method_returns_servlet_output_stream

**Languages: C#, Java, Visual Basic**

The `method_returns_servlet_output_stream` directive indicates that a
method returns a stream that writes data to the HTTP output. The XSS checker (for
cross-site scripting) reports a defect if tainted data is written to the stream without
proper escaping.

In Java, the returned object type should extend the `java.io.OutputStream`
or `java.io.Writer` classes. In C#, the returned object type should
extend the `System.IO.Stream` or `System.IO.TextWriter`
classes.

## Fields

This directive uses the following field:

`method_returns_servlet_output_stream`
:   Specifies a MethodSet value that identifies the methods to which this
    directive applies.

## Examples

**Configuration example:**

```
//"method_returns_servlet_output_stream" directive example

{
  "method_returns_servlet_output_stream" :
    { "named" :
        "examples.Test_method_returns_servlet_output_stream.getServletWriter()
         java.io.PrintWriter"
    }
},
```

**Java code example:**

```
//"method_returns_servlet_output_stream" directive example

package examples;

class Test_method_returns_servlet_output_stream extends HttpServlet
{
  PrintWriter pwField;
  PrintWriter getServletWriter() { return pwField; }
  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = getServletWriter();
    String taint = request.getParameter("taint");
    pw.println(taint); //XSS defect due to directive
  }
}
```
