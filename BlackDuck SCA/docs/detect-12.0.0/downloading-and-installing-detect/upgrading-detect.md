---
title: "Upgrading Detect"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/upgrading-detect.html"
content_id: "Wl8kLNbai0FJvLQn1b_JeQ"
version: "12.0.0"
section: "Downloading and Installing Detect"
scraped_at: "2026-10-04T23:33:18.577599+00:00"
content_hash: "7a17eee2b3b9857fafb055db81961c00156a95d8ec6180ae074c12e89b4c3c79"
---

# Upgrading Detect

We recommend reading the release notes for each new Detect version.

Detect version names follow [semantic versioning](https://semver.org/). Version strings follow the pattern MAJOR.MINOR.PATCH, with the following implications:

A PATCH version contains only fixes to functionality that already existed.

A MINOR version contans new features, and fixes to functionality that already existed.

Every MAJOR version (e.g. 7.0.0, 8.0.0, etc.) contains breaking changes. These breaking changes may not affect every user, but every user needs to check to see whether and how they to change the way they call Detect before upgrading to the next MAJOR version. To do this check and and upgrade to the next MAJOR version: In a test environment:

1. Upgrade to the latest MINOR.PATCH Detect version available for the MAJOR version you are currently running. Read all of the deprecation messages and the upgrade guidance they provide, and change the way you are calling Detect until all deprecation messages are gone. Read all of the documentation for the new properties you are using, and all of the documentation relevant to the features they control.
2. Upgrade to the next MAJOR version.
3. Test.

You must do this one MAJOR version at a time (do not skip over a MAJOR version).

For example, suppose you are running 7.12.1, and you want to upgrade to 8.0.0: In a test environment:

1. Upgrade to 7.14.0 (the latest 7.y.z version available). Read all of the deprecation messages and the upgrade guidance they provide, and change the way you are calling Detect until all deprecation messages are gone. Read all of the documentation for the new properties you are using, and all of the documentation relevant to the features they control.
2. Upgrade to 8.0.0.
3. Test.
