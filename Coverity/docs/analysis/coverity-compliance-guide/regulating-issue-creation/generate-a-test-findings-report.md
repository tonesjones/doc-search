---
title: "Generate a test findings report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generate-a-test-findings-report.html"
content_id: "~0CkNFBNBe09xbHIl9YOZg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:45.569071+00:00"
---

# Generate a test findings report

After creating your filtering policies, you should generate a test findings report by
running the `cov-manage-findings` command with the
`--action` option set to `readFromReport`, for
example:

```
cov-manage-findings --dir /my_idir --priority-filter /my_priority_filter.xlsx 
                    --action readFromReport --report /my_findings_report_output.xlsx
```

You will probably need to iteratively edit your filtering policies and generate test
reports until you are satisfied with the results.
