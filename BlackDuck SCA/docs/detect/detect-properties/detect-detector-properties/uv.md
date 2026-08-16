---
title: "uv"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/uv.html"
content_id: "8QP2~HiDrsUIKoodwOS5cw"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:47.047940+00:00"
---

# uv

## uv dependency groups

```
--detect.uv.dependency.groups.excluded
```

Set this value to indicate which UV dependency groups Detect should exclude from the BOM.

When specified, a pyproject.toml file and uv executable are required, or pyproject.toml file and either uv.lock or requirements.txt file are required. Components and related dependencies that belong to excluded groups will not be in the BOM unless the component also belongs to a non-excluded group. For example, to recursively exclude all components under the `[dependency-groups]` section of `pyproject.toml`: `detect.uv.dependency.groups.excluded='dev,abc'`. Note: In uv, `[project.optional-dependencies]` defines extras. Each extra (e.g., postgres, redis, mysql) is treated as its own dependency group. The group `optional` does not exist; therefore, specifying it in the `--detect.uv.dependency.groups.excluded` flag will have no impact.

| Details |  |
| --- | --- |
| Added | 10.5.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## uv Executable

```
--detect.uv.path
```

The path to the uv executable.

| Details |  |
| --- | --- |
| Added | 10.5.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## uv Exclude Workspace Members (Advanced)

```
--detect.uv.excluded.workspace.members
```

A comma-separated list of uv workspace members to exclude.

If set, Detect will only exclude those project members specified via this property when examining the uv project for dependencies.

| Details |  |
| --- | --- |
| Added | 10.5.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## uv Include Workspace Members (Advanced)

```
--detect.uv.included.workspace.members
```

A comma-separated list of uv workspace members to include.

If set, Detect will only include those uv workspace members specified via this property when examining the uv project for dependencies, unless the member is set for exclusion. Exclusion rules take precedence over inclusion. Leaving this property unset implies 'include all'.

| Details |  |
| --- | --- |
| Added | 10.5.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
