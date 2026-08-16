---
title: "Exported defect XML elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/exported-defect-xml-elements.html"
content_id: "9iu2983m1EcpSnF7JXvv~Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:53.264728+00:00"
---

# Exported defect XML elements

The following table lists and describes the elements contained in the XML file that is
produced when you use the Export button in the Defect Listing
pane. The XML file is saved to the following location:

<install_dir>/server/base/temp/

Because a defect can exist in multiple streams, and can be in different states, the XML
file displays the merged state information, as well as the state information for each
stream in which the defect exists.

Table 1. Exported defect XML elements

| Element | Description |
| --- | --- |
| cxp:exportedDefect | Root element of the XML file containing a single exported (merged) defect. |
| user | The name of the user that exported the defect XML file. |
| ldapDomain | The LDAP domain of the user that exported the defect XML file. If the user is local, the LDAP domain will also be `local`. |
| project | The name of the project that contains the exported defect. |
| timeStamp | The date and time that the defect export file was created. |
| cxp:mergedDefect | Container element that represents the merged defect. |
| checkerName | The name of the checker that found this defect. |
| checkerSubcategory | The sub-category of the defect reported by checkerName. |
| cid | The CID (Coverity ID) of this defect. |
| componentName | The map and name of the component, joined by a period, that contains this defect. If the defect is in multiple components, the name is `Various`. |
| defectStateAttributeValues | The name and value an assigned defect attribute. This element contains the following child elements: |
| attributeDefinitionId | The name of the attribute, inside <name> tags. |
| attributeValueId | The value of the given attribute, inside <name> tags. |
| domain | The type of analysis performed to find this defect: static C/C++, static C#, static Java, or dynamic. |
| filePathname | The complete path to the file that contains the defect. |
| firstDetected | The date and time in which the defect was first detected by the analysis. |
| firstDetectedSnapshotId | The snapshot in which the defect was first detected. |
| functionDisplayName | The name of the function that contains the defect. |
| lastDetected | The date and time in which the analysis most recently detected the defect. |
| lastDetectedSnapshotId | The most recent snapshot containing the defect. This is the same value as in latestSnapshotId. |
| mergeKey | A unique identifier that maps a CID across multiple projects or Coverity Connect instances. |
| occurrenceCount | The number of streams where the defect is found. |
| latestSnapshotId | The most recent snapshot containing the defect. This is the same value as in lastDetectedSnapshotId. |
| streamDefects | Container element that represents the occurrences of this CID in all streams within the project. |
| cxp:streamDefect | Container element that represents a single stream defect. |
| checkerSubcategoryId | The sub-category of this defect within the class of defects that are discoverable by the checker reported in the checker element. |
| subcategory | The sub-category of the defect reported by the checker. |
| checkerName | The name of the checker that caught this defect. |
| domain | The type of analysis performed to find this defect: static C/C++, static C#, static Java, or dynamic. |
| subcategory | The sub-category of the defect reported by the checker. |
| cid | The CID (Coverity ID) of this defect. |
| id | The identification container for information identifying the stream defect. |
| defectTriageId | Internal reference to latest triage ID. |
| defectTriageVerNum | The version number of the latest triage. |
| id | The ID of this stream defect. |
| verNum | An internal field used to prevent data corruption. |
| streamId | The name of the stream containing the stream defect, inside <name> tags. |
