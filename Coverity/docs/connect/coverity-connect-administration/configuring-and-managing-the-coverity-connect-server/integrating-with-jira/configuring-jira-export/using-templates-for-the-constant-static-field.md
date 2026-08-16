---
title: "Using templates for the Constant static field"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-templates-for-the-constant-static-field.html"
content_id: "UJBR0mypXWktVwVi4gx9bw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:18.487801+00:00"
---

# Using templates for the Constant static field

You can use simple variables in the Constant field to create templated
static fields. To do so, use angle brackets around the variable name, and the relevant
value will be substituted into the exported Jira field. For example, "<checker>
found in <file>" will be formatted to something like "`NULL_POINTER found
in main.c`".

The available variables are:

Table 1. Variables for static fields

| Variable | Description |
| --- | --- |
| action | The action that is being taken for the issue. |
| category | The checker category describing the nature of the software issue. |
| checker | The checker that found the issue. |
| cid | The CID of the issue. |
| classification | The classification of the issue. |
| comparison | Indicates if the issue is present in the snapshot used for comparison. |
| component | The component where the issue is found. |
| cwe | The Common Weakness Enumeration identifier for the issue. |
| file | The file where the issue was found. |
| firstdetected | Date when the issue was first detected |
| firstsnapshot | Snapshot when the issue was first committed. |
| firstdate | Date of snapshot when the issue was first committed. |
| firstdesc | Description of snapshot when the issue was first committed. |
| firststream | Stream in which the issue was first detected. |
| firsttarget | Target platform of the snapshot in which the issue was first detected. |
| firstversion | Version number of the snapshot in which the issue was first detected. |
| fixtarget | Target milestone for fixing the issue. |
| function | The name of the function where the issue is located. |
| functionmerge | Internal function name used as one of the criteria for merging separate occurrences of the same software issue, with the result that they are identified by the same CID. |
| impact | Issue impact as determined by Coverity Connect: High, Medium, Low, or Audit. |
| lastsnapshot | Snapshot where the issue was last detected. |
| lastdate | Date when the issue was last detected. |
| lastdesc | Description of the snapshot in which the issue was last detected. |
| laststream | Stream in which the issue was last detected. |
| lasttarget | Target platform of the snapshot in which the issue was last detected. |
| lastversion | Version number of the snapshot in which the issue was last detected. |
| lasttriaged | Date when the issue was most recently triaged. |
| legacy | The Legacy attribute of the issue. |
| line | Line number on which the issue is found |
| mergekey | Internal signature used to merge separate occurrences of the same software issue and identify them all by the same CID. |
| mergeextra | Internal property used as one of the criteria for merging occurrences of an issue. |
| username | The username of the owner of the issue. |
| owner | The first name and last name of the owner of the issue. |
| severity | Severity of the issue. |
| status | Issue status. |
| type | Type of issue. |
| url | URL to CID of issue. |

Figure 1. Add static mapping
  
 [image: image]
