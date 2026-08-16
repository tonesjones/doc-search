---
title: "Using environment variables"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/using-environment-variables.html"
content_id: "ffX6GHIQf6NoSbVFaU8KEw"
version: "11.5.1"
section: "Configuring Detect"
scraped_at: "2026-08-08T23:44:18.169771+00:00"
---

# Using environment variables

Detect properties can also be set using environment variables.

On Linux, when setting a property value using an environment variable, the environment variable name
is the property name converted to uppercase, with period characters (".") converted to underscore
characters ("_"). For example:

```
export DETECT_PROJECT_NAME=MyProject
bash <(curl -s -L https://detect.blackduck.com/detect11.sh)
```

On Windows, the environment variable name can either be the original property
name, or the property name converted to uppercase with period characters (".") converted to underscore
characters ("_"). For example:

```
$Env:DETECT_PROJECT_NAME = MyProject
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect"
```
