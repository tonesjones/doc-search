---
title: "About Project Versions"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-project-versions.html"
content_id: "HVIl7rdYLsppcoMxwWSxbA"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:12.244054+00:00"
content_hash: "8887766f1b1802e300d6d48170d8572a844b183928e5f7a11d14e3705b83ec8b"
---

# About Project Versions

A project version represents a specific release or iteration of a project in Black Duck SCA. Each version is scanned and analyzed independently, allowing you to track the open source and third-party components used in a particular release of your software and manage the associated security, license, and operational risks.

Project versions are created within a parent project, and multiple versions of the same project can exist simultaneously. This allows you to manage risk across different stages of your software's lifecycle — for example, maintaining an active production release while continuing development on a new version.

Each project version maintains its own:

- **Bill of Materials (BOM)**. The complete list of open source and third-party components, AI models, and subprojects identified through scanning, along with their associated risk data.
- **Scan history.** A record of all scans mapped to this project version.
- **Risk profile.** Security, license, and operational risk data specific to the components in this version.
- **Settings and metadata.** Configuration options, lifecycle phase, distribution type, and other version-specific properties.

A project version can also be added as a subproject of another project version, allowing you to represent shared or reused components across projects.

## Managing project versions

Depending on your role and permissions, you can perform the following actions:

- Creating a new version of a project
- Updating project version information
- Cloning project versions
- Deleting a project version

To view a project version:

1. Select the project name using the **Watching** or **My Projects** dashboard.
2. Select the desired version name.
