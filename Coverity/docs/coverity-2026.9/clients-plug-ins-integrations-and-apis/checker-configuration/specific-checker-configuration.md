---
title: "Specific checker configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/specific-checker-configuration.html"
content_id: "g1SprhLU~L9XwnUgyT2Xdg"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:04.052419+00:00"
---

# Specific checker configuration

Use the following keys to set options for specific checkers.

| Key | Type | Description |
| --- | --- | --- |
| enabled | Boolean | Specific checker to enable. Default: true indicates that if the checker is present in the configuration, it is enabled. This key need only be specified to disable the checker. |
| options | Map from String to String | Options to set for the checker. The map key is the name of the checker option and the string value is the setting to use for the option. |
