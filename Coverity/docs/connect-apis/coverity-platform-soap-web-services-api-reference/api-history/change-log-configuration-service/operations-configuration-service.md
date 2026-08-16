---
title: "Operations: Configuration Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operations-configuration-service.html"
content_id: "KfG5RI0Wn~Ng4m~xWBq0FQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:24.573199+00:00"
---

# Operations: Configuration Service

Change log for operations in the **Configuration Service**. Changes to
*fields* are logged from v6 through the latest version only. Field
modifications in earlier versions are not logged at this time. Note that v7 of the
API has changed between Coverity Connect versions 6.5.1 and 6.6. The v7 values in
the table make this distinction by using *v7 (6.6)* and *v7 (6.5.1)*.

| Configuration Operations | Introduced | Modified | Removed | Note |
| --- | --- | --- | --- | --- |
| getActions | < or = v3 |  | v4 | REMOVED. |
| copyStream | v4 | **v8 (7.5)**, v8 (7.0) |  | v8 (7.5): New return fields: enableDesktopAnalysis, summaryExpirationDays, analysisVersionOverride, pluginVersionOverride, versionMismatchMessage v8 (7.0): New return fiel outdated |
| createAttribute | v4 |  |  |  |
| createComponentMap | < or = v3 |  |  |  |
| createGroup | < or = v3 | v4 |  | Created in Admin Service. v4: Moved to Configuration service. |
| createLdapConfiguration | v7 (6.6) |  |  |  |
| createProject | v4 |  |  |  |
| createRole | v4 |  |  |  |
| createStream | v4 |  |  |  |
| createStreamInProject | v4 | v8 (7.0) |  | v8 (7.0) (new return field): outdated |
| createTriageStore | v5 |  |  |  |
| createUser | < or = v3 | v4 |  | Created in Admin Service. v4: Moved to Configuration service. |
| deleteAttribute | v4 |  |  |  |
| deleteComponentMap | v4 |  |  |  |
| deleteGroup | < or = v3 | v4 |  | Created in Admin Service. v4: Moved to Configuration service. |
| deleteLdapConfiguration | v7 (6.6) |  |  |  |
| deleteProject | v4 |  |  |  |
| deleteRole | v4 |  |  |  |
| deleteSnapshot | v4 |  |  |  |
| deleteStream | v4 | v6 |  | v6 (new fields): onlyIfEmpty |
| deleteTriageStore | v5 |  |  |  |
| deleteUser | < or = v3 | v4 |  | Created in Admin Service. v4: Moved to Configuration service. |
| executeNotification | v7 (6.6) |  |  |  |
| getAllDomains | v4 |  | v5 | REMOVED. |
| getAllGroups | < or = v3 | v4 | v4 | REMOVED/RENAMED. Created in Admin Service. v4: Renamed getGroups |
| getAllIntegrityControlPermissions | v5 |  | v7 (6.6) | REMOVED. |
| getAllLdapConfigurations | v7 (6.6) |  |  |  |
| getAllPermissions | v4 |  |  |  |
| getAllRoles | < or = v3 | v4 |  | Created in Admin Service. v4: Moved to Configuration service. |
| getArchitectureAnalysisConfiguration | v8 (7.5) |  | v9 (2023.6.0) | REMOVED. |
| getAssignableUsers | < or = v3 |  | v4 | REMOVED. |
| getAttribute | v4 |  |  |  |
| getAttributes | v4 |  |  |  |
| getBackupConfiguration | v8 (7.0) |  |  | New in v8 (7.0). |
| getCategoryNames | v9 |  |  |  |
| getCheckerNames | v9 |  |  |  |
| getCheckerProperties | v4 |  | v9 | REMOVED. The Defect Service, getStreamDefects, replaces getCheckerProperties.getStreamDefects returns the DefectInstanceDataObj, which contains all necessary checker properties.The other potential use case for getCheckerProperties was to receive a list of all categories, types, and checker names available for filtering. This can be accomplished with the following operations: getCategoryNames, getCheckerNames, getTypeNames |
| getClassifications | < or = v3 |  | v4 | REMOVED. |
| getCommitState | v5 |  |  |  |
| getComponent | v4 |  |  |  |
| getComponentMaps | v4 |  |  |  |
| getDefectStatuses | v4 |  |  |  |
| getDeleteSnapshotJobInfo | v7 (6.5.1) |  |  | v7 (new fields): snapshotId v7 (new response):getDeleteSnapshotJobInfoResponse |
| getDeveloperStreamsProjects | v8 |  |  |  |
| getGroup | < or = v3 | v4 |  | Created in Admin Service. v4: Moved to Configuration service. |
| getGroups | v4 |  |  | Replaced getAllGroups. |
| getLastUpdateTimes | v6 |  | v9 | REMOVED. |
| getLdapServerDomains | v6 |  |  |  |
| getLicenseConfiguration | v8 (7.0) |  |  | New in v8 (7.0). |
| getLicenseState | v5 |  |  |  |
| getLoggingConfiguration | v8 (7.0) |  |  | New in v8 (7.0). |
| getMessageOfTheDay | v5 |  |  |  |
| getProjects | v4 |  |  |  |
| getRole | v4 |  |  |  |
| getServerTime | < or = v3 | v4 |  | Created in Admin Service. v4: Moved to Configuration service. |
| getSeverities | < or = v3 |  | v4 | REMOVED. |
| getSignInConfiguration | v8 (7.0) |  |  | New in v8 (7.0). |
| getSkeletonizationConfiguration | v8 (7.0) |  |  | New in v8 (7.0). |
| getSnapshotInformation | v4 | **v8 (7.5)** |  | v8 (7.5): New return fields: portableAnalysisSettings, codeVersionDate, hasSummaries |
| getSnapshotPurgeDetails | v7 (6.5.1), v7(6.6) | v8 (7.0) |  | Deprecated in v8 (7.0):Use getSkeletonizationConfiguration() instead. First documented in v7 (6.6) but first available in the WSDL file for the 6.5.1 release. |
| getSnapshotsForStream | v4 |  |  |  |
| getStandardAttribute | v9 |  |  |  |
| getStandardAttributes | v9 |  |  |  |
| getStreams | v4 | v8 (7.0), **v8 (7.5)** |  | v8 (7.5): New return fields: enableDesktopAnalysis, summaryExpirationDays, analysisVersionOverride, pluginVersionOverride, versionMismatchMessage v8 (7.0): New return fiel outdated |
| getSystemConfig | v4 |  |  |  |
| getTriageStores | v5 |  |  |  |
| getTypeNames | v9 |  |  |  |
| getUser | < or = v3 | v4 |  | Created in Admin Service. v4: Moved to Configuration service. |
| getUsers | v4 |  |  | Replaced getUsersForGroup. |
| getUsersForGroup | < or = v3 | v4 | v4 | REMOVED/REPLACED. Created in Admin Service. v4: Replaced by getUsers in v4. |
| getVersion | v6 |  |  |  |
| importLicense | v8 (7.0) |  |  | New in v8 (7.0).Passes v8 licenseSpecDataObj. |
| notify | < or = v3 | v4 |  | Created in Admin Service. v4: Moved to Configuration service. |
| purgeSnapshotDetails | v7 (6.5.1) | v7 (6.6) |  | v7 (6.6): snapshotId field removed.First documented in v7 (6.6) but first available in the WSDL file for the 6.5.1 release. **Deprecated** in v8 (7.0).Use getSkeletonizationConfiguration() instead. |
| setAcceptingNewCommits | v5 |  |  |  |
| setArchitectureAnalysisConfiguration | v8 (7.5) |  | v9 (2023.6.0) | REMOVED. |
| setBackupConfiguration | v8 (7.0) |  |  | New in v8 (7.0).Passes v8 backupConfigurationDataObj. |
| setLoggingConfiguration | v8 (7.0) |  |  | New in v8 (7.0). Passes v8 loggingConfigurationDataObj. |
| setMessageOfTheDay | v5 | v7 (6.5.1) |  | v7 (new field name): *message* replaces *arg0* |
| setSkeletonizationConfiguration | v8 (7.0) |  |  | New in v8 (7.0). Replaces setSnapshotPurgeDetails(). Passes v8 signInSettingsDataObj. |
| setSnapshotPurgeDetails | v7 (6.6) | v8 (7.0) |  | Deprecated in v8 (7.0). Use setSkeletonizationConfiguration() instead. |
| updateActions | < or = v3 |  | v4 | REMOVED. |
| updateAttribute | v4 |  |  |  |
| updateComponentMap | v4 |  |  |  |
| updateGroup | v4 |  |  |  |
| updateLdapConfiguration | v7 (6.6) |  |  |  |
| updateProject | v4 |  |  |  |
| updateRole | v4 |  |  |  |
| updateSeverities | < or = v3 |  | v4 | REMOVED. |
| updateSignInConfiguration |  | v8 (8.7.0) |  | v8 (8.7.0): Added signInSettingsDataObj.authenticationMethod |
|  |  | v9 |  | Removed enableSessionTimeout parameter. |
| updateSnapshotInfo | v6 |  |  |  |
| updateStream | v4 | v8 (7.0) |  | v8 (7.0) (new return field): outdated |
| updateTriageStore | v5 |  |  |  |
| updateUser | v5 |  |  |  |
