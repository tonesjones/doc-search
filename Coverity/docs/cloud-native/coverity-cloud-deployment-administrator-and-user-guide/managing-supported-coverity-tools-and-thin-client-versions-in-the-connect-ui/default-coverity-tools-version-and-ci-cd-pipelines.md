---
title: "Default Coverity Tools version and CI/CD pipelines"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/default-coverity-tools-version-and-ci/cd-pipelines.html"
content_id: "1n5IXKGbMrCtg7IgOPIm0Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:45.840286+00:00"
---

# Default Coverity Tools version and CI/CD pipelines

The `default` variable enables an administrator to specify Coverity Tools
versions, one at a time, through the Coverity Connect UI. Using `default`
to specify a default Coverity Tools version in the CI/CD pipeline script eliminates the
need to change hard-coded version numbers in CI/CD pipeline scripts. You can code the
`default` Coverity Tools in the CI/CD script, then manage the default
version through the Connect UI. Refer to Setting the default Coverity Tools version for CI/CD pipelines
and Changing the default Coverity Tools version for CI/CD pipelines.

Note:

The default version is available for both CI/CD and end users, however the actual
`default` functionality is for CI/CD commands only.

Specifying and using a `default` Coverity Tools version makes it easier to
maintain pipelines. Specifying a default eliminates the task of updating or creating new
pipelines when a new Coverity Tools version is deployed. `default` always
points to the current configured `default` Coverity Tools version.

The following example illustrates a Coverity Tools URL that is hard-coded, but always
points to the configured `default` Coverity Tools version. This URL does
not need to be changed to reflect a new Coverity Tools version; the desired version is
simply configured as the `default`:

```
https://$COV_URL/api/v2/scans/downloads/coverity-all-platforms-default.tar.gz
```

where `$COV_URL` specifies the URL of the Coverity root directory.

The following example illustrates a URL that hard codes a specific Coverity Tools
version. This URL must be updated in CI/CD automation scripts to reflect any change in
the desired Coverity Tools version. This example hard codes only Coverity Tools version
2026.6.0:

```
https://$COV_URL/api/v2/scans/downloads/coverity-all-platforms-2026.6.0.tar.gz
```

where `$COV_URL` specifies the URL of the Coverity root directory.
