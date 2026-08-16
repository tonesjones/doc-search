---
title: "On the command line"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/on-the-command-line.html"
content_id: "8ZJ~jlJdhtjz1BIp2H2Whw"
version: "11.5.1"
section: "Configuring Detect"
scraped_at: "2026-08-08T23:44:17.543463+00:00"
---

# On the command line

One method for configuring Detect is by setting property values on the command line.
When setting a property value on the command line, prefix the property name with two hyphens (--).

To add one property setting to the command line, add the following at the end:

```
{space}--{property name}={value}
```

There is a space before and between each complete property setting, but there are no spaces around the equals sign (=).

For example,
to set property *detect.project.name*:

```
bash <(curl -s -L https://detect.blackduck.com/detect11.sh) --detect.project.name=MyProject
```
