---
title: "Compiler configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compiler-configuration.html"
content_id: "WZUInLdJ7ooqa2F2nlPlAQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:02.048893+00:00"
---

# Compiler configuration

Use one or the other of these keys to specify compiler configuration. You may not use both.

| Key | Type | Description |
| --- | --- | --- |
| `file` | string | Specifies a previously generated compiler configuration file to use. This key is mutually exclusive with the `cov-configure` key. |
| `cov-configure` | array of array of strings | Specifies a list of arguments to pass to `cov-configure` to generate the compiler configuration to use during capture. This key is mutually exclusive with the `file` key. |
