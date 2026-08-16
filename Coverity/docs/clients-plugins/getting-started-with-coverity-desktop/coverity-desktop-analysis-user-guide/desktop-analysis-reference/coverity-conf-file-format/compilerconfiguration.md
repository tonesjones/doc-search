---
title: "CompilerConfiguration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/compilerconfiguration.html"
content_id: "tRZm_kV4w~7CBg8PsPsl~g"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:25.985040+00:00"
---

# CompilerConfiguration

A `CompilerConfiguration` describes how to invoke
`cov-configure` one time to configure one compiler, or a family of
compilers that can all be configured by a single invocation. It has the following
attribute:

cov_configure_args: string[]
:   A command line word sequence to pass to `cov-configure`.
