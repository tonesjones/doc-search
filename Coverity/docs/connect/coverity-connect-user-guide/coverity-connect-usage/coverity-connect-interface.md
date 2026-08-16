---
title: "Coverity Connect interface"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-interface.html"
content_id: "f2ebu1SR4GRpdD6XsGGqIQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:46:50.257192+00:00"
---

# Coverity Connect interface

The Coverity Connect interface allows you to find, examine, and triage many types of issues that can occur in your source code.

Your Coverity Connect administrator uses Coverity Connect projects and streams to organize
issues found by Coverity Analysis in your code base. In Coverity Connect, each project
contains one or more streams into which the results of an analysis are pushed
(committed). Each time a new set of analysis results is committed to a Coverity Connect
stream, a new snapshot is created for it in
Coverity Connect. So, if an issue that appeared in past snapshots in a given stream has
been fixed, that issue will not appear in the latest snapshot.

The following sections describe the various areas of the Coverity Connect window, and
provide the general workflow for using Coverity Connect.

In this section:

- Understanding the primary Coverity Connect workflows
- Finding issues
- Managing issues
- Triaging issues
