---
title: "method_with_servlet_sinks_on_input"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/method_with_servlet_sinks_on_input.html"
content_id: "NpRDF_n49FbYnwW66ze9dw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:59.169666+00:00"
---

# method_with_servlet_sinks_on_input

**Languages: C#, Java, Visual Basic**

The `method_with_servlet_sinks_on_input` directive indicates that a
method’s argument is written to the HTTP output. The XSS (cross-site scripting) checker
reports a defect if tainted data is written to the HTTP output without proper
escaping.

## Fields

This directive uses the following fields:

`method_with_servlet_sinks_on_input`
:   Specifies a MethodSet that identifies the
    methods to which this directive will be applied.

`input_param_sinks`
:   Specifies a JSON array. Each object in this array describes an argument
    that the method writes to the HTTP output, and how that argument is
    escaped.

    Objects in the `input_param_sinks` array use the following
    fields:

    `input`
    :   A ParamIn value that names the
        argument that this object describes.

    `escaper`
    :   Either a MethodCallSpecifier value *or* a JSON `null` literal.

        If this escaper field is the `null` literal,
        or if it evaluates to `null`, then the
        `input` is written to the HTTP output
        as-is and without any escaping. Otherwise, the field
        indicates a method: The method’s `input` is
        where input is passed in, and the method’s
        `output` is written to the servlet output
        stream.

    `servlet_context`
    :   Specifies an HtmlOutputContext
        value.

        This field indicates the HTML context (that is, the place in
        the HTML parse tree) into which the argument flows. To avoid
        cross-site scripting (XSS), different contexts imply
        different escaping obligations.

## Examples

**Configuration example 1:**

```
//"method_with_servlet_sinks_on_input" directive example 1

// This example also demonstrates using the "html_prefix" HtmlOutputContext
// value to control the context.

{
  "method_with_servlet_sinks_on_input" :
    { "named" :
        "examples.Test_method_with_servlet_sinks_on_input1.pcdata_sink(java.lang.String)void"
    },
  "input_param_sinks" : [
    {
      "input" : "arg1",
      "escaper" : null,
      "servlet_context" : { "html_prefix" : "" }
    }
  ]
},

{
  "method_with_servlet_sinks_on_input" :
    { "named" :
        "examples.Test_method_with_servlet_sinks_on_input1
                .single_quoted_attribute_value_sink(java.lang.String)void"
    },
  "input_param_sinks" : [
    {
      "input" : "arg1",
      "escaper" : null,
      "servlet_context" : { "html_prefix" : "<tag foo='" }
    }
  ]
},
```

**Java code example 1:**

```
//"method_with_servlet_sinks_on_input" directive example 1

// This example also demonstrates using the "html_prefix" HtmlOutputContext
// value to control the context.

package examples;

class Test_method_with_servlet_sinks_on_input1 extends HttpServlet
{
  public void pcdata_sink(String val) {}

  public void single_quoted_attribute_value_sink(String val) {}

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();

    String taint = request.getParameter("taint");

    // The directive makes the analysis treat the argument to this function as
    // being written to servlet output in the HTML PCDATA context, so we get an
    // XSS defect here.
    pcdata_sink(taint); 

    // The directive makes the analysis treat the argument to this function as
    // being written to servlet output in the single-quoted HTML tag value
    // context, so we get an XSS defect here.
    single_quoted_attribute_value_sink(taint); 
  }
}
```

**Configuration example 2:**

```
//"method_with_servlet_sinks_on_input" directive example 2

// This also demonstrates using the "html_attribute_value_where_name_is_from_param" 
// HtmlOutputContext value to control the context.

{
  "method_with_servlet_sinks_on_input" :
    { "named" :
        "examples.Test_method_input_servlet_sinks2.sink(java.lang.String, java.lang.String)void"
    },
  "input_param_sinks" : [
    {
      "input" : "arg2",
      "escaper" : null,
      "servlet_context" : {
        "html_attribute_value_where_name_is_from_param" : "arg1",
        "value_quoting" : "single"
      }
    }
  ]
},
```

**Java code example 2:**

```
//"method_with_servlet_sinks_on_input" directive example 2

// This example also demonstrates using the
// "html_attribute_value_where_name_is_from_param" HtmlOutputContext value to
// control the context.

package examples;

class Test_method_input_servlet_sinks2 extends HttpServlet
{
  String unknownName;

  public void sink(String name, String val) {}

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();

    String taint = request.getParameter("taint");

    // The directive makes the analysis treat 'taint' a being written to the
    // servlet output as the single-quoted value to a 'color' attribute, for
    // example:
    // "<font color='" + taint + ...
    // Thus the directive causes an XSS report here.
    sink("color", taint); 

    // Similar to the above, but here it's an "onclick" single-quoted JavaScript
    // attribute value. Again the directive causes an XSS report here.
    sink("onclick", taint); 

    // Here we have something other than a String literal for the attribute
    // name, so the analysis treats it as the 'color' case above (including
    // reporting an XSS defect) and logs a warning.
    sink(unknownName, taint); 
  }
}
```

**Configuration example 3:**

```
//"method_with_servlet_sinks_on_input" directive example 3

// This example also demonstrates using a "lookup_by_constant_param"
// MethodCallSpecifier value to indicate that a boolean parameter controls an
// optional escaper.

{
  "define_lookup_method_call_map" : "escape_if_bool_is_true",
  "map" : {
    "true" : {
      "method_call" :
        "Escapers.escape_html(java.lang.String)java.lang.String",
      "input" : "arg1", "output" : "return"
    },
    "false" : null
  }
},

{
  "method_with_servlet_sinks_on_input" :
    { "named" :
        "examples.Test_method_input_servlet_sinks3.sink(java.lang.String, boolean)void"
    },
  "input_param_sinks" : [
    {
      "input" : "arg1",
      "escaper" : {
        "lookup_by_constant_param" : "arg2",
        "lookup_map" : "escape_if_bool_is_true"
      },
      "servlet_context" : { "html_prefix" : "" }
    }
  ]
},
```

**Java code example 3:**

```
//"method_with_servlet_sinks_on_input" directive example 3

// This also demonstrates using a "lookup_by_constant_param" MethodCallSpecifier
// value to indicate that a boolean parameter controls an optional escaper.

// NOTE: This example should include the Escapers.java code (for the
// 'escape_html' method call added by the directive).

package examples;

class Test_method_input_servlet_sinks3 extends HttpServlet
{
  boolean unknownBool;

  public void sink(String val, boolean escape) {}

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();

    String taint = request.getParameter("taint");

    // The directive makes the analysis (1) treat the first argument to 'sink'
    // ('taint') as if it is written to HTML PCDATA context; and also (2) if the
    // second argument to 'sink' is 'true', the analysis assumes the first
    // argument has been passed through 'escape_html' first.

    // No XSS because the 'escape_html' makes 'taint' safe for HTML PCDATA.
    sink(taint, true); 

    // XSS report because 'false' implies no escaping of 'taint'
    sink(taint, false); 

    // Since the second argument is not a boolean literal ('true' or 'false'),
    // the analysis does not know if the first argument is escaped. It logs a
    // warning, but does not report a defect.
    sink(taint, unknownBool);
  }
}
```

**Configuration example 4:**

```
//"method_with_servlet_sinks_on_input" directive example 4

// This example also demonstrates using a "lookup_by_constant_param"
// MethodCallSpecifier value to indicate that an enum parameter controls an
// optional escaper.

{
  "define_lookup_method_call_map" : "escape_if_Choice_is_YES",
  "map" : {
    "examples.Choice.YES" : {
      "method_call" :
        "Escapers.escape_html(java.lang.String)java.lang.String",
      "input" : "arg1", "output" : "return"
    },
    "examples.Choice.NO" : null,
    "null" : null
  }
},

{
  "method_with_servlet_sinks_on_input" :
    { "named" :
        "examples.Test_method_input_servlet_sinks4.sink(java.lang.String, examples.Choice)void"
    },
  "input_param_sinks" : [
    {
      "input" : "arg1",
      "escaper" : {
        "lookup_by_constant_param" : "arg2",
        "lookup_map" : "escape_if_Choice_is_YES"
      },
      "servlet_context" : { "html_prefix" : "" }
    }
  ]
},
```

**Java code example 4:**

```
//"method_with_servlet_sinks_on_input" directive example 4

// This example also demonstrates using a "lookup_by_constant_param"
// MethodCallSpecifier value to indicate that an enum parameter controls an
// optional escaper.

// NOTE: This example should include the Escapers.java code (for the
// 'escape_html' method call added by the directive).

package examples;

enum Choice { YES, NO }

class Test_method_input_servlet_sinks4 extends HttpServlet
{
  Choice unknownChoice;

  public void sink(String val, Choice escape) {}

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();

    String taint = request.getParameter("taint");

    // Similar to the example above, the directive causes the analysis to behave
    // as if 'taint' flows to a HTML PCDATA context after being escaped with
    // 'escape_html' and so the analysis does not report a defect here.
    sink(taint, Choice.YES); 

    // According to the directive, a Choice.NO argument indicates no escaping,
    // so the analysis reports an XSS defect report here.
    sink(taint, Choice.NO); 

    // The directive also indicates that the null Choice argument means no
    // escaping, so the analysis reports an XSS defect here too.
    sink(taint, null); // XSS sink from directive + no escaper 

    // The Choice controlling escaping is not an expected literal, so the
    // analysis logs a warning but does not report a defect.
    sink(taint, unknownChoice);
  }
}
```

## See also

define_lookup_method_call_map,
MethodCallSpecifier for
`define_lookup_method_call_map`
