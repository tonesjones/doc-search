---
title: "dataflow_checker_name"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dataflow_checker_name.html"
content_id: "PVasRPPQ9AnWb7Pm6ao_7g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:39.901724+00:00"
---

# dataflow_checker_name

**Languages: C#, Java, JavaScript, Visual Basic**

The `dataflow_checker_name` directive defines a DF.*CUSTOM_CHECKER*.

## Fields

The custom dataflow checker description uses the following fields:

`dataflow_checker_name`
:   Specifies a JSON string that names the custom checker. This name must
    begin with `DF.`. After that prefix, it must contain only
    capital letters or the underscore character ( `_` ). For
    example, `DF.MY_CHECKER` is allowable, but
    `DF.My_Checker` is not.

`taint_kinds`
:   Specifies a TaintKindGroup value that defines the kinds
    of taint that the checker tracks (subject to the global trust options;
    see TaintKind for details).

`sink_message`
:   Sets a JSON string to print as the event message where the tainted data
    flows into the sink. For defects in JavaScript code, this string appears
    in an event after several other events that describe the sink and the
    tainted data that flowed into it. For Java and C# checkers, you can use
    the following two placeholder values in this string:

    `{0}`
    :   This substring will be replaced by the name of the tainted
        expression that reached the sink.

    `{1}`
    :   This substring will be replaced by the name of the sink.

`remediation_advice`
:   Specifies a JSON string to print as remediation advice in each defect
    report.

`new_issue_type`
:   (Optional) Sets an IssueTypeDefinition value to
    describe the sorts of issues that this checker reports. The fields of
    this `IssueTypeDefinition` object are all optional in
    this context. Missing fields default to the following values:

    - `type`: `USER.` followed by the
      name of your checker
    - `name`: `Tainted data reached a
      sink.`
    - `description`: `User-controllable data
      reached a sink.`
    - `local_effect`: `Custom Dataflow
      Checker`
    - `impact`: `Medium`
    - `category`: `Medium impact
      security`
    - `quality_kind`: `false`
    - `security_kind`: `true`

    Note: The `new_issue_type` field replaces the deprecated
    `checker_properties` field. If
    `dataflow_checker_name` specifies neither
    `new_issue_type` nor
    `checker_properties`, then *all* the default
    values listed above are used.

## Deprecated fields—from prior to format version 8

As of Security Configuration format version 8, the fields described in this section are
deprecated and have been replaced with the `new_issue_type` field;
future Security Configuration format versions are not guaranteed to support them.
See Migrating the format from Version 8 to Version 12.

`local_effect`, `impact`, `category`, `cwe`
:   These fields are deprecated. See the documentation of the
    correspondingly named fields in IssueTypeDefinition.

`long_description`
:   This field is deprecated. See the documentation for the
    `description` field in IssueTypeDefinition.

`type`
:   This field is deprecated. See the documentation for the
    `name` field in IssueTypeDefinition. (Be aware:
    This deprecated `type` field is unrelated to the
    `type` field of
    `IssueTypeDefinition`.)

`kind`
:   This field is deprecated. See the documentation for the
    `quality_kind` and `security_kind`
    fields in IssueTypeDefinition
    and the discussion of migration in the following section. Valid values
    for this property are: `security` (for security issues),
    `quality` (for quality issues), or
    `both` (for security and quality issues).
