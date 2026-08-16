---
title: "Coverity Connect network connectivity requirements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-network-connectivity-requirements.html"
content_id: "BdOX1nDaQQSw_SAa0XbRYA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:50.970840+00:00"
---

# Coverity Connect network connectivity requirements

Table 1. Coverity Connect Network Connectivity Requirements

| Port name | Default port number | Protocol | Notes |
| --- | --- | --- | --- |
| HTTPS port | 8443 | **HTTPS** – Also hosts the Commit protocol via WebSocket protocol. | Secured web service port for API and GUI clients. See the Coverity Platform 2026.6.0 User and Administrator Guide for information on how to enable this port and set its certificates. |
| HTTP port | 8080 | **HTTP** – Also hosts the Commit protocol via WebSocket protocol. | Non-secured web service port for API and GUI clients.  Attention: Appropriate only for demonstration purposes because it's unencrypted. Credentials and sensitive data are visible in transit. See the Coverity Platform 2026.6.0 User and Administrator Guide for information on how to configure and disable this port. |
| Commit port | 9090 | **Commit** – Proprietary protocol used for uploading analysis results. This protocol is deprecated. | The Commit port must be reachable by clients if the Commit protocol is still being used in your environment to upload analysis results. The Commit protocol shares TLS certificates with the HTTPS protocol. See the Coverity Platform 2026.6.0 User and Administrator Guide for information on how to configure these certificates. |
| **Remote Config** – Proprietary protocol used for communication between Coverity Connect instances in a Coverity Connect cluster. | The Commit port must also be reachable by the other Coverity Connect instances in a Coverity Connect cluster environment. The Remote Config protocol uses a dedicated, private certificate store. See the Coverity Platform 2026.6.0 User and Administrator Guide for information on how to configure this certificate store. |
| Control port | 8005 | **TCP** | Receives a message from `cov-stop-im` and `cov-im-ctl` commands that tells Coverity Connect to shut down. The Control port is used only on the loopback interface. It should not be externally exposed. |
