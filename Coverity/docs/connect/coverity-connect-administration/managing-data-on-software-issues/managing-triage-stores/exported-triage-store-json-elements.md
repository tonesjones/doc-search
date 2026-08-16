---
title: "Exported triage store JSON elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/exported-triage-store-json-elements.html"
content_id: "QVebjJdyDJ~df5NZlk6K5A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:25.387910+00:00"
---

# Exported triage store JSON elements

The following table lists and describes the elements contained in the JSON file that is
produced when you use the Export button in the Triage Store
menu.

Table 1. Exported triage store JSON elements

| Element | Description |
| --- | --- |
| `Name` | The root element of the JSON file is a string containing the name of the triage store. The triage store may contain multiple defect objects, which each consist of the following attributes: `checker, cid, dateOriginated, detectedBy, domain, mergeKey, preventVersionExternal, preventVersionInternal,` and `triageStates`. |
| `checker` | The name of the checker that found the defect. |
| `cid` | The CID (Coverity ID) of the defect. |
| `dateOriginated` | The date and time that the defect was originally committed to Coverity Connect. |
| `detectedBy` | The process that was responsible for reporting the defect. |
| `domain` | The defect's programming language. |
| `mergeKey` | A unique identifier that maps a CID across multiple projects or Coverity Connect instances. |
| `preventVersionExternal` | The version of the Coverity Analysis tools that found the defect. |
| `preventVersionInternal` | The internal identifier for the Coverity Analysis version. |
| `triageStates` | A group of name/value pairs for the defect's triage attributes. `triageStates` contains the following child attributes: `action, classification, comments, customTriage, dateCreated, dateEnded, fixTarget, legacy, severity, userCreated,` and `userCreatedLdapServerName`. |
| `action` | Triage attribute used to specify the action to take with regard to the defect. |
| `classification` | Triage attribute that identifies the classification of the defect. |
| `comments` | User comments (if any) included by a user during triage of the defect. |
| `customTriage` | The `customTriage` object contains two child objects, `picklistAttributes` and `stringAttributes`, which contain any custom triage attributes and values created by the user or administrator. |
| `dateCreated` | Date and time when the current triage attribute values were stored. |
| `dateEnded` | Date and time when the current triage attribute values were updated or replaced. |
| `fixTarget` | Triage attribute used to set the release in which to fix an issue. |
| `legacy` | Triage attribute used to indicate whether a defect is a legacy issue or not. |
| `severity` | Triage attribute that identifies the severity of the defect. |
| `userCreated` | The user name that created the current defect triage state. |
| `userCreatedLdapServerName` | The LDAP server associated with the `userCreated` user name. |
| `Export Summary` | The `Export Summary` object contains information on the success or failure of the export process. It contains the following child objects: `failCount, successCount,` and `totalProcessed`. |
| `failCount` | The number of defect objects within the triage store that failed to export properly. |
| `successCount` | The number of defect objects within the triage store that exported properly. |
| `totalProcessed` | The total number of defect objects within the triage store. |
