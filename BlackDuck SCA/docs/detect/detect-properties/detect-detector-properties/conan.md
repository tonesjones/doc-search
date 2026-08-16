---
title: "conan"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/conan.html"
content_id: "UbFqaa8HueaGXVFRliPoXw"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:32.804249+00:00"
---

# conan

## Additional Conan Arguments

```
--detect.conan.arguments
```

A space-separated list of additional arguments to add to the 'conan info' command line when running Detect against a Conan project. Detect will execute the command 'conan info {additional arguments} .'

| Details |  |
| --- | --- |
| Added | 6.8.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `"--profile clang --profile cmake_316"` |

## Attempt Package Revision Match

```
--detect.conan.attempt.package.revision.match=false
```

If package revisions are available (a Conan lock file is found or provided, and Conan's revisions feature is enabled), require that each dependency's package revision match the package revision of the component in the KB.

| Details |  |
| --- | --- |
| Added | 6.8.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Conan Dependency Types Excluded

```
--detect.conan.dependency.types.excluded=NONE,BUILD
```

Set this value to indicate which Conan dependency types Detect should exclude from the BOM.

| Details |  |
| --- | --- |
| Added | 7.10.0 |
| Type | ConanDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, BUILD |
| Strict | Yes |
| Example | `BUILD` |

## Conan Executable

```
--detect.conan.path
```

The path to the conan executable.

| Details |  |
| --- | --- |
| Added | 6.8.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Conan Lockfile

```
--detect.conan.lockfile.path
```

The path to the conan lockfile to apply when running 'conan info' to get the dependency graph.

If set, the value will be used by CLI and lockfile detectors to determine the component versions and/or relationships.'

| Details |  |
| --- | --- |
| Added | 6.8.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
