---
title: "Local defect owner assignment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/local-defect-owner-assignment.html"
content_id: "dfIZT1TNJn2nFDYkSm1zdw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:00.973919+00:00"
---

# Local defect owner assignment

Defects found by Desktop Analysis are automatically assigned to the user running
`cov-run-desktop`
(see the `--user` option in the
Coverity 2026.6.0 Command Reference). This applies to all newly detected defects
(CIDs), which only exist locally and do not have a previously assigned owner.

This behavior is controlled by the `--set-new-defect-owner` option, described in
the Coverity 2026.6.0 Command Reference. When set to true, as it is by default,
automatic owner assignment will take place for all new defects, as long as there are 100
or fewer local-only defects found. Because the owner assignment adds to the total
runtime of the `cov-run-desktop` command, it is limited to 100 new
defects by default. This means that if `cov-run-desktop` finds more
than 100 local-only defects, no owner assignment will take place. However, if you
require owner assignment on a larger number of local defects, the limit can be adjusted
with the `--set-new-defect-owner-limit` option.
