---
title: "Monitor the logs"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/monitor-the-logs.html"
content_id: "oGasEBViqO0rYX5VjridPA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:26.485559+00:00"
---

# Monitor the logs

After you run a tuning job, monitor the logs for tuning results. How you do this depends
on whether it is a tuning-write or a tuning-suggest as follows.

## Tuning-suggest

When you run a `static-tuning-suggest` job, the static-tuning-suggest
job creates tuning logs for the pod. These logs contain the suggested tuning
information.

You can then open the tuning logs for the pod using the following command:

```
kubectl logs <suggest/write pod name> -n namespace
```

After reviewing the logs with the suggested settings, you can modify the PostgreSQL
settings if needed. If you do modify the PostgreSQL setings, you will need to
restart the database to use the new settings.

If a database restart is needed, continue with Restart the database.

## Tuning-write

When you run a tuning-write, the `cim.log` file will contain either of
the following log statements that specifies whether or not a database restart is
required:

- `Tuning requires a restart of the database service, please restart the
  database to make sure the parameters are up-to-date.`
- `Tuning does not require any restart for the database service, all
  parameters are up-to-date.`

If a database restart is needed, continue with Restart the database.
