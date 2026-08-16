---
title: "Health check"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/health-check.html"
content_id: "a3~5Vw18Y9s5ZQTtITkEOA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:10.575488+00:00"
---

# Health check

With Health Check, you can generate metrics about projects and
streams that have been analyzed. The resulting data can be an indicator of how useful
Coverity (SAST) has been to your business.

Note: To create Health Check reports, you need to have both
Manage server parameters and Manage
projects permissions.

**To generate a Health Check report:**

1. On the Coverity Connect menu bar, choose Configuration > System.
2. At the left of the Configuration - System dialog, scroll down so you can
   see Health Check. If you have the needed permissions,
   Health Check appears in the list.
3. Click the Health Check entry to highlight it.

   Now you can see the Health Check controls.

     
    [image: image]
4. Click to place a check mark next to the project/stream entries you want to
   inspect, or click to place a check mark next to All Projects and
   Streams.
5. Click Generate.

   Coverity Connect displays a message that the report is being generated. You can
   click Check Status to see more details about report
   generation.
6. When the report is complete, click Download.

   Coverity Connect downloads the report.

A Health Check report is in JSON format, and has the file name
SoftwareIntegrityMetrics_<date and sequence
numbers>.json. It contains an array of records for the projects or streams
that you chose, followed by report metadata. Here is an example:

```
{
    "Project Stats": [
        {
            "server": "server_name",
            "project_name": "Defector",
            "project_description": "Java QA/TA/SCM/xref testing",
            "loc": 364,
            "defect_density": 142.86,
            "current_outstanding_triaged": 0,
            "current_outstanding_untriaged": 52,
            "streams": "defectorstream",
            "component_maps": "Default",
            "first_snapshot": "2020-01-01",
            "latest_snapshot": "2020-06-19"
        },
        .
        .
        .
    ],
    "Report Metadata": [
        {
            "connect_version": "2021.06",
            "generation_date": "2021-05-04",
            "start_date": "2020-05-04",
            "end_date": "2021-05-04",
            "selection_count": "69/69"
        }
    ]
}
```
