---
title: "rapid-scan"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/rapid-scan.html"
content_id: "wX395_xKiZ2LNarbii31GA"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:28.020440+00:00"
---

# rapid-scan

## Rapid Compare Mode (Advanced)

```
--detect.blackduck.rapid.compare.mode=ALL,BOM_COMPARE,BOM_COMPARE_STRICT
```

Controls how Rapid Scan evaluates policy rules.

Sets the compare mode of Rapid Scan. A setting of ALL evaluates all RAPID or FULL policies. BOM_COMPARE_STRICT shows policy violations not present in a project version BOM that exists in Black Duck SCA. BOM_COMPARE depends on the type of policy rule modes and behaves like ALL if the policy rule is only RAPID and like BOM_COMPARE_STRICT when the policy rule is RAPID and FULL. For further explanation, refer to [Rapid Scan.](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/runningdetect/rapidscan%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.12.0 |
| Type | RapidCompareMode |
| Default Value | ALL |
| Comma Separated | No |
| Case Sensitive | Yes |
| Acceptable Values | ALL, BOM_COMPARE, BOM_COMPARE_STRICT |
| Strict | Yes |
