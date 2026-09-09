---
title: "Scan Request File"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/scan-request-file.html"
content_id: "QGJlbYoXlXoua0VcE1nRBw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:43.979813+00:00"
content_hash: "945dbb270b964b9b9d050d434ae0299818a1ede8a8b9a2dbc8ce103818581335"
---

# Scan Request File

An add-in tool is based on a scan request file that you define and register with Software
Risk Manager. A scan request file contains the instructions that the tool service needs
to invoke an application security testing tool on the k8s cluster and ingest its output
into Software Risk Manager. Scan request files use the [TOML](https://github.com/toml-lang/toml)
file format. You can specify any valid TOML content in your tool's scan request file
provided you specify the `request` table, which is a reserved section
with the following parameters.

Table 1.

| Key | Description | Required? |
| --- | --- | --- |
| `imageName` | The name of the Docker image containing your add-in tool | Yes |
| `workDirectory` | The work directory where your add-in tool can find tool inputs | Yes |
| `shellCmd` | The Bourne shell command to invoke your add-in tool | Yes |
| `resultFilePath` | The output of your add-in tool | Yes |
| `logFilePaths` | An array of log files produced by your add-in tool | No |
| `preShellCmd` | An optional command to run prior to invoking the shellCmd | No |
| `postShellCmd` | An optional command to run after invoking the shellCmd | No |
| `securityActivities` | The Intelligent Orchestration security activities supported by this tool (e.g., sca, sast, dast) | No |

A tool run ends in an error when either shellCmd, preShellCmd, or postShellCmd return a
non-zero exit code. When the tool service runs an add-in tool, it creates the following
directory structure at the path specified by the value of the
`workDirectory` key.

Table 2.

| Content | Description |
| --- | --- |
| `/ca-certificates` | A directory containing zero or more certificates that should be considered trusted certificate authorities |
| `/config/request.toml` | A copy of the tool's scan request file, including any project-specific configuration |
| `/input` | A directory containing an optional input file |
| `/volume-secret` | A system directory required for storing tool outputs |
| `/workflow-secrets` | Zero or more workflow secrets associated with an add-in tool's project configuration |

When the tool service invokes an add-in tool, it provides the tool with a copy of its
scan request file, so the file is a convenient place to store configuration data. After
you register an add-in tool, Software Risk Manager lets you edit TOML content outside
the `request` table on a per-project basis, so you can have key values
that vary by project. For example, a DAST tool might have a scan request file with a key
whose value indicates the URL from which to start a scan; the URL can vary from one
Software Risk Manager project to the next.
