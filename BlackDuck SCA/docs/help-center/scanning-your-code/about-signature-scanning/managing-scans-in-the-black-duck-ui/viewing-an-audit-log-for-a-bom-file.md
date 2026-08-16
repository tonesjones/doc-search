---
title: "Viewing an audit log for a BOM file"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-an-audit-log-for-a-bom-file.html"
content_id: "v4icGCkIuMt_fNiuQN59_A"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:53.262898+00:00"
---

# Viewing an audit log for a BOM file

Use the View Import Log to view your results of importing a BOM file. This log lists the
components and licenses that were mapped to Black Duck. It also
provides details for any items that were unable to be mapped.

To view an audit log:

1. Log in to Black Duck SCA.
2. Click [image: Scans icon] .

   The Scans page appears.

     
    [image: Scans page]
3. Select the scan you wish to view.

   The  *Scan Name* page appears. The host, path, and scan details (status of the scan,
   date, or time (if the date is today) the scan completed, and the username of the
   user that ran the scan) appear at the top of the page.

     
    [image: image]
4. Select **View Import Log** to view the log. If this code location has been scanned
   multiple times, only the latest BOM Import Log will be available to view.

   The BOM Import Log displays, if applicable, the number of components mapped and components
   not found above the table.

   Note: The BOM Import Log will not display licenses missing, mapped, or not found for scans
   imported after 2024.7.0. However, they will continue to be displayed for scans
   imported prior to 2024.7.0.

     
    [image: BOM Import Log]

## Component/License Import Events & Statuses

The Status column will display whether or not the component or license was
successfully imported. If a component or license was not successfully imported, an
error message will explain the reason for the failure.

Tip: The Import BOM Log table can also be filtered by these statuses.

The possible statuses are as follows:

- **Component mapped**. This status indicates that the component version was successfully
  mapped to the Black Duck KnowledgeBase.
- **Component not found**. This status indicates that the scanned component version was not
  successfully mapped to the Black Duck project version
  because no mapping is present for the given external identifier.
- **License mapped**. This status indicates that the license was successfully mapped to the
  Black Duck KnowledgeBase.
- **License not found**. This status indicates that the scanned license was not
  successfully mapped because no mapping is present for the given external
  identifier in the Black Duck KnowledgeBase .
- **License missing**. This status indicates that the scanned license was not found.

## Using the `GET/api/bom-import/<graphId>/component-import-events` API request

When using the `GET
/api/bom-import/<graphId>/component-import-events` API request, the
statuses will be displayed in the following responses. If the import was
unsuccessful, the `failureReason` value will provide more
information. See below for response examples.

A successful component import:

```
    {
      "event": "COMPONENT_MAPPING_SUCCEEDED",
      "importComponentName": "imported component name",
      "importComponentVersionName": "imported component version",
      "componentName": "full component name",
      "componentVersionName": "full component version",
      "externalId": "external identification"
    },
```

An unsuccessful component import:

```
    {
      "event": "COMPONENT_MAPPING_FAILED",
      "importComponentName": "imported component name",
      "importComponentVersionName": "imported component version",
      "externalId": "external identification",
      "failureReason": "Unable to map scanned component version to Black Duck project version because no mapping is present for the given external identifier"
    }
```

A successful license import:

```
    {
        "event" : "LICENSE_MAPPING_SUCCEEDED",
        "protexLicenseName" : "license name",
        "externalId" : "external identification",
    }
```

An unsuccessful license import may fail in one of the following reasons:

- Unable to map scanned license to Black Duck license because no external
  identifier is present
- Unable to map scanned license to Black Duck license because no mapping is
  present for the given external identifier
- Unsupported license mapping

Regardless of the failure, the API response will be formed as follows:

```
    {
      "event": "LICENSE_MAPPING_FAILED",
      "protexLicenseId": "license ID",
      "protexLicenseName": "license name",
      "externalId": "external identification",
      "failureReason": "see reasons above"
    }
```
