---
title: "Data Retention Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/data-retention-configuration.html"
content_id: "z26Pbr~qrNaWPrrEUkyryg"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:27.433892+00:00"
content_hash: "2c72ffe81442499b01f80e5849b5bb2f56d6c639d905b1ac642e158b7ea8dfb9"
---

# Data Retention Configuration

To help manage data retention, Software Risk Manager offers the following settings to
enable the purging of old data:

- `findings.purge-after-days` [default: unspecified] - if specified,
  sets the number of days to retain *Findings* marked as *Gone*. For
  example, `findings.purge-after-days = 90`.
- `results.purge-after-days` [default: unspecified] - if specified,
  sets the number of days to retain archived *Results*. For example,
  `results.purge-after-days = 7`.
- `visual-log.purge-after-days` [default: 30] - if specified, sets
  the number of days to retain *Visual Log* entries. For example,
  `visual-log.purge-after-days = 45`. Setting the value to -1
  will cause all visual log entries to be retained.
- `analysis.logs.cleanup-mode` [default: expired] - sets what strategy
  is used to clean up analysis logs. Valid values are:
  - `expired` - delete analysis logs older than
    `analysis.logs.days-to-keep`.
  - `archived` - delete logs for analyses where all of its inputs
    are archived.
  - `expired-or-archived` - delete logs for analyses that are
    either older than `analysis.logs.days-to-keep`, or have all
    of their inputs archived.
  - `expired-and-archived` - delete logs for analyses that are
    both older than `analysis.logs.days-to-keep`, and have all
    of their inputs archived.
  - `disabled` - analysis logs are not deleted.
- `analysis.logs.days-to-keep` [default: 7] - sets the number of
  days to retain analysis logs if the `analysis.logs.cleanup-mode`
  is set to `expired`, `expired-or-archived`, or
  `expired-and-archived`.
- `analysis.logs.cleanup-time` [default: 00:00] - sets the time
  of day that analysis log clean up is ran. A value for this property should
  be a 24-hour time in the form `HH:MM`. For example
  `01:00` for 1 in the morning, or `13:00` for 1 in
  the afternoon.

## Findings

When enabled, findings that are marked as *Gone* and have not been modified for
more than the specified number of days will be removed. For a finding to be eligible
for removal, it must be marked as *Gone* and not have been modified recently on
*all* Branches that it is present on. If the finding has been modified
recently or has a status other than *Gone* on any branch, then the finding will
be kept on all branches.

## Results

When enabled, results coming from *Analysis Inputs* that have been archived and
are older than the specified number of days will be removed. However, results that
are associated with findings that are marked as *Gone* will not be removed.
This is done to prevent a scenario where a *Gone* finding has no associated
results (since all results associated with a *Gone* finding will be archived).
Any findings removed per the data retention configuration above do not count toward
this condition. Results will be removed on any branch where these conditions are
met, regardless of their status in other branches.

## Visual Log

When enabled, *Visual Log* entries that are older than the specified number of
days will be removed.
