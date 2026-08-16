---
title: "Operations: Configuration Service"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operations-configuration-service.html"
content_id: "UT_KCCJnvG6PkUkg_qXASg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:22.754539+00:00"
---

# Operations: Configuration Service

## Description

Operations in the Configuration service.

## Operations

| Name | Description |
| --- | --- |
| copyStream | Make a copy of a stream. Does not copy stream role assignments. |
| createAttribute | Create an attribute. |
| createComponentMap | Create a component map with or without one or more components. |
| createGroup | Create a user group. |
| createLdapConfiguration | Create an LDAP configuration for users and groups. |
| createProject | Create a project. |
| createRole | Create a role. |
| createStream | Create a stream that is not associated with any project. The new stream will appear in the UI as one of the *Other Streams*. |
| createStreamInProject | Create a stream in a specified project. |
| createTriageStore | Create a triage store. |
| createUser | Create a user. |
| deleteAttribute | Delete an attribute. |
| deleteComponentMap | Delete a component map. |
| deleteGroup | Delete a user group. |
| deleteLdapConfiguration | Delete an LDAP configuration. |
| deleteProject | Delete a project. |
| deleteRole | Delete a role. |
| deleteSnapshot | Delete a snapshot. |
| deleteStream | Delete a stream. |
| deleteTriageStore | Delete a triage store to which no streams are associated. |
| deleteUser | Delete a user. |
| executeNotification | Initiates a view notification to preconfigured recipients. The view must belong to the user who calls this operation. |
| getAllLdapConfigurations | Retrieve all LDAP configurations. |
| getAllPermissions | Retrieve the complete list of permissions that can be associated with a role. |
| getAllRoles | Retrieve a list of all roles. |
| getAttribute | Retrieve the properties of a specified attribute. |
| getAttributes | Retrieve a list of all attributes. |
| getBackupConfiguration | Retrieve the schedule for automated backup of the Coverity Connect database. |
| getCategoryNames | Retrieve all known checker category names, as localizedValueDataObj. |
| getCheckerNames | Retrieve all known checker names. |
| getCommitState | Find out whether the database will accept new commits of analysis results. |
| getComponent | Retrieve the properties of a component. |
| getComponentMaps | Retrieve a list of component maps that matches a component name pattern. |
| getDefectStatuses | Retrieve the list of Status attribute values that can be associated with a software issue. |
| getDeleteSnapshotJobInfo | Find out whether a snapshot deletion process succeeded. |
| getDeveloperStreamsProjects | Get a list of project specifications in developer streams (for all such projects or for a filtered set of such projects). |
| getGroup | Retrieve the properties of a user group. |
| getGroups | Get a list of groups. |
| getLdapServerDomains | Retrieves the host name or host IP of one or more LDAP servers. |
| getLicenseConfiguration | Retrieve details on your Coverity Connect license. |
| getLicenseState | Find out whether Coverity Desktop analysis is enabled through your license. |
| getLoggingConfiguration | Retrieve information about your current Coverity Connect configurations for logging. |
| getMessageOfTheDay | Get the message of the day. |
| getOutputFileForSnapshot | Get a specified output file for a specified snapshot. |
| getProjects | Get a list of project specifications (for all projects or for a filtered set of projects). |
| getRole | Retrieve the properties of a role, including its associated permissions. |
| getServerTime | Retrieves the current date and time from the server. |
| getSignInConfiguration | Retrieve sign-in settings. These configurations are identical to Sign In Settings (a set of System Configuration settings) in the Coverity Connect UI. |
| getSkeletonizationConfiguration | Retrieve the configuration for the process that purges snapshot details. Purging these details can help you reduce and maintain the database size. |
| getSnapshotInformation | Retrieve information about a snapshot in a stream. |
| getSnapshotPurgeDetails | **Deprecated in v8**: Use getSkeletonizationConfiguration() instead to retrieve the configuration for the process that purges snapshot details. Purging these details can help you reduce and maintain the database size. |
| getSnapshotsForStream | Retrieve a set of snapshots that belong to a specified stream. |
| getStandardAttribute | Retrieve the properties of a specified standard attribute. |
| getStandardAttributes | Retrieve a list of all standard attributes. |
| getStreams | Retrieve a set of streams. |
| getSystemConfig | Retrieves system configuration properties, including properties of the database with which this API communicates. |
| getTriageStores | Retrieve a set of triage store specifications, including stream associations. |
| getTypeNames | Returns a list of all known defect types, as localizedValueDataObj. |
| getUser | Retrieve a user by user name. |
| getUsers | Get users (filtered or unfiltered). |
| getVersion | Retrieve the version of Coverity Connect. |
| importLicense | Import your Coverity Connect license file, license.dat. |
| notify | Send an email notification to a specified user. |
| refreshLdapGroup | Refresh an LDAP group. |
| setAcceptingNewCommits | Control whether the database will accept new commits of analysis results. |
| setBackupConfiguration | Set a schedule for automated backup of the Coverity Connect database. The name of the backup file looks something like the following: CIM.2013-12-04.10-35.backup |
| setLoggingConfiguration | Enable or disable logging options for Coverity Connect. Coverity Connect automatically logs system event information to the cim.log file. You can increase the amount of information that Coverity Connect records to this file by enabling additional logging options to work with Coverity Support on an issue. Coverity recommends that you leave all of the logging options disabled and only enable them by request from Coverity Support. |
| setMessageOfTheDay | Set the message of the day. (This does not create a visible message in the Coverity Connect GUI.) |
| setSkeletonizationConfiguration | Configure the process that purges snapshot details. Purging these details can help you reduce and maintain the database size. |
| setSnapshotPurgeDetails | **Deprecated in v8**: Use setSkeletonizationConfiguration() instead to configure the process that purges snapshot details. |
| updateAttribute | Update an attribute specification. |
| updateComponentMap | Update one or more properties of a component map. |
| updateGroup | Update a group specification. |
| updateLdapConfiguration | Update an LDAP configuration. |
| updateProject | Update a project specification. |
| updateRole | Update a role specification. |
| updateSignInConfiguration | Update sign-in settings. These configurations are identical to Sign In Settings (a set of System Configuration settings) in the Coverity Connect UI. |
| updateSnapshotInfo | Update a snapshot. |
| updateStream | Update a stream specification. |
| updateTriageStore | Update a triage store specification. |
| updateUser | Update a user specification. |
