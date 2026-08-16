---
title: "dc_checker_name"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dc_checker_name.html"
content_id: "1Y4q9_qEx1bIA7bn39Eg1A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:41.214628+00:00"
---

# dc_checker_name

**Languages: C, C++, C#, Java, Objective-C, Objective-C++**

The `dc_checker_name` directive defines a DC.*CUSTOM_CHECKER*.

Note: As of version 2020.03, if you need to migrate from the legacy checker SECURE_CODING,
we recommend that you use CodeXM instead of creating a new DC.*CUSTOM_CHECKER*. We
also recommend that you migrate custom DC checkers to CodeXM code. See
"Migrate DC
custom checkers to CodeXM" in the Coverity 2026.6.0 Checker Reference.

## Fields

In a configuration file, two directives manage custom DC checkers:

`dc_checker_name`
:   Defines a new DC checker and specifies the checker name; for example,
    `dc_checker_name : DC.CUSTOM_MY_CHECKER`.

`method_set_for_dc_checker`
:   Adds methods to a DC custom checker. Use this directive when you define a
    new DC checker, or to add methods to an existing DC checker. For a
    description, see method_set_for_dc_checker.

Two other fields can be present:

`new_issue_type`
:   (Optional) Specifies an IssueTypeDefinition value that
    describes the sort of issues that this checker reports.

    In the context of `new_issue_type`, all of these fields
    are optional. If a field is not present, its value defaults to the value
    shown in the following list:

    - `"type"`: `"USER."` followed by
      your custom checker name
    - `"name"`: `"Calling risky
      function."`
    - `"description"`: `"The called function is
      unsafe for security related code."`
    - `"local_effect"`: `"May result in a
      security violation."`
    - `"impact"`: `"Low"`
    - `"category"`: `"Security best practices
      violations"`
    - `"quality_kind"`:
      `"false"`
    - `"security_kind"`:
      `"true"`
    - `"cwe"`: `"676"`

    Note: The `new_issue_type` field replaces the deprecated
    fields `category`, `cwe`,
    `impact`, `kind`,
    `local_effect`, `long_description`,
    and `type`. If both the `new_issue_type`
    field and the subfield it replaces are absent, all of the default values
    listed above are used.

`antecedent_checker`
:   A string that names the custom DC checker (or SECURE_CODING checker) on
    which the present checker is based.

    Rather than use this field, unless you need to maintain legacy code we
    recommend that you use CodeXM to write new Don’t Call checkers. See
    "Migrate DC
    custom checkers to CodeXM" in the Coverity 2026.6.0 Checker Reference.

    The `antecedent_checker` field preserved existing triage
    results for the specified DC.*CUSTOM_NAME* checker in Coverity
    Connect. There were two use cases for this property:

    - When migrating from SECURE_CODING to a DC.*CUSTOM_**
      checker, you would specify
      `SECURE_CODING`.
    - When renaming a DC.*CUSTOM_** checker, you would specify the
      old name of the checker.

## Deprecated fields—from prior to format version 8

As of Security Configuration format version 8, the fields described in this section are
deprecated and have been replaced with the `new_issue_type` field;
future Security Configuration format versions are not guaranteed to support them.
See Migrating the format from Version 8 to Version 12.

`local_effect`, `impact`, `category`, `cwe`
:   These fields are deprecated. See the documentation of the correspondingly
    named fields in IssueTypeDefinition.

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
