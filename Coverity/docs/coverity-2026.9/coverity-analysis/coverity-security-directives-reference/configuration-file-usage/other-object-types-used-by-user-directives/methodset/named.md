---
title: "named"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/named.html"
content_id: "HJDPN_zS6JKO9S2S21AX~w"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:01.117796+00:00"
---

# named

A `named MethodSet` matches the method with the mangled name in the
`named` field.

See the MethodName section for a description of the
mangled name format.

## Fields

`named`
:   A `MethodName` value to identify the method.

## Examples

The following example of a `named MethodSet` matches a single
`print` method in `mypackage.MyClass`.

```
{ "named": "mypackage.MyClass.print(java.lang.String)void" }
```
