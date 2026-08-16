---
title: "Generating a Integrity report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generating-a-integrity-report.html"
content_id: "OMA_Got87OPkZoy0F3Oj_g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:37.921842+00:00"
---

# Generating a Integrity report

The Integrity report can only be generated via command line, as it is unavailable in GUI
mode.

Make sure that Coverity Connect is running. To start Coverity Connect, you can use the
following command, which is located in the Coverity Platform
<install_dir>/bin:

```
> cov-start-im
```

Note: If you need to create a report more than once, close all
open PDF-based reports before regenerating the report.

To generate a Integrity report, use the `cov-generate-integrity-report` command
along with the following options:

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

**Example:**

```
cov-generate-integrity-report mydir/config.yaml --password console --project demo
```
