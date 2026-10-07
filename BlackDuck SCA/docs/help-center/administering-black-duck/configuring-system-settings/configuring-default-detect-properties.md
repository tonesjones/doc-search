---
title: "Configuring Default Detect Properties"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-default-detect-properties.html"
content_id: "TgZMNsB645~W1istPYdSbQ"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:20.381009+00:00"
content_hash: "ed1865c3d6dd64f1a87572334e5878185f7273c49ddde0ddf5f1f1033d3cded3"
---

# Configuring Default Detect Properties

You can configure the default behavior for specific Black Duck Detect properties when running scans in online mode. Settings defined here will override Black Duck Detect’s standard default values globally; however, any client-side configurations will take precedence and can override these global defaults.

To configure default Black Duck Detect properties:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Select **System Settings**.
4. Click **Black Duck Detect** in the left-hand menu.

## Enabling Correlated Scans

Enabling correlation between different scanning methods enhances accuracy and yields more comprehensive scan results.

**Prerequisites**:

- Detect 11.4.0+
- SCASS must be enabled on your product registration key

To enable the correlated scans Detect property in Black Duck SCA:

1. Check the **Enable Correlated Scans** checkbox.
2. Click **Save**.
