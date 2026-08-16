---
title: "method_returns_param"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/method_returns_param.html"
content_id: "NxITklX8WmoNe_V1TEGGUg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:47.116103+00:00"
---

# method_returns_param

**Languages: C#, Java, Visual Basic**

The `method_returns_param` directive specifies a particular parameter for
a method to return.

This directive indicates methods where the analysis should follow dataflow paths as if
the method directly returned the specified parameter. This directive is useful when the
analysis fails to infer dataflow from a method parameter to its return value.

## Fields

This directive uses the following fields:

`method_returns_param`
:   Specifies a MethodSet value to identify the methods to
    which this directive applies.

`input`
:   A ParamIn value to be returned by the identified
    methods.

## Examples

**Configuration example:**

```
//"method_returns_param" directive example

{
  "method_returns_param" :
    { "named" :
        "examples.Test_method_returns_param.example1(java.lang.String)java.lang.String"
    },
  "input" : "arg1"
},

{
  "method_returns_param" :
    { "named" :
        "examples.Test_method_returns_param.example2(java.lang.String, 
          java.lang.String)java.lang.String"
    },
  "input" : "arg2"
},

{
  "ignore_method_dataflow" :
    { "named" :
        "examples.Test_method_returns_param.example2(java.lang.String, 
          java.lang.String)java.lang.String"
    }
},
```

**Java code example:**

```
//"method_returns_param" directive example

package examples;

class Test_method_returns_param extends HttpServlet
{
  HttpServletResponse resp;

  // The directive adds a dataflow path where this method returns 'str'.
  public String example1(String str) {
    PrintWriter pw = resp.getWriter();
    pw.println(str); //XSS reported here is unaffected by the directive
    return "";
  }

  // The "ignore_method_dataflow" directive ignores the original dataflow and
  // the "method_returns_param" directive adds back a dataflow edge where the
  // method returns 'str2'. Together these directives replace the inferred
  // dataflow with something entirely new.
  public String example2(String str1, String str2) {
    PrintWriter pw = resp.getWriter();
    pw.println(str1); // no XSS due to ignore_method_dataflow 
    return str1; // ignore_method_dataflow squelches this dataflow path
  }

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();
    String taint = request.getParameter("taint");

    // XSS: method returns 'taint' due to 'method_returns_param' directive
    pw.println( example1(taint) ); 

    // no XSS: first argument no longer returned due to 'ignore_method_dataflow'
    pw.println( example2(taint, "") );
    // XSS: second argument returned due to 'method_returns_param' directive
    pw.println( example2("", taint) ); 
  }
}
```
