---
title: "Processing jobs table"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/processing-jobs-table.html"
content_id: "t30zbmMqzjG0B3_YOsaqgg"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:18.416909+00:00"
content_hash: "17451ced7966af33e2ff75f27930297038c90670b9e0db540e34951d772f4d78"
---

# Processing jobs table

Clicking the Processing button displays all jobs currently processing in your environment. The table of jobs is composed of the following columns:

- **Job Name**: The name of the job.
- **Scheduler type**: The scheduler type of the job.

  - Periodic: Jobs that are permanently stored with one or more repeating triggers.
  - On Demand: Non-durable jobs that are triggered from a specific or periodic event and are auto-deleted after the triggering event.
- **Job Frequency**: How often the job is set to run.
- **Started**: When the job was started in your environment.
- **Elapsed Time**: How long the job has been running. A [image: Warning icon] icon appearing next to the job's elapsed time indicates that the job is running longer than normal. Mousing over the icon will display the typical amount of time this job takes to complete.

## Filtering the Processing table

You can refine the list of jobs displayed in the table by clicking the **+ Filter** button and selecting one of the following options:

- **Job Frequency Type**: Select any from Run Once, Cron Pattern, or Periodic Interval to display all jobs of the desired type. Multiple options can be selected simultaneously.
- **Job Name**: Selecting this filter displays a list of all available jobs. Once a job is selected, the table will show all completed entries for this job. Multiple jobs can be selected.
- **Long Running**: Selecting this filter displays a list of jobs that are currently running longer than normal.
- **Scheduler Type**: Selecting this filter displays a list of scheduler types. Once a scheduler type is selected, the table will show all entries of the selected scheduler type.
