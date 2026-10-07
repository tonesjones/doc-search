---
title: "Code Sight Standard Edition and the Coverity Cloud Deployment"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/code-sight-standard-edition-and-the-coverity-cloud-deployment.html"
content_id: "cfXbzvFJpluswPebdK8v3A"
version: "2026.9.0"
section: "Code Sight Standard Edition"
scraped_at: "2026-10-06T23:39:55.746355+00:00"
---

# Code Sight Standard Edition and the Coverity Cloud Deployment

It can be useful to understand how the Code Sight Standard Edition uses the
Coverity Cloud Deployment.

This is how Code Sight uses the Cloud Deployment, when that is available:

1. Verifies the license status to enable source-code scanning.
2. Downloads the authenticated scanning engines:

   SCA Scans (Detect)
   :   Detect collects dependency information for the project and sends it to the cloud service for analysis.
       The cloud service returns the vulnerability information for these dependencies.

       Detect is an open-source tool that is available at
       <https://github.com/blackducksoftware/detect>.

   SAST Scans (Sigma)
   :   No connection is made to the cloud service.
3. (Optional) Upload anonymized telemetry data.

   This is anonymized usage data: for example, which Code Sight features are being used and how they are being used.
   The data uploaded *does not include* any sensitive data, such as code itself.

   Sharing telemetry data is optional, and you can choose to disable this feature.
   For more information, see Telemetry in Code Sight.
