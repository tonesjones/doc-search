---
title: "Installation Using Docker Compose"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/installation-using-docker-compose.html"
content_id: "5Z4UhEX5KXKkmoXO10NZdw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:00.174266+00:00"
content_hash: "bd4a16129d93aeda20066ccc96f715968e7948d56e37478e04dd4f4a28a72039"
---

# Installation Using Docker Compose

A Docker-based installation consists of two parts: the SRM web application Docker image
and the database upon which it depends. You can provide your own MariaDB or MySQL
database instance or use the provided MariaDB Docker image.

For more information about using Docker Compose, see the sections below:

- Software Risk Manager Core Deployments
- Docker Compose
  Requirements
- Configuration Tasks
  (Pre-work)
  - Persistent Storage Pre-work
  - External Web Database Pre-work
  - Trust Certificates Pre-work
  - HTTPS
    Pre-work
- Installation
  - Installation
    Prerequisites
  - Volume
    Naming
  - Installation Without an External Database
  - Installation With an External Database
- Customizing Software Risk Manager
- Backup and
  Restore
  - Prerequisites
  - Creating a
    Backup
  - Backup
    Retention
  - Restoring
    a Backup
- Upgrading Software Risk
  Manager
  - Running Software Risk Manager After Upgrade
- Migrating from Software Risk Manager Installer to Docker Compose
  - Migration Without an External Database
  - Migration With an External Database
- Uninstall
