---
title: "Enable risk scoring"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/enable-risk-scoring.html"
content_id: "jcp5se3YbKQriw5d~toVYg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:22.235593+00:00"
content_hash: "0f4b393768b05ebcb8ba01706a045fc078c66ccf6802651d58063d9b6d6e7964"
---

# Enable risk scoring

To enable risk scoring, follow these steps:

Note: Only Organization Administrators can complete these steps.

1. Go to My Organization > Risk Scoring.
2. Select Enable risk scoring for all applications.

   When you enable risk scoring for the first time, the following risk factors appear:

   | Risk factor type | Risk factor name | Category | Risk impact |
   | --- | --- | --- | --- |
   | Application | Business Criticality | Non-Critical | -5 |
   | Business Supporting (default) | 0 |
   | Mission Critical | 5 |
   | Issue | Reachability | Reachable | 5 |
   | Undetermined | 0 |
   | CISA KEV | On KEV List | 5 |
   | Not on KEV List | 0 |
3. (Optional) Create or modify application risk factors, enable issue risk factors, and/or adjust other risk scoring settings, as required.
4. Select Save changes.
