---
title: "rapid-scan"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/rapid-scan.html"
content_id: "wX395_xKiZ2LNarbii31GA"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-09-07T21:16:38.890950+00:00"
---

# rapid-scan

## Rapid Compare Mode (Advanced)

```
--detect.blackduck.rapid.compare.mode=ALL,BOM_COMPARE,BOM_COMPARE_STRICT
```

Controls how Rapid Scan evaluates policy rules.

Sets the compare mode of Rapid Scan. A setting of ALL evaluates all RAPID or FULL policies. BOM_COMPARE_STRICT shows policy violations not present in a project version BOM that exists in Black Duck SCA. BOM_COMPARE depends on the type of policy rule modes and behaves like ALL if the policy rule is only RAPID and like BOM_COMPARE_STRICT when the policy rule is RAPID and FULL. For further explanation, refer to [Rapid Scan.](https://docs%2Eblackduck%2Ecom/r/detect/latest/black%2Dduck%2Ddetect/rapid%2Dscan%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.12.0 |
| Type | RapidCompareMode |
| Default Value | ALL |
| Comma Separated | No |
| Case Sensitive | Yes |
| Acceptable Values | ALL, BOM_COMPARE, BOM_COMPARE_STRICT |
| Strict | Yes |
