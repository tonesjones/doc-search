---
title: "cargo"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/cargo.html"
content_id: "4RDfKTkcTfGhD9CMy43o1w"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:32.168589+00:00"
---

# cargo

## Cargo Dependency Types Excluded

```
--detect.cargo.dependency.types.excluded=NONE,NORMAL,BUILD,DEV,PROC_MACRO
```

A comma-separated list of dependency types that will be excluded.

The Cargo CLI Detector uses cargo tree flags to exclude the specified types, while the Cargo Lockfile Detector filters dependencies by reading Cargo.toml. For example, passing `detect.cargo.dependency.types.excluded=DEV` will skip [dev-dependencies] from detection.

| Details |  |
| --- | --- |
| Added | 10.6.0 |
| Type | CargoDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, NORMAL, BUILD, DEV, PROC_MACRO |
| Strict | Yes |
| Example | `DEV` |

## Cargo Executable

```
--detect.cargo.path
```

The path to the cargo executable.

| Details |  |
| --- | --- |
| Added | 10.4.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Disable Default Features

```
--detect.cargo.disable.default.features=false
```

All default features are disabled by the Cargo detector.

| Details |  |
| --- | --- |
| Added | 11.3.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Ignore All Workspaces

```
--detect.cargo.ignore.all.workspaces=false
```

All workspaces are ignored by the Cargo detector.

| Details |  |
| --- | --- |
| Added | 11.2.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Cargo Exclude Workspaces (Advanced)

```
--detect.cargo.excluded.workspaces
```

A comma-separated list of Cargo workspace names to exclude.

By default, Detect includes all workspaces, but will skip any Cargo workspaces specified via this property. Workspace names are defined in the workspace member's Cargo.toml file, not their directory paths.

| Details |  |
| --- | --- |
| Added | 11.2.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
| Example | `workspace-a,workspace-b` |

## Cargo Include Features (Advanced)

```
--detect.cargo.included.features
```

A comma-separated list of Cargo features (specified by the `[feature]` manifest in Cargo.toml) to include, or special values ALL or NONE. By default, Detect only includes default features. Use ALL to enable all features, NONE to generate BOM with no features, or provide a comma-separated list of specific features (e.g., feature-a,feature-b) to include.

This property applies only to the Cargo CLI Detector and is ignored by the Cargo Lockfile Detector.

| Details |  |
| --- | --- |
| Added | 11.3.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
| Example | `feature-a,feature-b` |

## Cargo Include Workspaces (Advanced)

```
--detect.cargo.included.workspaces
```

A comma-separated list of Cargo workspace names to include.

By default, Detect includes all workspaces, but will only include the Cargo workspaces specified via this property when set. Workspace names are defined in the workspace member's Cargo.toml file, not their directory paths.

| Details |  |
| --- | --- |
| Added | 11.2.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
| Example | `workspace-a,workspace-b` |
