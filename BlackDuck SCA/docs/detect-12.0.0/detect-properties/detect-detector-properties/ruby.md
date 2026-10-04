---
title: "ruby"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/ruby.html"
content_id: "_O44pMYjxWkpA75OhryIdQ"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-10-04T23:33:22.840429+00:00"
content_hash: "e4cacc27e5439bb1e8491470e9e139edde20e766e8b42f4128bac660f8ec25c7"
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
