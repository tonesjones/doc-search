---
title: "Viewing jobs"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/viewing-jobs.html"
content_id: "tlQ4KvobYA_8JIZ7UjDzwA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:26.663981+00:00"
---

# Viewing jobs

You can view all the jobs in the system if you need to troubleshoot an issue and
determine if a process ran.

Note that any job older than 30 days is purged from the list.

Possible jobs are:

| Job Name | Description |
| --- | --- |
| Auto Remediate Unmapped | Auto remediate CVEs with unmapped related BDSAs. |
| BDIO Data Transfer | Processes scan data and prepares it for the matching process. |
| BDIO Storage Migration Check | Checks if there are any BDIO files to migrate to the storage service. |
| BOM Event Cleanup | Cleans up BOM events based on the retention policy. |
| BOM Vulnerability Recomputation Check | Checks if BOM computations are required when certain settings change and starts the necessary jobs. |
| Check Sigma Tool Version | Checks if the Sigma tool version is up to date and schedules the work if it is not. |
| Checks Need for Hierarchical BOM Calculation | Checks if hierarchical BOM computations are required and starts the necessary jobs to process them |
| Hierarchical Version BOM | Creates and updates the hierarchical version BOM. |
| Job History Statistics | Calculates statistics from the job history. |
| Journal Partition Maintenance | Creates new database partitions for the project audit trails and drops old partitions. The Journal table is partitioned by month. The first partition is special and contains all existing journal events. Journal events older than 5 years will be purged. |
| KnowledgeBase Update Check | Initiates updates received from the KnowledgeBase. See Understanding the Knowledge Base Update Job for more information. |
| License Term Check | Checks if license fulfillment processing is required and starts the necessary jobs. |
| LTS Transition Scheduler | Schedules LTS conversion jobs based on data retention settings. |
| Notification Purge Check | Checks if there are notifications that need cleanup and starts the necessary jobs. |
| Policy Rule Bulk Propagation | Publish BOM messages for policy rules that need propagation |
| Populate License Terms | Updates Black Duck with the latest Black Duck KB license term data. |
| Purge API Token Check | Determines if the access tokens auto purge job needs to run. |
| Purge API Token | Deletes inactive access tokens based on configured settings. |
| Purge Deleted Storage Objects | Removes deleted storage objects from the system and cleans out orphaned records. |
| Purge Notifications | Manages data retention for existing notifications. |
| Purge Orphan BOMs | Deletes any BOM data not associated with a project version. |
| Purge Orphan BOMs Check | Checks to see if any BOM data is not associated with a project version and starts the necessary jobs. |
| Purge Reports | Manages data retention for existing reports and purges expired reports. |
| Purge Scan Data - Delete Abandoned Scans | Deletes scans that were started but never completed. |
| Purge Scan Data - Delete Expired Scans | Deletes scans that are older than the expiration threshold. |
| Purge Scan Data - Delete Orphaned Scan Identifiers | Deletes orphaned snippet scan identifiers. |
| Purge Scan Data - Delete Orphaned Scans | Deletes orphaned scans. |
| Purge Scan Data - Delete Stale Projects | Deletes stale projects. |
| Purge Scan Data - Delete Stale Releases | Deletes stale releases. |
| Purge Scan Data - Delete Unmapped Scans | Deletes unmapped scans. |
| Purge Scan Data - Purge Component Mapping Audit Events | Purges component mapping audit events. |
| Purge Scan Data - Purge Deleted Scans | Deletes scans that were previously queued for deletion. |
| Purge Scan Data - Purge Scan Archives | Deletes scan archives that are eligible for deletion. |
| Purge Scan Data - Purge Unmatched Files | Deletes unmatched files from scans that are eligible for deletion. |
| Purge Scan Data Scheduler | Schedules job that removes old scan data. |
| Purge Scan Statistics | Removes old scan statistics. |
| Report Storage Migration Check | Checks whether there are reports that need to be migrated into the storage service. |
| Reporting Database Transfer | Migrates Black Duck data to the Black Duck reporting warehouse. |
| Reporting Database Transfer Scheduler | Schedules job that transfers reporting data to the reporting schemas for customers. |
| SBOM Report | Generates the SBOM report for a Project Version. |
| Scan Auto BOM Calculation | Calculates a BOM from a scan. |
| Scan Statistics | Collects scan statistics shown on the **usage: scan completion** section on the System Information page. |
| Scheduled Policy Rule Changes Check | Finds policy violation overrides with scheduled expirations. |
| Schema Difference Report | Calculates the differences between the current database schema and the ideal as determined at release. |
| SCM Onboarding daily auto scanning | Schedules nightly job that performs auto scanning of previously onboarded SCM repositories. |
| SCM Onboarding daily cleanup | Schedules nightly job that cleans up from SCM Onboarding. |
| Search Dashboard Refresh | Updates the information shown on the Projects and Components Dashboards. |
| Search Dashboard Refresh Check | Checks if it is time to refresh the Projects and Components Dashboards and starts the necessary job. |
| Snippet BOM Calculation | Calculates a BOM from a snippet scan. |
| Storage Migration Check | Checks to see if there is migration work to perform. |
| Storage Pruning Check | Checks if the object storage system has items to prune. |
| System Maintenance and Reporting | Processes system statistics and registers them with the KnowledgeBase. |
| Test Performance Dispatch | System diagnostic that tests the performance of job dispatch. |
| Update KnowledgeBase Data - BDSA Vulnerability Update | Updates BDSA vulnerability information received from the KnowledgeBase. |
| Update KnowledgeBase Data - Component Update | Updates component information received from the KnowledgeBase. |
| Update KnowledgeBase Data - Component Version Security Update | Processes component version updates received from the KnowledgeBase. |
| Update KnowledgeBase Data - License Update | Updates license information received from the KnowledgeBase. |
| Update KnowledgeBase Data - NVD Vulnerability Update | Updates NVD vulnerability information received from the KnowledgeBase. |
| Update KnowledgeBase Data - Summary | Issues a summary report about the most recent KnowledgeBase update. |
| Update Origin Copyrights | Updates origin copyrights. |
| Version BOM Notification | Notifies on various BOM-related events. |
| Version BOM Notification Check | Checks to see if any version BOM notifications need processing. |
| Version Bom Computation Check | Checks if any version BOMs need computations and schedules the work. |
| Version License Report | Creates the Notices File report. |
| Version Report | Creates the Project Version report. |
| Version Vulnerability Remediation Report | Creates the Project Version Vulnerability Remediation report. |
| Version Vulnerability Status Report | Creates the Project Version Vulnerability Status report. |
| Version Vulnerability Update Report | Creates the Project Version Vulnerability Update report. |
| Vulnerability Remediation Report | Creates the Vulnerability Remediation report. |
| Vulnerability Status Report | Creates the Vulnerability Status report. |
| Vulnerability Update Report | Creates the Vulnerability Update report. |
| Watchdog | Monitors the job subsystem for errors and reports or fixes issues as they arise. |

## Viewing jobs

To view a list of jobs and their current statuses:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Click **Jobs**.
4. Click the **Jobs** tab to display the Jobs page.

## Filtering the Jobs table

You can refine the jobs displayed in the table by selecting one of the following options:

- **Finished**: Displays all finished jobs.
- **Scheduled**: Displays all jobs set to run
  in your environment.
- **Processing**: Displays all jobs currently
  processing.
