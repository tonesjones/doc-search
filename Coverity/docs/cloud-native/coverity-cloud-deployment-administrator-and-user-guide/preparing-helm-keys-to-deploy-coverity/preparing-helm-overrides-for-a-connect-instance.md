---
title: "Preparing Helm overrides for a Connect instance"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/preparing-helm-overrides-for-a-connect-instance.html"
content_id: "wMIRWRSxYsCTJa2u0EAOGw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:20.137338+00:00"
---

# Preparing Helm overrides for a Connect instance

If you are installing a single instance of Coverity Connect, set the following Helm key
values:

- Enable Connect.
- Verify that the ingress controller is configured.
- Specify the name of the Connect license secret.
- By default, the `scan-services` subchart is disabled to prevent deployment
  of scan-services. Verify that scan-services is disabled.

These keys are described in the following sections.
