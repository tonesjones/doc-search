---
title: "go"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/go.html"
content_id: "jF8V2O_3Zo89HpCQJFNZ4Q"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:36.113604+00:00"
---

# go

## Go Executable

```
--detect.go.path
```

Path to the Go executable.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Go Forge Connection Timeout

```
--detect.go.forge.connection.timeout=30
```

The connection timeout in seconds to use when connecting to the Go Forge. If not set, the default connection timeout of 30 seconds will be used.

| Details |  |
| --- | --- |
| Added | 11.0.0 |
| Type | Integer |
| Default Value | 30 |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `30` |

## Go Forge Read Timeout

```
--detect.go.forge.read.timeout=60
```

The read timeout in seconds to use when reading from the Go Forge. If not set, the default read timeout of 60 seconds will be used.

| Details |  |
| --- | --- |
| Added | 11.0.0 |
| Type | Integer |
| Default Value | 60 |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `60` |

## Go Forge URL

```
--detect.go.forge
```

The Go Forge URL to fetch the go.mod descriptor of direct dependencies. If not set, the default Go Forge (https://proxy.golang.org) will be used. This is only applicable to the Go Mod File detector.

| Details |  |
| --- | --- |
| Added | 11.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Go Mod Dependency Types Excluded

```
--detect.go.mod.dependency.types.excluded=NONE,UNUSED,VENDORED
```

Set this value to indicate which Go Mod dependency types Detect should exclude from the BOM.

If UNUSED is provided, Detect will use the results of 'go mod why' to filter out unused dependencies from Go modules declaring Go 1.16 or higher. If VENDORED is provided, Detect will use the results of 'go mod why -vendor' to filter out all unused dependencies. This property is only applicable to the Go Mod CLI Detector.

| Details |  |
| --- | --- |
| Added | 7.10.0 |
| Type | GoModDependencyType |
| Default Value | NONE |
| Comma Separated | No |
| Case Sensitive | Yes |
| Acceptable Values | NONE, UNUSED, VENDORED |
| Strict | Yes |
| Example | `VENDORED` |
