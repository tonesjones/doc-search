---
title: "define_lookup_method_call_map"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/define_lookup_method_call_map.html"
content_id: "c7__BVE3aDZqRfTn6_U_5A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:41.856262+00:00"
---

# define_lookup_method_call_map

**Languages: C#, Java, Visual Basic**

The `define_lookup_method_call_map` directive defines a map that can be
shared across many `MethodCallSpecifier` objects in other directives. In
particular, the lookup_by_constant_param variant of
MethodCallSpecifier can refer to this
map by name.

## Fields

This directive uses the following fields:

`define_lookup_method_call_map`
:   A JSON string value that names the map defined by this directive.

`map`
:   A JSON object that consists of a series of fields, to be interpreted as
    follows:

    - The name of each field is a lexical expression string that is
      mapped to the value of the field.

      Valid lexical expression strings are described in lookup_by_constant_param.
    - The value of the field must be either a method_call value or a JSON
      `null` literal.

## Examples

Configuration example:

See Configuration example 3
and Configuration example 4.

Java code example:

See Java example 3
and Java example 4.
