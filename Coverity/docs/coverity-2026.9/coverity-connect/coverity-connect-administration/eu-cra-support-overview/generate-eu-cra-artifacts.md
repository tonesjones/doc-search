---
title: "Generate EU-CRA artifacts"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/generate-eu-cra-artifacts.html"
content_id: "TIAnfBRHaF6m4FeF3aoYew"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.082268+00:00"
---

# Generate EU-CRA artifacts

Generate EU-CRA reports and CSAF/VEX reports from Coverity issue.

- Ensure that Coverity Connect is running.
- Ensure that issues have been committed to a stream.
- Ensure that you have permission to generate reports.
- Ensure that issues have a Security Impact classification for CSAF/VEX
  reports.

Important: Generate EU-CRA artifacts only from analysis performed using the
`--cra` option. Reports generated from other analysis
configurations might omit CRA-relevant findings and provide incomplete or misleading
results.

EU-CRA reports are generated as a ZIP archive that contains PDF and HTML files.
CSAF/VEX reports are generated as JSON artifacts.

1. Log in to Coverity Connect.
2. Click **Preview Modern UI** in the header bar.

   The modern UI opens in a new browser tab.
3. From the **Projects** page, open the project that
   contains the stream for which you want to generate an
   artifact.
4. Select the **Stream** for which you want to generate an artifact.
5. Open the **Issues** tab.
6. (Optional) Apply filters to restrict the findings included in the generated
   artifact.
7. Select a snapshot.

   Note: If no snapshot is selected, the latest snapshot is
   used.
8. Click **Export** and select
   **Generate CRA Artifacts**.

   The **Generate CRA Artifacts** dialog opens.
9. Select the artifact type that you want to generate.
   - EU-CRA report
   - CSAF/VEX
10. Click **Generate**.

Generated artifacts become available from the **Reports** tab.

To review, download, or delete generated artifacts, see Manage EU-CRA reports.
