---
title: "Upload a priority filter"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upload-a-priority-filter.html"
content_id: "jC6__uE2LdMkFkUYGWtfOA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:46.217369+00:00"
---

# Upload a priority filter

When you are satisfied with your test findings report, it is time to upload your priority
filter to Coverity Connect using the `cov-manage-findings` command with
the `--action` option set to `sendToConnect`, for
example:

```
cov-manage-findings --dir /my_idir --stream my_stream 
                    --url http://connect_host:8080 --user my_username 
                    --password my_password --action sendToConnect 
                    --priority-filter /my_priority_filter.xlsx
```

The priority filter is now fully operational.
