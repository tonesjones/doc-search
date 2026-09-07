---
title: "dart"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/dart.html"
content_id: "7E2ClUlZjYHIHNtemJrUBA"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-09-07T21:16:46.722619+00:00"
---

# dart

## dart Executable

```
--detect.dart.path
```

The path to the dart executable.

| Details |  |
| --- | --- |
| Added | 7.5.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Dart Pub Dependency Types Excluded

```
--detect.pub.dependency.types.excluded=NONE,DEV
```

Set this value to indicate which Dart pub dependency types Detect should exclude from the BOM.

If DEV is excluded, the Dart Detector will pass the option --no-dev when running the command 'pub deps'.

| Details |  |
| --- | --- |
| Added | 7.10.0 |
| Type | DartPubDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, DEV |
| Strict | Yes |
| Example | `DEV` |

## flutter Executable

```
--detect.flutter.path
```

The path to the flutter executable.

| Details |  |
| --- | --- |
| Added | 7.5.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
