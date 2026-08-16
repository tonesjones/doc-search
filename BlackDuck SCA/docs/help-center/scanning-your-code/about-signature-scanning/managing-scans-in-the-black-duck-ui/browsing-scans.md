---
title: "Browsing scans"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/browsing-scans.html"
content_id: "jQk5kVACYrhVmf1KehaHpQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:52.334964+00:00"
---

# Browsing scans

You can view the results of a scan and the status of a scan that is in progress on the
*Scan Name* page.

To browse component scans:

1. Log in to Black Duck SCA.
2. Click [image: image] .

## Scans page

The Scans page displays a list of all scans available in Black Duck. These can be created
through Detect (as BDIO files) or by importing SBOM
files.

[image: Scans page]

The Scans page is composed of the following elements:

- The header bar contains the options to upload new scans,
  delete scans, export
  the scan list to CSV, and filter the scan
  list.
- The table contains the list of scans available in Black Duck:

  - The **Status** column displays whether or not the scan was a success with a [image: Checkmark] or a failure with a [image: Red exclamation point] .
  - The **Name** column displays the scan's name. If the scan or upload failed, an error will
    be displayed in this column under the name of the scan.
  - The **Scan Size** column displays the file size of the scan.
  - The **Created** column displays when the scan was added to Black Duck. Note that this
    timestamp may not necessarily reflect when the scan was created. To
    find the creation date of the scan, click the scan and see the
    **Created On** timestamp in the **Scan Details**
    section.
  - The **Updated** column displays the date when the scan was last modified.
  - The **Mapped To** column displays the project name to which this scan is mapped.
  - Additional options by clicking [image: Options button] for the desired scan:

    - **Map to Project**
    - **Download Scan
      Archive**
    - **Download Scan CSV
      Data**
    - **Delete**

## Exporting to CSV

You can export your search results to CSV which converts the individual rows to tabular data. To do
so, click the [image: Export CSV button] button and select CSV.

## Scan name page

To view the details of a particular scan:

1. Click the name of the scan in the **Name** column to open the *Scan Name* page.

     
    [image: Scan Name Page]

The **Scan Details** section provides the following information:

- Path: Path to the code.
- Host: Name of the machine where the latest scan was performed.
- Created on: When the scan was created. This is the specific timestamp when the scan was
  completed. This may not necessarily reflect the time displayed in the Scan
  table.
- Scan Size: File size of the scan.
- Match count: The total number of folders and files matched.
- Folders: Number of folders found in the scanned code.
- Files: Number of files in the scanned code.

The **Mapped to Project Version** section displays the project and project versions to
which the scan is currently mapped. If this scan is unmapped, use the **Map Scan to
Project Version** section to map this scan to a project or create a project and/or
version.

The **Scan History** section displays the following information about each of the
scans:

- State of a scan. Possible values are:
  - **PROCESSING**: Scanning is in progress. This is a running state. A
    reason will also be added to further explain the current state. These
    include:

    - **TOOL_SUBMISSION**
    - **USER_UPLOAD**
    - **SCAN_INGESTED**
  - **COMPLETE**: The scanner has completed the scan successfully. This is
    a terminal state. It will be accompanied with a transition reason
    explaining further how the scan was successfully completed. These
    include:

    - **COMPLETE**: The scan and matching process is complete and
      that BOM computation may proceed. Note that this status also
      appears if Black Duck has determined that the scan was a duplicate.
    - **CLONED**: Black Duck is cloning the project
      version.
    - **SKIPPED**: The scan has been skipped.
  - **ERROR**: The scanner was not able to complete the scan successfully.
    This is a terminal state, meaning that it will be accompanied with a
    transition reason explaining further how the scan failed. These
    include:

    - **CANCELLED**: A user cancelled the scan before it was
      completed.
    - **ERROR_TOOL**: "Scan Submitted and Errored". The scan was
      submitted but an error or timeout occurred in the tool that
      submitted the scan and the tool is failing the scan.
    - **ERROR_SCANNING**: "Scan Error". The scan could not be
      completed by scanner.
    - **ERROR_SAVING_SCAN_DATA**: "Saving Scan Data Error". An error
      occurred when attempting to save scan data.
    - **ERROR_MATCHING**: "Matching Error". An error occurred during
      the matching process.
    - **ERROR_BUILDING_BOM**: "Building BOM Error". An error
      occurred when attempting to build the BOM. This is for migration
      and backward compatibility only.
    - **ERROR**: A schema error has occurred.
- Host name of the machine where the latest scan was performed.
- Path to the code.
- Scan size.
- Time the scan was created.
- User who initiated the component scan.
- View Import Log: The import log is a collection of audit records that detail information on
  KB component matching successes and failures for external namespaces and
  identifiers. An example of use would be to help identify what components were "not found" during the scan and subsequently not
  added to the BOM report as it may not be immediately obvious from looking at the
  BOM.

  This only applies for the following scan types:

  - Package manager scans
  - Binary analysis scans
  - Docker inspector scans
  - Protex BOM import scans

  Signature/snippet scans do not have this functionality and that is intended. The Source tab
  should be used when reviewing signature/snippet matches.
