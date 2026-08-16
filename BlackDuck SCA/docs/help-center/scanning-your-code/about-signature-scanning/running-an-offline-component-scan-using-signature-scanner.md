---
title: "Running an offline component scan using Signature Scanner"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/running-an-offline-component-scan-using-signature-scanner.html"
content_id: "ZnfrCPmC25w1zQ9vTf3glw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:40.550163+00:00"
---

# Running an offline component scan using Signature Scanner

If a client does not have access to Black Duck, you can use the command line for Signature Scanner to run an offline scan to identify the
open source software (OSS) components contained in an archive or a directory of files.
Running an offline scan lets you:

- Use the Signature Scanner to run a scan and save the results to a
  data file.
- Upload the data file from a client that does have access to Black Duck to create a BOM.

Note: An error message appears if you exceed the scan size limit, which is 5 GB. Contact Customer
Support if you receive this message.

To run an offline component scan:

1. Be sure that you have a code scanner role.
2. Using a client that has access to Black Duck, download the Signature Scanner CLI for the platform where the
   offline scan will occur.
3. Move the zip file to the client that does not have access to Black Duck and extract the files.
4. From the client that does not have access to Black Duck, go to the
   directory where the Signature Scanner is installed and enter the
   command to run the scan.

   For example:

   **Linux/Mac OS
   X**:

   ```
   ./scan.cli.sh --dryRunWriteDir <data_directory>  <scan_path>
   ```

   **Windows**:

   ```
   scan.cli.bat --dryRunWriteDir <data_directory> <scan_path>
   ```
5. Move the `data` directory that contains the JSON file to a client
   that has access to Black Duck.
6. From the client that has access to Black Duck, send the scan
   data to Black Duck using the user interface or the Signature Scanner.

To send the data using the user interface:

1. Log in to Black Duck SCA.
2. Click [image: Scans icon] .
3. In the Scans page, click **+Add** and select **Scan File**.
4. Use the Upload Scan File dialog box to locate the JSON file, and click
   **Close**.

To send the data using the Signature Scanner CLI:

1. Open a command prompt.
2. Go to the directory to which the Signature Scanner is installed and
   run the following command:

   For example:

   **Linux/Mac OS
   X**:

   ```
   ./scan.cli.sh --dryRunReadFile <data directory> --username <username>  --host <host> --port <port>
   ```

   **Windows**:

   ```
   scan.cli.bat --dryRunReadFile <data directory> --username <username> --host <host> --port <port>
   ```
