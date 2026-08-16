---
title: "method_returns_tainted_data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/method_returns_tainted_data.html"
content_id: "TcD_OKBt6reAZBYEAUMqXA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:48.414441+00:00"
---

# method_returns_tainted_data

**Languages: C#, Java, Visual Basic**

The `method_returns_tainted_data` directive identifies methods that return
tainted data. The returned data should extend or implement a built-in taintable type,
such as a string, byte array, input stream, or collection. It cannot be used to indicate
that members of a user-defined class instance are tainted. The current trust model and
trust options control whether the type of taint should be distrusted.

## Fields

This directive uses the following fields:

`method_returns_tainted_data`
:   Specifies a MethodSet value that identifies the methods to
    which this directive applies.

`taint_kind`
:   A TaintKind string value to be returned by the
    identified methods.

## Examples

Configuration example:

```
// "method_returns_tainted_data" example
{
    "method_returns_tainted_data" : {
        "matching": "examples\\.Test_method_returns_tainted_data\\.returns_tainted_data\\(.*"
     },
    "taint_kind" : "http"
}
```

Java code example:

```
package examples;
import java.sql.Statement;
import java.sql.Connection;

public class Test_method_returns_tainted_data {

  Connection connection;
  Statement  statement;

  String returns_tainted_data() {
    return "foo";
  }

  void test_SQLI() throws Exception {
    String val = returns_tainted_data();

    // The method call to returns_tainted_data is considered to return
    // tainted data of "http" type.

    String sqlQuery1 = "select * from " + val;

    // An SQLI defect is reported on the following line
        statement = connection.prepareStatement(sqlQuery1);
  }
}
```
