---
title: "Migrating from the SOAP API to the REST Web Services API"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/migrating-from-the-soap-api-to-the-rest-web-services-api.html"
content_id: "KvP_MegWzEESyq9yg~sIOQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:29.668954+00:00"
---

# Migrating from the SOAP API to the REST Web Services API

The Coverity Platform SOAP API has been deprecated, and support for it will
be discontinued in a future relesae of Coverity.
If you use the SOAP API, we recommend that you begin migrating to the REST API as soon as possible.

Use the tables that follow as guides to migrating your SOAP API code into the REST interface.

Note:
If you identify a SOAP API feature that does not have equivalent functionality in the REST API,
[and is not listed here [QUERY: NEEDED? -RC 16 May 2025]], please open a Support case by going to
<https://community.blackduck.com/s/contactsupport>.
Create a Community account if you don’t already have one.

## SOAP Operations that *do not* have an associated endpoint in the REST API

- `getLicenseState`
- `notify`
- `getMergedDefectHistory`
- `updateDefectInstanceProperties`

  Note:
  The SOAP API guide says not to use this operation,
  but it still lists it.
- `updateStreamDefects`

## Operations for configuration services

Table 1. SOAP operations and associated REST operations

| SOAP operation | Associated REST endpoint | Swagger category | Version |
| --- | --- | --- | --- |
| `copyStream` | POST `/api/v2/streams/<name>` | Streams | 2021.06 |
| `createAttribute` | POST `/api/v2/attributes` | Triage Attributes | 2022.3.0 |
| `createComponentMap` | POST `/api/v2/componentMaps` | Component Maps | 2022.3.0 |
| `createGroup` | POST `/api/v2/groups` | User Groups | 2021.9.0 |
| `createLdapConfiguration` | POST `/api/v2/ldapConfigurations` | LDAP Configurations | 2021.9.0 |
| `createProject` | POST /api/v2/projects | Projects | 2021.06 |
| `createRole` | POST `/api/v2/roles` | Roles | 2021.9.0 |
| `createStream` | POST `/api/v2/streams` | Streams | 2021.06 |
| `createStreamInProject` | POST `/api/v2/streams` | Streams | 2021.06 |
| `createTriageStore` | POST `/api/v2/triageStores` | Triage Stores | 2021.12 |
| `createUser` | POST `/api/v2/users` | Users | 2021.9.0 |
| `deleteAttribute` | DELETE `/api/v2/attributes/<name>` | Triage Attributes | 2022.3.0 |
| `deleteComponentMap` | DELETE `/api/v2/componentMaps/<name>` | Component Maps | 2022.3.0 |
| `deleteGroup` | DELETE `/api/v2/groups/<name>` | User Groups | 2021.9.0 |
| `deleteLdapConfiguration` | DELETE `/api/v2/ldapConfigurations/<name>` | LDAP Configurations | 2021.9.0 |
| `deleteProject` | DELETE `/api/v2/projects/<name>` | Projects | 2021.06 |
| `deleteRole` | DELETE `/api/v2/roles/<name>` | Roles |  |
| `deleteSnapshot` | DELETE `/api/v2/snapshots/<id>` | Snapshots | 2021.12.0 |
| `deleteStream` | DELETE `/api/v2/<name>` | Streams | 2021.06 |
| `deleteTriageStore` | DELETE `/api/v2/triageStores/<name>` | Triage Stores | 2021.12.0 |
| `deleteUser` | DELETE `/api/v2/users/<name>` | Users | 2021.9.0 |
| `executeNotification` | POST `/api/v2/emailNotifications/view/<viewName>` | Email Notifications |  |
| `getAllLdapConfigurations` | GET `/api/v2/ldapConfigurations` | LDAP Configurations | 2021.9.0 |
| `getAllPermissions` | GET `/api/v2/permissions` | Permissions | 2021.9.0 |
| `getAllRoles` | GET `/api/v2/roles` | Roles | 2021.9.0 |
| `getAttribute` | GET `/api/v2/attributes/<name>` | Triage Attributes |  |
| `getAttributes` | GET `/api/v2/attributes` | Triage Attributes | 2022.3.0 |
| `getBackupConfiguration` | GET `/api/v2/maintenance/backupConfiguration` | Maintenance | 2022.9 |
| `getCategoryNames` | GET `/api/v2/checkerAttributes/<name>` | Checker Attributes | 2022.9 |
| `getCheckerNames` | GET `/api/v2/checkerAttributes/<name>` | Checker Attributes | 2022.9 |
| `getCommitState` | GET `/api/v2/commitGate/commitState` | Commit Gate | 2022.9 |
| `getComponent` | GET `/api/v2/components/<name>` | Components | 2022.3.0 |
| `getComponentMaps` | GET `/api/v2/componentMaps` | Component Maps | 2022.3.0 |
| `getDefectStatuses` | GET `/api/v2/issueAttributes/status` | Issue Attributes | 2022.9.0 |
| `getDeleteSnapshotJobInfo` | GET `/api/v2/snapshots/status/<id>` | Snapshots | 2021.12.0 |
| `getDeveloperStreamsProjects` | GET `/api/v2/projects/developerStreams` | Projects | 2021.06 |
| `getGroup` | GET `/api/v2/groups/<name>` | User Groups | 2021.9 |
| `getGroups` | GET `/api/v2/groups` | User Groups | 2021.9 |
| `getLdapServerDomains` | GET `/api/v2/ldapConfigurations/serverDomains` | LDAP Configurations | 2021.9 |
| `getLicenseConfiguration` | GET `/api/v2/licenses/configuration` | Licenses | 2021.12 |
| `getLicenseState` | N/A | - | -0 |
| `getLoggingConfiguration` | GET `/api/v2/loggingConfiguration` | Logging Configuration | 2022.9 |
| `getMessageOfTheDay` | GET `/api/v2/serverInfo/messageOfTheDay` | Server Information | 2022.9 |
| `getOutputFileForSnapshot` | GET `/api/v2/snapshots/{id}/outputFile/<fileName>` | Snapshots | 2021.12.0 |
| `getProjects` | GET `/api/v2/projects` | Projects | 2021.06 |
| `getRole` | GET `/api/v2/roles/<name<` | Roles | 2021.9.0 |
| `getServerTime` | GET `/api/v2/serverInfo/time` | Server Information | 2022.6.0 |
| `getSignInConfiguration` | GET `/api/v2/signInConfigurations` | Sign-In Configurations | 2021.9.0 |
| `getSkeletonizationConfiguration` | GET `/api/v2/maintenance/purgeAnalysisSummaries` | Maintenance | 2021.12.0 |
| `getSnapshotInformation` | GET `/api/v2/snapshots/<id>` | Snapshots | 2021.12.0 |
| `getSnapshotPurgeDetails` | Deprecated/removed in SOAP version 8. | | |
| `getSnapshotsForStream` | GET `/api/v2/streams/stream/snapshots` | Streams | 2021.12.0 |
| `getStandardAttribute` | GET `/api/v2/standardAttributes/<name>` | Standard Attributes | 2022.3.0 |
| `getStandardAttributes` | GET `/api/v2/standardAttributes` | Standard Attributes | 2022.3.0 |
| `getStreams` | GET `/api/v2/streams` | Streams | 2021.06 |
| `getSystemConfig` | GET `/api/v2/serverInfo/config` | Server Information | 2022.6 |
| `getTriageStores` | GET `/api/v2/triageStores/<name>` | Triage Stores | 2021.12.0 |
| `getTypeNames` | GET `/api/v2/checkerAttributes/<name>` | Checker Attributes | 2022.9 |
| `getUser` | GET `/api/v2/users/<name>` | Users | 2021.9.0 |
| `getUsers` | GET /api/v2/users | Users | 2021.9.0 |
| `getVersion` | GET `/api/v2/serverInfo/version` | Server Information | 2022.6.0 |
| `importLicense` | POST `/api/v2/licenses` | Licenses | 2021.12.0 |
| `notify` | N/A | - | - |
| `refreshLdapGroup` | POST `/api/v2/ldapConfigurations/refreshGroup` | LDAP Configurations | 2021.9.0 |
| `setAcceptingNewCommits` | PUT `/api/v2/commitGate/commitState` | Commit Gate | 2022.9.0 |
| `setBackupConfiguration` | PUT `/api/v2/maintenance/backupConfiguration` | Maintenance | 2022.9.0 |
| `setLoggingConfiguration` | PUT `/api/v2/loggingConfiguration` | Logging Configuration | 2022.9.0 |
| `setMessageOfTheDay` | PUT `/api/v2/serverInfo/messageOfTheDay` | Server Information | 2022.9.0 |
| `setSkeletonizationConfiguration` | PUT `/api/v2/maintenance/purgeAnalysisSummaries` | Maintenance | 2021.12.0 |
| `setSnapshotPurgeDetails` | Deprecated/removed in SOAP version 8. | | |
| `updateAttribute` | PUT `/api/v2/attributes/<name>` | Triage Attributes | 2022.3.0 |
| `updateComponentMap` | PUT `PUT /api/v2/componentMaps/<name>` | Component Maps | 2022.3.0 |
| `updateGroup` | PUT `/api/v2/groups/<name>` | User Groups | 2021.9.0 |
| `updateLdapConfiguration` | PUT `/api/v2/ldapConfigurations/<name>` | LDAP Configurations | 2021.9.0 |
| `updateProject` | PUT `/api/v2/projects/<name>` | Projects |  |
| `updateRole` | PUT `/api/v2/roles/<name>` | Roles | 2021.9.0 |
| `updateSignInConfiguration` | PUT `/api/v2/signInConfigurations` | Sign-In Configurations | 2021.9.0 |
| `updateSnapshotInfo` | PUT `/api/v2/snapshots/<id>` | Snapshots | 2021.12.0 |
| `updateStream` | PUT `/api/v2/streams/<name>` | Streams | 2021.06 |
| `updateTriageStore` | PUT `/api/v2/triageStores/<name>` | Triage Stores | 2021.12.0 |
| `updateUser` | PUT `/api/v2/users/<name>` | Users | 2021.9.0 |

## Operations for defect services

Table 2. SOAP operations and associated REST operations

| SOAP operation | Associated REST endpoint | Swagger category | Version |
| --- | --- | --- | --- |
| `getComponentMetricsForProject` | GET `/api/v2/projects/<name>/componentMetrics` | Projects | 2022.9.0 |
| `getFileContents` | POST `/files/file/contents` | Files | 2025.6 |
| `getMergedDefectDetectionHistory` | GET `/api/v2/issues/detectionHistory` | Issues | 2022.6.0 |
| `getMergedDefectHistory` | N/A | - | - |
| `getMergedDefectsForProjectScope` | POST `/api/v2/issues/search` | Issues | 2021.03 |
| `getMergedDefectsForSnapshotScope` | POST `POST /api/v2/issues/search` | Issues | 2021.03 |
| `getMergedDefectsForStreams` | POST `/api/v2/issues/search` | Issues | 2021.03 |
| `getStreamDefects` | GET `/api/v2/issues/sourceCodeInfo` | Issues | 2023.9.0 |
| `getStreamDefects` | POST `/api/v2/issues/sourceCodeInfo/search` POST `/api/v2/issues/triageHistory/search` | Issues | 2025.6.0 |
| `getTrendRecordsForProject` | GET `/api/v2/projects/<name>/trendRecords` | Projects | 2022.9.0 |
| `getTriageHistory` | GET `/api/v2/issues/triageHistory` | Issues | 2022.6.0 |
| `updateDefectInstanceProperties` | DO NOT USE | - | - |
| `updateStreamDefects` | N/A | - | - |
| `updateTriageForCIDsInTriageStore` | PUT `/api/v2/issues/triage` | Issues | 2022.6.0 |
