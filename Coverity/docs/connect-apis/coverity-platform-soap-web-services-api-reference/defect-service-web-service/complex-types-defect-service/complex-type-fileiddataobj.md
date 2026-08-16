---
title: "Complex type: fileIdDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-fileiddataobj.html"
content_id: "MqVo65glZ9t10QV2_yEK~Q"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:34.302659+00:00"
---

# Complex type: fileIdDataObj

## Description

Contents of and path to a source code file.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| contentsMD5 | string | Required. MD5 checksum (a fingerprint or message digest) of the file contents. You can get the contentsMD5 and filePathname for an instance of a CID by using getStreamDefects() with the includeDefectInstances filter set to true. |
| filePathname | string | Required. Path to the file that contains the instance of the CID. You can get the contentsMD5 and filePathname for an instance of a CID by using getStreamDefects() with the includeDefectInstances filter set to true. |
