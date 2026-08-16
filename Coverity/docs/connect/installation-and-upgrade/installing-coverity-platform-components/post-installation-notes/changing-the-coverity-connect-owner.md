---
title: "Changing the Coverity Connect owner"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changing-the-coverity-connect-owner.html"
content_id: "I5zS_Sy5AK7eb9rNaZr08w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:05.093383+00:00"
---

# Changing the Coverity Connect owner

Note: If Coverity Connect is deployed in the cloud, this section does not apply.

In Unix, when installing Coverity Connect the current user becomes the owner of all
unpacked files, and is the only user who can execute command-line tools such as
`cov-im-ctl`. The user name is also recorded as the
`os_user` in the config/system.properties
file.

If the owner's account is removed, then a new owner must be assigned. Perform the
following two actions to change the Coverity Connect owner:

- At the command line,
  execute:

  ```
  chown -R new_owner_username[:new_group] <installation_dir>
  ```
- Edit the config/system.properties file and change
  `os_user` to the new user name.

This has no effect on the database user name.
