---
title: "Using system environment variables"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-system-environment-variables.html"
content_id: "OA_KhBUDk3sfUdKLyFcOVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:19.475020+00:00"
---

# Using system environment variables

In addition to the PDF report output, the Security Report generator can also output three
additional files:

- **A .csv (Severities CSV) file** that provides a mapping
  from CID and CWE values to the assigned Technical Impact and Severity Level
  values that are found in the Security Details' Technical Impact Table of a
  generated security report. This information is presented in a form that can be
  easily imported into an Excel spreadsheet.
- **An .xml file** that provides the report output in a form
  that makes it easy for you to include reported data in your own documentation or
  reports.
- **A .yaml file** that lists the CWE IDs with their
  respective severity values. Each line will list a name and value pair, where the
  CWE ID (an integer value) is listed next to name of the severity. The report
  generation will fail either because the file is invalid or because the user does
  not have proper read/write permissions.

To use a system environment variable for your report generator, write the path and
filename where you would like the output file to be created and stored.

On Windows, you would set the environment variable like this:

```
set WRITE_REPORT_XML=<filename>
```

On Linux, you would set the environment variable like this:

```
export WRITE_REPORT_XML=<filename>
```

For the Security Report, the following environment variables are available:

- `DEFECT_OCCURRENCES_INCLUDE`: When set to `true`, or to any integer
  value greater than zero, entries in the **Detailed Issues** list include the
  number of times that the issue was detected.
- `IGNORE_ISSUES_DETAIL`: This variable produces a PDF report that only includes
  high level defect and issue data, omitting issue details. If this environment
  variable is set to `true`, then the Detailed Issues
  Ranked by Severity section is omitted from the generated
  report.
- `WRITE_ISSUES_JSON`: This variable writes defect or issue data to the JSON output
  file. If a file with the same filename exists, it will be overwritten. A warning
  is issued if the file cannot be opened.
- `WRITE_REPORT_XML`: This variable writes properties from the report's
  configuration to the XML output file. If a file with the same filename exists,
  it will be overwritten. A warning is issued if the file cannot be opened.
- `WRITE_SEVERITIES_CSV`: This variable writes severities and technical impacts of
  each CID to a CSV file. If a file with the same filename exists, it will be
  overwritten. A warning is issued if the file cannot be opened.
- `WRITE_CWES_YAML`: This variable writes CWE Partition data to the YAML output
  file. If a file with the same filename exists, it will be overwritten. A warning
  is issued if the file cannot be opened.
