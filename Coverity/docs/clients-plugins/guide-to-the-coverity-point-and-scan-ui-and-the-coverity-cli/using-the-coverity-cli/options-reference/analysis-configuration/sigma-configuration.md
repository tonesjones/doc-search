---
title: "Sigma configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sigma-configuration.html"
content_id: "F94oUFJyBxF~yNiE~GVamw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:15.842126+00:00"
---

# Sigma configuration

This optional key specifies a set of Sigma checks to run.

**Location in the configuration file (YAML format):**

```
analyze:
    sigma:
        base-check-set: <string> [all, cis, default, empty]
        enable-check-set: <list of values>
        malicious-url-patterns-file: <list of values>
```

| Key | Type | Description |
| --- | --- | --- |
| `base-check-set` | string | Similar to the `enable-check-set` option, but specifies only a single *base set* of checks at a time. Enables a base set of checks. Only one of the following values can be specified in the configuration:  `"all"`  Enables all checks, except for checks that are disabled, either by default, or by explicitly disabling them with the `--disable` option.  `"cis"`  Enables the CIS (Center for Internet Security) benchmark checks.  `"default"`  Enables all Sigma checks, except for the disabled checks (those either disabled by default, or explicitly disabled with the --disable option).  `"empty"`  Disables all Sigma checks, except for the checks which are explicitly enabled using the --enable option.  If this option is not specified, the default set of checks is enabled. |
| `enable-check-set` | array of strings | A list of Sigma check sets to enable.  `"all"`  Enables all checks, except for checks that are disabled, either by default, or by explicitly disabling them with the `--disable` option.  `"cis"`  Enables the CIS (Center for Internet Security) benchmark checks.  `"default"`  Enables all Sigma checks, except for the disabled checks (those either disabled by default, or explicitly disabled with the --disable option).  `"empty"`  Disables all Sigma checks, except for the checks which are explicitly enabled using the --enable option.  If this option is not specified, the default set of checks is enabled. |
| `malicious-url-patterns-file` | array of strings | A list of files used to customize the behavior of the `SIGMA.malicious_url` checker, which is used to detect malicious URLs in source code.  A file given as a value for the `malicious-url-patterns-file` setting should contain a list of URLs that need to be reported, with one URL per line. |
