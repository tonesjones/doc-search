---
title: "Logging and diagnostics"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/logging-and-diagnostics.html"
content_id: "M~WZ67m_J7DZBiK6_hxlkA"
version: "latest"
section: "Bridge CLI reference"
scraped_at: "2026-08-08T23:47:35.079161+00:00"
---

# Logging and diagnostics

Bridge CLI offers multiple logging and diagnostic options. By default, logs are written to `<current_working_directory>/.bridge` directory. User can change this default location by passing the `--home <directory_path>` option.

## Logging

Bridge CLI offers the following JSON format logging options:

- Pass `--json-log` to output JSON format logs to console.
- Pass `--json-log-file` to enable JSON format logs in the `bridge.log` file in the Bridge CLI home directory.

## Diagnostics

To enable Bridge CLI diagnostics mode, pass a `--diagnostics` command line option. With this option set, Bridge CLI:

- writes additional diagnostics information to `bridge.log`.
- passes diagnostics related options to underlying tools so that they create logs under the Bridge CLI home directory.
- writes execution state data to `diagnostics.json` file under the Bridge CLI home directory.
