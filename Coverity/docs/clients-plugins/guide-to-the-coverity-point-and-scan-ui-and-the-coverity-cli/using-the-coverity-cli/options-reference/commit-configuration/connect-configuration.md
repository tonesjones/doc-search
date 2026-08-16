---
title: "Connect configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/connect-configuration.html"
content_id: "aSEHIj8dQHcTxFlLowK0Iw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:17.904139+00:00"
---

# Connect configuration

Use these values to define the Coverity Connect configuration.

| Key | Type | Description |
| --- | --- | --- |
| `auth-key-file` | string | The name of the authentication key file to use when authenticating to Coverity Connect while committing defects. Default: "$HOME/.coverity/ak-hostname-port" |
| `ca-certs-file` | string | The name of a file that contains additional certificates to trust in addition to the ones in the system certificate store and the Coverity TFT (Trust First Time) store. Default: System CA certificates |
| `comparison-only` | Boolean | If `true`, analysis results will not be committed to Coverity Connect. Instead, results compared to a reference snapshot might be saved locally, as specified by the Local configuration settings. Default: `false` |
| `comparison-report` | string | Names an output file to which analysis results should be written, instead of being committed to Coverity Connect. The output includes a comparison against the latest snapshot for the specified stream. |
| `cov-commit-defects-args` | array of strings | Additional arguments to pass to the `cov-commit-defects` command during the commit phase. |
| `description` | string | A string to describe the committed snapshot. |
| `on-new-cert` | string | Indicates whether to trust self-signed certificates presented by Coverity Connect that are not currently trusted. Possible values are `"trust"` or `"distrust"`.  If you specify `"trust"`, an untrusted self-signed certificate presented by Coverity Connect will be trusted and automatically added to the Coverity TFT (Trust First Time) store.  CAUTION:  Setting `on-new-cert` to `"trust"` does not currently work with Coverity Analysis and Black Duck® Bridge. The workaround is to manually add the self-signed certificate to your operating system's certificate store. This will tell the operating system that it can trust this certificate, and should allow you to continue.  Default: `distrust` |
| `project` | string | The name of the project to use when creating a new stream. Ignored when stream creation is not needed. If not specified, the stream name is used for the project name. Important: Project names and stream names are case-sensitive and must be 1 - 256 characters. Project names and stream names can NOT contain the following special characters:  - `:` (colon) - `*` (asterisk) - `/` (forward slash) - `\` (back slash) - `` ` `` (backtick) - `'` (single quote) - `"` (double quote) |
| `proxy-client-cert-file` | string | Specifies the file containing the client certificate to use when communicating with Coverity Connect via a forward proxy. If not specified, no client certificate will be used. |
| `proxy-client-key-file` | string | Specifies the file containing the client certificate key to use when communicating with Coverity Connect via a forward proxy. If not specified, no client certificate key will be used. |
| `proxy-url` | string | A URL for a forward proxy to use when communicating with Coverity Connect. This must be a URL that uses the `http` or `https` scheme. If not specified, no proxy is used. You can also specify the proxy server URL by using the environment variables `HTTP_PROXY` or `HTTPS_PROXY` (or their lowercase equivalents `http_proxy` and `https_proxy`).  **Proxies and WebSocket requests:** The proxy server must support the use of WebSocket requests. To determine whether your server supports proxying WebSocket requests, refer to the server's documentation; if it does, use the documentation to learn how this can be configured. |
| `scm` | string | The name of the source control management system (SCM). The valid values are as follows:  - `"git"` - `"perforce"` - `"plastic"` - `"plastic-distributed"` - `"svn"`   Note: This key is mutually exclusive with the Capture configuration `import-scm` key. Both serve the same purpose, but we recommend that you upgrade to `import-scm`, as it is more general and more widely applicable. |
| `snapshot` | Snapshot configuration | Specifies how to select a reference snapshot to use for a comparison report. |
| `stream` | string | **Required**: The name of the stream where the results are to be committed.  For a Coverity Cloud deployment, if caching is used, the `stream` option also specifies the cache key. For information on the `stream` option and the cache key in Coverity Cloud, refer to these topics in the Coverity Analysis 2026.6.0 User and Administrator Guide:   - Initiating a scan in the cloud"Initiating a scan" - Cache key"Cache key"   Important: Project names and stream names are case-sensitive and must be 1 - 256 characters. Project names and stream names can NOT contain the following special characters:  - `:` (colon) - `*` (asterisk) - `/` (forward slash) - `\` (back slash) - `` ` `` (backtick) - `'` (single quote) - `"` (double quote) |
| `target` | string | A target platform for the committed snapshot. |
| `triage` | Triage configuration | Specifies how new defects should be handled. |
| `upload-artifacts` | string | Specifies artifacts to upload following analysis when the analysis location is Connect. Valid values are `"All"` (the default), `"LogsOnly"`, `"None"`, and `"OnFailure"`. |
| `url` | string | **Required**: The absolute URL of the Coverity Connect instance where you want to commit analysis results. |
| `version` | string | Specifies a project version for the committed snapshot. |
