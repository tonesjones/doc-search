---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "SOmuYHK4AkMuE5zsYLcPGA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:57.947133+00:00"
---

# Examples

Generate a findings report using a local priority filter:

```
> cov-manage-findings --dir /my_idir --action readFromReport 
                 --priority-filter /my_priority_filter.xlsx 
                 --report /my_findings_report_output.xlsx
```

Upload a priority filter to Coverity Connect:

```
> cov-manage-findings --dir /my_idir --stream my_stream 
                 --url http://connect_host:8080 --user my_username 
                 --password my_password --action sendToConnect 
                 --priority-filter /my_priority_filter.xlsx
```

Generate a findings report using a centrally-stored priority
filter:

```
> cov-manage-findings --dir /my_idir --stream my_stream 
                 --url http://connect_host:8080 --user my_username 
                 --password my_password --action readFromConnect 
                 --report /my_findings_report_output.xlsx
```
