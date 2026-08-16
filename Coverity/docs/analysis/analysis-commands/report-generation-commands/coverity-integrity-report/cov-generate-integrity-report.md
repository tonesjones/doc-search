---
title: "cov-generate-integrity-report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cov-generate-integrity-report.html"
content_id: "Od6lVKrPwLSCflI6JwbaDQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:09.367423+00:00"
---

# cov-generate-integrity-report

A command-line application for generating a Coverity Integrity Report.

## Synopsis

```
cov-generate-integrity-report <configuration-file>
    [--auth-key-file <auth-key-file> | --password <spec>]
    [--company-logo <company-logo>] 
    [--help]
    [--locale <locale>]
    [--on-new-cert <value>] 
    [--output <output-path-to-pdf>]     
    [--project <project-name>]    
    [--user <username>]
```

## Description

The `cov-generate-integrity-report` command runs the Coverity Integrity
Report application for generating a Coverity Integrity Report. For information about
the Coverity Integrity Report, see "Coverity Integrity report" in Configuring and Generating Coverity Reports.

## Options

**Optional arguments:**

`--company-logo`
:   Path to the company logo file.

`--help`
:   Display this help message and exit.

`--locale <locale>`
:   (Optional) Locale of the report. Default value: `en_US` (English).

    The
    Coverity Integrity report also supports `ja_JP`
    (Japanese).

    The CVSS report, MISRA report and Security report also
    support `ja_JP` (Japanese), `ko_KR` (Korean),
    and `zh_CN` (Simplified Chinese).

`--on-new-cert <value>`
:   (Optional) When connecting to the Coverity Connect server via TLS/SSL, this parameter
    specifies whether to trust (with trust-first-time) self-signed certificates,
    presented by the server, that the application has not seen before. The
    `<value>` parameter can have one of two values:

    `distrust`
    :   (The default) If the certificate is self-signed, the connect attempt will fail.

    `trust`
    :   The certificate will be accepted, even if it is self-signed.

        CAUTION:

        Setting `on-new-cert` to
        `trust` does not currently work with Coverity Analysis and
        Black Duck® Bridge. The workaround is to manually
        add the self-signed certificate to your operating system's
        certificate store. This will tell the operating system that it can
        trust this certificate, and should allow you to continue.

    For information on the TLS/SSL certificate management functionality, please
    see Coverity Platform 2026.6.0 User and Administrator Guide.

`--output <output_file>`
:   (Optional) Specifies a PDF file in which to save the report.

    If a file of this name
    already exists, the new report overwrites the old one.

`--project <project-name>`
:   (Optional) Name of the Coverity project to assign defect metrics. This can be set via
    command line or entered directly in the YAML configuration file.

    Note that if a user has already set the project in the
    config.yaml file and also tries to set the
    `--project` name through the command line, the command
    line will supercede what is written in the configuration file.

`--user <username>`
:   Username for connecting to Coverity Connect. This can be set via command line or entered
    directly in the YAML configuration file.

**Required arguments:**

`--auth-key-file <auth-key-file>`
:   (Required if `--password` is not present.) Specify the location of a
    previously created authentication key file, used for connecting to the Coverity
    Connect server. Authentication keys can be registered with a Coverity Connect
    instance and used for authentication in place of the `--user` and
    `--password` options. See "Working with
    authentication keys" in the Coverity Platform 2026.6.0 User and Administrator Guide.

`<configuration-file>`
:   A .yaml file containing server configuration, Coverity
    Connect project, and other report-related parameters.

    For detailed information about configuration values, please see the "Configuring report
    generators" section of the Configuring and Generating Coverity Reports and the README to which it
    refers.

`--password <spec>`
:   (Required if `--auth-key-file` is not present.) Specifies how to provide your
    Coverity Connect password. The password `<spec>` has one
    of the following forms:

    `console`
    :   Tells Coverity Connect to prompt for the password from standard input. Coverity Connect
        does not echo the password characters.

    `file:<filename>`
    :   Tells Coverity Connect to read the password from the specified file.

        Entering `file:-` tells Coverity Connect to
        prompt for the file name from standard input. This is used with
        pipes and redirection.

    `env:<variable>`
    :   Tells Coverity Connect to read the password from the specified environment variable.

## Example

`cov-generate-integrity-report`

## Exit codes

Most Coverity Analysis commands can return the following exit codes:

- 0: The command successfully completed the requested task.
- 1: The requested task is complete, but it did not return (or find) any results.
  Note that some Coverity Analysis commands do not return this error code.
- 2: The command was unable to complete the requested task. This error typically
  includes an error message and some remediation advice.
- 4: An unexpected error occurred. This error should not occur when the product is
  used in a supported way. Very likely, the requested task was not completed. This
  error typically provides some diagnostic and/or debugging output, such as a
  stack trace.

For exceptions, see cov-commit-defects, cov-analyze, and cov-build.
