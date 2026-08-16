---
title: "lookup_by_constant_param"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/lookup_by_constant_param.html"
content_id: "oK2ogw_qsUyEXcKo3~R4DA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:24.526897+00:00"
---

# lookup_by_constant_param

A `lookup_by_constant_param MethodCallSpecifier` indicates that the method
to call depends on the value of another argument, which is interpreted within the scope
of the directive that contains this `MethodCallSpecifier`).

## Fields

The `lookup_by_constant_param_value MethodCallSpecifier` has the
following fields:

`lookup_by_constant_param`
:   A ParamIn value.

    Given a call site indicated by the parent directive, the ParamIn value indicates a particular
    argument.

`lookup_map`
:   A JSON string.

    The `lookup_map` value is the name of a
    `String` to `MethodCallSpecifier` map
    defined by a define_lookup_method_call_map directive.

    If the argument expression's `String` form is a key in the map, the
    corresponding `MethodCallSpecifier` value or JSON
    `null` literal is evaluated in place of this
    `lookup_by_constant_param MethodCallSpecifier`.

    If the key is not in the map, the parent directive using this lookup
    cannot be evaluated, and a warning is logged.

    Coverity supports matching the `String` form of
    the following kinds of constant literals:

    - `null` for a null reference
    - `true`/`false` for a Boolean
      constant
    - An `enum` constant

      This is the name of the `enum` class (in ClassName value format), followed by
      a dot, followed by the identifier for the constant.
