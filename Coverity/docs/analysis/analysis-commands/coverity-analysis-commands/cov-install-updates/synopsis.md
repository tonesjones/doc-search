---
title: "Synopsis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synopsis.html"
content_id: "uQ2oRirjc662Z2WOL1VHUg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:29.283329+00:00"
---

# Synopsis

```
cov-install-updates 
    <COMMANDS> <COMMAND OPTIONS> 
    [SHARED_OPTIONS]
```

**COMMANDS and COMMAND OPTIONS:**

```
check 
    [--installer-dir] 
    [--installation-dir] 
    [CONNECTION_OPTIONS]
```

```
install 
    [--continue] 
    [--end-version] 
    [--force] 
    [--installer-dir] 
    [--installation-dir] 
    [CONNECTION_OPTIONS]
```

```
cov-install-updates list 
    [--installer-dir] 
    [--installation-dir] 
    [--show raw|upgrades}] 
    [CONNECTION_OPTIONS]
```

```
cov-install-updates rollback 
    [--force] 
    [--installer-dir] 
    [--installation-dir]
```

```
cov-install-updates version 
    [--installation-dir]
```

**[CONNECTION_OPTIONS]**:

```
    [--auth-key-file <keyfile>]
    [--authenticate-ssl]    
    [--certs <filename>]
    [--connect-timeout <n>]
    [--dataport <coverityconnect_commitport>]
    [--host <coverityconnect_host>]
    [--https-port <coverityconnect_port>]
    [--max-retries <n>]
    [--on-new-cert <trust | distrust>]
    [--port <coverityconnect_port>]
    [--response-timeout <n>]
    [--sleep-before-retry <n>]
    [--ssl]
    [--user <username>]
    [--password <password>]
    [--url <path>]
```

**[SHARED_OPTIONS]**:

```
    [--debug]
    [--ident]    
    [--verbose <level>]
```
