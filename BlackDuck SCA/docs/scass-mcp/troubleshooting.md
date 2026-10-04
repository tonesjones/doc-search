---
title: "Troubleshooting"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/troubleshooting.html"
content_id: "MO6IoRzd3dHcAvHmMblppw"
version: "latest"
section: "SCASS MCP Server"
scraped_at: "2026-10-04T23:32:44.397905+00:00"
content_hash: "a8d7c0f80c0bbcc19ff2c4c15d3108e8d7ff4da5a8f4957a5ac4646efe71521f"
---

# Troubleshooting

## Enable Debug Logging

The fastest way to diagnose any issue is to capture a full debug log. Add these
environment variables to your MCP server configuration:

```
BLACKDUCK_BDSCA_LOG_LEVEL=DEBUG
BLACKDUCK_BDSCA_LOG_FILE=/tmp/bdsca-mcp.log
```

**Claude Code:**

```
export BLACKDUCK_BDSCA_LOG_LEVEL=DEBUG
export BLACKDUCK_BDSCA_LOG_FILE=/tmp/bdsca-mcp.log
claude
```

**VS Code / Claude Desktop** — add to the env block in your config:

```
"env": {
  "BLACKDUCK_BDSCA_URL": "https://<your-instance-url>",
  "BLACKDUCK_BDSCA_TOKEN": "<api-token>",
  "BLACKDUCK_BDSCA_LOG_LEVEL": "DEBUG",
  "BLACKDUCK_BDSCA_LOG_FILE": "/tmp/bdsca-mcp.log"
}
```

Then run the failing operation and inspect `/tmp/bdsca-mcp.log`.

## Verifying Environment Variables Are Set

On a successful start the log will contain:

```
INFO BDSCA MCP server starting version=1.2.3 bdsca_url=https://... token=eyJh...9Qw
```

- If `token=<not_set>` →
  `BLACKDUCK_BDSCA_TOKEN` was not passed to the MCP
  process. Check your client configuration and restart.
- If `bdsca_url` shows `None` or is missing →
  `BLACKDUCK_BDSCA_URL` is also unset.

## Authentication Failures

**Symptom:**`check_status` returns an error, or every tool call
fails with an authentication error.

**Steps:**

1. Open the log file and look for `Could not authenticate with
   token` or `api_call status=401`.
2. Verify the token in your Black Duck instance:

   - Log in → **User → My Access Tokens** → confirm the token is active
     and not expired.
3. Update the token in your MCP client configuration and restart.

Note: API tokens are user-specific. If the token owner's account is disabled, existing
tokens may be invalidated.

## Permission Errors

**Symptom:** Scan or remediation operations fail with "Insufficient
permissions".

**Steps:**

1. The log will show the specific missing roles, e.g.:

   ```
   Missing scan access role. Required one of: GLOBAL_CODE_SCANNER, ...
   ```
2. Ask a Black Duck administrator to assign one of the required roles to the
   account associated with your API token.

## Java Not Found

**Symptom:** Source scan fails with `Java executable not found:
'java'`.

The MCP server searches for Java in this order:

1. `DETECT_JAVA_PATH` env var (direct path to the
   `java` executable)
2. `JAVA_HOME` env var
3. `java` on the system `PATH`

**Steps:**

1. Verify Java is installed:

   ```
   java -version
   ```
2. If installed but not on PATH, set in your MCP
   config:

   `DETECT_JAVA_PATH=/path/to/jdk/bin/java`

## Detect JAR Download Issues

**Symptom:** Source scan fails with `Could not obtain Detect JAR`
or `Failed to contact repository`.

The MCP server downloads the Detect JAR from
`https://repo.blackduck.com` on first use. If that host is
blocked by a corporate firewall:

**Option A — Use an internal mirror:**

```
DETECT_SOURCE=https://your-internal-mirror/detect-X.Y.Z.jar
```

**Option B — Pre-download and provide the local path:**

```
DETECT_JAR_PATH=/path/to/detect-X.Y.Z.jar
```

## SSL Certificate Errors

**Symptom:** Connection fails with a certificate verification error.

If your Black Duck SCA instance uses a self-signed or internally-issued
certificate:

```
BLACKDUCK_BDSCA_SSL_VERIFY=false
```

Or point to your CA bundle:

```
BLACKDUCK_BDSCA_SSL_VERIFY=/path/to/ca-bundle.crt
```

## Rate Limiting

**Symptom:** Tool calls return "Rate limit exceeded" or slow down significantly
under heavy use.

Increase the rate limit environment variables as needed (see Configuration & Security). If sharing the instance with other users,
keep the outbound limit conservative.
