---
title: "Docker Compose Requirements"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/docker-compose-requirements.html"
content_id: "nbSQJFlI39KEvqhDAh5YMQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:01.750779+00:00"
content_hash: "c69efda614a167565596beaad7b517950e0ebbc4e2a80c473a0ddb7736d51a3e"
---

# Docker Compose Requirements

Software Risk Manager deployment requires Docker Compose version 2.

## System Size

Hardware requirements can vary based on a number of factors, including how many Software
Risk Manager projects will be active at the same time, how frequently analyses will be
conducted, whether built-in tools are being used, the number of results from tools in use,
how many concurrent users are expected to use the system, and what other system interactions
might be configured. Taking that into account, you can refer to the tables below for some
general guidelines to help determine the size of your deployment.

Table 1.

| Size | Total Projects | Daily Analyses | Concurrent Analyses |
| --- | --- | --- | --- |
| Small | 1–100 | 1,000 | 8 |
| Medium | 100–2,000 | 2,000 | 16 |
| Large | 2,000–10,000 | 10,000 | 32 |
| Extra Large | 10,000+ | 10,000+ | 64 |

## Core Feature Requirements

This section describes the web and web database requirements based on the system size.

### Core Web Workload Requirements

Table 2.

| Size | CPU Cores | Memory | IOPs | Storage |
| --- | --- | --- | --- | --- |
| Small | 4 | 16 GB | 3,000 | 64 GB |
| Medium | 8 | 32 GB | 6,000 | 128 GB |
| Large | 16 | 64 GB | 12,000 | 256 GB |
| Extra Large | 32 | 128 GB | 32,000 | 512 GB |

### Core Web Database Workload Requirements

Table 3.

| Size | CPU Cores | Memory | IOPs | Storage |
| --- | --- | --- | --- | --- |
| Small | 4 | 16 GB | 3,000 | 192 GB |
| Medium | 8 | 32 GB | 6,000 | 384 GB |
| Large | 16 | 64 GB | 12,000 | 768 GB |
| Extra Large | 32 | 128 GB | 32,000 | 1536 GB |

### Core Persistent Storage Requirements

Table 4.

| Volume | Feature | Description |
| --- | --- | --- |
| Web AppData | Core | Required volume for web workload |
| DB Data | Core (when not using external database) | Database volume for database |

### Core Internet Access Requirements

Software Risk Manager uses internet access in the background for some activities, such as
keeping tool data up-to-date and periodically checking for a new Software Risk Manager
release.

Software Risk Manager does not require internet access; however, internet access is
highly recommended to ensure full functionality.

To disable background internet access by Software Risk Manager, customize your Software Risk
Manager deployment by setting `codedx.offline-mode = true`. The
default is `false`. Note that this will not disable any internet access
that may occur due to user action or configuration settings, such as Tool Connector, Git,
or Issue Tracker configurations.

When internet access is enabled, Software Risk Manager will perform the following
actions:

- **Update notifications.** Software Risk Manager will periodically check for newer
  versions and display an update notification when one is available. Requests for the
  latest version are sent to <https://service.codedx.com/updates/latestVersionData.json>.
- **Dependency-Check updates.** Dependency-Check will periodically download updates
  from the National Vulnerability Database, the Retire.js repository, or reach out to
  Maven Central while scanning Java dependencies (this aids in the dependency
  identification process, to cut down on both false positive and false negative
  results).
- **Offline mode.** If Software Risk Manager is in offline mode, this may lead to
  lower quality results when running Dependency-Check as a bundled tool.
- **Secure Code Warrior.** Unless noted elsewhere, Software Risk Manager will reach
  out to any URLs belonging to the `securecodewarrior.com` domain.
