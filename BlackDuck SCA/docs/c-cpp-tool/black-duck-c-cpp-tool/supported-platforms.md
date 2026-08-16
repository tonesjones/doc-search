---
title: "Supported platforms"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/supported-platforms.html"
content_id: "FyYgakeoWulkUW30v2l4Ow"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:53.558260+00:00"
---

# Supported platforms

Supported platforms include Debian, Redhat, Ubuntu, openSUSE, Fedora, CentOS, macOS, and
Windows.

The macOS ARM platform is currently not supported.

The signature scan and binary scan will be completed on all supported platforms as
permitted by your Black Duck SCA license. Any scan cli parameters can be used and passed
to Black Duck C/CPP tool through the `additional_sig_scan_args`
parameter.

On Unix-like operating systems, a package manager scan will also be run.

Note: Windows does not have a supported package manager. Scans run on Windows will not
include the package manager scan and will not produce a BDIO file. Here, package manager
scan refers to usage of O/S package managers such as yum, apt, etc.
