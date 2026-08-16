---
title: "Announcements for Version 2021.8.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements-for-version-2021.8.0.html"
content_id: "_ckAtRckWoqWXYGlvQUfdg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:05.686783+00:00"
---

# Announcements for Version 2021.8.0

## Detect 7.4 required for Black Duck 2021.8.0 release

Black Duck version 2021.8.0 requires Detect 7.4 in order to run. Please ensure you
meet this minimum version requirement when upgrading.

## Desktop Scanner on CentOS-7

As a result of updated dependencies, the latest version of Desktop Scanner will not
run on CentOS-7. Therefore, a different RPM was created specifically for the
CentOS-7 build which will be running with an older version of Electron 12. We will
maintain this separate CentOS-7 build for as long as Electron 12 is supported.

In addition to our current downloads, a link has been added on the Tools page
specifically for the CentOS-7 download. The regular RPM, debian package, macOS and
Windows installers are available as usual.

## Japanese language

The 2021.6.0 version of the UI, online help, and release notes has been localized to
Japanese.

## Simplified Chinese language

The 2021.2.0 version of the UI, online help, and release notes has been localized to
Simplified Chinese.

## Deprecated APIs

The following endpoint has been removed:

- GET /api/scan/{scanId}/bom-entries

The following defunct endpoints will now return a 410 GONE error to indicate that
access to the target resource is no longer available:

- GET /oauthclients
- POST /oauthclients
- DELETE /oauthclients/{oAuthClientId}
- GET /oauthclients/{oAuthClientId}
- PUT /oauthclients/{oAuthClientId}
- POST /vulnerabilities/vulndb-copy
