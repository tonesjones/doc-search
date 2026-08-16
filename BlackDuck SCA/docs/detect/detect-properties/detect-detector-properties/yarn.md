---
title: "yarn"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/yarn.html"
content_id: "4O_OpUaqTEtK9ciJwT7Gng"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:47.666520+00:00"
---

# yarn

## Ignore All Workspaces

```
--detect.yarn.ignore.all.workspaces=false
```

All workspaces are ignored by the Yarn detector for increased performance and precision to scan a massive codebase.

| Details |  |
| --- | --- |
| Added | 9.4.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Yarn Dependency Types Excluded

```
--detect.yarn.dependency.types.excluded=NONE,NON_PRODUCTION
```

Set this value to indicate which Yarn dependency types Detect should exclude from the BOM.

| Details |  |
| --- | --- |
| Added | 4.0.0 |
| Type | YarnDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, NON_PRODUCTION |
| Strict | Yes |
| Example | `NON_PRODUCTION` |

## Yarn Exclude Workspaces (Advanced)

```
--detect.yarn.excluded.workspaces
```

A comma-separated list of Yarn workspaces (specified by the workspace directory's relative path) to exclude.

By default, Detect includes all workspaces, but will skip any Yarn workspaces specified via this property. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
| Example | `workspaces/workspace-a,workspaces/*-test` |

## Yarn Include Workspaces (Advanced)

```
--detect.yarn.included.workspaces
```

A comma-separated list of Yarn workspaces (specified by the workspace directory's relative path) to include.

By default, Detect includes all workspaces. If workspaces are excluded or included, Detect will include any workspace included by this property that is not excluded. Exclusion rules always win. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
| Example | `workspaces/workspace-a,workspaces/workspace-b` |
