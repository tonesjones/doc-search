---
title: "pnpm"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/pnpm.html"
content_id: "q_87Gx6MubZjvvu6ITuVJw"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-10-04T23:33:22.780013+00:00"
content_hash: "c06ad21e4bd59c00b027acce25fd061ec98807d585b769679056d7b47c40bbab"
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

If set, Detect will only exclude those pnpm directories specified via this property when examining the pnpm project for dependencies. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://docs%2Eblackduck%2Ecom/r/detect/latest/black%2Dduck%2Ddetect/property%2Dwildcard%2Dsupport%2Ehtml)

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

If set, Detect will only include the pnpm directories specified via this property when examining the pnpm project for dependencies, unless the directory is set for exclusion. Exclusion rules take precedence over inclusion. Leaving this property unset implies 'include all'. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://docs%2Eblackduck%2Ecom/r/detect/latest/black%2Dduck%2Ddetect/property%2Dwildcard%2Dsupport%2Ehtml)

| Details |  |
| --- | --- |
| Added | 10.4.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
