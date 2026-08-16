---
title: "lerna"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/lerna.html"
content_id: "HhT_OFJMpf84PQ~jZKbgRQ"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:38.054072+00:00"
---

# lerna

## Lerna Executable

```
--detect.lerna.path
```

Path of the lerna executable.

| Details |  |
| --- | --- |
| Added | 6.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Lerna Package Types Excluded

```
--detect.lerna.package.types.excluded=NONE,PRIVATE
```

Set this value to indicate which Lerna package types Detect should exclude from the BOM.

| Details |  |
| --- | --- |
| Added | 7.10.0 |
| Type | LernaPackageType List |
| Default Value | NONE |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | NONE, PRIVATE |
| Strict | Yes |
| Example | `PRIVATE` |

## Lerna Packages Excluded (Advanced)

```
--detect.lerna.excluded.packages
```

A comma-separated list of Lerna packages to exclude.

As Detect parses the output of lerna ls --all --json, Detect will exclude any Lerna packages specified via this property. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |

## Lerna Packages Included (Advanced)

```
--detect.lerna.included.packages
```

A comma-separated list of Lerna packages to include.

As Detect parses the output of lerna ls --all --json2, if this property is set, Detect will include only those Lerna packages specified via this property that are not excluded. Leaving this unset implies 'include all'. Exclusion rules always win. This property accepts filename globbing-style wildcards. For more information, refer to the [Property wildcard support page.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/configuring/propertywildcards%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.0.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
