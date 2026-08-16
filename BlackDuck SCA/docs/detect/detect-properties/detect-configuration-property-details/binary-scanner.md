---
title: "binary-scanner"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/binary-scanner.html"
content_id: "c6fsfEGVdvjgLk09ZRAgpQ"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:16.412931+00:00"
---

# binary-scanner

## Binary Scan Filename Patterns

```
--detect.binary.scan.file.name.patterns
```

If specified, files in the source directory whose names match these file name patterns will be zipped and uploaded for binary scan analysis. This property will not be used if detect.binary.scan.file.path is specified. Search depth is controlled by property detect.binary.scan.search.depth. Directories specified via property detect.excluded.directories are excluded from the file search. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 6.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `*.jar` |

## Binary Scan Search Depth

```
--detect.binary.scan.search.depth=0
```

When binary scan filename patterns are being used to search for binary files to scan, this property sets the depth at which Detect will search for files (that match those patterns) to upload for binary scan analysis.

| Details |  |
| --- | --- |
| Added | 6.9.0 |
| Type | Integer |
| Default Value | 0 |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Binary Scan Target

```
--detect.binary.scan.file.path
```

If specified, this file and this file only will be uploaded for binary scan analysis. This property takes precedence over detect.binary.scan.file.name.patterns. The BINARY_SCAN tool does not provide project and version name defaults to Detect, so you need to set project and version names via properties when only the BINARY_SCAN tool is invoked.

| Details |  |
| --- | --- |
| Added | 4.2.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
