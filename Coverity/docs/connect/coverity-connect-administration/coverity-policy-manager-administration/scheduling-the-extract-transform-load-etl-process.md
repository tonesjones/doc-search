---
title: "Scheduling the Extract Transform Load (ETL) process"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scheduling-the-extract-transform-load-etl-process.html"
content_id: "QKhTxOJsIm~Q~vUWgAZM1Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:05.021838+00:00"
---

# Scheduling the Extract Transform Load (ETL) process

During the Extract Transform Load (ETL) process, Policy Manager extracts and aggregates
raw data from the database, updating the information in the PM tables. You can schedule
the ETL process to run at any (designated) time. By default, an ETL task is scheduled to
run one hour after completion of the previous run. Note that this process can be
time-consuming, however, and often requires extra disk space.

You can switch to `cron`-based scheduling by setting property values in
config/cim.properties. You can either use the same schedule for
both status and trend ETL processes, or you can set up separate schedules, depending on
which properties you set.

Note: Data aggregated by the ETL process does not last indefinitely. Daily data is kept for
40 days, weekly data is kept for 30 weeks, monthly data is kept for 24 months, and
yearly data is kept indefinitely. Older data is deleted after new data is
inserted.

Also, be aware that the ETL process does not save a history of previous
configurations (that is, component map and stream settings). Whenever the current
project configuration is changed, Policy Manager data is recomputed based on the new
settings.

**To set up a single schedule for both status and trend ETL
processes, set the following properties as indicated:**

- `policymanager.etl.scheduled.disable=false`
- `policymanager.etl.cron.enable=true`
- `policymanager.etl.cron.schedule=date-and-time`

Note: The scheduled `cron` job follows a specific syntax. For
example:

```
policymanager.etl.cron.schedule=0 30 2 * * *
```

The
example above represents a `cron` job scheduled to run every night
at 0230 hours.

You can disable this schedule by setting the properties as follows:

- `policymanager.etl.scheduled.disable=true`
- `policymanager.etl.cron.enable=false`

**To set up separate schedules for status and trend ETL processes,
set the following optional properties in addition to the three properties listed
above:**

- `policymanager.etl.trend.scheduled.disable=false`
- `policymanager.etl.trend.cron.enable=true`
- `policymanager.etl.trend.cron.schedule=date-and-time`

These properties control the schedule only for trend ETL processes. Once you set these
trend properties, the previous three properties control only status ETL processes.

With all six properties set, you can specify different schedules for status and trend ETL
processes. You can also enable and disable the status and trend schedules separately.
For example, to disable the trend schedule, set the following properties as
indicated:

- `policymanager.etl.trend.scheduled.disable=true`
- `policymanager.etl.trend.cron.enable=false`

Note: You can set only some of the trend properties, if you desire. For example, if you want
separate status and trend schedules, but want to enable/disable them together, then set
only this property (in addition to the first three):

- `policymanager.etl.trend.cron.schedule=date-and-time`

Similarly, if you want to use the same schedule for status and trend ETL
processes but want to separately enable/disable them, set only these properties (in
addition to the first three):

- `policymanager.etl.trend.scheduled.disable=false`
- `policymanager.etl.trend.cron.enable=true`
