---
title: "Complex type: configurationDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-configurationdataobj.html"
content_id: "4u52WfMXaEFHZOfMge4zdg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:30.068731+00:00"
---

# Complex type: configurationDataObj

## Description

Returns system configuration data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| commitPort | long | Port number that supports commits of analysis results. |
| dbDialect | string | Database dialect. |
| dbDriver | string | Database driver. |
| issueExportUrl | string | URL used to handle exported defect information. |
| maindbName | string | Name of the database. |
| maindbUrl | string | URL of the database. |
| maindbUser | string | Authorized user of the database. |
