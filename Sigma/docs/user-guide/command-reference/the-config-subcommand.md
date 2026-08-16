---
title: "The config Subcommand"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-config-subcommand.html"
content_id: "t7xjPskmlHyUtlhfC8WKDw"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:33.309355+00:00"
---

# The config Subcommand

## Syntax

sigma
config
SUBCOMMAND

## Description

The `config` command manages configuration. Subcommands allow you to
create a default configuration, get command help, or validate a configuration.

| Subcommand | Description |
| --- | --- |
| create-default [`-f`, `--force`] [file] | Create a default configuration for Sigma analysis.  - Use `-f` flag to overwrite the   existing file. - Use the file parameter to specify   the name of the configuration file. |
| dump [`-f`, `--force`] [file] | Dump the aggregated configuration loaded from all sources.   - Use the `-f` flag to overwrite the   existing file. - Use the file parameter to specify the   name of the dump file.   Note: If you don't specify a file name, .sigma-config.yml will be used. |
| help | Display help for the sigma config command. |
| validate | Validate all the configuration settings from the command line and configuration files. |
