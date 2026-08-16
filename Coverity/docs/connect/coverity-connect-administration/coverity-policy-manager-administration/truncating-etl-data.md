---
title: "Truncating ETL data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/truncating-etl-data.html"
content_id: "4DKSdbWjoxNxUBredy8JZg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:05.686674+00:00"
---

# Truncating ETL data

By default, policy manager ETL (Extract, Transform, Load), described in Scheduling the Extract Transform Load (ETL) process, is enabled and can
generate large data loads. This can impact system performance and efficiency, which can
be an issue, especially if you do not need or use the ETL data. If you do not use the
policy manager, you can disable it and set ETL truncate to free up storage and improve
performance.

If you disable policy manager and enable ETL truncate, an ETL truncate will be performed
during each system startup.

Note: The ETL truncate operation takes less than a second.

To set this up, you must edit the `cim.config` file as described in the
following subsection, .

## Configure ETL truncate in the `cim.config` file

To disable policy manager and enable ETL truncate, edit the
`cim.config` file as follows.

To disable policy manager, change the value of the following existing parameter from
`false` to `true`:

```
policymanager.etl.scheduled.disable = true
```

Important: You must disable policy manager when you
enable ETL truncate.

Add the following parameter to enable ETL truncate:

```
policymanager.etl.truncate.enable = true
```

The next restart and all subsequent restarts will trigger an ETL data truncation, and
free-up storage.

## Optional: check database size

Optionally,
you can check the database size before and after truncating ETL using the following
`pg_size_pretty` PostgreSQL command:

`select
pg_size_pretty(pg_database_size('cim'));`
