---
title: "Configuring Automatically Deactivating Users"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/configuring-automatically-deactivating-users.html"
content_id: "3xdv2LJFwLRCIguMtB6ing"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:42.188923+00:00"
content_hash: "70b6d2abed71d395b501b9f004df55d22eb97544358c51b40da92d407edf91f2"
---

# Configuring Automatically Deactivating Users

SRM can automatically deactivate inactive users. The following props can be configured:

- `maintenance.deactivate-inactive-users.enabled` - [default: false] set this to true to have
  SRM automatically deactivate inactive users.
- `maintenance.deactivate-inactive-users.scheduling-strategy` - [default: daily] defines when the job
  will be ran. Allowed values are `daily` and `interval.`
- `maintenance.deactivate-inactive-users.run-time` - [default: 00:00:00] the exact time when this job
  will run. Only used when `maintenance.deactivate-inactive-users.scheduling-strategy` is set to `daily`.
- `maintenance.deactivate-inactive-users.interval` - [default: 24 hours] the interval of time in which
  this job run. Only used when `maintenance.deactivate-inactive-users.scheduling-strategy` is set to `interval`.
- `maintenance.deactivate-inactive-users.after-days` - [default: 30] the number of days a user
  can be inactive before this job will automatically deactivate them. A user is considered active if they have either logged
  in or have been activated within this number of days.
