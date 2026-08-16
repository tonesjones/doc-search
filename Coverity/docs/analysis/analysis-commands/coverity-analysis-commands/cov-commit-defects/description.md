---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "qc5rhufpd6vVlgKkIEregw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:11.879373+00:00"
---

# Description

The `cov-commit-defects` command reads analysis output and source data
stored in an intermediate directory and writes the data to a Coverity Connect instance
in a stream that you specify. The data are written as a unit; this unit is a
snapshot.

The command passes the data to the Coverity Connect server either through the server's HTTPS
port or its Commit port, depending on the command-line options you choose. You should
use the HTTPS port because the Commit port is deprecated and will be removed in a future
release. (Passing data through the HTTPS port employs the feature known as "commit over
HTTPS".)

To use the HTTPS port, both Coverity Connect and Coverity Analysis must be release
2020.12 or later and you must use one of the following command options:

- The `--url` option with a scheme of `https`, for
  example:

  ```
  --url https://my_domain.com:8443
  ```
- The `--https-port` option. (This option is not recommended because
  it is deprecated and will be removed in a future release.)

See the --url option for more information
about sending data to the HTTPS port.

The Commit port is used if any of the following are true:

- Coverity Connect is older than release 2020.12.
- Coverity Analysis is older than release 2020.12.
- You use the `--dataport` command option. (This option is
  deprecated and will be removed in a future release.)
- You use the `--url` command option with a `commit`
  scheme, for example:

  ```
  --url commit://my_domain.com:9999
  ```

  (This scheme is deprecated and will be removed in a future release.)

Note: Although you can use the HTTP port instead of the HTTPS port, HTTP is not secure and
is therefore suitable only for demonstration purposes. For information on how to use the
HTTP port, see the --url
option.

Commits conducted over the HTTPS port are always secure.

Commits
conducted over the Commit port are secure by default but can be conducted without
security if the Coverity administrator configures the server to not enforce
security.

After you perform a commit, you can view the defects in Coverity Connect alongside the
source code that generated them. The issues in the intermediate directory are discovered
through the cov-analyze command.

Note: It is possible to use the `cov-build` command to capture builds for
many different languages to the same intermediate directory. The target stream's
"Language" configuration setting must match the source code language in the intermediate
directory. The recommended "Any" setting accepts everything, including mixed-language
intermediate directories.

After a successful commit, `cov-commit-defects` checks for any new
Coverity Analysis updates. If there are updates, a message appears with the number of
updates that you can download. Use the `cov-install-updates` command to
manage and install the updates.

Note:
SCM-related command line
options (`--scm*`) are used to collect SCM (source code
management) data solely for the purposes of automatic ownership assignment (see the `cov-blame` documentation and the Coverity Platform 2026.6.0 User and Administrator Guide).
To display SCM data in the Coverity Connect source browser, use
`cov-import-scm` prior to running
`cov-analyze`.

This command requires that source files remain in
their usual locations in the checked-out source tree. If the files are copied to a
new location after checkout, the SCM query will not work.
