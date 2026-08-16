---
title: "Coverity Connect upgrade environment variable parameters"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-upgrade-environment-variable-parameters.html"
content_id: "GucUv0EpAXadcOK4C0lIcg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:37.806127+00:00"
---

# Coverity Connect upgrade environment variable parameters

*Defect event processing*

If you have a large number of events per defect (over 250) or are performing upgrade on a
machine with limited memory it is recommended that you use the defaults or use slightly
lower values (.5x) for these variables, particularly for DB_UPGRADE_EVENTS_LATEST_BATCH.
If you have a large number of defects (and moderate numbers of events per defects) and
are sensitive to upgrade speed, you can use a slightly higher value (2-4x) for
DB_UPGRADE_EVENTS_NON_LATEST_BATCH.

Table 1. Defect event processing

| Property | Description |
| --- | --- |
| DB_UPGRADE_EVENTS_​LATEST_BATCH | The default is 1000, however the recommended value is 32000 (with 32GB+ RAM). Controls upgrade batch processing of latest defects lower values allow the upgrade to succeed on machines with lower RAM thresholds at the expense of speed.  This parameter is needed only when upgrading a database from version 6.0.3 or earlier. |
| DB_UPGRADE_EVENTS_​NON_LATEST_BATCH | The default is 5000. The recommended value is 2000000 (with 32GB+ RAM). Controls upgrade batch processing of no-latest defects lower values allow the upgrade to succeed on machines with lower RAM thresholds at the expense of speed. The settings for these values are conservative. For machines with 32GB+ RAM, the values should be set substantially higher to reduce the upgrade time by ~75%.  This parameter is needed only when upgrading a database from version 6.0.3 or earlier. |

COVERITY_RESTORE_JOBS
:   This option
    is only available with version 6.5.1 and later. It controls
    the level of parallelism in the `pg_restore` command. The
    default value is the number of processor cores. Alternatively, you can pass in
    the `-j` parameter to `cov-admin-db
    restore`.
