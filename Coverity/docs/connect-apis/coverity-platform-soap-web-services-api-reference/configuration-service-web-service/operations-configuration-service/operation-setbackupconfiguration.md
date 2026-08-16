---
title: "Operation: setBackupConfiguration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-setbackupconfiguration.html"
content_id: "UGuDOhKqY1faAdD_bTKfkQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:06.870946+00:00"
---

# Operation: setBackupConfiguration

## Name

setBackupConfiguration

## Description

Set a schedule for automated backup of the Coverity Connect database. The name of the
backup file looks something like the following: CIM.2013-12-04.10-35.backup

## Parameters

backupConfigurationDataObj
:   **Type:** 
    backupConfigurationDataObj

    The settings correspond to the Maintenance options (System settings) in
    Coverity Connect.

    | Field name | Type | Description |
    | --- | --- | --- |
    | backupLocation | string | Full path to a backup directory on the disk where Coverity Connect is installed. |
    | backupTime | string | Time of the backup, for example: 01:15 |
    | fridayEnabled | boolean | Friday backup if set to true. Defaults to false. |
    | mondayEnabled | boolean | Monday backup if set to true. Defaults to false. |
    | saturdayEnabled | boolean | Saturday backup if set to true. Defaults to false. |
    | sundayEnabled | boolean | Sunday backup if set to true. Defaults to false. |
    | thursdayEnabled | boolean | Thursday backup if set to true. Defaults to false. |
    | tuesdayEnabled | boolean | Tuesday backup if set to true. Defaults to false. |
    | wednesdayEnabled | boolean | Wednesday backup if set to true. Defaults to false. |

## Remarks

See also getBackupConfiguration().
