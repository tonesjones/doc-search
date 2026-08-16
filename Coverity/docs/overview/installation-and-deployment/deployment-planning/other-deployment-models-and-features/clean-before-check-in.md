---
title: "Clean before check-in"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/clean-before-check-in.html"
content_id: "cG2iLWJaWdnc4pqucJfJ~g"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:45.255941+00:00"
---

# Clean before check-in

The clean before check-in model is a way to verify that your code is "clean" before it is
checked in to your source control management (SCM) system. Before you commit the defects
you can run a command line executable to produce a Commit Preview Report. This report
(in JSON format) shows the current state of the issues on your system. Using this
report, you can determine if you want to proceed with the commit.

The definition of "clean" is a policy that is determined by your organization; it is not
necessarily defined by Coverity. (Although, Coverity does offer the Deployment Maturity
Model -- a Professional Services program to bring your deployment to be "Coverity
Clean." See The Coverity deployment maturity model.) So, these clean
policies will most likely differ from organization to organization. For example, your
organization may only determine the code to be clean if there are no New issues were
found after a given analysis.
