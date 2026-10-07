---
title: "Creating keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/creating-keys.html"
content_id: "L1SYMgDLYuwlWSQTa1ZWSw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:08.648386+00:00"
---

# Creating keys

Users can create authentication keys from the Coverity Connect UI or from the command line.

**To create a key from the UI:**

1. After logging in to Coverity Connect, select
   <User> > Authentication Keys...

   The "Manage My Authentication Keys" page displays.
2. In the New Authentication Key field, enter a name for the key.
3. Click Create and Download.

**To create a key from the command line:**

1. Create the key using the `cov-manage-im` command in `auth-key` mode.
   For example:

   ```
   cov-manage-im --host <host_name> --port <port_number> \ 
                 --user <user_name> --password <password> --mode auth-key \
                 --create --output-file <keyfile>
   ```

**To set an expiration date for the key:**

1. Use the `--set-expiration` option with the `cov-manage-im` command.
   For example:

   ```
   cov-manage-im --host <host_name> --port <port_number> \ 
                		      --user <user_name> --password <password> --mode auth-key \
                                    --create --output-file <keyfile> \
                                    --set expiration:2030-12-31
   ```

   There are other options for how to specify the date:
   See "Authentication key mode" in the *Coverity Command Reference.*

**To set an expiration date for the key using the cim.properties file:**

1. Use the cim property `cim.authkey.expiration.duration` to set the
   expiration duration of authentication keys in hours, days, months or years in
   the format <durationValue><unit>, for example 10h. Accepted units are
   hours (h/H), days (d/D), months (m/M) and years (y/Y). The default value is 30Y
   (30 years). For
   example:

   ```
   cim.authkey.expiration.duration=20Y
   ```

   Note: The `cim.authkey.expiration.duration`
   property specifies the default and maximum expiration duration for
   authentication keys. The default value is `30Y` (30
   years).
