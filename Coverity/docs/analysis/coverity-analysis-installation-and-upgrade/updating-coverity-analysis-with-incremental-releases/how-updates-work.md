---
title: "How updates work"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/how-updates-work.html"
content_id: "8lyQ04Hn~iyvzQ8YcAXqWQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:22.497533+00:00"
---

# How updates work

After a new (major) release of `cov-analysis`, incremental releases will
be published when enhancements to that release become available. These enhancements can
be viewed on the Customer Portal and are provided as part of our support for the Coverity® Analysis product.

Once each day, each Coverity Connect instance contacts the Customer Portal and
automatically downloads update packages, storing them locally. These updates are then
available for downloading and installation on connected Coverity Analysis platforms.

When the results of an analysis run are uploaded to Coverity Connect using the
`cov-commit-defects` command, the Coverity Connect instance will
check if it has any updates that can be installed on that Coverity Analysis client. If
so, the client is informed and the `cov-commit-defects` prints a
message to that effect before exiting.

Since even small changes can be disruptive in certain development environments, we leave
it up to the Coverity Analysis administrator when to install updates. You can choose the
most appropriate time to run `cov-install-updates` to complete the
update process.
