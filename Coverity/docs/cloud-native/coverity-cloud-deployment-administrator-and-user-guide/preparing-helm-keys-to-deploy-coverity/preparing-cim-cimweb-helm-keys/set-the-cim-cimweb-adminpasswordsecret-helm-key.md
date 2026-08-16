---
title: "Set the cim.cimweb.adminPasswordSecret Helm key"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/set-the-cim.cimweb.adminpasswordsecret-helm-key.html"
content_id: "rzYV_0eufOOGnhAOYu7Iag"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:28.648500+00:00"
---

# Set the cim.cimweb.adminPasswordSecret Helm key

Note: You should need to set this Helm key only once, when you develop
your custom Helm chart.

As of the 2024.9.0 release, you can specify an administrator password for Connect Web
application administrators within a secret. This enables you to set the administrator
password for the Connect Web UI, and include it in a deployment install, upgrade, or
update.

Note: To create the secret, see Create a Connect Web application administator password secret.

If you create a secret that contains the Connect Web application admin password, you must
specify the name of the secret within the `cim.cimweb.adminPasswordSecret:
"<secretName>"` Helm key which is located in the cnc chart. For example,
for the `webapp-admin-password.yaml` secret:

```
cim: 
  cimweb:
    adminPasswordSecret: "<secretName>"
```

or:

```
cim: 
  cimweb:
    adminPasswordSecret: "webapp-admin-password"
```

Provide the name of the secret that contains the Connect Web UI administrator password.

Alternatively, you can use the following Helm override in a Helm install command to
include this secret within a new or existing deployment:

```
--set cim.cimweb.adminPasswordSecret="<secretName>"
```

For example:

```
--set cim.cimweb.adminPasswordSecret="webapp-admin-password"
```

See also:

- cim.cimweb Helm keys
- Create a Connect Web application administator password secret
