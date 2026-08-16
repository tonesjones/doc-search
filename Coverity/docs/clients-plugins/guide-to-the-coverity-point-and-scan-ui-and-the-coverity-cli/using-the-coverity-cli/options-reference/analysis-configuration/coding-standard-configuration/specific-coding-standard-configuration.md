---
title: "Specific coding standard configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specific-coding-standard-configuration.html"
content_id: "u9C37ipF_l75P_9ddSZc2Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:10.036025+00:00"
---

# Specific coding standard configuration

The following table describes they keys to specify a coding standard configuration.

| Key | Type | Description |
| --- | --- | --- |
| `pre-canned` | string | For C, C++, and Java: This key specifies the name of a pre-canned coding standard configuration to use. The available pre-canned coding standard configurations depend on the coding standard in question. These are detailed in the next table.  The special value `default` indicates that the default pre-canned configuration should be used for the coding standard. The `default` pre-canned configuration will correspond to the `all` configuration for each pre-canned coding standard configuration. |
| `config` | Resolved coding standard configuration | For C, C++, and Java: This key specifies the coding standard configuration for the given coding standard. The actual type of this key is specific to the particular coding standard.  This key is mutually exclusive with the `file` key.  A temporary configuration file will be generated containing the in-line configuration and then passed to the `cov-analyze` command using the `--coding-standard-config config_file` option. |
| `file` | string | For C, C++, and Java: This key specifies the filename containing the configuration to use for the corresponding coding standard. This key is mutually exclusive with the `config` key. |
