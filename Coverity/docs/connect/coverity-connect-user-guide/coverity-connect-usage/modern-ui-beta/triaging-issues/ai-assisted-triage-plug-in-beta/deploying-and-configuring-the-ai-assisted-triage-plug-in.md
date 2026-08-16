---
title: "Deploying and configuring the AI-Assisted Triage Plug-in"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deploying-and-configuring-the-ai-assisted-triage-plug-in.html"
content_id: "O~MeNVQLO4l5sgScecebGg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:03.576383+00:00"
---

# Deploying and configuring the AI-Assisted Triage Plug-in

Deploy the AI-Assisted Triage Plug-in in standalone or distributed mode, then integrate it with
Coverity Connect.

## Standalone deployment

Standalone mode runs all service components in a single binary. Use this mode with
Coverity Connect.

**Prerequisites**

AI Triage CLI binary
:   Download the `cov-triage-issue` CLI tool. The CLI is
    typically available as
    `cov-triage-issue-linux64-2026.6.0.tar.gz` or
    `cov-triage-issue-win64-2026.6.0.tar.gz`. Files can be
    downloaded from either the Black Duck Community site or repo.blackduck.

System requirements
:   Linux, Windows, or macOS on amd64 or arm64. Minimum 2 GB RAM, 4 GB
    recommended. 10 GB disk space. Network access to the LLM endpoint.

Note: The AI-assisted triage service requires either Anthropic
Claude Sonnet 4 or OpenAI ChatGPT 5.4. Other LLM models are not currently
supported.

## **Security considerations**

The data shared with the configured LLM is limited to what is required to explain and
triage the selected issues. However the data collected includes unredacted source
files and issue data. By enabling the feature, you are automatically consenting to
send the data as needed for the triage. Ensure that your organization’s policies
allow sharing the required data with the configured LLM.

Important: You are responsible for securing the service, the logs, and the
network environment.

**Step 1: Download the standalone binary.**

Available platforms:

- `cov-triage-suggestion-service-standalone-macosx-2026.6.0`
- `cov-triage-suggestion-service-standalone-macos-arm-2026.6.0`
- `cov-triage-suggestion-service-standalone-linux64-2026.6.0`
- `cov-triage-suggestion-service-standalone-linux-arm64-2026.6.0`
- `cov-triage-suggestion-service-standalone-win64-2026.6.0.exe`

These files will be located on BlackDuck Community Downloads and
repo.blackduck.com/releases/2026.6.0.

**Step 2: Extract the AI Triage CLI binary.**

```
tar -xzf cov-triage-issue-linux64-2026.6.0.tar.gz
cd cov-triage-issue-linux64-2026.6.0
```

Note the path to `bin/cov-triage-issue` for the configuration
file.

**Step 3: Generate a key pair.**

**Step 4: Configure the authentication
secrets.**

**Step 5: Configure the LLM API
keys.**

**Step 6: Create a configuration file.**

Create a `triage-suggestion-service.yaml` file in the same directory
as the binary:

Note: The port specified for the service must be an unused port.
Also, the path to the file needs to be a full path, as shown in the example. For
information on authentication secrets, see Configuring authentication secrets.

```
# ── Service ───────────────────────────────────────────────────────────────────
service_name: triage-suggestion-service
service_mode: standalone

# ── HTTP Server ───────────────────────────────────────────────────────────────
http_port: 9191
metrics_port: 9192

# ── Worker ────────────────────────────────────────────────────────────────────
worker_count: 5
queue_buffer_size: 200

# ── CLI (AI Triage) ───────────────────────────────────────────────────────────
cli_path: /path/to/cov-triage-issue-linux64-2026.6.0/bin/cov-triage-issue
cli_timeout: 600s
max_concurrent_cli: 20
work_dirs: ./workdirs
cleanup_work_dirs: false 

# ── LLM ──────────────────────────────────────────────────────────────────────
llm_url: https://api.anthropic.com/v1
llm_name: <llm_name>

# ── Storage (in-memory for standalone) ───────────────────────────────────────
storage_type: memory
queue_type: memory
cleanup_interval: 10m
request_retention: 2h
results_retention: 30m
artifact_retention: 15m

# ── Artifact Storage ──────────────────────────────────────────────────────────
artifact_storage_type: local
artifact_storage_path: ./artifacts
artifact_max_size: 104857600
upload_url_expiration: 20m

# --- Authentication secrets ---------------------------------------------------
# Generate each value on a secure host with: openssl rand -base64 32.
# 
# File-based secrets (preferred in production so secrets do not appear in process
# environment or YAML on disk). The service reads the value from the file path:
#
# jwt_secret_file: /etc/triage-suggestion-service/secrets/jwt-secret
# jwt_encryption_key_file: /etc/triage-suggestion-service/secrets/jwt-encryption-key
# auth_key_file: /etc/triage-suggestion-service/secrets/auth-key
# auth_hmac_secret_file: /etc/triage-suggestion-service/secrets/auth-hmac-secret
#
# Inline values (suitable for local development and testing):
jwt_secret: "<output of: openssl rand -base64 32>"
jwt_encryption_key: "<output of: openssl rand -base64 32>"
auth_key: "<output of: openssl rand -base64 32>" # must match Coverity Connect
auth_hmac_secret: "<output of: openssl rand -base64 32>"
encryption_private_key_file: <path_to_private_key_file>
token_ttl: 30m

# ── Logging ───────────────────────────────────────────────────────────────────
log_level: debug
log_format: json
log_file: <path_of_log_file>
```

**Step 7: Start the service.**

Linux / macOS:

```
# Use config file in current directory
./cov-triage-suggestion-service-standalone-linux64-2026.6.0

# Or specify config file location
./cov-triage-suggestion-service-standalone-linux64-2026.6.0 --config /etc/triage-suggestion-service/triage-suggestion-service.yaml

# Or use environment variables
export CLI_PATH=/path/to/cov-triage-issue-linux64-2026.6.0/bin/cov-triage-issue
export LLM_URL=https://api.anthropic.com/v1

./cov-triage-suggestion-service-standalone-linux64-2026.6.0
```

Windows:

```
.\cov-triage-suggestion-service-standalone-win64-2026.6.0.exe

.\cov-triage-suggestion-service-standalone-win64-2026.6.0.exe --config C:\triage-suggestion-service\triage-suggestion-service.yaml
```

**Step 8: Verify the service is running.**

```
# Liveness check
curl https://localhost:8080/liveness
# Expected: {"status":"ok","message":"service is alive"}

# Readiness check
curl https://localhost:8080/readiness
# Expected: {"status":"ready","checks":{"storage":"healthy"}}
```

## Integration with Coverity Connect

**Standalone deployment**

Add the triage service URL to the Coverity Connect
configuration file (`cim.properties`):

```
ai.triage.suggestion.service.url=https://triage-suggestion-service-host:8080
```

Replace `triage-suggestion-service-host` with the hostname or IP
address of the standalone service. Use `localhost` if the service
runs on the same server. For both HTTP and HTTPS, specify the port under
`http_port` in the yaml file. However, when listing the url in
`cim.properties`, make sure to specify HTTPS instead of HTTP.

Restart Coverity Connect using the following from the platform
bin folder:

```
cov-stop-im
cov-start-im
```

**Network requirements**

Standalone
:   Open the port set in the yaml file for HTTP or HTTPS on the triage service
    host. Allow inbound connections from the Coverity Connect server.

**TLS/HTTPS**

To enable TLS, apply the following settings (the specified location is an example,
specify the path to your crt and key files):

```
tls_enabled: true
tls_cert_file: /etc/tls/server.crt
tls_key_file: /etc/tls/server.key
```

Update the Coverity Connect configuration to use HTTPS. If you
use self-signed certificates, add the cert to the Coverity Connect trust store in both of the following:

- The `truststore.jks` (found in `<platform install
  dir>/config`) using the `cov-import-cert` tool
  (found in `<platform install dir>/bin`).
- Cacerts (found in `<platform install
  dir>/jre/lib/security/cacerts`) using keytool.

## Configuration reference

The service uses a hierarchical configuration system. The following list shows the
order of priority, from highest to lowest.

1. Environment variables
2. Configuration file in YAML or JSON format
3. Built-in defaults

The service searches for configuration files in the following order.

1. Path set with the `--config` or `-c` command-line
   flag
2. Path set with the `TRIAGE_SERVICE_CONFIG_FILE` environment
   variable
3. `triage-suggestion-service.yaml` or
   `triage-suggestion-service.json` in the current
   directory

**Service settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| service_mode | SERVICE_MODE | standalone | Deployment mode. Options are `standalone`, `api`, or `worker`. |

**HTTP server settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| http_port | HTTP_PORT | 8080 | HTTP/HTTPS server port |
| metrics_port | METRICS_PORT | 9090 | Prometheus metrics endpoint port |
| base_url | BASE_URL | Auto-generated | Public base URL for the service. If empty, the service generates `http(s)://localhost:port` automatically. |

**TLS settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| tls_enabled | TLS_ENABLED | false | Enable HTTPS. Requires a certificate and key. |
| tls_cert_file | TLS_CERT_FILE | (none) | Path to TLS certificate file in PEM format |
| tls_key_file | TLS_KEY_FILE | (none) | Path to TLS private key file in PEM format |

**Worker settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| worker_count | WORKER_COUNT | 5 for standalone/default, 3 for Helm/Docker distributed | Number of concurrent workers. Must be 1 in distributed mode for data isolation. |

**CLI settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| cli_path | CLI_PATH | /opt/cov-triage-issue-linux64-main/bin/cov-triage-issue | Path to AI triage CLI binary |
| cli_timeout | CLI_TIMEOUT | 600s (10 minutes) | CLI execution timeout |
| work_dirs | WORK_DIRS | ./work_dirs | Directory for artifact extraction and processing |
| cleanup_work_dirs | CLEANUP_WORK_DIRS | true | Clean up working directories after processing |

**LLM settings**

See Configuring LLM API keys.

**Storage settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| storage_type | STORAGE_TYPE | memory | Storage backend. Use `memory` for standalone or `postgres` for distributed. |
| request_retention | REQUEST_RETENTION | 1h | How long to keep request metadata |
| results_retention | RESULTS_RETENTION | 10m | How long to keep triage results |
| artifact_retention | ARTIFACT_RETENTION | 15m | How long to keep uploaded artifacts |

**Artifact storage settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| artifact_storage_type | ARTIFACT_STORAGE_TYPE | local | Artifact storage backend. Options are `local`, `s3`, or `azure`. |
| artifact_storage_path | ARTIFACT_STORAGE_PATH | ./artifacts | Local filesystem path for artifacts |
| artifact_max_size | ARTIFACT_MAX_SIZE | 104857600, which is 100 MB | Maximum artifact size in bytes |

## Health check endpoints

**GET /liveness**

Liveness probe. Use as a Kubernetes liveness probe to determine whether to restart
the pod.

```
{"status":"ok","message":"service is alive"}
```

**GET /readiness**

Readiness probe. Use as a Kubernetes readiness probe to determine whether the pod can
receive traffic.

```
# Healthy
{"status":"ready","checks":{"storage":"healthy"}}

# Unhealthy (503)
{"status":"not ready","checks":{"storage":"unhealthy: connection failed"}}
```

## Prometheus metrics

The service exposes Prometheus-compatible metrics on the metrics port (default 9090)
at `/metrics`.

## Logging

The service uses structured logging. The default format is JSON. You can change the
format to text with `log_format`.

Log levels are `debug`, `info`, `warn`,
and `error`. The default log level is `info`.

## Troubleshooting

**Coverity Connect cannot reach the triage service**

- Verify the service is running with `curl
  http://triage-suggestion-service-host:8080/liveness`.
- Check network connectivity from the Coverity Connect
  server with `telnet triage-suggestion-service-host 8080`.
- Verify firewall rules and security groups allow the connection.
- In Kubernetes, check NetworkPolicies with `kubectl get networkpolicies -n
  triage-suggestion-service`.

**Triage requests failing**

- Check service logs.

  ```
  # Standalone
  journalctl -u triage-suggestion-service -f

  # Kubernetes
  kubectl logs -f deployment/triage-suggestion-service-worker -n triage-suggestion-service
  ```
- Verify the CLI binary is accessible with `ls -l
  /opt/cov-triage-issue/bin/cov-triage-issue`.
- Verify LLM connectivity with `curl -v
  https://llm-endpoint.com`.
- Check worker pod resources, including CPU and memory limits.

**Requests stuck in queued or processing status**

- Check that worker pods are running and consuming from the queue.
- Verify RabbitMQ connectivity in distributed mode.
- Check the CLI timeout setting. Increase `cli_timeout` if the LLM
  is slow to respond.
- Verify the LLM API key file is readable and the key is valid.

**Service readiness check failing**

- Check the `/readiness` endpoint for specific check failures.
- In distributed mode, verify PostgreSQL connectivity and credentials.
- Check that the storage backend is accessible and has sufficient disk space.

**Requests timing out**

cli_timeout is set to 10 minutes by default. If a request times out, consider
triaging fewer issues or increasing the cli_timeout setting.

**AI triage returns an error for MISRA issues**

MISRA-related checkers are not supported in the 2026.6.0 release. When AI triage is
run on a MISRA issue, the following error is returned:

```
[ERROR] Triage of MISRA issues is not supported in this context for legal compliance
```

This is expected behavior. No action is required.
