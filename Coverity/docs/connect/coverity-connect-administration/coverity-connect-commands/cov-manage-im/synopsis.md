---
title: "Synopsis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synopsis.html"
content_id: "r3_aypUUFF5Txskpr1m4jQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:31.344090+00:00"
---

# Synopsis

```
cov-manage-im 
  --mode {defects|projects|streams|triage|motd|commit|notification|auth-key}
  <MODE OPTIONS>
  [CONNECTION_OPTIONS]
  [SHARED_OPTIONS]
```

**[CONNECTION_OPTIONS]**:

```
   [--auth-key-file <keyfile>]
   [--certs <filename>]
   [--host <server-hostname>]
   [--on-new-cert <trust | distrust>]
   [--password <password>]
   [--port <server-port >]
   [--ssl]
   [--url <path>]
   [--user <user_name>]
   [--userLdapServer <domain>]
```

**[SHARED_OPTIONS]**:

```
   [--config <coverity_config.xml>]
   [--debug]
   [--response-file <file>]
   [--verbose <level>]
```
