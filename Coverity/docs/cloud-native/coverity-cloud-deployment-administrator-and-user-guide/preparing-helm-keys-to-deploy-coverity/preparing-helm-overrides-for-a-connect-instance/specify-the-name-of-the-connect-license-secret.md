---
title: "Specify the name of the Connect license secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specify-the-name-of-the-connect-license-secret.html"
content_id: "sEgTpW8sJdPZzGxkEVuTPg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:22.112664+00:00"
---

# Specify the name of the Connect license secret

In the `licenseSecretName` root Helm key within the `cnc`
chart, you need to specify the name of the secret that contains the Coverity Connect
license. For example, for a secret named 'connectsecret', change the default value:

```
licenseSecretName: ""
```

to:

```
licenseSecretName: "connectsecret"
```

This secret was created in Create a Connect license secret.

For further information on the `licenseSecretName` key, see Root Helm keys.
