---
title: "Enabling Intelligent Orchestration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/enabling-intelligent-orchestration.html"
content_id: "alDWzvUpnLUqTm3AfFljpA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:18.510394+00:00"
content_hash: "319094053c1d09a53c2dc91336d000a3a4b6110eead9820c84b141f9261d6b4e"
---

# Enabling Intelligent Orchestration

Software Risk Manager provides an Intelligent Orchestration integration that allows the
application of an IO Pre-Scan policy to a Software Risk Manager analysis. (For more
information on Intelligent Orchestration and its use, see Intelligent Orchestration in the Software Risk Manager User Guide.)

**Note:** Intelligent Orchestration requires a separate IO license and may not be
available in all implementations.

To enable IO functionality, add the following configuration settings to the codedx.props
file:

- `io.enabled = true` - sets whether or not to enable IO [default:
  false]
- `io.url = io-url` - sets the base URL for your IO server [example:
  https://io.codedx.com]
- `io.api-key = io-token` - sets the token used by Software Risk Manager to access
  the IO API [example: ABCD...===]

(For more information on property settings and the `codedx.props` file,
see Configuration Files.)
