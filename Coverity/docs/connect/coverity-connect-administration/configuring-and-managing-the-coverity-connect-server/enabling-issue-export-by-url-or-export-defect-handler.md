---
title: "Enabling issue export by URL or export defect handler"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enabling-issue-export-by-url-or-export-defect-handler.html"
content_id: "AxCfEUUrtk050jRUDufzyg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:05.458103+00:00"
---

# Enabling issue export by URL or export defect handler

Issues can be exported from Coverity Connect to an export defect handler program, a URL,
or a JIRA instance. When any of these three methods is configured, the
Export button displays in the Triage
pane. It is recommended that you create a URL to receive and display the exported defect
data. However, you can also create an export-defect-handler program
to do the same thing. Instructions for both configurations are listed below. For
information on JIRA configuration, see Integrating with Jira.

If multiple issue export methods are configured, then the first one in this order is
selected: export-defect-handler, URL, or JIRA.

Note: The Export button will not be displayed in the
Triage pane if JIRA, a URL, or an export defect handler
program is not properly configured.

**To export issue data to your URL (recommended method):**

1. Edit your cim.properties file to include the following
   properties:
   - `export.issue.url=https://yourURL/?mergedDefectId={mergedDefectId}&projectId={projectId}`
   - `export.issue.request.confirmation=true`
2. Restart Coverity Connect.

   To restart, run `<install_dir>/bin/cov-stop-im`, then
   run `<install_dir>/bin/cov-start-im`.

When the user clicks Export, Coverity Connect opens a new window
to your configured URL, with the current defect data displayed. The
`{mergedDefectId}` and `{projectId}` variables in the
`export.issue.url` parameter will be replaced with their respective
exported values. You can also include additional variables at the end of the URL,
separated by ampersands (&).

For more information on available issue data variables, see the export XML file in Exported defect output.

**To create a program to handle an exported issue XML file:**

1. Name your program export-defect-handler.

   On non-windows systems, do not use a file extension. On Windows systems, the
   program must have an extension, such as .com,
   .exe, or .bat. It can be any
   extension, but make sure that the extension is in the
   PATHEXT environment variable so the program can
   run.
2. Copy the program to the following directory:

   <install_dir>/bin
3. Restart Coverity Connect.

   To restart, run `<install_dir>/bin/cov-stop-im`, then
   run `<install_dir>/bin/cov-start-im`.

   The Export button is enabled when Coverity Connect locates
   export-defect-handler upon start-up.

When the user clicks Export, Coverity Connect runs the
export-defect-handler program and it passes the exported XML
file name as the first argument. What export-defect-handler writes
to `stdout` is written to the
<install_dir>/logs/cim.log file. If the program
returns a non-zero status, the program writes to `stderr` which is also
written to the <install_dir>/logs/cim.log file.

For more information, see the export XML file in Exported defect output.
