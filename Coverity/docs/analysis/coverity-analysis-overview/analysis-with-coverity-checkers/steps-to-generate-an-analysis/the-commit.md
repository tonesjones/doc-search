---
title: "The commit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-commit.html"
content_id: "lbnT~o6iokCJsR1dxLIrQA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:48.514628+00:00"
---

# The commit

After completing the analysis, you commit (or "push") the analysis results to Coverity Connect
so that developers and team leads can view, manage, and fix the software issues that they own.

Run `cov-commit-defects` to add the defect reports to the Coverity Connect database.

Note:
If it has been set up to do so, developers and team leads can also view issues in Coverity Desktop.

Here is the general format of invoking `cov-commit-defects:`

```
> cov-commit-defects  --url <server_url> \
  --dataport <port_number> \
  --stream <stream_name> \
  --user admin --dir <intermediate_directory>
```

- `--stream`: The `<stream_name>` value specifies an
  existing Coverity Connect stream (see analysis Prerequisites).
- <intermediate_directory> is the directory that contains the
  defect reports.

For example:

```
> cov-commit-defects --url coverity_server1 \
  --dataport 9090 --stream apache --dir apache_int_dir \
  --user admin --password 1256
```

When the commit is successful, Coverity Analysis displays a message that looks like the following:

```
Connecting to server 10.9.9.99:9090
2013-10-11 23:47:49 UTC - Committing 34 file descriptions...
|0----------25-----------50----------75---------100|
****************************************************
2013-10-11 23:47:49 UTC - Committing 34 source files...
|0----------25-----------50----------75---------100|
****************************************************
2013-10-11 23:47:49 UTC - Calculating 34 cross-reference bundles...
|0----------25-----------50----------75---------100|
****************************************************
2013-10-11 23:47:50 UTC - Committing 34 cross-reference bundles...
|0----------25-----------50----------75---------100|
****************************************************
2013-10-11 23:47:51 UTC - Committing 12 functions...
|0----------25-----------50----------75---------100|
****************************************************
2013-10-11 23:47:51 UTC - Committing 12 defect files...
|0----------25-----------50----------75---------100|
****************************************************
2013-10-11 23:47:53 UTC - Committing 3 output files...
|0----------25-----------50----------75---------100|
****************************************************
New snapshot ID 10001 added.
Elapsed time: 00:00:05
```

## Specifying ports and domains

- --dataport and --port: When you run
  `cov-commit-defects`, you have a choice of specifying
  --dataport (the default is `9090`) or
  --port (the default is `8080`). The Coverity Connect installer refers to the data port as the
  *commit port*.

  Note: If you are committing to a TLS/SSL-enabled instance of Coverity
  Connect, use the `--https-port` option instead of
  `--port`. For more information, see the description of `cov-commit-defects` in the Coverity 2026.6.0 Command Reference

## For more information:

For information about compatibility between different versions of Coverity Connect and Coverity Analysis, see Compatibility between Coverity product components in the Coverity 2026.6.0 Installation and Upgrade Guide.

For more information about using Coverity Connect to view and manage issues, see
"Understanding the primary Coverity Connect workflows
in Coverity Platform 2026.6.0 User and Administrator Guide.
