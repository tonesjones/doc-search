---
title: "Finished jobs table"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/finished-jobs-table.html"
content_id: "7Ol~pG1Ao3hUzPNvKmTgUQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:27.227990+00:00"
---

# Finished jobs table

Clicking the Finished button on the Jobs page displays a table of all completed jobs
listed in chronological order. The table of jobs is composed of the following
columns:

- **Status**: Displays the current state of the job. The statuses are as follows:

  - Success
  - Error
- **Job name**: The name of the job run.
- **Attempts**: How many times the job was run.
- **Scheduler type**: The scheduler type of the job.

  - Periodic: Jobs that are permanently stored with one or more repeating triggers.
  - On Demand: Non-durable jobs that are triggered from a specific or periodic event and are
    auto-deleted after the triggering event.
- **Started**: When the job was started in your environment.
- **End Time**: When the job was finished in your environment.
- **Duration**: The amount of time the job took to complete its run.

## Filtering the Finished jobs table

You can refine the list of jobs displayed in the table by clicking the **+ Filter** button
and selecting one of the following options:

- **End Time**: Selecting this filter displays a date picker where you can
  choose a start and end date. Once selected, the table will show all jobs
  finished within the specified time frame.
- **Error Status**: Selecting this filter will show all jobs that ended with
  an error.
- **Job Name**: Selecting this filter displays a list of all available jobs.
  Once a job is selected, the table will show all completed entries for this
  job. Multiple jobs can be selected.
- **Scheduler Type**: Selecting this filter display a list of scheduler types.
  Once a scheduler type is selected, the table will show all entries of the
  selected scheduler type.
