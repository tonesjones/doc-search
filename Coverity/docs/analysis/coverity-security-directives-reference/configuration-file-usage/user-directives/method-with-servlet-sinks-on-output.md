---
title: "method_with_servlet_sinks_on_output"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/method_with_servlet_sinks_on_output.html"
content_id: "N4npdHU9daljhljOa7TOYA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:59.816539+00:00"
---

# method_with_servlet_sinks_on_output

**Languages: C#, Java, Visual Basic**

The `method_with_servlet_sinks_on_output` directive indicates that one of
the outputs of a method (its return value or the final state of one of its mutable
parameters) is written to the HTTP output. The XSS (cross-site scripting) checker
reports a defect if tainted data is written to the HTTP output without proper
escaping.

## Fields

This directive uses the following fields:

`method_with_servlet_sinks_on_output`
:   Specifies a MethodSet that identifies the
    methods to which this directive will be applied.

`output_param_sinks`
:   Specifies a JSON array. Each object in this array indicates that one of
    the outputs of this method (either its return value, or the final state
    of one of its mutable parameters) flows to the HTTP output.

    Objects in the `output_param_sinks` array use the
    following fields:

    `output`
    :   Specifies a ParamOut value that
        names the output of the method that this object
        describes.

    `servlet_context`
    :   An HtmlOutputContext
        value that indicates the HTML context (that is, the place in
        the HTML parse tree) into which the `output`
        flows. Different contexts imply different escaping
        obligations to avoid cross-site scripting (XSS).

        CAUTION:

        The `servlet_context` is an
        `HtmlOutputContext` value but its type
        *must not* be html_attribute_value_where_name_is_from_param.

## Examples

**Configuration example:**

```
// "method_with_servlet_sinks_on_output" directive example

// This example also demonstrates using the "html_prefix" HtmlOutputContext
// value to control the context.

{
  "method_with_servlet_sinks_on_output" :
    { "named" :
        "examples.Test_method_with_servlet_sinks_on_output.appendString_PCDATAsink(
                java.lang.StringBuffer,
                java.lang.String)void"
    },
  "output_param_sinks" : [
    {
      "output" : "arg1",
      "servlet_context" : { "html_prefix" : "" }
    }
  ]
},

{
  "method_with_servlet_sinks_on_output" :
    { "named" :
        "examples.Test_method_with_servlet_sinks_on_output.appendString_AttrValSink(
                java.lang.StringBuffer,
                java.lang.String)void"
    },
  "output_param_sinks" : [
    {
      "output" : "arg1",
      "servlet_context" : { "html_prefix" : "<tag attr='" }
    }
  ]
},
```

**Java code example:**

```
//"method_with_servlet_sinks_on_output" directive example

// This example also demonstrates using the "html_prefix" HtmlOutputContext
// value to control the context.

package examples;

class Test_method_with_servlet_sinks_on_output extends HttpServlet
{
  public void appendString_PCDATAsink(StringBuffer sb, String str) {
    // The directive makes the analysis treat appending to 'sb' as writing to
    // servlet output in the HTML PCDATA context, so we get an XSS defect here.
    sb.append(str); 
  }

  public void appendString_AttrValSink(StringBuffer sb, String str) {
    // The directive makes the analysis treat appending to 'sb' as writing to
    // servlet output in the single-quoted HTML tag value context, so we get an
    // XSS defect here.
    sb.append(str); 
  }

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();

    String taint = request.getParameter("taint");

    appendString_PCDATAsink(new StringBuffer(), taint);
    appendString_AttrValSink(new StringBuffer(), taint);
  }
}
```
