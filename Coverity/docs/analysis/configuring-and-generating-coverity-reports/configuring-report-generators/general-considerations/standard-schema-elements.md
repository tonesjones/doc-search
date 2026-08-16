---
title: "Standard schema elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/standard-schema-elements.html"
content_id: "7zkzXG0xilxP_5LrMmvoIg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:55.707589+00:00"
---

# Standard schema elements

The standard schema is the same for all reports and is required for all reports. It looks
like this:

```
################## Sections that apply to all reports #############
version:
     schema-version: 7
connection:
    url: https://coverity.example.com:8443/
    username: admin
    ssl-ca-certs:
project: "My project"
title-page:
    company-name: ABC
    project-name:
    project-version: 0.9
    logo:
    organizational-unit-name: Widgets
    organizational-unit-term: Division
    prepared-for: "Jane Doe"
    project-contact-email: prj@abc.com
    prepared-by: "John Smith"
locale:
issue-cutoff-count: 200
snapshot-id:
snapshot-date:
issue-kind:
components:
```

The following sections describe these fields in alphabetical order.
