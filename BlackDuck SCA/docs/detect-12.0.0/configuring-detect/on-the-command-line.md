---
title: "On the command line"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/on-the-command-line.html"
content_id: "8ZJ~jlJdhtjz1BIp2H2Whw"
version: "12.0.0"
section: "Configuring Detect"
scraped_at: "2026-09-07T21:15:15.300277+00:00"
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
bash <(curl -s -L https://detect.blackduck.com/detect12.sh) --detect.project.name=MyProject
```
