---
title: "pear"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/pear.html"
content_id: "~dyJIIWEhJPWVHOXTrhSdg"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-10-04T23:33:22.724905+00:00"
content_hash: "384458f388af4c34d02d388acfd6ee4c04171c1a63c096524cfc18ec28649631"
---

# pear

## Pear Dependency Types Excluded

```
--detect.pear.dependency.types.excluded=NONE,OPTIONAL
```

Set this value to indicate which Pear dependency types Detect should exclude from the BOM.

| Details |  |
| --- | --- |
| Added | 7.10.0 |
| Type | PearDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, OPTIONAL |
| Strict | Yes |
| Example | `OPTIONAL` |

## Pear Executable

```
--detect.pear.path
```

The path to the pear executable.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
