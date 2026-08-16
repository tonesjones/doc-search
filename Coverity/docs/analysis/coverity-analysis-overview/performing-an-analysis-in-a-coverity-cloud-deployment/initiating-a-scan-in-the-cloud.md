---
title: "Initiating a scan in the cloud"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/initiating-a-scan-in-the-cloud.html"
content_id: "XamtjEZeivy5vmJGclQIAw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:35.698655+00:00"
---

# Initiating a scan in the cloud

As noted in Scan workflows, to perform a scan, you can initiate the scan at
the command line (CLI) by issuing either a single `coverity scan` command
or by issuing the series of commands `coverity capture`, `coverity
analyze`, and `coverity commit` to perform the scan steps one
at a time. Also, for CI/CD, you can develop scripts to run scans. These scripts can
include the command line parameters that define the scan.

You can create a configuration file, `coverity.yaml` or
`coverity.json`, to provide command options to coverity commands,
thereby simplifying the command that you issue at the command prompt. Parameters
specified in the command line override parameters defined in a configuration file.

Note: See the following sections in the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI
for more information:

- "Specify where to commit scan results"
- "Options reference"
- "Using
  the Coverity CLI to override configuration defaults"

## Coverity cloud scan parameters

To run scans in Kubernetes containers in the cloud, you use a number of parameters that direct
the scans to cloud-based containers, as well as other required or optional
parameters to manage performance, etc. You can configure these parameters either at
a command line or in the `coverity.yaml` configuration file. When
designing a CI/CD pipeline, you can provide these parameters within scripts to run
and configure scans in the cloud.. This enables you to perform scans without needing
to create a configuration file.

Attention: The Coverity CLI has a known issue when
reading the Coverity Connect password in the Cygwin shell using the `coverity
setup` or `coverity scan` commands. To work around this
issue, run `coverity setup` using the Windows command shell
`cmd.exe`. You can then switch back to the Cygwin shell.

You can specify the following Coverity cloud parameters at either a command line or in the
`coverity.yaml` config file:

Table 1. Coverity cloud scan parameters

| Option | Description |
| --- | --- |
| `COVERITY_CLI_CONNECT_USERNAME` and `COVERITY_CLI_CONNECT_PASSWORD` | **Coverity Connect authentication**: Specify the environment variables `COVERITY_CLI_CONNECT_USERNAME` and `COVERITY_CLI_CONNECT_PASSWORD` to authenticate Coverity Connect. |
| ``` -o commit.connect.url=<URL> ``` | **Connect URL**: Specify the Connect URL.  **CLI example**  To to override the value set in the `coverity.yaml` file, and specify the Connect URL in the CLI command, add the option:   ``` coverity scan -o commit.connect.url=<URL> ```   **`coverity.yaml` config file example**  To specify the Connect URL in the `coverity.yaml` file, add the environment variable:   ``` commit:   connect     url <URL> ``` |
| ``` -o commit.connect.stream=<streamName> ``` | **Stream name**: Specify the stream name.  **CLI example**  To to override the value set in the `coverity.yaml` file, and specify the stream name in the CLI command, add the option:   ``` coverity scan -o commit.connect.stream=<streamName> ```   **`coverity.yaml` config file example**  To specify the stream name in the `coverity.yaml` file, add the environment variable:   ``` commit:   connect:     stream: <streamName> ``` |
| ``` -o analyze.location=<location> ``` | Optional: **Analysis location**  `analyze.location` specifies the scan (analysis) location:  - `-o analyze.location=connect` perform the   scan (analysis) in the cloud. - `-o analyze.location=local` perform the   scan locally. This option is available for classic   Coverity, or if the full Coverity Analysis client is installed   on the client system. It will not work with Thin Client.  **CLI example**  To set the CLI command to override the value set in the `coverity.yaml` file, and perform the analysis within a Kubernetes container in the cloud, add the option:   ``` coverity scan -o analyze.location=connect ```   **`coverity.yaml` config file example**  To configure the `coverity.yaml` file to perform analysis within a Kubernetes container in the cloud, add the environment variable:   ``` analyze:   location: connect ``` |
| ``` --pool-size <size> ``` | Optional: **pool (container) size**  `analyze.pool-size` specifies the analysis container size. Valid values:   - `small` (not case sensitive) - `medium` (not case sensitive) - `large` (not case sensitive) - `extralarge` (not case sensitive) - Custom pool names (case-sensitive, as configured by the   Coverity cloud administrator) - Empty string or omitted: Uses automatic pool selection   (default behavior)   **CLI example**  To specify the analysis pool size in the CLI command, add the option:   ``` coverity scan --pool-size large ```   **`coverity.yaml` config file example**  To specify the container size in the `coverity.yaml` file, add the environment variable:   ``` analyze:   pool-size: extralarge ```   To override the value set in the `coverity.yaml` file:   ``` coverity scan -o analyze.pool-size=large ``` |

**Examples**

These values can be set within the `coverity.yaml` config file. For
example:

```
COVERITY_CLI_CONNECT_USERNAME=<userName>
COVERITY_CLI_CONNECT_PASSWORD=<password>
commit.connect.url=https://connect.example.com:8443
commit.connect.stream=my-project
analyze.location=connect
analyze.pool-size=medium
```

The following example, uses the `-o` (override) option to override values in
the `coverity.yaml` file:

```
$ COVERITY_CLI_CONNECT_USERNAME=<userName> \
  COVERITY_CLI_CONNECT_PASSWORD=<password> \
  coverity scan -o commit.connect.url=https://connect.example.com:8443 \
                -o commit.connect.stream=my-project \
                -o analyze.location=connect \
                -o analyze.pool-size=medium
```
