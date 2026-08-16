---
title: "Building with Cygwin"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/building-with-cygwin.html"
content_id: "ilS7bbWPj_Bxij4d3dhzHg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:31.645392+00:00"
---

# Building with Cygwin

Observe the following guidelines and limitations when working with Cygwin. Cygwin 1.7
(32-bit) is supported on all supported versions of Windows. The 64-bit version is not
supported.

- Versions 1.7.1–1.7.9. of Cygwin have a bug that can cause `cov-build` to fail
  to print the native build's output, and might cause build failures. You can fix this
  issue by upgrading your version of Cygwin. You can work around this issue by using
  `--instrument` or by redirecting the output of
  `cov-build`.
- Due to a change in Cygwin, `cov-build` cannot capture builds for Cygwin
  versions 1.7.21 and 1.7.22. Cygwin has provided a workaround in the form of an
  environment variable in versions 1.7.23 or later. The `cov-build`
  command will now attempt to automatically set this environment variable if Cygwin
  version 1.7.23 (or later) is detected. You can set the environment variable manually
  from a Cygwin shell prompt as
  follows:

  ```
  $ export CYGWIN=wincmdln
  ```
- Cygwin processes are known to be vulnerable to a Microsoft Windows defect (see Known Issue
  58684 in the Coverity 2026.6.0 Release Notes Archive) and compiler
  mis-configurations might occur when using Cygwin compilers. Upgrade to Cygwin
  version 1.7.18, which contains a workaround for this issue. If you are using later
  versions of Cygwin, note that Coverity is unable to support Cygwin versions 1.7.21
  and 1.7.22 (see above). Coverity recommends Cygwin 1.7.23 or later.
