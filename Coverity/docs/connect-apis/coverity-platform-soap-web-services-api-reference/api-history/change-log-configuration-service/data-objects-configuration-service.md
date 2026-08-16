---
title: "Data objects: Configuration Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/data-objects-configuration-service.html"
content_id: "j1W4_hNrNu~vuuPI3bEI2g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:25.320227+00:00"
---

# Data objects: Configuration Service

Change log for data objects in the **Configuration Service**. Changes to *fields*
are logged from v6 through the latest version only. Field modifications in earlier
versions are not logged at this time. Note that v7 of the API has changed between
Coverity Connect versions 6.5.1 and 6.6. The v7 values in the table make this
distinction by using *v7 (6.6)* and *v7 (6.5.1)*.

| Data Object | Introduced | Modified | Removed | Notes |
| --- | --- | --- | --- | --- |
| attributeDefinitionDataObj | v4 |  |  |  |
| attributeDefinitionIdDataObj | v4 |  |  |  |
| attributeDefinitionSpecDataObj | v4 |  |  |  |
| attributeValueChangeSpecDataObj | v4 |  |  |  |
| attributeValueDataObj | v4 | v7 (6.5.1) |  | v7 (new fields): issueKindList |
| attributeValueIdDataObj | v4 |  |  |  |
| attributeValueSpecDataObj | v4 |  |  |  |
| checkerPropertyDataObj | v4 |  | v9 | REMOVED |
| checkerPropertyFilterSpecDataObj | v4 |  | v9 | REMOVED |
| checkerSubcategoryIdDataObj | v4 |  |  |  |
| commitStateDataObj | v5 |  |  |  |
| componentDataObj | < or = v3 |  | v7 (6.5.1) | v7 (new fields): roleAssignments (a roleAssignmentDataObj) v7 (removed fields): groupPermissions (a groupPermissionsDataObj) |
| componentDefectRuleDataObj | < or = v3 |  |  |  |
| componentIdDataObj | < or = v3 |  |  |  |
| componentMapDataObj | < or = v3 |  |  |  |
| componentMapFilterSpecDataObj | < or = v3 |  |  |  |
| componentMapIdDataObj | < or = v3 |  |  |  |
| componentMapSpecDataObj | < or = v3 |  |  |  |
| componentPathRuleDataObj | < or = v3 |  |  |  |
| configurationDataObj | v4 | v7, v9 |  | v7 (removed fields): groupPermissions (a groupPermissionsDataObj) v9 (new field): issueExportUrl |
| deleteSnapshotJobInfoDataObj | v7 |  |  | v7 (fields): snapshotId, status |
| featureUpdateTimeDataObj | v6 |  |  |  |
| groupDataObj | < or = v3 | v6 |  | Appeared v3 Configuration and Admin Service. v6: domainName field renamed *domain* |
| groupFilterSpecDataObj | < or = v3 |  |  |  |
| groupIdDataObj | < or = v3 | v7 (6.6) |  | Appeared in v3 Configuration and Admin Service. New field in v7 (6.6): displayName |
| groupPermissionDataObj | < or = v3 |  | v7 (6.5.1) | REMOVED. Contained the groupId and groupRole fields. |
| groupsPageDataObj | < or = v3 |  |  | Introduced in Admin Service. |
| groupSpecDataObj | < or = v3 | v6 |  | Introduced in Admin Service. v6: domainName field renamed *domain* |
| ldapConfigurationDataObj | v7 (6.6) |  |  |  |
| ldapConfigurationSpecDataObj | v7 (6.6) |  |  |  |
| licenseStateDataObj | v5 |  |  |  |
| localizedValueDataObj | v9 |  |  | displayName, name |
| pageSpecDataObj | < or = v3 |  |  | Introduced in Admin Service. |
| permissionDataObj | v4 |  |  |  |
| projectDataObj | < or = v3 | v6 |  | v6 (removed fields): defaultTriageScope |
| projectFilterSpecDataObj | < or = v3 | v7 (6.6) |  | New field in v7 (6.6): includeChildren, includeStreams |
| projectIdDataObj | < or = v3 |  |  |  |
| projectFilterSpecDataObj | < or = v3 | v6 |  | v6 (removed fields): defaultTriageScope |
| projectIdDataObj | < or = v3 |  |  |  |
| projectSpecDataObj | < or = v3 |  |  |  |
| roleAssignmentDataObj | v4 |  |  |  |
| roleDataObj | < or = v3 |  |  | Introduced in Admin Service. |
| roleIdDataObj | v4 |  |  |  |
| roleSpecDataObj | v4 |  |  |  |
| serverDomainIdDataObj | v4 |  |  |  |
| signInSettingsDataObj |  | v8 (8.7.0) |  | v8 (8.7.0): Added authenticationMethod field. |
|  |  | v9 |  | Removed `enableSessionTimeoout` parameter. |
| snapshotFilterSpecDataObj | < or = v3 | v8 (7.5) |  | v8 (7.5). New fields: hasSummaries, lastBeforeCodeVersionDate |
| snapshotIdDataObj | < or = v3 |  |  |  |
| snapshotInfoDataObj | < or = v3 | v6, v8 (7.0) |  | v8 (7.0) typo fix: Misspelled field name aysisIntermediateDir is now analysisIntermediateDir |
| snapshotPurgeDetailsObj | v7 (6.6) |  |  |  |
| standardAttributeDataObj | v9 |  |  |  |
| standardAttributeIdDataObj | v9 |  |  |  |
| standardAttributeValueDataObj | v9 |  |  |  |
| standardAttributeValueIdDataObj | v9 |  |  |  |
| streamDataObj | < or = v3 |  |  | v6 (new fields): autoDeleteOnExpiry |
| streamFilterSpecDataObj | < or = v3 |  |  |  |
| streamIdDataObj | < or = v3 |  |  |  |
| streamSpecDataObj | < or = v3 | v6, v7 (6.6), v8 (7.5) |  | v8 (7.5): New fields: enableDesktopAnalysis, summaryExpirationDays, analysisVersionOverride, pluginVersionOverride, versionMismatchMessage v6 (new fields): autoDeleteOnExpiry New field in v7 (6.6): allowCommitWithoutPassword |
| triageStoreDataObj | v5 | v7 (6.5.1) |  | v7 (new fields): streamIds |
| triageStoreFilterSpecDataObj | v5 | v7 (6.6) |  | New field in v7 (6.6): roleAssignments |
| triageStoreIdDataObj | v5 | v7 (6.6) |  | New field in v7 (6.6): roleAssignments |
| triageStoreSpecDataObj | v5 |  |  |  |
| userDataObj | < or = v3 | v6 |  | Introduced in Admin Service. v6 (new fields): superUser |
| userFilterSpecDataObj | v4 | v7 (6.6) |  | New field in v7 (6.6): includeDetails |
| usersPageDataObj | < or = v3 |  |  | Introduced in Admin Service. |
| userSpecDataObj | < or = v3 |  |  | Introduced in Admin Service. |
| versionDataObj | v6 |  |  |  |
