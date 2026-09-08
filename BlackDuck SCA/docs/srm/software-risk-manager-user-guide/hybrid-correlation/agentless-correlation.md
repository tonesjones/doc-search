---
title: "Agentless Correlation"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/agentless-correlation.html"
content_id: "265ep8Qv6JfX~u8eeCezvQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:35.270049+00:00"
content_hash: "b6ab58afea0f61477a785c4d2f742d0e13d80419e052ba953cad06fb4ff3f67a"
---

# Agentless Correlation

Agentless correlation uses a static analysis approach on source code and binaries to
correlate SAST and DAST results. No configuration steps are required to make use of
agentless correlation. The only requirement is uploading source code at some point
in an analysis.

## Correlation Performance Impact

Agentless Correlation greatly expands the set of possibilities that must be considered to create
a hybrid finding. Since exact code paths aren't provided, many inferred paths are
created and evaluated during correlation. This can greatly impact the speed of
correlation during analysis.

## Requirements and Known Limitations

For information on requirements and known limitations, see the following topics:

- Requirements.
- Known
  Limitations.
