---
title: "Scheduled jobs table"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scheduled-jobs-table.html"
content_id: "thiPtaI8bmPlYZ1OfRQhbA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:27.792210+00:00"
---

# Scheduled jobs table

Clicking the Scheduled button displays all jobs set to run in your environment. The table
of jobs is composed of the following columns:

- **Job Name**: The name of the job.
- **Scheduler type**: The scheduler type of the job.

  - Periodic: Jobs that are permanently stored with one or more repeating triggers.
  - On Demand: Non-durable jobs that are triggered from a specific or periodic event and are
    auto-deleted after the triggering event.
- **Job Frequency Type**: The job's type of trigger and its recurrence.
- **Scheduled Time**: The next time the job is scheduled to run.
- **Enabled**: Whether or not the job is enabled to run in your environment.

## Enabling or disabling jobs

You can enable or disable a particular job by clicking the [image: image]
button at the end of its row and selecting the desired option.

## Filtering the Scheduled table

You can refine the list of jobs displayed in the table by clicking the **+
Filter** button and selecting one of the following options:

- **Enable**: Select either Enabled or Disabled to display all jobs of the
  desired type.
- **Job Frequency Type**: Select any from Run Once, Cron Pattern, or
  Periodic Interval to display all jobs of the desired type. Multiple options
  can be selected simultaneously.
- **Job Name**: Selecting this filter displays a list of all available jobs.
  Once a job is selected, the table will show all completed entries for this
  job. Multiple jobs can be selected.
- **Scheduler Type**: Selecting this filter display a list of scheduler types.
  Once a scheduler type is selected, the table will show all entries of the
  selected scheduler type.
