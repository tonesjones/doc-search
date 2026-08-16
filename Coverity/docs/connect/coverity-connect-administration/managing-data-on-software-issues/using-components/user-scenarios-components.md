---
title: "User Scenarios: Components"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/user-scenarios-components.html"
content_id: "Qul2ipt~u7haWR_pN_8qRQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:18.079419+00:00"
---

# User Scenarios: Components

The following scenarios illustrate the use of components through the Coverity Connect
interface. The first scenario focuses on component configuration and the second scenario
describes the work-flow of a user who is assigned to the component.

The recommended configuration pattern is to have streams which are based on the same code
base share a single component map. Streams which are unrelated should generally not
share a component map. For example:

- Code-A version1 - Uses component map "X"
- Code-A version2 - Uses component map "X"
- Code-B version1 - Uses component map "Y"

This way, the same components and file rules will apply to any stream associated
with a component map, while maintaining the best performance possible.
