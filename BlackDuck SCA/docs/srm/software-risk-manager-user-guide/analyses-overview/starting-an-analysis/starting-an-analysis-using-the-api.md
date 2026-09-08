---
title: "Starting an Analysis Using the API"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/starting-an-analysis-using-the-api.html"
content_id: "DZDVGwB851kFHodHR9qWmg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:42.112482+00:00"
content_hash: "b8c2c7ea0e47af474542397f58b52e8fc3dbc389741266970283b9cf167f6afe"
---

# Starting an Analysis Using the API

Software Risk Manager offers an expanding API to interface with the system's
functionality programmatically. The ability to push files for an analysis by Software
Risk Manager is exposed by the API. This enables automated integration scenarios such as
continuous integration. In a continuous integration scenario, a post-build step can be
added to the build jobs to automatically push the source and compiled artifacts to
Software Risk Manager for analysis. This type of setup is strongly recommended for
development teams to catch potential issues within their codebases early for quick
remediation. (Software Risk Manager offer a [Jenkins plugin](https://wiki.jenkins-ci.org/display/JENKINS/Code+Dx+Plugin) to facilitate use in a continuous integration
context.)

Before an API key can be
used for automated analyses, the key must be assigned the `create`
role for the
project. The API call to push the files and initiate the analysis is documented in the
Software Risk Manager API Guide.
