---
title: "How to run a component scan with the Signature Scanner command line"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/how-to-run-a-component-scan-with-the-signature-scanner-command-line.html"
content_id: "~0SpFpFAQIIWxlZaJ8hVkQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:38.068444+00:00"
---

# How to run a component scan with the Signature Scanner command line

This section provides instructions for executing a component scan using the Signature Scanner command line tool. A component scan allows you to
identify all components within a specified archive or directory of files.

Note: If the client running the component scans needs to
communicate to Black Duck SCA via a proxy server, you must set a SCAN_CLI_OPTS
environment variable prior to running the client.

Attention: By default, the Signature Scanner does not include
components declared in supported package management files. Use Black Duck Detect
to discover declared dependencies.

## Command Line Parameters

This section lists all available parameters for the Signature Scanner
command line tool, along with their descriptions. Each parameter modifies the
behavior of the scan, allowing for customization based on your specific
requirements. Review the parameters carefully to ensure you use the correct options
for your scanning needs.

**Command syntax**:

```
scan.cli.bat [parameter1]...[parameterN]...<scan_path>
```

| Parameter | Description |
| --- | --- |
| **-?**, **--help** | Shows help for this tool. |
| <*scan_path*> | Path to the file directory location or archive that you want to scan. |
| **--bdio2** | Use BDIO 2's JSON-LD format for storing and transmitting scan evidence to the Black Duck server. |
| **--binaryAllowedList** <*file extensions*>  **--sourceAllowedList** <*file extensions*> | Use to create approved signature lists.   - **--binaryAllowedList** *x, y, x* where *x*,   *y*, *z* are the approved file extensions   for SHA-1 (binary) files. - **--sourceAllowedList** *a, b, c* where *a*,   *b*, *c*, are the approved file extensions   for clean SHA-1 (source code) files. |
| **--cloneFrom** <*version*> | Specifies the name of an existing project version to use as a clone.  To clone a project version, use the:   - **--project** parameter to specify the project you   wish to clone from. - **--release** parameter to specify the new project   version. - **--cloneFrom** parameter to specify the project   version to use as a clone.   For example, to clone version 1.0 of project SampleProject to a new version called 2.0, you would include these parameters:   ``` --project SampleProject --release 2.0 --cloneFrom 1.0 ``` |
| **--context** <*context*> | Additional URL context. Use this parameter, for example, if the X-Forwarded-Prefix header is being specified in a proxy server/load balancer configuration. |
| **--copyright-search** | Enables copyright text detection. |
| **--correlationId** *<value>* | Used by the Black Duck system to provide the ability to correlate results from different types of scan (package manager scan and signature scan) for the same code location to improve the reliability of results. |
| **--debug** | Shows debug output. |
| **--dryRunReadFile** <*data directory*> | Specifies the directory, including the file name, from a dryRun scan and posts the scan to the Black Duck server. |
| **--dryRunWriteDir** <*data directory*> | Specifies the directory to which the Signature Scanner outputs a BDIO file with the original file metadata used for scanning. The Signature Scanner does not connect to or post the scan to the Black Duck server. Note that the `data` directory is created inside the specified directory. |
| **--exclude** <*pattern*> **--exclude-from** <*Filename*> | Excludes specified directories from scanning. For detailed guidelines and automatic exclusions, see Exclusion Parameter Guidelines. |
| **--fs-wait-time** <*number of minutes*> | Number of minutes the scan client waits for the File System scan (signature scan) to be in either the completed or error status before starting the snippet or string search scan. Must be a positive integer number. |
| **--host** <*host*> | Server hosting the Black Duck installation. |
| **--individualFileMatching** *<option>* | Individual file matching is the identification of a component based purely upon the checksum information of a single file. By default, individual file matching is disabled. To enable individual file matching, select one of the following options:   - **source**. Performs individual file matching only on   files with this extension: `.js`,   `c`, `h`,   `c+`, `cc`,   `cpp`, `cxx`,   `hh`, `hpp`,   `hxx`, `h+`,   `cs`, `idl`,   `rc` - **binary**. Performs individual file matching on files   with these extensions: `.apklib`,   `.bin`, `.dll`,   `.exe`, `.o`, and   `.so`. - **all**. Performs individual file matching on all   files with extensions matching "*". - **both**. Performs individual file matching on file   extensions only using both approved signature   lists.   Any other value will be ignored and individual file matching will remain disabled.  Click here for more information on using this parameter with approved signature lists. |
| **--insecure** | Ignores TLS validation errors, allowing the Signature Scanner to connect to the Black Duck server. |
| **--license-search** | Enables searching for embedded licenses. |
| **--logDir** <*log directory*> | Location of the `log` directory which contains all Signature Scanner log files. You must specify the **--logDir** parameter for log files to be saved. |
| **--matchConfidenceThreshold** <*value*> | Specify the match confidence threshold as a percentage value between 1 - 100. A low value returns more matches; whereas a high value returns fewer matches. |
| **--max-request-body-size** <*size*>  **--max-update-size** <*size*> | Controls how scan data is streamed (buffered) from the Signature Scanner to Black Duck.  In rare cases, you may need to modify these values to better suit your network, for example, decreasing the values if there are issues with your network or increasing the default values if your network is highly stable.   - **--max-request-body-size**. Size of the main request   that uploads the scan data for scanned paths.  Specify a value, in bytes. The default is 20000000 bytes.   The recommended minimum value is 2000000 bytes; the   recommended maximum value is 2000000000 bytes. - **--max-update-size** Buffers an update request to   inform Black Duck SCA when Signature Scanner has completed uploading   the data of individual URIs (scanned paths).  Specify a value, in bytes. The default value of 10000   bytes. The recommended minimum value is 1000 bytes; the   recommended maximum value is 1000000 bytes. |
| **--min-scan-interval**=<*time in hours*> | Minimum scan interval setting (in hours), which may be used to limit daily rate of the Signature Scanner for given code location. If set to greater than 0, signature scans will not be processed if they occur before the set scan interval. |
| **--name** <*scan name*> | Unique name identifying this scan. This name is displayed on the Scans page. Click here for more information.  Note: The **--name** parameter is not supported when specifying multiple scan paths in a single command line. |
| **--no-prompt** | Non-interactive mode.  Instead of the **--no-prompt** parameter, you can set the BD_HUB_NO_PROMPT environment variable to enable non-interactive mode. |
| **--no-signature-generation** | Use the traditional Signature Scanner instead of the Enhanced Signature Generation. |
| **--password** <*password*> | Provides the password for the Black Duck SCA server account. |
| **--port** <*port*> | Port on which the Black Duck server instance is listening. |
| **--project** <*project*> | Name of the project to which you want to map the scan results.  If you specify a project, you must specify a version.   - If the project and project version exist, the Signature Scanner maps or remaps the scan   results. - If the project exists, but the version does not, the Signature Scanner creates the version and   maps the scan results. |
| **--project-group** <*project group name*> | Assigns the project to the designated project group. If the project does not already exist, it is created in the corresponding project group.  This parameter has no effect if the project already exists or if the specified project group does not exist. |
| **--release**<*release*> | Name of the project version to which you want to map the scan results.  If you specify a version, you must specify a project.   - If the project and project version exist, the Signature Scanner maps or remaps the scan   results. - If the project exists, but the version does not, the Signature Scanner creates the version and   maps the scan results. |
| **--retain-unmatched-files** **--discard-unmatched-files** | Used to retain or discard, respectively, any unmatched files discovered by this scan and this scan only. If either option is supplied, project and global retention settings are ignored; otherwise, retention is determined by project or global settings as described in "Settings". Specifying both options with a single scan is an error. |
| **--scheme** <*scheme*> | Protocol to use to connect to the server hosting the Black Duck SCA installation. Possible values are http or https; https is the default value. You must include `-scheme https` to specify the https protocol. |
| **--statusWriteDir** <*directory*> | Specifies the directory to which the Signature Scanner outputs a JSON file which contains the complete scan status information. |
| **--selfTest** | Performs a self-test; will not connect to or post the scan to the Black Duck SCA server. |
| **--snippet-matching**  **--snippet-matching-only**  **--snippet-matching-all-source**  **--full-snippet-scan** | These parameters control snippet matching behavior during scans. |
| **--tlscertpass** | Forces the Signature Scanner to prompt you for the password for the client certificate.  You can specify the **--tlscertpass** parameter and/or set the BD_HUB_CLIENTCERT_PASS environment variable which specifies the private key password for the client certificate, for example, when **--tlscert** points to an encrypted PKCS #12 key store.  The result of specifying the **--tlscertpass** parameter depends on whether the key is encrypted.   - If the key *is* encrypted, the scan will fail if you do   not set the BD_HUB_CLIENTCERT_PASS environment variable   *or* specify the **--tlscertpass** parameter.   - If you set the environment variable *and*     specify the **--tlscertpass** parameter, the     Signature Scanner prompts you for     the password; it does not check the password value     against the value specified in the environment     variable. - If the key *is not* encrypted, regardless of whether   the BD_HUB_CLIENTCERT_PASS environment variable is set:   - Specifying the **--tlscertpass** parameter     forces the Signature Scanner to     prompt you for the password for the client     certificate. The scan will fail unless the     password is empty.   - If you do not specify the **--tlscertpass**     parameter, the scan will succeed. |
| **--tlskey** <*keyFile*> | Black Duck client certificate private key file. Automatically sets **--scheme** to https.  Note: This parameter is optional as the key and certificate can be in included in the key store file specified with **--tlscert**. |
| **--tlscert** <*certFile*> | Black Duck client certificate chain file or key store file. Automatically sets **--scheme** to https. Click here for more information on using certificate-based authentication. |
| **--upload-source** | Uploads the source file, an optional feature for snippet matching, embedded license search, and copyright text search.  This parameter is optional with the **--snippet-matching** or **--snippet-matching-only** parameters or with the **--license-search** and/or **--copyright-search** parameters. |
| **--upload-csv** | Generates a CSV file during the scan and uploads it to Black Duck. The CSV file can be downloaded from the Scans page. |
| **--username** <*username*> | Black Duck user account with the code scanner role.  Instead of specifying a username and password, use the **BD_HUB_TOKEN** environment variable to specify a Black Duck API token. |
| **-V**, **--version** | Shows the version information of this tool. |
| **-v**, **--verbose** | Sets the logging level to verbose. |
| Other environment variable:   - **BD_HUB_TOKEN** | Used to specify the Black Duck API token which is the preferred authentication method over username and password.  Use the Profile page in the Black Duck UI or the api-token-rest-server API to manage API tokens. |

## Command Line Examples

These examples demonstrate common scanning scenarios using the  command line.

- Scanning and sending scan data to
- Scanning and mapping the scan data

Important:

- All examples require a user account with the code scanner role.
- The examples show only required parameters. Add optional parameters as needed.

### Basic Scan

This example shows how to scan files and send the results to the  server.

1. Open a command prompt.
2. Go to the directory where the  is installed.

   For example:

   **Linux/MAC OSX**:

   `/opt/blackduck/hub/scan.cli-/scan.cli-/bin`

   **Windows**:

   `C:\scan.cli-\scan.cli-\bin`
3. Run the following command to configure and initiate the scan.

   For example:

   **Linux/Mac OSX**:

   ```
   ./scan.cli.sh --username <username> --host <host> --port <port> <scan_path>
   ```

   **Windows**:

   ```
   scan.cli.bat --username <username> --host <host> --port <port> <scan_path>
   ```

   The  sends the scan data to 's server. Log in to 
   to map the component scan to a
   project, which adds the identified components to the project
   BOM.

### HTTPS Scan with Project Mapping

This example demonstrates scanning over HTTPS and automatically mapping the
results to a specific project version.

1. Open a command prompt.
2. Go to the directory to which the scanner is installed.

   **Linux/MAC OSX**:

   `/opt/blackduck/hub/scan.cli-/scan.cli-/bin`

   **Windows**:

   `C:\scan.cli-\scan.cli-\bin`
3. Run the following command to configure and initiate the scan.

   **Linux/Mac OSX**:

   ```
   ./scan.cli.sh --username <username> --host <host> --port <port> --scheme HTTPS --project <project> --release <release> <scan_path>
   ```

   **Windows**:

   ```
   scan.cli.bat --username <username> --host <host> --port <port> --scheme HTTPS --project <project> --release <release> <scan_path>
   ```

The  sends the scan data to the  server and automatically maps the scan to the
version of the project you specified.
