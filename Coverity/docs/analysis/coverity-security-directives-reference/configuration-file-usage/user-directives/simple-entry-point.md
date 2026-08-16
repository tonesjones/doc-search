---
title: "simple_entry_point"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/simple_entry_point.html"
content_id: "OQiLmU6oTPKMl6Bg94eAWA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:03.042402+00:00"
---

# simple_entry_point

**Languages: C#, Java, Visual Basic**

The `simple_entry_point` directive identifies methods that are entry
points for a Web application. By default all parameters of the methods will be deeply
tainted (meaning that the object, its fields, and the fields that belong to those fields
are treated as though they are tainted) with the specified taint types. You can override
this behavior with the optional `tainted_args` field. The level of depth
of fields that are tainted is affected by the `cov-analyze` option
`--webapp-security-aggressiveness-level`.

## Fields

This directive uses the following fields:

`simple_entry_point`
:   Specifies a MethodSet to identify the
    methods that are entry points to the Web app.

`taint_kinds`
:   A JSON array of TaintKind values that
    identify the kinds of taint to report.

`tainted_args`
:   (Optional) Specifies an array of ParamIn
    values that identify which arguments passed to the entry point should be
    considered tainted. If `tainted_args` is not present,
    *all* arguments passed to the entry point are considered to be
    tainted.

`treat_as_xss_entry_point`
:   (Optional) A JSON Boolean value.

    If this value is set to `true`, any output to the HTTP
    response of this method will be rendered as HTML, and the XSS checker
    will report defects if untrusted strings are not escaped correctly.

    If this value is not specified, or if it is set to
    `false`, output to the method’s HTTP response is not
    handled by the XSS checker.

## Examples

**Configuration example:**

```
//"simple_entry_point" directive example

{
  "simple_entry_point" : {
    "named" : "examples.Test_simple_entry_point.entry(java.lang.String, examples.UserBean)void"
  },
  "taint_kinds" : [ "http", "network" ]
},
```

**Java code example:**

```
//"simple_entry_point" directive example

package examples;
import java.sql.Connection;
import java.sql.Statement;

class InnerInnerBean
{
  private String innerInnerData;

  public String getInnerInnerData()           { return innerInnerData; }
  public void   setInnerInnerData(String arg) { innerInnerData = arg;  }
}

class InnerBean
{
  private String         innerData;
  private InnerInnerBean innerInnerBean;

  public String getInnerData()           { return innerData; }
  public void   setInnerData(String arg) { innerData = arg;  }
  public InnerInnerBean getInnerInnerBean()              { return innerInnerBean; }
  public void      setInnerInnerBean(InnerInnerBean arg) { innerInnerBean = arg;  }
}

class UserBean
{
  private String    data;
  private InnerBean innerBean;

  public String getData()           { return data; }
  public void   setData(String arg) { data = arg;  }
  public InnerBean getInnerBean()              { return innerBean; }
  public void      setInnerBean(InnerBean arg) { innerBean = arg;  }
}

public class Test_simple_entry_point
{
  Connection connection;
  Statement  statement;
  
  public void entry(String simpleString, UserBean customData)
    throws Exception
  {
    // The string 'simpleString' is considered to be tainted with
    // "http" and "network" taint. SQLI cares about both so it
    // reports a defect when we see the taint (aliased to sqlQuery1)
    // flow into connection.prepareStatement.
    String sqlQuery1 = 
      "select * from " + simpleString;
    statement = connection.prepareStatement(sqlQuery1); //SQLI
    
    // This example demonstrates that we consider fields of classes
    // as tainted in addition to simple objects like "simpleString".
    String sqlQuery2 =
      "select * from " + customData.getData();
    statement = connection.prepareStatement(sqlQuery2); //SQLI
    
    // This example demonstrates that, at default aggressiveness levels,
    // we do not consider InnerInnerBean's fields as tainted.
    String sqlQuery3 =
      "select * from " +
      customData.getInnerBean().getInnerInnerBean().getInnerInnerData();
    statement = connection.prepareStatement(sqlQuery3); //no SQLI
  }
}
```
