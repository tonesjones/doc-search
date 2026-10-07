---
title: "named"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/named.html"
content_id: "Ko042vVI2H~ptsiOZHINiQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:00.012088+00:00"
---

# named

A `named AnnotationSet` matches all uses of the Java annotation or C#
attribute whose entire mangled class name matches the `named` string. See
ClassName for a description of the mangled name
format.

## Fields

A `named AnnotationSet` has a single field called
`named`:

`named`
:   A JSON string value that specifies the mangled class name of the analysis
    annotation to match.

## Examples

The following example of a `named AnnotationSet` matches uses of the
Java `@Deprecated` annotation:

```
{ "named": "java.lang.annotation.Deprecated" }
```
