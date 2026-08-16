---
title: "Data retention policy"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/data-retention-policy.html"
content_id: "THL80w_PdcCyR4CwhxVCYg"
version: "2026.7"
section: "Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:46.854478+00:00"
---

# Data retention policy

Black Duck stores all sensitive customer data locally, behind the
customer’s firewall, including projects, components, and vulnerabilities. No binary
files or proprietary customer data (projects, BOMs, licenses, vulnerabilities, and so
on) is ever sent to Black Duck or the KnowledgeBase. No source code is sent to Black Duck
unless the customer has enabled the uploading of source files. If a customer has enabled
uploading source files, the encrypted source files are retained for 180 days and then
deleted; customers can configure a different data retention period with the
DATA_RETENTION_IN_DAYS system parameter as described in the Black Duck installation
guides.

Registration keys are used to authenticate web requests. Once a request is successfully
authenticated, no customer-specific information is retained:

- IP addresses from the originating requestor are “stripped” by the load
  balancer.
- All weblogs retained for operational purposes do not contain session data.
- All data that is retained for KB improvement (statistics related to web service
  requests) is anonymized – there are no identifiers which can be used to
  associate a customer to a particular KB request.
