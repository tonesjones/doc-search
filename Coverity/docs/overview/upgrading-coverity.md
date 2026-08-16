---
title: "Upgrading Coverity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-coverity.html"
content_id: "VNCnKHaDlE8vBzaXZ2EPSA"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:47.094393+00:00"
---

# Upgrading Coverity

This guide covers the process of upgrading or updating your Coverity deployment from an older
supported release to the current release.

1. An *upgrade* brings your deployment up to date with a newer major release, for example
   2018.12.
2. An *update* brings your deployment up to date with a newer update release, for example
   2018.06-3.

Updates were introduced in the 2017.07-SP2 release and provide the means to install new or
updated features between major releases. At present, updates apply only to Coverity
Analysis. Normally, updates apply only to the most recent major release, and are not
back-ported to earlier major releases. Updates are only supported for these platforms:
linux64, linux, win32, win64 and macosx.

Note: If you are upgrading from a release that is more than one major release older than the
oldest currently supported release, file a support ticket at <https://community.blackduck.com/s/contactsupport> and ask for guidance. It's possible, for example,
that you should upgrade to an intermediate release before upgrading to the current
release. For a listing of currently supported Coverity releases, refer to Coverity product components: supported versions and compatibility.

Important: If you are upgrading a Coverity cloud deployment, refer to
"Upgrading a Coverity cloud deployment"
in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide. This document provides
important information for administrators who are deploying or upgrading Coverity in a
Kubernetes container environment.
