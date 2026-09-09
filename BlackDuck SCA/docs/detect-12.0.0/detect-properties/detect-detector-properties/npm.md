---
title: "npm"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/npm.html"
content_id: "YoplzFVIzX4JCqsO2SuiKw"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-09-07T21:16:52.387188+00:00"
---

# npm

## Additional NPM Command Arguments

```
--detect.npm.arguments
```

A space-separated list of additional arguments that Detect will add at then end of the npm ls command line when Detect executes the NPM CLI Detector on an NPM project.

| Details |  |
| --- | --- |
| Added | 4.3.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `--depth=0` |

## Ignore All Workspaces

```
--detect.npm.ignore.all.workspaces=false
```

All workspaces are ignored by the NPM detector for increased performance and precision to scan a massive codebase.

| Details |  |
| --- | --- |
| Added | 12.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Npm Dependency Types Excluded

```
--detect.npm.dependency.types.excluded=NONE,DEV,PEER,OPTIONAL
```

Set this value to indicate which Npm dependency types Detect should exclude from the BOM.

| Details |  |
| --- | --- |
| Added | 7.10.0 |
| Type | NpmDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, DEV, PEER, OPTIONAL |
| Strict | Yes |
| Example | `DEV,PEER` |

## NPM Executable

```
--detect.npm.path
```

The path to the Npm executable.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## NPM Exclude Workspaces (Advanced)

```
--detect.npm.excluded.workspaces
```

A comma-separated list of npm workspace relative paths to exclude.

By default, Detect includes all workspaces. Workspaces are identified by their path relative to the project root (e.g. packages/react-components). This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 12.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
| Example | `packages/test-harness,packages/internal-*` |

## NPM Include Workspaces (Advanced)

```
--detect.npm.included.workspaces
```

A comma-separated list of npm workspace relative paths to include.

By default, Detect includes all workspaces. If workspaces are excluded or included, Detect will include any workspace included by this property that is not excluded. Exclusion rules always win. Workspaces are identified by their path relative to the project root (e.g. packages/react-components). This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 12.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
| Example | `packages/frontend,packages/api` |
