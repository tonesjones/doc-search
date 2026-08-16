---
title: "Managing the Connect Web application administator password"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-the-connect-web-application-administator-password.html"
content_id: "CxMIt3o7wsnSX33YuCEGqg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:53.358983+00:00"
---

# Managing the Connect Web application administator password

As of the 2024.9.0 release, you must specify an administrator password for Connect Web
application administrators. This enables you to set the administrator password for the
Connect Web UI, and include it in a deployment install, upgrade, or update. You set this
password by creating a secret, configuring a Helm key, and deploying the change. You can
change the password manually or automatically, by changing the value in the secret.

Important: When you deploy Connect for the first time, we
highly recommend that you create a secure password for future administrator access to
the Connect Web application. If you do not create a password, to re-connect to the web
app as administrator, you will need to manually create a password secret or contact
Black Duck Software for the default password.

Important: You must also specify the name of the password
secret in the `cim.cimweb.adminPasswordSecret:` Helm key.

Create the secret and update the `cim.cimweb.adminPasswordSecret` Helm key
in preparation for the initial deployment, as follows:

1. Create the secret. You perform this task when you initially create your custom Helm
   chart. See Create a Connect Web application administator password secret.
2. Set the `cim.cimweb.adminPasswordSecret` Helm key value to point to
   the Connect Web application administator password secret that you just created. See
   Set the cim.cimweb.adminPasswordSecret Helm key.
3. Deploy the Helm chart.

After this initial deployment, you can periodically change the password either
automatically using a script or other means, or manually. For example, to manually
change the password, see Manually changing a Connect Web application administator password.
