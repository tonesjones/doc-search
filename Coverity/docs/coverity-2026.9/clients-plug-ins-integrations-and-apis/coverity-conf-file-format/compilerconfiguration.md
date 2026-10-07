---
title: "CompilerConfiguration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/compilerconfiguration.html"
content_id: "tRZm_kV4w~7CBg8PsPsl~g"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:08.610213+00:00"
---

# CompilerConfiguration

A `CompilerConfiguration` describes how to invoke
`cov-configure` one time to configure one compiler, or a family of
compilers that can all be configured by a single invocation. It has the following
attribute:

cov_configure_args: string[]
:   A command line word sequence to pass to `cov-configure`.
