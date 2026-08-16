---
title: "Complex type: backupConfigurationDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-backupconfigurationdataobj.html"
content_id: "sM6pGQfr46wJOxLJYaCSqQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:23.488380+00:00"
---

# Complex type: backupConfigurationDataObj

## Description

Specification for Coverity Connect database backup settings.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| backupLocation | string | Full path to a backup directory on the disk where Coverity Connect is installed. |
| backupTime | string | Time of the backup, for example: 01:15 |
| fridayEnabled | boolean | Friday backup if set to true. Defaults to false. |
| mondayEnabled | boolean | Monday backup if set to true. Defaults to false. |
| saturdayEnabled | boolean | Saturday backup if set to true. Defaults to false. |
| sundayEnabled | boolean | Sunday backup if set to true. Defaults to false. |
| thursdayEnabled | boolean | Thursday backup if set to true. Defaults to false. |
| tuesdayEnabled | boolean | Tuesday backup if set to true. Defaults to false. |
| wednesdayEnabled | boolean | Wednesday backup if set to true. Defaults to false. |
