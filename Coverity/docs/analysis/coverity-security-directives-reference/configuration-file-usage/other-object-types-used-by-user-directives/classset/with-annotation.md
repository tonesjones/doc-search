---
title: "with_annotation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/with_annotation.html"
content_id: "0METXMuS5XGCqpSXssD~Ew"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:16.780480+00:00"
---

# with_annotation

A `with_annotation ClassSet` uses an AnnotationSet value to match a class whose definition
has any of the specified annotations.

## Fields

This kind of `ClassSet` object has a single field:

`with_annotation`
:   An AnnotationSet value that contains names or regular
    expressions to identify classes that will be included in the
    `ClassSet`.

## Examples

The following `with_annotation ClassSet` example matches any class
defined with the annotation `java.lang.annotation.Documented`.

```
{ "with_annotation": 
    { "matching": "java\\.lang\\.annotation\\.Documented" }
}
```

Example of a matching Java class definition:

```
@Documented
public class FooBar {
    // ...
}
```

The following `with_annotation ClassSet` example matches any class
defined with the annotation `MyWebController`.

```
{ "with_annotation": 
    { "named": "MyWebController" }
}
```

Example of a matching C# class definition:

```
[MyWebController]
class AccountController {
    // ...
}
```
