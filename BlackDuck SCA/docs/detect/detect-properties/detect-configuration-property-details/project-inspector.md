---
title: "project-inspector"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/project-inspector.html"
content_id: "iYrHZkQnQ4fHG7oAAuPVjw"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:26.051129+00:00"
---

# project-inspector

## Project Inspector Additional Arguments (Advanced)

```
--detect.project.inspector.arguments
```

A space-separated list of additional options to pass to all invocations of the project inspector.

| Details |  |
| --- | --- |
| Added | 7.7.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Project Inspector Global Arguments (Advanced)

```
--detect.project.inspector.global.arguments
```

A space-separated list of global options to pass to all invocations of the project inspector.

| Details |  |
| --- | --- |
| Added | 8.8.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `--help --quiet` |

## Project Inspector Path (Advanced)

```
--detect.project.inspector.path
```

Use this property to point Detect to a local Project Inspector zip file, instead of the default Project Inspector zip file that Detect downloads from the binary repository. You need to ensure the version is compatible (the same major version that Detect downloads by default).

| Details |  |
| --- | --- |
| Added | 8.1.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
