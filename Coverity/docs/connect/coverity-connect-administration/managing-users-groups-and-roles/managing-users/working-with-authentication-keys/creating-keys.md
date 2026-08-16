---
title: "Creating keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-keys.html"
content_id: "L1SYMgDLYuwlWSQTa1ZWSw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:37.256142+00:00"
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
