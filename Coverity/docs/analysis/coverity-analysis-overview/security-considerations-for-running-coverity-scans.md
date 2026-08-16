---
title: "Security considerations for running Coverity scans"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-considerations-for-running-coverity-scans.html"
content_id: "w7qC~MlyPr1Ich3fiDTXNw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:25.045843+00:00"
---

# Security considerations for running Coverity scans

To perform a high-fidelity analysis, Coverity collects the following data and stores it in the intermediate directory (`idir/`):

1. Source code
2. A semantic representation of the code; in other words, an *abstract syntax tree* (AST)
3. Cross-reference information
4. The commands used to build the software
5. The environment variables that were defined while the build was running

Given the potential sensitivity of this information and your concern about this, appropriate care should be taken to secure your `idir/`.
Commands used to build the software and environment variables defined during the build can be of particular concern, since they can contain passwords or
security tokens. The best practice is to avoid having any sensitive information on hard-coded command lines, and instead to store these in environment
variables.

Coverity does not store environment variables in its build-log.txt or configure-log.txt files
unless the environment variable COVERITY_LOG_ENVIRONMENT_VARIABLES is set to 1 or the --debug-flags envvars option is specified.
Environment variables on command lines such as `bash -c "MYVAR=secret command"` are still at risk, because command lines *are* logged.
Care must be taken to make sure that scripts such as Makefiles are not invoking commands in this way. To be sure of this, review the contents of the
build-log.txt file.

Environment variables are recorded in the emit database in the `idir/`.
Sensitive environment variables can be excluded from the emit database by adding them to the environment variable
COVERITY_FILTER_ENVVARS_DENYLIST; for example, `COVERITY_FILTER_ENVVARS_DENYLIST=var1,var2,...`.

Which environment variables are being recorded can be examined in two ways:
by setting `COVERITY_LOG_ENVIRONMENT_VARIABLES=1` and looking in the build-log.txt and configure-log.txt
files, or by using `cov-manage-emit --dir idir print-environment-variables`.

The environment variables stored in the emit database in the `idir/` are encrypted, which should protect your code from random scans of the
`idir/`; however, as just mentioned, they can be output by anybody using `cov-manage-emit --dir idir print-environment-variables`.
Since this is fairly weak protection, you should still take care to secure the `idir/`, but this setup does provide a degree of protection from
accidental exposure. To increase protection, we suggest you use a private key by defining an environment variable COVERITY_IDIR_KEY in a
similar way for all commands.
Defining this during a build, but not in subsequent commands, will result in decryption failures when environment variables are needed.
Use of a private key is not supported with Polaris at this time.

## See also

Sensitive data might persist on a local machine

Security considerations for TLS/SSL certificates

"Coverity Security Dynamic Analysis" in the 2026.6.0 Safety Manual
