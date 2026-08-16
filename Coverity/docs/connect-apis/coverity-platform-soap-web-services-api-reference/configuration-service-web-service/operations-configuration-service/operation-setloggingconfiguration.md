---
title: "Operation: setLoggingConfiguration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-setloggingconfiguration.html"
content_id: "OS04fqbER9SsjsuRxjg4Bg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:07.531070+00:00"
---

# Operation: setLoggingConfiguration

## Name

setLoggingConfiguration

## Description

Enable or disable logging options for Coverity Connect.

Coverity Connect automatically logs system event information to the cim.log file. You
can increase the amount of information that Coverity Connect records to this file by
enabling additional logging options to work with Coverity Support on an issue.
Coverity recommends that you leave all of the logging options disabled and only
enable them by request from Coverity Support.

## Parameters

loggingConfigurationDataObj
:   **Type:** 
    loggingConfigurationDataObj

    The settings correspond to the Logging Configuration options (System
    settings) in Coverity Connect.

    | Field name | Type | Description |
    | --- | --- | --- |
    | accessControlLogging | boolean | Access control logging. |
    | backgroundLogging | boolean | Background tasks logging. |
    | bugTrackingSystemLogging | boolean | Bug tracking system logging. |
    | commitLogging | boolean | Commit logging. |
    | configurationLogging | boolean | Configuration logging. |
    | databaseLogging | boolean | Database logging. |
    | frameworkLogging | boolean | Framework logging. |
    | internalLogging | boolean | Internal logging. |
    | kerberosLogging | boolean | Kerberos logging. |
    | metricsAndHistoryLogging | boolean | Metrics and history logging. |
    | notificationLogging | boolean | Notifications logging. |
    | performanceLogging | boolean | Performance logging. |
    | policyManagerLogging | boolean | Policy Manager logging. |
    | remoteConfigLogging | boolean | Remote Configuration logging. |
    | requestPerformanceLogging | boolean | Request Performance logging. |
    | skeletonizationLogging | boolean | Snapshot Details Purge logging. |
    | testAdvisorLogging | boolean | Test Advisor logging. |
    | triageLogging | boolean | Triage logging. |
    | triageSynchLogging | boolean | Triage & CID Synchronization logging. |
    | webLogging | boolean | Web logging. |
    | webServicesLogging | boolean | Web Services logging. |

## Remarks

See also getLoggingConfiguration().
