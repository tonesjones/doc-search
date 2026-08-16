---
title: "with_annotation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/with_annotation.html"
content_id: "ZpqzJyBqQhSDA2bYkNDXxQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:29.720680+00:00"
---

# with_annotation

A `with_annotation MethodSet` uses an `AnnotationSet` to
match methods in the source code that contain the annotations specified by the set.

## Fields

The `with_annotation MethodSet` has a single field:

`with_annotation`
:   An AnnotationSet value. The `with_annotation
    MethodSet` matches a method whose definition contains any of
    the specified analysis annotations.

## Examples

The following `with_annotation MethodSet` example matches any method
defined with the annotation `java.lang.annotation.Documented`.

```
{ "with_annotation": 
    { "matching": "java\\.lang\\.annotation\\.Documented" }
}
```

Example of a matching Java method definition:

```
@Documented
void printHello() {
   System.out.println("Hello!");
}
```

The following `with_annotation MethodSet` example matches any method
defined with the annotation `MyCsharpAttribute`.

```
{ "with_annotation": 
    { "named": "MyCsharpAttribute" }
}
```

Example of a matching C# method definition:

```
[MyCsharpAttribute]
string GetCorporateName() {
    return "Black Duck";
}
```
