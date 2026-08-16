---
title: "Enhanced usage logging"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enhanced-usage-logging.html"
content_id: "xxxp4EBi3ofAwkj__suyfw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:02.918376+00:00"
---

# Enhanced usage logging

Coverity Connect records events related to user activity in usage logs. In the 8.6
release, Coverity Connect adds additional logging entries focused on user events such as
changing user preferences, viewing source files and issues, creating users, and logging
in to Coverity Connect.

Events are recorded as JSON-formatted log entries. Each event is recorded on a single
line of the machine-readable log file. Log files are stored in the Coverity Connect logs
directory. Each log file contains one day's worth of logging, based on the local time
zone. Customers may write programs that consume these log files.

The system administrator is responsible for deleting log files as needed. Usage logging
is always enabled; there is no provision to turn it off.

The formats of some of the values in the JSON key:value pairs are given in the following
table.

Table 1. Standard value formats

| Format name | Format | Example | Notes |
| --- | --- | --- | --- |
| `datetime` | UTC | `2022-09-05T19:15:59.629+0000` | Date and time. |
| `username` | user@domain | `maribel@example` | A domain of *local* refers to a user whose repository is Coverity Connect. Domains other than *local* are names of LDAP domains. The `@domain` portion can be dropped: In this case, any customer program that consumes the log file should assume the domain to be `@local`. |
| `host` | IP address (IPv4 or IPv6) | `192.138.8.145` |  |
| `id` | non-negative number | `10014` | A low-level identifier for an object. |
| `filename` | An absolute or relative path, with directory names delimited by the slash character. | `path/to/a/file.cpp` |  |

Customer programs that consume the log files should ignore the following:

- unparsable lines
- unexpected types
- unexpected fields

Some pairs appear in every entry, as described in the following table. The "Value type"
column refers to a JSON type name.

Table 2. Standard pairs

| Name | Value type | Value format | Value example | Semantics |
| --- | --- | --- | --- | --- |
| `@type` | string |  | `LogInEvent` | Describes the semantics of the entry, including what name:value pairs will appear in it. |
| `timestamp` | string | datetime | `2016-07-08T17:20:39+​0000` | The time and date at which the event occurred. |
| `userId` | number | ID | `12` | Persistent, unique user ID of the user executing the operation. |
| `remoteHost` | string | host |  | IP address of the remote host from which the operation was initiated. |
| `ipv6` | Boolean |  | `false` | Should be `true` if `remoteHost` is an IPv6 address. |

The following events were added to Coverity Connect logging.

- Creation of a user. All user creations are logged.

  Table 3. UserCreatedEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `targetId` | number | ID | User ID of the new user. |
  | `userName` | string |  | The user name of the new user. |
- Deletion of a user. All user deletions, whether local or LDAP in origin, are
  logged.

  Table 4. UserDeletedEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `targetId` | number | ID | User ID of the deleted user. |
- Changing of a user's password.

  Table 5. UserPasswordChangeEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `targetId` | number | ID | User ID of the user whose password is being changed. |
- Change of a user's preference.

  Table 6. UserPreferenceChangeEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `setting` | string |  | Name of the user preference setting that was changed. |
- The user has changed the project scope for subsequent requests.

  Table 7. ProjectScopeChangeEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `projectName` | string |  | Name of the new project scope |
- The user has viewed a source file.

  Table 8. SourceFileViewedEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `filename` | string | file name | Name of the file viewed |
- The user has viewed an issue in the context of the source file in which it
  occurs. Note that other views of issues, such as tables, are not logged.

  Table 9. IssueViewedInSourceEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `cid` | number | CID | Identifier of the issue that was viewed |
  | `filename` | string | file name | Name of the file viewed |
- A session has been created for a user.

  Table 10. SessionCreatedEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `sessionId` | number | ID | Identifies the session |
- A session has been deleted.

  Table 11. SessionDeletedEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `sessionId` | number | ID | Identifies the session |
- Attempted user authentication.

  Table 12. LogInEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `userName` | string |  | The user name of the authenticated user. |
  | `protocol` | string | one of `"GUI"`, `"WS"`, `"commit"` | *GUI* means use of the Web UI. *WS* means use of Web Services. *commit* means use of the commit protocol. |
  | `logInSucceeded` | Boolean |  | `true` if the login was successful. |
  | `failureReason` | string |  | If the login failed, the reason for the failure. |
  | `authenticationSource` | string | `"LOCAL"` or `"LDAP"` or `"AUTHENTICATION_KEY"` | How the user authenticated. |
- Performance log event with metrics.

  Table 13. PerformanceLogEvent

  | Name | Value type | Value format | Value example | Semantics |
  | --- | --- | --- | --- | --- |
  | `@type` | string |  | `PerformanceLogEvent` | The semantics of the entry. |
  | `timestamp` | string | datetime | `2021-05-07T16:01:25.331+0000` | The time and date at which the event occurred. |
  | `level` | string |  | `INFO` | The log level which is generally specified in the code when writing out the log message (e.g. `INFO`, `WARN`, `ERROR`, etc) |
  | `hostname` | string |  |  | The name of the host for the currently running Coverity Connect server. |
  | `count` | int |  | `1` | Used for `IssueExportEvent` logging event types. |
  | `metrics` |  |  | See next table. | Statistical data returned by `PerformanceLogEvent`. |

  .The following table identifies metrics returned by
  `PerformanceLogEvent`.

  Table 14. PerformanceLogEvent metrics

  | Name | Value type | Value example | Semantics |
  | --- | --- | --- | --- |
  | `backUpInProgress` | number | `0. 0` | A value of `1.0` indicates that a backup is currently in progress. Otherwise a value of `0.0` is reported. |
  | `commitExecutorSize` | number | `5.0` | The maximum number of parallel commits that can be handled concurrently. |
  | `unixOneMinuteLoadAverage` | number | `18.0` | The system load average for the last minute. |
  | `cimCpuUsage` | number | `55.843336597332336` | The system wide CPU load. |
  | `memoryUsed` | number | `7.2692143744E10` | Approximation of currently free JVM memory in bytes subtracted from the total JVM memory. |
  | `webRequestsPerSecond` | number | `0.0` | The number of Coverity Connect HTTP/S requests handled per second for the UI (currently unused). |
  | `diskBytesRead` | number | `1.541250048E10` | The number of bytes read from all devices since the last measured value. |
  | `activeCommitCount` | number | `1.0` | The number of commit jobs that are currently being processed by Coverity Connect. |
  | `commitQueueSize` | number | `0.0` | The number of commit jobs that are waiting to be processed. |
  | `memoryTotal` | number | `1.57840048128E11` | The maximum number of bytes that the JVM will attempt to use. |
  | `wsRequestsPerSecond` | number | `0.0` | The number of Coverity Connect HTTP/S requests handled per second for the web services APIs (currently unused). |
  | `commitGateOpen` | number | `1.0` | A value of `1.0` indicates that commit jobs might be processed. A value of `0.0` indicates that the commit gate is closed and incoming commit jobs must wait until the gate is open. |
  | `diskBytesWritten` | number | `5.687561216E9` | The number of bytes written to all devices since last measured value. |
  | `skeletonizationInProgress` | number | `0.0` | A value of `1.0` indicates that the background snapshot purge process is in progress. |
- A new role is associated with an entity (project, stream, triage store, component
  map, or component), a user, or a group.

  Table 15. RoleAssignmentAddEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `entityID` | number | ID | Identifies the project, stream, triage store or component. |
  | `entityType` | string | one of `"project"`, `"stream"`, `"triageStore"`, `"component map"`, `"component"` | Type of entity to which the role is being added. |
  | `groupName` | string |  | Group to which the roles are being assigned. |
  | `roleAssignment` | string | ID | Role being assigned. |
  | `roleAssignments` | string | comma-separated list of role IDs | List of roles being assigned. |
  | `username` | string |  | User to whom the roles are assigned. |
- A check was done to verify that the current user is not attempting to modify
  their roles or permissions.

  Table 16. RoleAssignmentCheckSelfOperationEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `checkMessage` | string |  | Explanation about the outcome of a check operation. |
  | `currentUserId` | number | ID | User trying the role assignment change. |
  | `roleAssignment` | number | id | Role assignment being checked to forbid self-changes. |
  | `roleAssignments` | string | comma-separated list of role IDs | List of roles assignments being checked to forbid self-changes. |
  | `success` | Boolean |  | `true` if check succeeds. |
  | `targetUserId` | number | ID | User for which the role assignment change is attempted. |
- Global removal of role assignments.

  Table 17. RoleAssignmentGlobalRemoveEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `groupName` | string |  | Group from which the role assignment is being removed. |
  | `username` | string |  | User from whom the role assignment is being removed. |
- Removal of role assignments at the entity level.

  Table 18. RoleAssignmentRemoveEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `entityID` | number | ID | Identifies the project, stream, triage store, component map, or component. |
  | `entityType` | string |  | Type of entity from which the role is being removed. |
  | `groupName` | string |  | Group from which the entity role assignment is being removed. |
  | `roleAssignment` | string | ID | Role assignment being removed. |
  | `roleAssignments` | string | comma-separated list of role IDs | List of role assignment being removed. |
  | `username` | string |  | User from whom the role assignment is removed. |
- A new role was created.

  Table 19. RoleCreateEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `role` | string | JSON representation of the role:   ``` {     "roleId": <roleId>,     "name": <name>,     "description": <description>,     "permissions": [         <permission1>,         ... ,         <permissionN>     ] } ``` | Role being created. |
- An attempt to update a non-editable role was made.

  Table 20. RoleForbiddenUpdateAttemptEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `role` | string | JSON representation of the role:   ``` {     "roleId": <roleId>,     "name": <name>,     "description": <description>,     "permissions": [         <permission1>,         ... ,         <permissionN>     ] } ``` | Role on which the rejected attempt was made. |
- A role was updated.

  Table 21. RoleUpdateEvent

  | Name | Value type | Value format | Semantics |
  | --- | --- | --- | --- |
  | `role` | string | JSON representation of the role:   ``` {     "roleId": <roleId>,     "name": <name>,     "description": <description>,     "permissions": [         <permission1>,         ... ,         <permissionN>     ] } ``` | Role being updated: the state after update. |
- Log out event

  Table 22. LogOutEvent

  | Name | Value type | Value example | Semantics |
  | --- | --- | --- | --- |
  | level | string | INFO | The log level which is generally specified in the code when writing out the log message (e.g. `INFO`, `WARN`, `ERROR`, etc) |
  | count | number | 1 | Used for `IssueExportEvent` logging event types. |
  | protocol | string | GUI | *GUI* means use of the Web UI. *WS* means use of Web Services. *commit* means use of the commit protocol. |
  | authenticationSource | string | LOCAL | How the user authenticated: one of `"LOCAL"` or `"LDAP"` or `"AUTHENTICATION_KEY"` |
- Project event

  Table 23. Project Event

  | Name | Value type | Value example | Semantics |
  | --- | --- | --- | --- |
  | level | string | INFO | The log level which is generally specified in the code when writing out the log message (e.g. `INFO`, `WARN`, `ERROR`, etc) |
  | count | number | 1 | Used for `IssueExportEvent` logging event types. |
  | action | string | CREATE | One of CREATE, UPDATE, DELETE. |
  | protocol | string | GUI | *GUI* means use of the Web UI. *WS* means use of Web Services. *commit* means use of the commit protocol. |
  | details | string | "deleted JavaPrjNew" | Information about the event |
- A stream event

  Table 24. StreamEvent

  | Name | Value type | Value example | Semantics |
  | --- | --- | --- | --- |
  | level | string | INFO | The log level which is generally specified in the code when writing out the log message (e.g. `INFO`, `WARN`, `ERROR`, etc) |
  | count | number | 1 | Used for `IssueExportEvent` logging event types. |
  | action | string | CREATE | One of CREATE, UPDATE, or DELETE |
  | protocol | string | GUI | *GUI* means use of the Web UI. *WS* means use of Web Services. *commit* means use of the commit protocol. |
  | details | string | "created JavaStream | Information about the event |
- Triage store event

  Table 25. TriageStoreEvent

  | Name | Value type | Value example | Semantics |
  | --- | --- | --- | --- |
  | level | string | INFO | The log level which is generally specified in the code when writing out the log message (e.g. `INFO`, `WARN`, `ERROR`, etc) |
  | count | number | 1 | Used for `IssueExportEvent` logging event types. |
  | action | string | CREATE | One of CREATE, UPDATE, or DELETE |
  | protocol | string | GUI | *GUI* means use of the Web UI. *WS* means use of Web Services. *commit* means use of the commit protocol. |
  | details | string | "created new store | Information about the event |
- Component event

  Table 26. ComponentEvent

  | Name | Value type | Value example | Semantics |
  | --- | --- | --- | --- |
  | level | string | INFO | The log level which is generally specified in the code when writing out the log message (e.g. `INFO`, `WARN`, `ERROR`, etc) |
  | count | number | 1 | Used for `IssueExportEvent` logging event types. |
  | action | string | DELETE | One of CREATE, UPDATE, or DELETE |
  | protocol | string | GUI | *GUI* means use of the Web UI. *WS* means use of Web Services. *commit* means use of the commit protocol. |
  | details | string | "deleted TestComponent" | Information about the event |
- Snapshot event

  Table 27. Snapshot Event

  | Name | Value type | Value example | Semantics |
  | --- | --- | --- | --- |
  | level | string | INFO | The log level which is generally specified in the code when writing out the log message (e.g. `INFO`, `WARN`, `ERROR`, etc) |
  | count | number | 1 | Used for `IssueExportEvent` logging event types. |
  | action | string | CREATE | One of CREATE, UPDATE, or DELETE |
  | protocol | string | GUI | *GUI* means use of the Web UI. *WS* means use of Web Services. *commit* means use of the commit protocol. |
  | details | string | "created NewJava1 - 10004" | Information about the event |
