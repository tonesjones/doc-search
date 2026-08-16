---
title: "ruby"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/ruby.html"
content_id: "_O44pMYjxWkpA75OhryIdQ"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:45.190739+00:00"
---

# ruby

## Ruby Dependency Types Excluded

```
--detect.ruby.dependency.types.excluded=NONE,RUNTIME,DEV
```

Set this value to indicate which Ruby(Gempsec) dependency types Detect should exclude from the BOM.

| Details |  |
| --- | --- |
| Added | 7.10.0 |
| Type | GemspecDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, RUNTIME, DEV |
| Strict | Yes |
| Example | `DEV,RUNTIME` |
