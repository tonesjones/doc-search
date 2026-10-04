---
title: "Web services hosted on Black Duck servers"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/web-services-hosted-on-black-duck-servers.html"
content_id: "BnqYgXkoSrUtHZmJeG~B8Q"
version: "2026.7"
section: "Hosted Architecture and Network Communications"
scraped_at: "2026-10-04T23:32:22.243691+00:00"
content_hash: "65066a31bfe6523fdea86cd121a8f1d77c49c2c3065672c5d3639c502bbe4d1b"
---

# Web services hosted on Black Duck servers

The Black Duck application works in conjunction with services that are hosted in Black Duck data centers. These services are:

- **Registration service**: Used to validate Black Duck software license and entitlements.

  This service is datacenter-managed by Black Duck in Massachusetts, USA.
- **Black Duck KnowledgeBase (KB)**: Contains meta-data (versions, signatures, licenses, vulnerability data, and so on) on all of the open source projects tracked by Black Duck. As a web service, the KB provides real-time updates, for example, new components or versions, vulnerabilities, and so on, which are immediately available to the Black Duck application.

  The KB resides on Google Cloud Platform (GCP) Services with a variety of locations. Currently the KB is running of an instance of GCP in North America, Europe, and Asia.
