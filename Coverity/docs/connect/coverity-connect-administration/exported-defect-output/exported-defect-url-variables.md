---
title: "Exported defect URL variables"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/exported-defect-url-variables.html"
content_id: "A40HgqDfwkIMiAzMDDD5oA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:52.546886+00:00"
---

# Exported defect URL variables

The following table lists and describes the variables supplied to your chosen URL
(specified in the cim.properties
export.issue.url property) when you click the
Export button.

If you have configured an export-defect-handler program to work with
your exported defect data, see Exported defect XML elements.

Table 1. Exported defect URL replacement strings

| Variable | Description |
| --- | --- |
| `{mergedDefectId}` | If the issue being shown has a numeric CID, its ASCII decimal representation; otherwise returns an empty string. |
| `{projectId}` | The ASCII decimal representation of the numeric project ID. |
| `{userName}` | The user name of the logged in user who presses Export. |
| `{userLdapDisplayName}` | If the logged in user is an LDAP user, the administrator-provided "display name" of the LDAP server; otherwise returns an empty string. |
| `{mergeKey}` | The merge key of the issue shown, as 32 hexadecimal characters in `[0-9a-f]`. |
| `{projectName}` | The name of the Coverity Connect project associated with the issue. |
