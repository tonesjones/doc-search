---
title: "sbt"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/sbt.html"
content_id: "Q~q~Bkb5RkJL0WmxjzymlQ"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:45.803424+00:00"
---

# sbt

## Additional sbt command Arguments

```
--detect.sbt.arguments
```

A space-separated list of additional arguments to add to sbt command line when running Detect against an SBT project. Detect will execute the command 'sbt {additional arguments} {Detect-added arguments}'.

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `"-Djline.terminal=jline.UnsupportedTerminal"` |

## Sbt Executable

```
--detect.sbt.path
```

Path to the Sbt executable.

If set, Detect will use the given Sbt executable instead of searching for one.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `C:\Program Files (x86)\sbt\bin\sbt.bat` |
