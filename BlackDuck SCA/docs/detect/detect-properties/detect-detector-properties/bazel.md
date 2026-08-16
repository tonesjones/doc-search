---
title: "bazel"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/bazel.html"
content_id: "yoRNnJ27auYQaQAcDUERFg"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:30.809969+00:00"
---

# bazel

## Bazel cquery additional options

```
--detect.bazel.cquery.options
```

A comma-separated list of additional options to pass to the bazel cquery command. e.g., --enable_bzlmod, --enable_workspace

| Details |  |
| --- | --- |
| Added | 6.1.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Bazel dependency sources

```
--detect.bazel.dependency.sources=ALL,NONE,MAVEN_JAR,MAVEN_INSTALL,HASKELL_CABAL_LIBRARY,HTTP_ARCHIVE
```

Replaces the deprecated detect.bazel.workspace.rules property. Manually specify which dependency sources to extract. Valid values: MAVEN_INSTALL, MAVEN_JAR, HTTP_ARCHIVE, HASKELL_CABAL_LIBRARY, ALL, NONE. By default (NONE), Detect automatically probes the Bazel dependency graph to determine which sources are present and runs the appropriate pipelines. This property works for both BZLMOD and WORKSPACE projects.

Set this property when you know which dependency sources are present in your target to skip the probing step and improve performance, especially in CI/CD environments. Use ALL to extract from all supported sources without probing. Example: MAVEN_INSTALL,HTTP_ARCHIVE extracts only Maven and HTTP archive dependencies.

| Details |  |
| --- | --- |
| Added | 11.3.0 |
| Type | DependencySource List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | ALL, NONE, MAVEN_JAR, MAVEN_INSTALL, HASKELL_CABAL_LIBRARY, HTTP_ARCHIVE |
| Strict | Yes |

## Bazel Executable

```
--detect.bazel.path
```

The path to the Bazel executable.

| Details |  |
| --- | --- |
| Added | 5.2.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `$HOME/bin/bazel` |

## Bazel Mode Override

```
--detect.bazel.mode
```

Override Bazel mode detection. By default, Detect automatically determines whether the Bazel project uses BZLMOD or WORKSPACE-based dependency management by running bazel mod graph. Valid values: WORKSPACE, BZLMOD.

Only set this property if auto-detection produces incorrect results or for testing purposes. Incorrect values may cause extraction to fail. Auto-detection falls back to WORKSPACE mode if the project is on Bazel 5.x or earlier, or if bazel mod graph returns an empty graph (common in hybrid repos that declare MODULE.bazel for compatibility but manage dependencies via WORKSPACE).

| Details |  |
| --- | --- |
| Added | 11.3.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Bazel query additional options

```
--detect.bazel.query.options
```

A comma-separated list of additional options to pass to the bazel query command. e.g., --enable_bzlmod, --enable_workspace

| Details |  |
| --- | --- |
| Added | 11.3.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Bazel Target

```
--detect.bazel.target
```

The Bazel target (for example, //foo:foolib) for which dependencies are collected. For Detect to run Bazel, this property must be set.

| Details |  |
| --- | --- |
| Added | 5.2.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Bazel workspace rules (Deprecated)

```
--detect.bazel.workspace.rules=ALL,NONE,MAVEN_JAR,MAVEN_INSTALL,HASKELL_CABAL_LIBRARY,HTTP_ARCHIVE
```

By default Detect discovers Bazel dependencies using all supported Bazel workspace rules that it finds in the WORKSPACE file. Alternatively you can use this property to specify the list of Bazel workspace rules Detect should use.

Setting this property (or letting it default) to NONE tells Detect to use supported rules that it finds in the WORKSPACE file.

**DEPRECATED: This property has been deprecated. Please use detect.bazel.dependency.sources instead. This property will be removed in 12.0.0.**

| Details |  |
| --- | --- |
| Added | 7.12.0 |
| Type | WorkspaceRule List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | ALL, NONE, MAVEN_JAR, MAVEN_INSTALL, HASKELL_CABAL_LIBRARY, HTTP_ARCHIVE |
| Strict | Yes |
