---
title: "Model for methods to which tainted data must not flow (sinks)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/model-for-methods-to-which-tainted-data-must-not-flow-sinks-.html"
content_id: "mI43cTVSx6VundT7IOKUNg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:58.660032+00:00"
---

# Model for methods to which tainted data must not flow (sinks)

False negatives can occur when the analysis does not recognize sinks, which are
method parameters to which tainted data must not flow—due to the risk of an attacker
subverting the database, taking control of a new operating system process, or otherwise
compromising your application.

For example, if the SQLI checker does not recognize a method parameter in your program as
one that is executed as an SQL, HQL, or JPQL query, you can model it as such, and you
can create similar models for OS_CMD_INJECTION.

The following sample model makes the SQLI checker report a defect if tainted data flows
into the `query` parameter of the `MyClass.executeSql()`
method, and it makes the OS_CMD_INJECTION checker report a defect if tainted data flows
into the `commandLine` parameter of the
`MyClass.execute()` method.

```
public class MyClass {

    void executeSql(
        String query,
        boolean somethingElse,
        String unrelated
    ) {
        com.coverity.primitives.SecurityPrimitives.sql_sink(query);    
    }

    void execute(String commandLine) { 
        com.coverity.primitives.SecurityPrimitives.os_cmd_one_string_sink(
            commandLine
        ); 
    }

}
```

The following command line shows one way to generate the new model file:

```
> cov-make-library --output-file user_models --disable-default --webapp-security MyClass.java
```
