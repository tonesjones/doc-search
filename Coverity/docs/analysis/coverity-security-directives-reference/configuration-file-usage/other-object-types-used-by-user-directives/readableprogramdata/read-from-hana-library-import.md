---
title: "read_from_HANA_library_import"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/read_from_hana_library_import.html"
content_id: "RAomY84VojYPWtymwT0zNg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:36.143057+00:00"
---

# read_from_HANA_library_import

**Languages: JavaScript**

A `read_from_HANA_library_import ReadableProgramData` value identifies a
readable value along an access path that is relative to a HANA XSC library returned from
a `$.import` call site found in a `.xsjs` or
`.xsjslib` source file.

This directive mirrors the `$.import` method, in that two import formats
are supported:

1. A file path

   This directive format uses the `read_from_HANA_library_import`
   field to specify a file path that locates the library source file. The optional
   `package` field is not used.

   This format corresponds to a call to `$.import` using a single
   argument.
2. A package specifier and a library name

   In this directive format, the `read_from_HANA_library_import`
   field specifies the library name (without the `.xsjslib`
   extension), and the `package` field specifies the library's
   `.`-separated package name.

   This format corresponds to a call to `$.import` using two
   arguments.

## Fields

A `read_from_HANA_library_import ReadableProgramData` object has the
following fields:

`read_from_HANA_library_import`
:   A string value that is either the name of the HANA XSC module specified
    in the `$.import` call site, or a file path that locates
    the library file.

`package`
:   A string value. If this field is present, then import method #2,
    described above, is used.

`path`
:   (Optional) A non-empty array of AccessPathElement values, for use with
    import method #2.

## Examples

The following two example directives are equivalent:

```
{
      "read_from_HANA_library_import" : "/package/name/lib.xsjslib",
      "path" : [ { "property" : "p"} ]
},
```

```
{
      "read_from_HANA_library_import" : "lib",
      "package" : "package.name",
      "path" : [ { "property" : "p"} ]
},
```

Both directives specified above will match both of the following equivalent import
expressions found within an `.xsjs` or `.xsjslib`
source file.

```
{
var p1 = $.import("/package/name/lib.xsjslib").p;
var p2 = $.import("package.name", "lib").p;
},
```
