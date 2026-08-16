---
title: "Downloading and installing the Signature Scanner CLI"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/downloading-and-installing-the-signature-scanner-cli.html"
content_id: "kDMN1WSrV0ZsOS~853YScQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:36.114542+00:00"
---

# Downloading and installing the Signature Scanner CLI

Ensure your client meets
the requirements and then download and install the Signature Scanner CLI.

## Downloading the Signature Scanner CLI

The Signature Scanner CLI is packaged as a .zip file. Download it from
the Black Duck application.

Before downloading the Signature Scanner CLI, be sure that:

- Your Black Duck
  license is enabled for Component Scanning.
- Your Black Duck account has the Global or Project Code
  Scanner role.
- Your Black Duck license is enabled for Component
  Scanning.
- Your Black Duck account has the Global or Project
  Code Scanner role.

Note: Java Runtime Environment (JRE) is included with the download of Signature Scanner. However, there may be situations that require you
to use your version of JRE, for example you have self-signed certificates stored in
a preferred version of Java or your company policy only allows you to run a specific
version of JAVA or JRE. In these instances, you need to set the BDS_JAVA_HOME environment variable
prior to running Signature Scanner.

To download the Signature Scanner CLI from the Black Duck user interface:

1. Log in to Black Duck SCA.
2. Navigate to the drop-down menu under your username, and select
   **Tools**.
3. On the Tools page under **Legacy Downloads**, click the expand arrow to
   view and select the download link for the Linux, Mac OS X, or Windows CLI of
   the Signature Scanner.

## Installing the Signature Scanner CLI

Install the scanner on the computer that contains the archives to be scanned. You
cannot scan archives on a remote server.

To install the Signature Scanner CLI:

1. Unzip the Signature Scanner CLI.

   The following is the directory
   structure for Windows:

     
    [image: Windows directory structure]

## Installing the Signature Scanner CLI on Alpine Linux or ARM64

Install a supported version of Java. Then set the `BDS_JAVA_HOME` environment
variable to the same path at the `JAVA_HOME` variable for that Java
installation. This tells Detect to use the correct Java version for the Signature
Scanner.

For example:

```
export BDS_JAVA_HOME=$JAVA_HOME
```

Or:

```
export BDS_JAVA_HOME=/your/jre/root
```
