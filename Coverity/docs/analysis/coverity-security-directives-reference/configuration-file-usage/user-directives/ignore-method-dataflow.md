---
title: "ignore_method_dataflow"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ignore_method_dataflow.html"
content_id: "BdbHjnyeE_ukrD0aqc8wfw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:43.160392+00:00"
---

# ignore_method_dataflow

**Languages: C#, Java, Visual Basic**

The `ignore_method_dataflow` directive indicates methods where the analysis
should ignore all dataflow paths within the method. Dataflow paths added by the method_returns_param directive are not ignored.

## Fields

This directive uses the following field:

`ignore_method_dataflow`
:   Specifies a MethodSet value that identifies the methods whose dataflow
    will be ignored.

## Examples

**Configuration example 1:**

```
//"ignore_method_dataflow" directive example 1

{
  "ignore_method_dataflow" :
    { "named" :
        "examples.Test_ignore_method_dataflow1.getTaint(
                javax.servlet.http.HttpServletRequest, 
                javax.servlet.http.HttpServletResponse)java.lang.String"
    }
},
```

**Java code example 1:**

```
//"ignore_method_dataflow" directive example 1

package examples;

class Test_ignore_method_dataflow1 extends HttpServlet
{
  boolean beSafe;

  // The directive suppresses all dataflow through this function.
  public String getTaint(HttpServletRequest request, HttpServletResponse resp)
  {
    if (beSafe) return "";

    PrintWriter pw = resp.getWriter();
    String taint = request.getParameter("taint");
    pw.println(taint); //no XSS due to directive 

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

**Configuration example 2:**

```
 //"ignore_method_dataflow" directive example 2

{
  "ignore_method_dataflow" :
    { "named" :
        "examples.Test_ignore_method_dataflow2.manyPaths(java.lang.String, 
          java.lang.StringBuffer)java.lang.String"
    }
},
```

**Java code example 2:**

```
//"ignore_method_dataflow" directive example 2

package examples;

class Test_ignore_method_dataflow2 extends HttpServlet
{
  String field1;
  String field2;

  public void setField2(String str) {
    field2 = str;
  }

  // This method demonstrates several kinds of dataflow paths that the directive
  // suppresses.
  public String manyPaths(String str, StringBuffer sb) {
    field1 = str;
    setField2(str);
    sb.append(str);
    return str;
  }

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();
    String taint = request.getParameter("taint");
    StringBuffer sb = new StringBuffer();

    // the directive suppresses all dataflow through manyPaths
    String ret = manyPaths(taint, sb);

    pw.println(ret); //no XSS due to directive 
    pw.println(sb); //no XSS due to directive 
    pw.println(field1); //no XSS due to directive 
    pw.println(field2); //no XSS due to directive 
  }
}
```
