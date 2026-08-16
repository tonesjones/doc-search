---
title: "Stopping and starting Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stopping-and-starting-coverity-connect.html"
content_id: "m2FSQHfwSItgwVgF7D8gpg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:04.478859+00:00"
---

# Stopping and starting Coverity Connect

Note: If Coverity Connect is deployed in the cloud, this section does not apply.

To stop or start Coverity Connect:

- On Linux, go to <install_dir>/bin and run the
  `cov-im-ctl` command.

  The command accepts the maintenance,
  start, stop, or status options. For example, to get status information:

  ```
  > cd <install_dir>/bin
  > ./cov-im-ctl status
  ```
- On Windows, go to <install_dir>\bin and run the
  cov-im-ctl.exe program.

  When Coverity Connect is
  installed as a service, the cov-im-ctl.exe program is often
  unnecessary because Coverity Connect starts and stops automatically when the
  system boots up or shuts down. When Coverity Connect is installed as a service,
  any administrator can use this program.

  When Coverity Connect is not
  installed as a service, only the user who installed Coverity Connect is able to
  use this program to start or stop it.

Note: If you need to restart your external PostgreSQL database, see the [PostgreSQL documentation](http://www.postgresql.org/docs/manuals/).
