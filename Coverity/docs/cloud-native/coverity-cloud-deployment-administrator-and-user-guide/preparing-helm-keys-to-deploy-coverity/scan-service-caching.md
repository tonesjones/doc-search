---
title: "Scan Service caching"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-service-caching.html"
content_id: "GomjFWtb3K0Sa1Y~Fq1F8A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:49.336997+00:00"
---

# Scan Service caching

If you are using Scan Service, you can optionally use caching via the Cache Service.
Caching improves analysis performance when running subsequent scans after an initial
scan of a project. Caching avoids needing to upload libraries and modules that have
already been uploaded and have not changed since the last scan. Also, caching reuses
partial analysis of unchanged modules, saving scan time. Caching can include jars
(Java), DLLs (.NET), Translation Units (TU) and intermediate work products from scans.
The benefits vary depending upon the language which drives the caching types that are
enabled.

Coverity uses the following caching:

- bytecode caching - Coverity caches bytecode (Jar and DLL) files, reducing the amount
  of data that needs to be uploaded on subsequent scans when used with Java and C#
  projects. Caching of Jar and DLL files is enabled by default.
- decompilation caching - Coverity stores decompiled code in the cache.
- results caching - Coverity stores code analysis output (results) in the cache.

In the `values.yaml` file, you can enable caching and configure caching
options. For cache Helm key descriptions, refer to scan-services Helm subchart: Helm keys.

Note: For cache installation and requirements, refer to Create and configure a cache storage bucket.

Note:

For cloud provider caching information, refer to the appropriate cloud provider
subsection in Infrastructure and configuration:

- Amazon AWS infrastructure and configuration
- Google GCP infrastructure and configuration
- Microsoft Azure infrastructure and configuration

Note: Caching requires a prior full analysis of a coding project as a
baseline.

When planning and scanning code projects, caching can be configured as part of the
Coverity configuration options or command line options. Refer to the Coverity Analysis 2026.6.0 User and Administrator Guide.

## Redis

If caching is deployed, you must install the Redis Remote Directory Server or an
equivalent tool to manage data structures in the cache.

For information on the supported Redis version, see .

For information on setting up Redis keys in the Helm chart, see Redis keys.
