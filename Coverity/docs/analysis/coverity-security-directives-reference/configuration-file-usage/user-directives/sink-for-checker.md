---
title: "sink_for_checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sink_for_checker.html"
content_id: "d7DWCt~IQi4HPnNSv~5Qfw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:03.682386+00:00"
---

# sink_for_checker

**Languages: C#, Java, JavaScript, Visual Basic**

The `sink_for_checker` directive identifies a sink for a checker.

## Fields

This directive uses the following fields:

`sink_for_checker`
:   A JSON string that contains the name of the checker. This checker can be
    one of the following checker types:

    - A user-defined checker, created with the dataflow_checker_name
      directive.
    - (JavaScript only) Any built-in tainted dataflow checker.

    The checker indicated in `sink_for_checker` reports a
    defect when data that has a taint kind the checker cares about (and does
    not trust) is routed to the sink indicated by the `sink`
    field. The "DF.*CUSTOM_CHECKER"* section
    in the Coverity 2026.6.0 Checker Reference explains in more detail how
    trust/distrust settings affect when a dataflow checker reports a
    defect.

`sink`
:   A WritableProgramData value that
    describes the sink; for example, by identifying a particular argument to
    a particular function.

    The analysis supports different kinds of
    `WritableProgramData` values for
    `sink`, depending on the programming language to
    which this directive applies.

    - For Java, Visual Basic, and C#, `sink` must be a
      to_callsite
      `WritableProgramData` object.
    - For JavaScript, `sink` can be any of the following
      kinds of `WritableProgramData` objects:

      - to_callsite
      - write_to_object_with_tag
      - write_path_off_global
      - write_off_any

`sink_kind`
:   This field is only supported by the JavaScript SENSITIVE_DATA_LEAK
    checker.

    Specifies a SinkKind string, which
    specifies the type of `sink`.

## Examples

**Java directive example:**

```
{
  sink_for_checker : "DF.MY_CUSTOM_DATAFLOW_CHECKER",
  sink : {
    to_callsite : {
      callsite_with_static_target : {
        "named" : "examples.SinkForChecker.SinkStuff(java.lang.String)void"
      },
    },
    input : "arg1"
  }
}
```

**Java source code example:**

```
package examples;

public class SinkForChecker
{
    // This could be defined in source, defined in bytecode, or
    // somewhere else. The part we care about is the "call" to
    // this method.
    public void SinkStuff(String data) {
        // Sinks the data.
    }

    // This method illustrates a call to SinkStuff. The directive
    // matches the call to SinkStuff. The directive is told that
    // "arg" (arg1) of SinkStuff is what is sinking.
    public void SomeOtherMethod()
    {
        SinkStuff("arg");
    }
}
```

**Client-side JavaScript example:**

The following directive adds a sink to the DOM_XSS checker (which checks for
cross-site scripting via the Document Object Model). Writing tainted data to the
global variable location results in a defect report.

```
{
    "sink_for_checker" : "DOM_XSS",
    "sink" : {
        "write_path_off_global" : [ { "property" : "location" } ]
    }
}
```
