---
title: "class_like_print_writer_for_servlet_output"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/class_like_print_writer_for_servlet_output.html"
content_id: "WZE5LjuEkZwT8fo2afYqOA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:37.046477+00:00"
---

# class_like_print_writer_for_servlet_output

**Languages: C#, Java, Visual Basic**

The `class_like_print_writer_for_servlet_output` directive indicates
classes with `print()`, `println()`, and
`write()` methods that function like `PrintWriter`
methods of the same name, and that should always be treated as if they were writing to a
servlet output stream. The XSS checker reports a defect on tainted data that flows to a
servlet output stream without proper escaping.

## Fields

This directive uses the following field:

`class_like_print_writer_for_servlet_output`
:   Specifies a ClassSet value.

## Examples

**Configuration example:**

```
//"class_like_print_writer_for_servlet_output" directive example

{
  "class_like_print_writer_for_servlet_output" :
    { "named" : "examples.LikeServletPrintWriter" }
},
```

**Java code example:**

```
//"class_like_print_writer_for_servlet_output" directive example

package examples;

interface LikeServletPrintWriter
{
  public void print(String s);
  public void println(String x);
  public void write(String s);
}

class Test_class_like_print_writer_for_servlet_output extends HttpServlet
{
  LikeServletPrintWriter writer;
  Locale l;
  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    // XSS reported on 'print' 'println' and 'write' due to the directive
    // treating these calls like writing to servlet output.
    writer.print(request.getParameter("taint")); 
    writer.println(request.getParameter("taint")); 
    writer.write(request.getParameter("taint"));
  }
}
```
