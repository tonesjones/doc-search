---
title: "Overview & Capabilities"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/overview-capabilities.html"
content_id: "ZM1iT7d3OevNipW6Y498_g"
version: "latest"
section: "SCASS MCP Server"
scraped_at: "2026-10-04T23:32:44.316504+00:00"
content_hash: "2154abde3cbef4c6e014e145c946caf1bd6ced90bf426bb58e130d8bddbe3335"
---

# Overview & Capabilities

## What Is the Black Duck SCA MCP Server?

The Black Duck SCA MCP Server connects AI coding assistants to your Black Duck
Software Composition Analysis (SCA) instance using the Model Context Protocol (MCP).
It exposes your Black Duck data as a set of tools that any MCP-compatible AI harness
can call — enabling you to investigate your software's security posture, triage
vulnerabilities, generate reports and SBOMs, and more, all from within your IDE or
AI assistant.

Warning: API tokens inherit the full permissions of the associated user
account. If you provide a token with write access, the AI assistant can modify data
in your Black Duck SCA instance — including updating vulnerability remediation
status and policy overrides. We recommend creating a dedicated service account with
the minimum permissions required for your use case.

## Supported Capabilities

| Capability | Description |
| --- | --- |
| **SBOM Generation** | Generates SBOMs for scanned projects. Prompts user for SBOM template selection. May require explicit prompting (e.g., "generate an SBOM"). |
| **VEX Report Generation** | Fully functional. |
| **Notices Report Generation** | Basic notices reports generate successfully. |
| **Policy Violation Summary** | Retrieves and summarises policy violations with remediation suggestions based on criticality. |
| **Vulnerability Triage (CVE/BDSA)** | Can ignore/triage specified vulnerabilities. Correctly detects already-ignored or non-existent vulns. |
| **Vulnerability Remediation** | Assists with upgrading vulnerable components directly. Uses the newer project-version-level API path. |
| **Project & Version Search** | Searches Black Duck for existing projects using package manager or git metadata. |
| **Scanning** | Run scans for source, binary, container, and SBOM inputs; check scan status and results; match code snippets. |
| **Dashboard Summary** | View instance-wide security posture, activity trends, and vulnerability breakdowns. |
| **IDE Compatibility** | Confirmed working in Claude Code, Claude Desktop, VS Code, GitHub Copilot, Cursor, and RooCode. |

## Known Limitations & Gaps

|  |  |  |
| --- | --- | --- |
| Area | Status | Details |
| Notices with full license/compliance data | ❌ Not supported | Fails; gets stuck in loops with invalid generation formats. Does not prompt the user for what data to include. |
| Code locations & scan history | ❌ Not supported | No endpoint or tool exists to query code locations, scan types, or scan history. |
| Deep license & license risk analysis | ❌ Not supported | Cannot review deep license data or identify components with the riskiest licenses. |
| Global/server-wide risk queries | ⚠️ Partial | Cannot yet answer questions like "which projects on my server have the highest security risk?" (expected to be addressed in a future release). |
| Dashboard-level reporting | ⚠️ Limited | Only the dashboard summary is available; no global reports. |
| Re-scanning via Detect | ⚠️ Improved | Previously unreliable; now functional but may still require some manual guidance for complex scenarios. |
