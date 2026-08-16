---
title: "Proxy server requirements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/proxy-server-requirements.html"
content_id: "GfPQ_qcHJ269ygVetRmdXQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:32.311697+00:00"
---

# Proxy server requirements

Black Duck supports:

- No Authentication
- Digest
- Basic
- NTLM

If you are going to make proxy requests to Black Duck, work with the
proxy server administrator to get the following required information:

- The protocol used by proxy server host (http or https).
- The name of the proxy server host
- The port on which the proxy server host is listening.
