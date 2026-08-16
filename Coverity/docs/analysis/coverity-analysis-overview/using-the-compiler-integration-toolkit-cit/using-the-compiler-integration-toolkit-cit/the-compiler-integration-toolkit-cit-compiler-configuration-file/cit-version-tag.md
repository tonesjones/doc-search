---
title: "<cit_version> tag"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cit_version-tag.html"
content_id: "aAchHGQqt4Mp3DrDMAtxtg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:11.024329+00:00"
---

# <cit_version> tag

The CIT version tag (`<cit_version>`) identifies the compatibility version
used for a given template or configuration. The CIT version is a single unsigned
integer, with larger numbers representing newer versions. This is used for backwards
compatibility between releases.

Newer static analysis releases will be able to understand older CIT compatibility
versions, but older releases may not be able to understand newer compatibility versions.
The current compatibility version is 1.
