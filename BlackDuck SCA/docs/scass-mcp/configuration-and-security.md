---
title: "Configuration & Security"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/configuration-security.html"
content_id: "vAaNiREaj50BF07qlYS60g"
version: "latest"
section: "SCASS MCP Server"
scraped_at: "2026-10-04T23:32:44.355866+00:00"
content_hash: "e1ddfac54dd46267583e74e0a0e4d3b49691ab6714a13f17a1acbea3e342cd2c"
---

# Configuration & Security

## Configuration Reference

| Variable | Default | Description |
| --- | --- | --- |
| `BLACKDUCK_BDSCA_URL` | `https://localhost` | Base URL of the Black Duck SCA instance |
| `BLACKDUCK_BDSCA_TOKEN` | *(required)* | API bearer token for authentication |
| `BLACKDUCK_BDSCA_SSL_VERIFY` | `true` | Whether to verify SSL/TLS certificates |
| `BLACKDUCK_BDSCA_LOG_LEVEL` | `INFO` | Logging level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `BLACKDUCK_BDSCA_LOG_FORMAT` | `colored` | Log format: `colored`, `json`, `simple` |
| `BLACKDUCK_BDSCA_LOG_FILE` | *(none)* | Path to a log file (written in addition to stderr) |
| `BLACKDUCK_MCP_ENABLE_RESOURCES_AS_TOOLS` | `false` | Expose MCP resources as tools (required for GitHub Copilot) |
| `BLACKDUCK_BDSCA_MCP_MAX_REQUESTS_PER_SEC` | `10` | Rate limit for inbound MCP requests from the AI agent |
| `BLACKDUCK_BDSCA_API_MAX_REQUESTS_PER_SEC` | `10` | Rate limit for outbound API calls to Black Duck |

All logging variables can also be set via CLI flags (--log-level, --log-format,
--log-file), which take precedence over environment variables.

## Security & Permissions

**Best practices:**

- Create a dedicated service account for the MCP server with the minimum
  required roles.
- Do not use a personal admin token unless necessary.
- Refer to the Black Duck **Role and Permission Matrix** for details on role
  assignments.

**Common role requirements:**

| Operation | Minimum Required Role |
| --- | --- |
| Run scans | `GLOBAL_CODE_SCANNER`, `PROJECT_CODE_SCANNER`, or `PG_CODE_SCANNER` |
| Create new projects | `PROJECT_CREATOR`, `FULL_ACCESS`, or `PG_MANAGER` |
| Update vulnerability remediation | Write access to the project version |

## Rate Limiting

The MCP server applies two independent rate limits:

| Limit | Environment Variable | Default |
| --- | --- | --- |
| Inbound MCP requests (from AI agent) | `BLACKDUCK_BDSCA_MCP_MAX_REQUESTS_PER_SEC` | 10 |
| Outbound API calls (to Black Duck) | `BLACKDUCK_BDSCA_API_MAX_REQUESTS_PER_SEC` | 10 |

If you have exclusive use of the instance and need higher throughput, increase both
values. If sharing the instance, keep the outbound limit conservative.
