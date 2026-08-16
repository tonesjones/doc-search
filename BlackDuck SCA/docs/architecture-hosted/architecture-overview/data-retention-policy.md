---
title: "Data retention policy"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/data-retention-policy.html"
content_id: "n7MfqD~zSm7tgJ3SfUocBg"
version: "2026.7"
section: "Hosted Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:54.809933+00:00"
---

# Data retention policy

All customer source code and binary code remains on the customer premise and is never sent to
Black Duck, unless the customer has enabled the uploading of source files. Black Duck,
running in the secure Black Duck hosted environment, stores each customer’s proprietary
data, including projects, components, vulnerabilities, user and organizational
information, in an isolated database. No customer proprietary data is sent to the Black
Duck services running in the Black Duck data centers.

Registration keys are used to authenticate web requests. Once a request is successfully
authenticated, no customer-specific information is retained:

- IP addresses from the originating requestor are “stripped” by the load
  balancer.
- All weblogs retained for operational purposes do not contain session data.
- All data that is retained for KB improvement (statistics related to web service
  requests) is anonymized – there are no identifiers which can be used to
  associate a customer to a particular KB request.

If a customer has selected to enable uploading source files, the encrypted source files
are retained for 180 days and then deleted; customers can request a different data
retention period.
