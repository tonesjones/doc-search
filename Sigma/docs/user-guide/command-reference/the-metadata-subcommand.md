---
title: "The metadata Subcommand"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-metadata-subcommand.html"
content_id: "LZji~EAEIwsa5rWvcnZoiA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:35.195459+00:00"
---

# The metadata Subcommand

## Syntax

sigma
metadata
SUBCOMMAND

## Description

The `sigma metadata` command manages documentation. Subcommands allows you to
output Sigma's metadata, output the hardcoded secret patterns, or get command
help.

| Subcommand | Description |
| --- | --- |
| documentation [help | json [FLAGS]] | The `sigma metadata documentation` command allows you to output Sigma's metadata, or get help for printing the information.   - Use `sigma metadata documentation help` to display help for this   subcommand. - Use `sigma metadata documentation json [FLAGS]` to   output Sigma's metadata as a JSON file. |
| hardcoded-secret-patterns [help | text [FLAGS]] | The `sigma metadata hardcoded-secret-patterns` command allows you to output the hardcoded secret patterns, or get help for printing the information.   - Use `sigma metadata hardcoded-secret-patterns   help` to display help for this subcommand. - Use `sigma metadata hardcoded-secret-patterns text   [FLAGS]` to output the   hardcoded secret patterns as a text file. |
| help | Display help for the sigma metadata command. |

## Flags for `sigma metadata documentation`

| Flag | Description |
| --- | --- |
| `-h`, `--help` | Print help information. |
| `-o, OUTPUT`, `--output OUTPUT` | Specify the file to save the output to. You can also set this value using the environment variable `SIGMA_METADATA_DOCUMENTATION_JSON_OUTPUT`.  If unspecified, the output is written to the standard output (`stdout`). |
| `-p`, `--pretty` | Pretty-print the JSON output. This is equivalent to setting the environment variable `SIGMA_METADATA_DOCUMENTATION_JSON_PRETTY` to `1`. |
| `-s`, `--schema` | Output the JSON schema instead of the metadata. This is equivalent to setting the environment variable `SIGMA_METADATA_DOCUMENTATION_JSON_SCHEMA` to `1`. |
| `-v VERSION`, `--version VERSION` | Specify the version of the output.  This allows locking into a specific version of the output. One situation where you might want to do this is if you need to delay upgrading to a new version, if you have a script that is incompatible. To include taxonomy information, set the version to `v2` (or higher). You can also set this value using the environment variable `SIGMA_METADATA_DOCUMENTATION_JSON_VERSION`.  Possible values: `v1`, `v2`.  Default value: the highest version (`v2`). |

## Flags for `sigma metadata hardcoded-secret-patterns`

| Flag | Description |
| --- | --- |
| `-h`, `--help` | Print help information. |
| `-o, OUTPUT`, `--output OUTPUT` | Specify the file to save the output to. You can also set this value using the environment variable `SIGMA_METADATA_HARCODED_SECRET_PATTERNS_OUTPUT`.  If unspecified, the output is written to the standard output (`stdout`). |

## Examples

`./sigma metadata documentation json -p -o sigma-checkers.json -v v1`

`./sigma metadata hardcoded-secret-patterns text --output hcs.txt`
