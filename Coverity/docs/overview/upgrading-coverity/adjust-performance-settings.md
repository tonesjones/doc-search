---
title: "Adjust performance settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adjust-performance-settings.html"
content_id: "hM8fqLd5iBeKFxBfr0WR7A"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:50.203891+00:00"
---

# Adjust performance settings

Adjust your PostgreSQL and JVM performance tuning settings for best performance
during the upgrade and subsequent production operations. Incorrect settings with a
large database can cause an upgrade to take 5x to 10x longer, or to fail and require
multiple restarts.

Tuning can be critical when
upgrading because some steps in the upgrade process might require
considerably more system resources than normal production operations. For more
information, see "Coverity
Connect upgrade environment variable parameters"
in the latest Coverity 2026.6.0 Installation and Upgrade Guide.

If you have any doubt about your tuning settings, open a Support
case by logging in to the[Black Duck Community site](https://community.blackduck.com/s/contactsupport) and
ask for advice. Send the following information:

- From what version are you upgrading? To what version are you upgrading?
- What is the size of your database on disk? What size is your database backup
  file?
- Is the machine dedicated to Coverity Connect (y/n)?
- What is the amount of system RAM in GB?
- Is your Coverity Connect database packaged with the Coverity Platform
  installer (an embedded PostgreSQL database), or is it an external PostgreSQL
  database?
- On what OS platform are you running Coverity Connect?
- What is the number of CPU cores on the machine, excluding
  hyper-threading?
