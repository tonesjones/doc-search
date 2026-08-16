---
title: "Detect Properties"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-properties.html"
content_id: "3o3A7Cthec3O5zG~3eQKFA"
version: "11.5.1"
section: "Getting started with Detect"
scraped_at: "2026-08-08T23:44:09.564320+00:00"
---

# Detect Properties

Properties in Black Duck® Detect provide information used to determine how and what actions Detect takes during a scanning run. A property to which you assign a value is like a flag or a parameter on the command line or in a script that provides instructions for the Detect scan task.

When setting a property value, the property name is prefixed with two hyphens (--).

```
bash <(curl -s -L https://detect.blackduck.com/detect11.sh) <--property=value>
```

Example using properties to specify project name and Black Duck SCA URL:

```
bash <(curl -s -L https://detect.blackduck.com/detect11.sh) --detect.project.name=MyProject --blackduck.url=https://blackduck.yourdomain.com
```

Note: When configuring Detect via environment variables or configuration file, specific property handling applies. See Using environment variables or Using a configuration file.
