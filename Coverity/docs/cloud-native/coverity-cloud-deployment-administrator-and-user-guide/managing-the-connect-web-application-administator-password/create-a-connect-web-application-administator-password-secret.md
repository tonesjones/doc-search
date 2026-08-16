---
title: "Create a Connect Web application administator password secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-connect-web-application-administator-password-secret.html"
content_id: "W~DsSphpkN_2l6zvZt_RXQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:54.666642+00:00"
---

# Create a Connect Web application administator password secret

As of the 2024.9.0 release, you can specify an administrator password for Connect Web
application administrators within a secret. This enables you to set the administrator
password for the Connect Web UI, and include it in a deployment install, upgrade, or
update.

As of 2024.12.0, when you change a password, you must comply with password
requirements.

Note: After you create this password secret, you can subsequently
change the password by editing the secret.

Note: As of 2024.12.0, when you change a password, you must comply
with password requirements. See the password requirements here: Connect Web application administator password requirements.

Note: If you upgrade to 2024.12.0 or newer from an older release, you
can continue to use your non-compliant password. However, when you change the password,
you must comply with the password requirements from then on. Changing the password
triggers the compliance mechanism.

To create a secret and specify the name of the secret in the Helm chart:

1. Create the following `webapp-admin-password.yaml` file.

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: ${secretName}
   type: Opaque
   stringData:
     password: "${password]"
   ```

   For example, to create a password secret named
   `webapp-admin-password`:

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: webapp-admin-password
   type: Opaque
   stringData:
     password: "myPaswd!11"
   ```

   You can create the secret using the following `kubectl`
   command:

   ```
   kubectl create secret generic "${secretName}" --from-literal=password="${password]"
   ```

   For example, to create a secret named `webapp-admin-password` and
   password `myPaswd!11`:

   ```
   kubectl create secret generic "webapp-admin-password" --from-literal=password="myPaswd!11"
   ```

   Using this password object in this secret, you can manage the Web application
   administrator password.
2. After you create the secret, you must specify the name of the secret in the
   `cim.cimweb.adminPasswordSecret: "<secretName>"` Helm key
   which is located in the cnc chart. See Set the cim.cimweb.adminPasswordSecret Helm key.

   Alternatively, you can use the following Helm override in a Helm install command
   to include this secret within a new or existing deployment:

   ```
   --set cim.cimweb.adminPasswordSecret="<secretName>"
   ```

   For example:

   ```
   --set cim.cimweb.adminPasswordSecret="webapp-admin-password"
   ```

   See also:

   - Set the cim.cimweb.adminPasswordSecret Helm key
   - cim.cimweb Helm keys
