---
title: "Using the MCP Server"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/using-the-mcp-server.html"
content_id: "kaETQdGvZx1O4DW3EpLjzw"
version: "latest"
section: "SCASS MCP Server"
scraped_at: "2026-10-04T23:32:44.375426+00:00"
content_hash: "deb16c8347aef7c9adf8a9e8b58709ae4706a25458299798a982fc9416ccdbcf"
---

# Using the MCP Server

## Getting Started — Verify Your Setup

After installation, the first thing to do is verify connectivity. Ask your AI
assistant:

> "Check the Black Duck MCP server status"

This calls the `check_status` tool and returns a full diagnostic
snapshot: Python and server version, registered tool and resource counts, all
relevant environment variables (with tokens redacted), Java availability, Detect JAR
cache state, and a live connection test against your Black Duck instance.

## Example Prompts

| Task | Example Prompt |
| --- | --- |
| Check setup | "Check the Black Duck MCP server status" |
| Security overview | "What's the security posture of my project?" |
| Find a project | "Search for project X in Black Duck" |
| Triage a vulnerability | "Ignore CVE-2024-XXXX for project Y version Z" |
| Generate an SBOM | "Generate an SBOM for project Y version Z" |
| Generate a VEX report | "Create a VEX report for project Y" |
| Check policy compliance | "Are there any policy violations on project Y?" |
| Run a scan | "Scan the current directory with Black Duck" |
| List available tools | "What Black Duck SCA tools do you have access to and what are their functions?" |

## Available Tool Surface Reference

| Area | Tool Names |
| --- | --- |
| Dashboard | `get_dashboard_summary` |
| Projects | `search_projects_versions`, `fetch_project_components`, `fetch_project_vulnerabilities` |
| Components | `search_components` |
| Vulnerabilities | `search_vulnerabilities`, `update_vulnerability_remediation` |
| Policies | `fetch_policy_violation_status` |
| Scanning | `scan`, `search_scans`, `get_scan_status`, `match_code_snippet` |
| Reports | `create_report` |
| Status | `check_status` |
