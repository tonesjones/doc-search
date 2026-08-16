---
title: "move_xss_outside_method"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/move_xss_outside_method.html"
content_id: "XupSriBE0lhnvK~jG3G1fQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:00.460705+00:00"
---

# move_xss_outside_method

**Languages: C#, Java, Visual Basic**

The `move_xss_outside_method` directive directs the analysis to report
cross-site scripting (XSS) defects outside the specified methods.

## Fields

This directive uses the following field:

`move_xss_outside_method`
:   A MethodSet value that identifies the
    methods that this directive will affect.

## Examples

**Configuration example:**

```
//"move_xss_outside_method" directive example

{
  "move_xss_outside_method" :
    { "named" :
        "examples.Test_move_xss_outside_method.addUrlPrefix(
                java.lang.String)java.lang.String"
    }
},
```

**Java code example:**

```
//"move_xss_outside_method" directive example

package examples;

class Test_move_xss_outside_method extends HttpServlet
{
  public String addUrlPrefix(String str) {
    return "http://" + str; //directive moves XSS out of this method. no defect 
  }

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();

    String taint1 = request.getParameter("taint1");
    pw.println( addUrlPrefix(taint1) ); //directive moves XSS report to here 

    String taint2 = request.getParameter("taint2");
    pw.println( addUrlPrefix(taint2) ); //directive moves XSS report to here 
  }
}
```
