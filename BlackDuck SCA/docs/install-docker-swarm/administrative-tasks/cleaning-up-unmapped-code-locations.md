---
title: "Cleaning up unmapped code locations"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/cleaning-up-unmapped-code-locations.html"
content_id: "XK6PuUici~e_Wgy0emQwHw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:50.105652+00:00"
---

# Cleaning up unmapped code locations

Unmapped code locations are code locations that are not mapped to a project version.
Internally in Black Duck, a code location is represented by one or more scans.

- Sometimes code scanning creates code locations without mapping them to a project
  version, which results in unmapped code locations.
- Code locations/scan data can be orphaned when users delete project versions.

Users who don't want to purge unmapped code location data might want to disable this
feature in the `blackduck-config.env` file, which, by default, is set to
true and to purge every 30 days.

Users who scan regularly and want to discard the data frequently might want to set the
retention period to a low number of days, such as 14 days.

To schedule a cleanup of unmapped code locations, configure the following properties in
the `blackduck-config.env` file:

- `BLACKDUCK_HUB_UNMAPPED_CODE_LOCATION_CLEANUP=true`

  The default setting is true.

- `BLACKDUCK_HUB_UNMAPPED_CODE_LOCATION_RETENTION_DAYS=<number of days
  between 1-365, for example, 14>`

  The default setting is 30 days.

Note: When you configure the cleanup of unmapped code locations and restart the system, the scan
purge starts to remove unmapped code locations that meet the retention criteria (older
than the configured number for retention days). By default, the scan purge job runs
every 15 minutes.

## Schedule a scan purge job by using a cron string

You can configure a scan purge by setting a variable in the
`blackduck-config.env` file for docker swarm implementations.

The scan purge job can be scheduled by setting a variable in
`blackduck-config.env` by using either of the following:

- using a cron job:
  `blackduck.scan.processor.scanpurge.cronstring`

  Use the
  following cron format: `second minute hour dayOfMonth month
  daysOfWeek`

- using fixed delay:
  `blackduck.scan.processor.scanpurge.fixeddelay`
  (configured as the frequency to run scanpurgejob in milliseconds, which
  defaults to 15 minutes)

Note: If the `blackduck.scan.processor.scanpurge.cronstring` is provided, then the
`blackduck.scan.processor.scanpurge.fixeddelay` setting is
ignored because the cron string is used instead.
