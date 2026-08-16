---
title: "Generating a previously configured report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generating-a-previously-configured-report.html"
content_id: "i90wJkMUTRyO_D7tVtqkug"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:11.730344+00:00"
---

# Generating a previously configured report

You can save the configuration for a report as a .yaml file, and then use
this configuration file to regenerate the report, with the same settings, when the
analysis data is updated. You can regenerate the report using the GUI or the command
line.

## Regenerating a report through the GUI

1. Launch the `cov-cert-report` application.
2. Click File > Open Configuration, and select an existing configuration file.
3. Click Create Report to generate the report.

## Regenerating a report through the command line

You can generate a report based on a previously saved configuration by running
`cov-generate-cert-report` with the following settings:

```
cov-generate-cert-report <config-file>
    [--auth-key-file <auth-key-file> | --password <spec>]
    [--help] 
    [--on-new-cert [ trust | distrust ] ]
    [--output <output-file>]
```

**Optional arguments:**

`--help`
:   Display this help message and exit.

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
