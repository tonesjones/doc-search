---
title: "method_set_for_dc_checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/method_set_for_dc_checker.html"
content_id: "u1BvwnT8b2cocT3qY3sMbA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:58.443256+00:00"
---

# method_set_for_dc_checker

**Languages: C, C++, C#, Java, Objective-C, Objective-C++**

The `method_set_for_dc_checker` directive adds a method to a dc_checker_name.
You can use this directive to specify the method
initially tested by the new DC custom checker. You can also use it to add methods to an
existing DC.*CUSTOM_CHECKER*.

Note: We recommend that you use CodeXM to develop custom "don't call" checkers (which in
releases before 2020.03 had to be implemented using DC.*CUSTOM_CHECKER*
directives). See "Migrate DC custom checkers to CodeXM"
in the Coverity 2026.6.0 Checker Reference.

## Fields

A method set entry must contain a pair of directive fields,
`method_set_for_dc_checker` and `methods`. A
couple other fields can also be present.

`method_set_for_dc_checker`
:   Names the custom checker to which the methods will be added; for example,
    `"method_set_for_dc_checker" :
    "DC.CUSTOM_MY_CHECKER"`.

`methods`
:   A named
    MethodSet value that identifies the method to add to
    the method set; for example, `"methods" : { "named" : "strcmp"
    }`, where `strcmp()` is the method to
    check.

`txt_defect_message`
:   (Optional) Specifies a string to display when the checker finds an issue.
    This string should describe the issue.

`txt_remediation_advice`
:   (Optional) Specifies a string to display when the checker finds an issue.
    This string should describe how to avoid the issue.
