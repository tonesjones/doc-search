---
title: "Configuring a local scan engine"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/configuring-a-local-scan-engine.html"
content_id: "vrV0idIuIHKAh47at5KRTA"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.464282+00:00"
---

# Configuring a local scan engine

This section describes configuring Coverity to view issues detected locally.

The main choice, when configuring Coverity Analysis for a locally installed Coverity engine, is whether to use the
Coverity on Polaris Software Integrity Platform, or a Coverity Connect server.

- **If Coverity on Polaris is your server:**

  The server itself requires no extra configuration. A client system
  *might* require some special configuration. If so, we strongly
  recommend that all systems used by a team have the same configuration
  settings. See Configure Coverity Analysis to use Coverity on Polaris.
- **If Coverity Connect is your server, you have two choices:**
  - If your setup already uses legacy ‘coverity.conf’ configuration files, you can continue to do so.
  - If you are adding support for Coverity, you can create a new scan configuration
    and choose the Coverity (.yaml, .json) option.

    These files, which support Coverity CLI option specifications, are the preferred method.

  **Preparing the Coverity Connect server:**
  To install Coverity Analysis locally, the Coverity Connect server must provide a license file and the installers for
  downloading and installing Coverity analysis on various platforms.
  See Preliminaries: Server-side configuration for Coverity Connect.
- **If you plan not to use a server:**

  You can also run local Coverity (SAST) scans of your source code, without
  connecting to the Internet. Instructions for installing Code Sight on a
  disconnected (or *air-gapped)* system are provided in each
  installation guide.
- **Special-purpose configurations:**

  Some setups might need additional configuration settings before you run Code Sight. For more
  details, see the section Alternative configuration settings.
