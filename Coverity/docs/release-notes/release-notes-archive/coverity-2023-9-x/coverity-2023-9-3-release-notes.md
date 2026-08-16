---
title: "Coverity 2023.9.3 Release Notes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-2023.9.3-release-notes.html"
content_id: "HaOSCYkRH17_XNIMvVqRjw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:40.719145+00:00"
---

# Coverity 2023.9.3 Release Notes

## Important information for 2023.9.3

Support for this version of Coverity will be discontinued 18 months after the base version of this release.

All Coverity products, including the installers, support only ASCII characters for file and directory names.
Non-ASCII characters, such as Japanese characters, are not supported for these names.

If you are upgrading your Coverity installation, make sure to read the [Important upgrade considerations](https://documentation.blackduck.com/bundle/coverity-docs/page/upgrade-guide/topics/important_upgrade_considerations.html) in the Coverity Installation and Upgrade Guide. Any changes related to checkers will be listed in the corresponding "Upgrade considerations" section.

## Coverity Platform 2023.9.3

This section provides release notes for Coverity Platform components.

### Coverity Connect 2023.9.3

#### New or changed features

IM-31423
:   The Apache Tomcat version has been upgraded to 9.0.83.

#### Bug fixes

CNC-2478
:   Reported in version: 2022.12.0
:   The OpenSSL binary is now available in the web app UBI image. Customers don't need to install OpenSSL separately.

IM-30640
:   Reported in version: 2023.3.0
:   Fixed an issue where Coverity Connect didn't start as a service on a Windows machine without manual intervention.

IM-31046
:   Reported in version: 2023.6.0
:   Fixed source code management (SCM) annotations to now show all annotations, as expected.

IM-31263
:   Reported in version: 2023.6.0, 2023.9.0
:   Fixed the add/edit SAML user functionalities to no longer expect a user to provide or confirm a password.
