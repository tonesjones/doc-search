---
title: "Windows monitoring and diagnosis tools"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/windows-monitoring-and-diagnosis-tools.html"
content_id: "cRY2owWQjw6WO~F~ekHw8A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:18.859006+00:00"
---

# Windows monitoring and diagnosis tools

You can use the following commands to monitor and diagnose the performance of your
Coverity Connect deployment on Windows:

CPU Core Count
:   The following command will help you monitor the CPU usage.

    ```
    # systeminfo | findStr "Processors(s)"
    ```

Total RAM
:   The following command will help you monitor the total RAM
    usage:

    ```
    # systeminfo | findStr "Total Physical Memory"
    ```
