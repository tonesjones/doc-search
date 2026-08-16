---
title: "Using system environment variables"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-system-environment-variables.html"
content_id: "lvmwe8_DhN8AahdEGk2OGw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:11.052200+00:00"
---

# Using system environment variables

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

For this report generator, you can use the following two environment variables:

- `WRITE_ISSUES_JSON`: This variable writes defect or issue data to the JSON output
  file. If a file with the same filename exists, it will be overwritten. A warning
  is issued if the file cannot be opened.
- `WRITE_REPORT_XML`: This variable writes properties from the report's
  configuration to the XML output file. If a file with the same filename exists,
  it will be overwritten. A warning is issued if the file cannot be opened.
