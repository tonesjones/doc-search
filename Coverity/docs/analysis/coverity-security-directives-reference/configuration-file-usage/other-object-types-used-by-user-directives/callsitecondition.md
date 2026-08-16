---
title: "CallsiteCondition"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/callsitecondition.html"
content_id: "_xDiJQbKLcZyIDHdEEjrRA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:12.850027+00:00"
---

# CallsiteCondition

**Used by these objects:**
`CallsiteSet`

A `CallsiteCondition` value provides a condition that must be satisfied in order
for a CallsiteSet value to match a given call site.

## Fields

This object uses the following fields.

The `only_if_arg_index` field must always be present:

`only_if_arg_index`
:   An integer value, starting from `1`, that specifies the
    position of the argument to which this condition applies.

The following optional fields are mutually exclusive. Only one of these, if any, must
be present:

`equals_string`
:   (Optional) A JSON string value. If this field is present, the argument
    indicated by `only_if_arg_index` must be a string literal
    that has exactly this value and capitalization.

`iequals_string`
:   (Optional) A JSON string value. If this field is present, the argument
    indicated by `only_if_arg_index` must be a string literal
    that equals this value. The comparison for the
    `iequals_string`
    *is not* case-sensitive.

`regex_string`
:   (Optional) A JSON string value that specifies a Perl-style regular
    expression. If this field is present, the argument indicated
    by `only_if_arg_index` must match this regular
    expression. The comparison for the `regex_string` is
    case-sensitive.

`iregex_string`
:   (Optional) A JSON string value that specifies a Perl-style regular
    expression. If this field is present, the argument indicated
    by `only_if_arg_index` must match this regular
    expression. The comparison for the `iregex_string`
    *is not* case-sensitive.

`equals_int`
:   (Optional) Specifies an integer value. If this field is present, the
    argument indicated by `only_if_arg_index` must be an
    integer literal that equals this value.

Finally, the following field, `is_last_arg`, can be specified alone
or in concert with one of the other optional fields:

`is_last_arg`
:   (Optional) A JSON Boolean value.

    If this field is present, the argument indicated by
    `only_if_arg_index` must be the last argument in the
    call site.

    If `is_last_arg` is the *only* optional field
    specified, then `only_if_arg_index` is allowed to equal
    `0`, in order to express that the call site has no
    arguments.

## See also

The example of a call_on for a CallsiteSet example.
