---
title: "Thin Client"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/thin-client.html"
content_id: "vX1H5E~7K0UpZrN1K7dPTg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:20.290439+00:00"
---

# Thin Client

Important: Coverity Thin Client is an option that
works only with Scan Service.

Coverity Thin Client is much smaller than the full client and therefore it is better for
embedding into Continuous Integration/Continuous Deployment (CI/CD) pipelines. With Thin
Client, Coverity capture tools are installed on the client and analysis tools are
installed as part of Scan Service in the cloud. When you perform a scan, the capture is
performed on the client and the analysis is performed in the cloud using Coverity Scan
Service. The Scan Service reports the scan status to the Thin Client.

Note: If you install Scan Service in the cloud and full classic
Coverity on the client, you can choose whether to run the scan/analysis locally on the
client or in the cloud using Scan Service. For information on running scans, refer to
Coverity Analysis 2026.6.0 User and Administrator Guide.

The following figure illustrates the scan process for a scan performed by the Scan
Service installed in the cloud. In this example, Coverity Connect and Scan Service are
installed in the cloud, and Thin Client is installed on the client. In the illustration,
from left to right, files to be analyzed are captured to an intermediate directory
(iDIR) which is then uploaded for analysis. The analysis is performed in the cloud by
Coverity Scan Service and the results are committed to Coverity Connect. Coverity
Connect stores the analysis results in the Connect PostgreSQL database and reports the
analysis status to the client. This enables you to create analysis containers within a
Kubernetes cluster and not rely on local compute resources.

Figure 1. Scan process of Coverity Cloud deployment
[image: Cloud Coverity Scan Process]
