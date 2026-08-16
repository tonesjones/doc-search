---
title: "Downloading a scan file"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/downloading-a-scan-file.html"
content_id: "XxVlhnSanKY7YGbL6VacoQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:56.624599+00:00"
---

# Downloading a scan file

You may need a scan file, which is a file of a scan that has been imported to Black Duck, similar to a dry run file. For example, you may need to
provide Customer Support with the scan file if you are experiencing scanning issues, as
this file may help them investigate the issue.

Note: This feature is not available if you initially scanned using Black Duck version 5.x or
earlier. If the option does not appear, delete the code location and re-scan.

## Downloading Scan Archive

To download a scan archive:

1. Log in to Black Duck SCA.
2. Do one of the following:

   - For unmapped scans, click [image: image] .

       
      [image: Scans page]
   - For scans mapped to a project version, from the **Settings** tab for a
     project version, select **Scans**.

       
      [image: Project Version Scans tab]
3. Click [image: Options button] and select **Download Scan Archive** in the row of the scan that you
   want to obtain a scan file.

   The file is downloaded with a `.bdio` extension and is a compressed zip file.
   It contains the original scan data, without any modifications made after the
   initial scan.

## Downloading Scan CSV Data

In order to download scan CSV data, the original scan must have been performed with the
`--upload-csv`
scan CLI option. To
download a scan CSV data:

1. Log in to Black Duck SCA.
2. Do one of the following:

   - For unmapped scans, click [image: image] .

       
      [image: Scans page]
   - For scans mapped to a project version, from the **Settings** tab
     for a project version, select **Scans**.

       
      [image: Project Version Scans tab]
3. Click [image: Options button] and select **Download Scan CSV Data** in the row of the scan
   that you want to obtain a scan file.

   The file is downloaded with a `.csv` extension and is a
   compressed zip file. It contains the original scan data, without any
   modifications made after the initial scan.
