---
title: "Manually changing a Connect Web application administator password"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/manually-changing-a-connect-web-application-administator-password.html"
content_id: "zPZYjKXIdxL~IRxdQmUhbQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:55.972223+00:00"
---

# Manually changing a Connect Web application administator password

You can automate password updates, however to manually edit a password that is within a
secret, modify the data field in your manifest and apply the file to your cluster.

1. You can edit the existing secret password object using the command:

   ```
   kubectl edit secrets <secret-name>
   ```

   For example, to change the password in the
   `webapp-admin-password.yaml` file:

   ```
   kubectl edit secrets webapp-admin-password
   ```
2. This opens the secret in an editor.

   ```
   apiVersion: v1
   data:
     password: "myPaswd!11"
   kind: Secret
   ...
   ```
3. Change the password, then save and close the edited file. For example, change the password`"myPaswd!11"`:to
   `"myNEWPaswd!22"`.

   Note: You must comply with password requirements listed here:
   Connect Web application administator password requirements.

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: webapp-admin-password
   type: Opaque
   stringData:
     password: "myNEWPaswd!22"
   ```
4. Apply the update to your cluster using the `helm upgrade`
   command.
