---
title: "Uploading a scan file in Black Duck SCA"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/uploading-a-scan-file-in-black-duck-sca.html"
content_id: "M_IrtzhCtsDMOe55KDPlng"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:51.392980+00:00"
---

# Uploading a scan file in Black Duck SCA

If you output the scan to a file, you can import the file into Black Duck using the UI.

To upload a file:

1. Log in to Black Duck SCA.
2. Do one of the following:

   - Click [image: image] .

       
      [image: Scans page]
   - From the **Settings** tab for a project version, select
     **Scans**.

       
      [image: Project Version Scans tab]
3. Click **Upload File** and select a file format:

   - BDIO Scan: Supported file types: .json, .bdio, .bdmu.
   - SBOM-SPDX: Supported file types and formats: .json, .yaml, .rdf, .spdx
   - SBOM-CycloneDX: Supported file types and formats: .json
4. Upload the desired file(s) in **Upload *file format*** dialog box:

   - Click **Browse Computer...** or anywhere inside the dotted line box
     and navigate to the desired report file.
   - Drag the report file into the dialog box.

   You can multiple files by repeating the step above. The selected report files
   will be listed as Queued, ready to be uploaded.

   You can remove unwanted report files from the list by clicking the [image: Remove icon] .
5. Optionally, you can enable the **Unmatched Component Auto-Creation** checkbox to automatically create custom components from SBOM unmatched origin
   IDs.
6. Click **Scan** in the Upload dialog box after uploading the file.

   The **Upload *file format*** dialog box will remain open after the scan(s) have
   completed, should you want to add additional report files to scan.
7. Click **Close** to dismiss the **Upload *file format*** dialog box.

Warning: When uploading a BDIO or SBOM file, it will override an existing BDIO or SBOM
file if they share the same name. This will update the BOM of the project version to
which it is mapped.

Note: The scan will not appear on the project version's **Settings** tab unless you mapped the
scan to this project version during the scan; view the scan on the Scans page.

After uploading the file, if the scan is unmapped, use Black Duck to map the file to a
project.

## Error code references

If the scan upload fails, it will display an error code and a message.

Table 1. External communication errors

| Error code | Message |
| --- | --- |
| ERR01_1001 | ScanCLI REST communication error |
| ERR01_1002 | Host name could not be resolved |
| ERR01_1003 | ScanCLI Host connection error |

Table 2. Internal communication errors

| Error code | Message |
| --- | --- |
| ERR02_1001 | Unknown connection error |
| ERR02_1002 | Scan processing timed out |

Table 3. Resource allocation errors

| Error code | Message |
| --- | --- |
| ERR03_1001 | Failed to establish the validity of the server's certificate |
| ERR03_1002 | Failed to establish a secure connection to the server |
| ERR03_1003 | Failed to verify the server certificate for host |
| ERR03_1004 | Unable to secure the connection to the host |
| ERR03_1005 | File not found |

Table 4. Registration errors

| Error code | Message |
| --- | --- |
| ERR04_1001 | Registration is invalid |

Table 5. Internal error codes

| Error code | Message |
| --- | --- |
| ERR05_1001 | Unable to update scan status |
| ERR05_1002 | Unable to persist results to scan database |
| ERR05_1017 | Unrecognized error |
| ERR05_1018 | Failed to run the scan |
| ERR05_1019 | An error occurred while ingesting chunk |
| ERR05_1020 | BDIO archive upload processing failed |
| ERR05_1021 | Unable to process KnowledgeBase component matching |
| ERR05_1022 | Unable to process KnowledgeBase signature matching |
| ERR05_1023 | Unable to process KnowledgeBase signature polling request |
| ERR05_1024 | kbMatchData is required for IP scans |
| ERR05_1025 | Scan processing failed in Match Engine |
| ERR05_1026 | Knowledge Base lookup failed in Match Engine |
| ERR05_1027 | Signature lookup failed in Match Engine |
| ERR05_1028 | Failed to create or update code location |
| ERR05_1029 | Scan match creation failed |
| ERR05_1030 | Failed to run scan auto BOM job |
| ERR05_1031 | Snippet scan auto BOM job failed |
| ERR05_1032 | Failed to run BOM job |
| ERR05_1033 | Failed to transfer BDIO data |
| ERR05_1034 | An error occurred while ingesting chunk |
| ERR05_1035 | FS scan waiting period was surpassed |
| ERR05_1036 | Exception thrown when trying to poll match results |
| ERR05_1037 | Scan data was not present in the database |
| ERR05_1038 | Error processing KB request message |
| ERR05_1039 | Error processing KB request message |
| ERR05_1040 | Failed saving document data for document |
| ERR05_1041 | Failed to complete post work for scan |
| ERR05_1042 | Scan failed while adding chunk data |

Table 6. External error codes

| Error code | Message |
| --- | --- |
| ERR06_1003 | Cannot create output directory |
| ERR06_1004 | Username missing |
| ERR06_1005 | Authorization failure |
| ERR06_1006 | Bad exclude file |
| ERR06_1007 | Provided bdio archive has wrong format |
| ERR06_1008 | Failed exclude file |
| ERR06_1009 | Failed global exclude file |
| ERR06_1010 | Invalid key store |
| ERR06_1011 | Failed key store |
| ERR06_1012 | Certificate password missing |
| ERR06_1013 | Invalid certificate password |
| ERR06_1014 | Failed key pair |
| ERR06_1015 | Invalid dry run file |
| ERR06_1016 | Server scan was not found |

Table 7. Stopped by user codes

| Error code | Message |
| --- | --- |
| ERR06_1002 | Scan Stopped by user |
