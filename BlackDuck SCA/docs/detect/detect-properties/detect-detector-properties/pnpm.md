---
title: "pnpm"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/pnpm.html"
content_id: "q_87Gx6MubZjvvu6ITuVJw"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:43.333316+00:00"
---

# pnpm

## pnpm Dependency Types

```
--detect.pnpm.dependency.types.excluded=NONE,DEV,OPTIONAL
```

Set this value to indicate which pnpm dependency types Detect should exclude from the BOM.

| Details |  |
| --- | --- |
| Added | 7.11.0 |
| Type | PnpmDependencyType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, DEV, OPTIONAL |
| Strict | Yes |

## pnpm Exclude Directories (Advanced)

```
--detect.pnpm.excluded.packages
```

A comma-separated list of pnpm directories to exclude.

If set, Detect will only exclude those pnpm directories specified via this property when examining the pnpm project for dependencies. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 10.4.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## pnpm Include Directories (Advanced)

```
--detect.pnpm.included.packages
```

A comma-separated list of pnpm directories to include.

If set, Detect will only include the pnpm directories specified via this property when examining the pnpm project for dependencies, unless the directory is set for exclusion. Exclusion rules take precedence over inclusion. Leaving this property unset implies 'include all'. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 10.4.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
