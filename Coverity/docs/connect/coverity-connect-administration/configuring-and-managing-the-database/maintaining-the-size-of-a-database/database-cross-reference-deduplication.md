---
title: "Database cross-reference deduplication"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/database-cross-reference-deduplication.html"
content_id: "vQAs4tSJRG7y8FP3SLumQQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:16.111526+00:00"
---

# Database cross-reference deduplication

Coverity Connect PostgreSQL databases use cross reference tables to link data between
tables. Over time, duplicate cross-reference link entries are created within the cross
reference table. The database cross-reference deduplication tool deletes duplicate cross
reference entries in PostgreSQL cross-reference tables. Performing database
cross-reference deduplication during a database migration can reduce cross-reference
table size by as much as 80%, thereby improving Coverity commit performance because
there is less data to load.

A database migration involves moving data from one database to another. Deduplication is
the process of removing redundant data within a database. Performing a database
cross-reference deduplication during a PostgreSQL migration reduces the amount of data
that needs to be transferred, and optimizes storage space on the target system.
Depending on database size, load, and available resources, a database deduplication and
migration might take hours or days. Once a cross reference deduplication starts, you can
not disable it.

The default migration schedule runs at 2 AM local time every day for one hour until the
migration is complete. The migration pauses after one hour and restarts the next day at
2 AM, continuing from where it paused. You can configure this behavior as described in
"Scheduling cross-reference deduplication."

Note: For very large PostgreSQL tables with hundreds of millions or
even billions of rows, using the default migration schedule that triggers at 2 AM can
take many days to complete. In this case, we recommend increasing the deduplication
frequency using the scheduling parameters.

Performing a migration consumes 5-10% of
the memory during the migration.

Database migration does not impact Coverity Connect functionality. Connect continues to
work properly while the database is partially migrated. When a migration restarts, it
resumes from where it stopped.

Also, all new commits load data to new tables.

## Procedure: configuring and performing a database cross-reference deduplication

To perform a database cross-reference deduplication:

1. Back up your PostgreSQL database.
2. Configure the `cim.properties` file to schedule and enable
   cross-reference deduplication.
3. Monitor the deduplication progress.
4. Validate that the deduplication was successful by checking cross references.
   Click on any files in the `Files in Latest Snapshot` view. On the
   source code which appears in the lower pane, check the cross-references; they
   should work within the file and across multiple files.
5. When the migration completes, compare the original database size
   `old_xref_count` with the deduplicated database with
   `new_xref_count`. See "Monitoring a database cross-reference
   deduplication."
6. If everything passes validation, repeat this procedure for the production
   database.

## Enabling cross-reference deduplication

To enable cross-reference deduplication, add the following property to the
`cim.properties` file. Once you have configured these parameters
and enabled cross-reference deduplication, the deduplication will begin at the next
scheduled time.

- To enable cross-reference deduplication, add the following parameter, where
  `true` enables cross-reference deduplication and
  `false` disables cross-reference deduplication:

  ```
  xrefs.enable_linksets=true
  ```

  Note: Database cross-reference deduplication is disabled
  by default

  Important: You cannot reverse a database
  cross-reference deduplication once it has started. You must let the tool
  complete all deduplications.

`xrefs.enable_linksets=true` is the main parameter which decides
whether to trigger the migration job or not. Nore that once is enabled there is no
going back.

## Scheduling cross-reference deduplication

The default migration schedule runs at 2 AM local time every day for 1 hour until the
migration is complete. The migration pauses after one hour and restarts the next day
at 2 AM, continuing from where it paused.

Note: For very large PostgreSQL tables with hundreds of millions
or even billions of rows, using the default migration schedule that triggers at 2 AM
can take many days to complete. In this case, we recommend increasing the
deduplication frequency using the scheduling parameters.

To override the default schedule, add the following properties to the
`cim.properties` file. Once you have configured these parameters
and enabled cross-reference deduplication, the deduplication will begin at the next
scheduled time.

- Use the `xrefs.migration_schedule` parameter to
  **schedule** the database migration. This parameter uses the Spring
  [CRON](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/scheduling/support/CronExpression.html#method-detail) syntax.

  ```
  xrefs.migration_schedule=<CRON>
  ```

  Note:

  The Spring [CRON](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/scheduling/support/CronExpression.html#method-detail) syntax contains a
  'Seconds' field:

  ```
  xrefs.migration_schedule=* * * * * *
  ```

  From left to right: Seconds, Minutes, Hours, Day of month, Month, Day of
  week

  For example, to override the default setting and run continuously until
  completed, add the following parameter:

  ```
  xrefs.migration_schedule=0 * * * * *
  ```

  To schedule a database migration at 12:30 AM every day, add the following
  parameter:

  ```
  xrefs.migration_schedule=* 30 0 * * *
  ```
- To change the **duration** of each batch migration, add the following
  parameter:

  ```
  xrefs.migration_max_batch_duration=<duration>
  ```

  where the `<duration>` value is in milliseconds. You can
  set the the duration to any value.

  For example, to set the batch duration to one hour:

  ```
  xrefs.migration_max_batch_duration=3600000
  ```

  For example, to set the batch duration to six hours (6 hrs x 60 mins x 60
  secs x 1000 ms = 21600000):

  ```
  xrefs.migration_max_batch_duration=21600000
  ```

Note: If you do not add the
`xrefs.migration_schedule` and
`xrefs.migration_max_batch_duration` parameters, cross reference
deduplication will automatically use the default schedule and trigger at 2 AM each
day for one hour.

## Examples

Thie following examples enable, schedule, and set the job duration of cross reference
deduplication.

- If you need the job to go slower, maybe avoid any system load or to run
  during the night, you can schedule it any hour, or increase the maximum
  duration, etc.

  For example, to enable and schedule a job to run at 12 AM, and run for 6
  hours:

  ```
  xrefs.enable_linksets=true
  xrefs.migration_schedule=0 0 0 * * *
  xrefs.migration_max_batch_duration=21600000
  ```
- The following `migration_schedule` parameter continues the job
  one minute after each pause. This means that after a job reaches its maximum
  duration, it gets paused, then is restarted in the next minute. The maximum
  duration is set to 2 hours.

  ```
  xrefs.enable_linksets=true
  xrefs.migration_schedule=0 * * * * *
  xrefs.migration_max_batch_duration=7200000
  ```

## Monitoring a database cross-reference deduplication

You can monitor the progress of a cross-reference deduplication. Refer to the
`xref_migration_state` table; it provides information such
as:

- Status
- Total old rows
- Processed rows
- New rows
- Elapsed time

The `xref_migration_state` table, described below, is updated
periodically as defined by the `xrefs.migration_max_batch_duration`
parameter, or each hour if not set.

The status of a cross-reference deduplication is reported using the following log
entries to the `cim.log` file:

- `Starting Xref migration job`
- `Finished Xref migration job, all data has been
  migrated`
- `Stopping Xref migration job, an exception occurred`
- `Stopping Xref migration job, time limit reached`

The following table defines the `xref_migration_state` table fields
and values.

Table 1. The `xref_migration_state` table

| Column | Data Type | Description | Examples |
| --- | --- | --- | --- |
| id | int8 | Primary key. | 1 |
| jobruns | int8 | Job run counter tracks the number of times a deduplication starts or restarts. This value begins at zero and increments when the deduplication first starts as well as each time the deduplication restarts after a pause. | 1 |
| batch_size | int8 | The default batch is 100k rows. The batch size can decrease based on memory usage. | 100k |
| time_in_s | bigint | Total deduplication time in seconds. This value is updated every hour. | 600s |
| start_dttm | timestamp | Deduplication start date and time. | 2025-02-05 11:28:00.092 |
| end_dttm | timestamp | Deduplication end date and time. | 2025-02-05 11:38:00.092 |
| migration_status | int8 | - `In Progress` - Migration is running in the   backend. If the `migration_status` is   `In Progress`, wait for the process to   complete. We do not recommend monitoring anything else at   this stage. Wait until the migration completes. - `Completed` - All old cross reference data   moved to new tables. Wait until   `migration_status` is   `Completed` before verifying the   deduplication. - `Error` - An error has occurred.    - For an `Out of Memory` error, the     deduplication tool will automatically reduce the     batch size and retry the deduplication.   - If the error is something else, the deduplication     retries again based on the schedule.   - The `error` column contains further     details on the error.   - If a migration fails, especially after multiple     tries, contact Black Duck to help debug the     issue. - `Paused` - The deduplication is paused. This   can occur as scheduled, or manually via a restart.   Note: PostgreSQL autovacuum errors do not affect or stop a cross reference migration. Autovacuum is an independent PostgreSQL daemon job. Ignore PostgreSQL autovacuum errors as relates to migration. | Completed |
| old_xref_count | bigint | Total number cross reference rows in the old tables.  (`xref_declaration_file` + `local_xref_decl_file`) | 50000 |
| processed_xref_count | bigint | Total number of duplicate rows removed from the old tables. By default, this value is updated every hour. | 50000 (Do not worry if this value is different than old_xref_count) |
| new_xref_count | text | Total number of cross reference rows in the new tables (updated at the end). | ``` xref_symbolset:10000; xref_linkset:10000 ``` |
| timer_stats | text | Individual timings for each sub-program in the migration. | ``` xref_migration                          :       6000735.742000 (1) xref_migration.ext_refs                          :        22.716208 (1) xref_migration.ext_refs.migrate_lobs             :        11.204375 (1) xref_migration.ext_refs.migrate_names            :         9.717501 (2) xref_migration.initial_vacuuming                 :        17.594750 (1) xref_migration.local_refs                        :        87.781542 (1) xref_migration.local_refs.insert                 :        80.438333 (1) xref_migration.old_counts                        :         9.386500 (1) xref_migration.xref_decl.delete_xds              :        29.175625 (1) xref_migration.xref_decl_linksets                :       601.453334 (1) xref_migration.xref_decl_linksets.insert_symbols :        16.478084 (2) xref_migration.xref_decl_linksets.load           :        50.455416 (3) xref_migration.xref_decl_linksets.load_symbols   :       143.782932 (5792) xref_migration.xref_decl_linksets.process        :       480.300041 (2) xref_migration.xref_decl_linksets.process.3      :         0.889322 (5792) xref_migration.xref_decl_linksets.process.4      :         1.976179 (5792) xref_migration.xref_decl_linksets.process.5      :         8.67019 (5792) xref_migration.xref_decl_linksets.process.6      :        12.719653 (5792) xref_migration.xref_decl_linksets.process.7      :         2.924568 (5792) xref_migration.xref_decl_linksets.process.8      :         0.492625 (2) xref_migration.xref_decl_linksets.update_symbols :        29.630083 (2) xref_migration.xref_decl_linksets.upsert_linksets:        11.279668 (2) ``` |
| error | text | Describes any error that might have occurred. |  |

## Verify and review the deduplicated database

After the deduplication successfully completes, verify that duplicated data was
removed and valid data remains within the database. You can compare the new database
sizes with the sizes recorded before you began the deduplication.

## Run the deduplication on the production database

If you ran the first pass of the deduplication on a test database and the
deduplication was successful, you can now run the deduplication on the production
database.
