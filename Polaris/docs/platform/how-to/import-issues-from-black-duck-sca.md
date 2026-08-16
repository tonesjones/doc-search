---
title: "Import issues from Black Duck SCA"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/import-issues-from-black-duck-sca.html"
content_id: "ROFB221kv6H8TGgaZD16ng"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:26.262069+00:00"
content_hash: "15a964dbba8e240b33c4454e162b92e68a193b8cc23d64786bf8c1640531fd4d"
---

# Import issues from Black Duck SCA

Set up a connection to Black Duck Black Duck® SCA to sync vulnerabilities to Polaris as third-party issues, either daily or demand.

## Overview

You can set up a connection to sync vulnerabilities from your Black Duck Black Duck® SCA instance to Polaris, either daily or on demand. Vulnerabilities synced from Black Duck Black Duck® SCA appear as third-party issues in Polaris, where you can use them with standard features, such as reports and dashboards, issue policies, risk scoring, and Black Duck Assist.

To get started, set up a new Black Duck Black Duck® SCA connection in the Polaris Web UI and initiate your first data sync.

## Black Duck SCA Mappings

When you first sync a Black Duck SCA connection, it maps projects and versions in Black Duck SCA to applications, projects, and branches in Polaris. These objects are mapped and named as shown here:

[image: Mappings between Black Duck SCA and Polaris defined in a connection]

## Frequency of data syncs

Data syncs from Black Duck SCA to Polaris occur automatically, at least once per day.

You can also manually trigger a data sync at any time, when you:

- Start a sync on the Integrations page.
- Start a sync for an individual project in the Project settings tab.

## About data syncs

The direction of data syncs from Black Duck SCA to Polaris is one-way.

- Data sync is across all mapped projects and branches in your Polaris tenant.
- During a data sync, Black Duck projects and versions not already in Polaris are added.
- Issues not previously imported in the last sync are included in the next sync.
- Deleting projects or versions in Black Duck SCA does not delete them in Polaris.
- You can delete a Polaris project manually, but this won't delete the source project in Black Duck SCA.
- After a project or version is imported, later name changes in Black Duck SCA are not synced to Polaris.

This means you can rename applications, projects, and branches without them reverting to their original Black Duck SCA names on the next data sync.
