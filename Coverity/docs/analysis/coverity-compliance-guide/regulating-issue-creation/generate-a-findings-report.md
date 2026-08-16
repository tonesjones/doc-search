---
title: "Generate a findings report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generate-a-findings-report.html"
content_id: "vulFBXx6yeIML5TdWel3Dw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:43.591702+00:00"
---

# Generate a findings report

After running a code analysis, you should generate a findings report by running the
Coverity Analysis `cov-manage-findings` command with the
`--action` option set to `readFromConnect`, for
example:

```
cov-manage-findings --dir /my_idir --stream my_stream 
                    --url http://connect_host:8080 --user my_username 
                    --password my_password --action readFromConnect 
                    --report /my_findings_report_output.xlsx
```

Assuming that you have not yet uploaded a priority filter to Coverity Connect, this
command will generate a blank priority filter along with the findings report. Both will
be contained in the path specified by `--report`
(`my_findings_report_output.xlsx` in the example). If you have
already uploaded a priority filter to Connect, the generated priority filter will mirror
the uploaded priority filter.
