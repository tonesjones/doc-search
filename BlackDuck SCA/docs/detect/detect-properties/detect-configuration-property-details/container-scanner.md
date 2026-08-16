---
title: "container-scanner"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/container-scanner.html"
content_id: "~gh72qGXK_kWkUNo6w~gGQ"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:18.336279+00:00"
---

# container-scanner

## Container Scan Target

```
--detect.container.scan.file.path
```

If it is specified, only this .tar file will be uploaded for Container Scan analysis.

Detect will accept either a user provided local .tar file path, or remote HTTP/HTTPS URL to fetch a container image .tar file for scanning. The CONTAINER_SCAN tool does not provide project and version name defaults to Detect, so you need to set project and version names via properties when only the CONTAINER_SCAN tool is invoked.

| Details |  |
| --- | --- |
| Added | 9.1.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
